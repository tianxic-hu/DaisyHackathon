import os
import json
from base64 import b64decode
from pathlib import Path
import openai
import pandas as pd
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import cv2

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

DATA_DIR = os.path.join(Path.cwd(),"images_json")
IMAGE_DIR = os.path.join(Path.cwd() / "images")

df = pd.read_csv("input_flyer.csv")

for index, row in df.iterrows():
    prompt_name = row[0]
    #prompt = prompt_name + " , depth of field. bokeh. soft light. by Yasmin Albatoul, Harry Fayt. centered. extremely detailed. Nikon D850, (35mm|50mm|85mm). award winning photography."
    prompt = prompt_name + "| center shot | intricate | elegant | cinematic | character design | highly detailed | illustration | concept art | digital art | digital painting | depth of field | realistic | hyperrealistic",


    response = openai.Image.create(
    prompt = prompt[0],
    n=1,
    size="512x512",
    response_format="b64_json",
    )

    image_data = b64decode(response["data"][0]["b64_json"])
    image_file = os.path.join(IMAGE_DIR,prompt_name+".png")
    if os.path.exists(image_file):
        os.remove(image_file)

    with open(image_file, mode="wb") as png:
        png.write(image_data)

    # Add price
    image = cv2.imread(image_file)
    font = cv2.FONT_HERSHEY_SIMPLEX

    # org
    org = (0, 50)
    
    # fontScale
    fontScale = 2
    
    # Blue color in BGR
    color = (255, 0, 0)
    
    # Line thickness of 2 px
    thickness = 5
    
    # Using cv2.putText() method
    image = cv2.putText(image, row[1], org, font, 
                    fontScale, color, thickness, cv2.LINE_AA)
    org = (5,500)
    fontScale = 1
    image = cv2.putText(image, row[0], org, font, 
                    fontScale, color, thickness, cv2.LINE_AA)
    cv2.imwrite(image_file, image)

        


