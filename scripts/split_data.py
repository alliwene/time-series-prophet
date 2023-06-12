from typing import List
import pandas as pd

def split(data: pd.DataFrame, year: int | List[int]):
    if type(year) == int:
        val_df = data[data["ds"].dt.year == year]
        train_df = data[data["ds"].dt.year != year]
    elif type(year) == list:
        val_df = data[data["ds"].dt.year.isin(year)]
        train_df = data[~(data["ds"].dt.year.isin(year))]
    else: 
        raise ValueError("Please enter a valid year or list of years")
    return train_df, val_df

if __name__ == '__main__':
    split()
