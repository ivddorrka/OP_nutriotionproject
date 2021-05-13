'''
This module demonstrates how to use some pandas functionality
'''
import pandas as pd

def series_examples():
    '''
    This function demonstrates some basic pandas functionality on how to work with Series
    '''
    nums_list = [1, 7, 2]
    nums_list_serie = pd.Series(nums_list, index=["x", "y", "z"])
    print(nums_list_serie, end='\n\n')

    nums_dict = {"day1": 420, "day2": 380, "day3": 390}
    nums_dict_serie = pd.Series(nums_dict, index = ["day1", "day3"])
    print(nums_dict_serie)

def read_and_work_with_csv(path : str = 'example.csv'):
    '''
    This function demonstrates some examples of using pandas to filter data,
    get entries from top/bottom, sort dataframe, det information about dataframe, etc.
    '''
    df = pd.read_csv(path, sep=';')

    # print whole DataFrame
    print(df)
    # print 1 row from top
    print(df.head(1))
    # print 1 row from bottom
    print(df.tail(1))

    print('Length with duplicates: ', len(df))
    df.drop_duplicates(inplace = True)
    print('Length without duplicates: ', len(df))

    # we can also get a lot of useful information about out dataframe and change that values
    # print DataFrame columns as list
    print(f'Columns: {list(df.columns)}')
    print(f'Shape: {df.shape}')
    print(f'Indices: {list(df.index)}')

    # filter only those entries with Location value Manchester and not Department == 'Sales'
    manchester_df = df[(df.Location == 'Manchester') & ~(df.Department == 'Sales')]

    # since some values have been dropped during filtering, we should reset indices so that indices
    # go from 0 to number of indices-1 and not their old indices wich may be not consequent
    manchester_df = manchester_df.reset_index(drop=True)
    print(manchester_df)

    # print sum of Identifier column
    print(manchester_df['Identifier'].sum())

    # sort dataframe by Identifier column in ascending order
    manchester_sorted_df = manchester_df.sort_values(by='Identifier', ascending=True)
    print(manchester_sorted_df)

    # drop One-time password and Recovery code columns
    new_df = manchester_df.drop(['One-time password', 'Recovery code'], axis=1)
    print(new_df)

    # write to file without indices column
    new_df.to_csv('new-1.csv', index=False)


if __name__ == '__main__':
    series_examples()
    read_and_work_with_csv()
