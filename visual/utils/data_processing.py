# import pandas as pd

# def fetch_products(collection):
#     # Convert data to pandas DataFrame
#     data = list(collection.find())
#     df = pd.DataFrame(data)
#     # Drop _id column since there's 
#     # no need for sensetive info on display
#     if '_id' in df.columns:
#         df.drop(columns=['_id'], inplace=True)
#     return df


import pandas as pd

def fetch_yearly_trends(yearly_trends_cursor):
    # Convert MongoDB cursor to a list of dicts
    data = list(yearly_trends_cursor)
    
    # Create a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Make sure the year column is in integer format
    df['year'] = df['year'].astype(int)
    
    # handling missing values:
    df.fillna(0, inplace=True)
    
    return df
