import pandas as pd

# get the entire inventory from the .csv file
def get_inventory():
    df = pd.read_csv('inventory.csv')
    return df

# get a specific value with the name of a column in the .csv file
def get_value(column):
    df = get_inventory()
    return str(df.iloc[0][column])

# update a value in a column of the csv file
def update_csv(new_value, column, df):
    df.loc[0, column] = new_value
    df.to_csv('inventory.csv', index=False)