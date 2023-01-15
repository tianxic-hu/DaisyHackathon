import json

import pandas as pd


def dp_1():
    """Scipt to merge 2 sheets into 1 for ORII dataset."""
    df_2010 = pd.read_excel(io="online_retail_II.xlsx",
                            sheet_name="Year 2009-2010")
    df_2011 = pd.read_excel(io="online_retail_II.xlsx",
                            sheet_name="Year 2010-2011")
    df = pd.concat([df_2010, df_2011])
    df.to_csv("or2.csv", index=False)
    return

def dp_2():
    """Script to resolve cancellation invoices."""
    df_old = pd.read_csv("or2_franc.csv")
    indexes_rows_to_delete = []
    counter = 0
    total_row = df_old.shape[0]
    for idx, row, in df_old.iterrows():
        # cancellation invoice starts with letter 'C'
        if not row["Invoice"].lower().startswith("c"):
            continue
        counter += 1
        print("Processing: {}, #{}, row {}/{}".format(row["Invoice"],
                                                      counter,
                                                      idx+1,
                                                      total_row))
        indexes_rows_to_delete.append(idx)
        # cancellation invoice has negative quantity
        num_items_returned = -int(row["Quantity"])
        for r_idx in range(idx-1, -1, -1):
            row_inspect = df_old.iloc[r_idx]
            # corresponding purchase invoice cannot be cancellation invoice
            if not row_inspect["Invoice"].lower().startswith("c"):
                continue
            # corresponding purchase invoice must be the same product
            if row_inspect["StockCode"] != row["StockCode"]:
                continue
            # corresponding purchase invoice must be made by the same customer
            if row_inspect["Customer ID"] != row["Customer ID"]:
                continue
            num_items_purchased = int(row_inspect["Quantity"])
            # if purchased quantity is larger than cancelled quantity,
            # subtract cancelled quantity from purchased quantity
            if num_items_purchased > num_items_returned:
                df_old.iloc[r_idx]["Quantity"] -= num_items_returned
                break
            # if purchased quantity equals cancelled quantity,
            # remove purchase invoice
            elif num_items_purchased == num_items_returned:
                indexes_rows_to_delete.append(r_idx)
                break
            # if purchased quantity is less than cancelled quantity,
            # remove purchase invoice and look for the rest
            else:
                indexes_rows_to_delete.append(r_idx)
                num_items_returned -= num_items_purchased
                continue
    print("#Row dropped: {}".format(len(indexes_rows_to_delete)))
    df_new = df_old.drop(indexes_rows_to_delete)
    df_new.to_csv("or2_franc_clean.csv", index=False)
    return

if __name__ == "__main__":
    dp_1()
    dp_2()