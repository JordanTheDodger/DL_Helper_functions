def date_diff(df:polars.DataFrame,cols_list:list[str]):
    """
        This function read dataframe and generates date diff for date data in format "YYYY/MM/DD - YYYY/MM/DD" present in the passed columns.
        Usage: date_diff(df,['date_col1','date_col2'])
        Args: df - polars DataFrame, cols_list - list of columns passed with "," as seperator.
        
    """
    
    import polars as pl
    from argparse import ArgumentParser

    #create temp that equals to len of passed col names
    col_len = len(cols_list) 
    print(f'You passed {col_len} columns that has date data. These columns will be used to create date diff')
    
    # parse list of string
    parser = ArgumentParser()
    parser.add_argument('-n', '--names-list', nargs='+', default=[])
    args = parser.parse_args()

    if col_len == 0: 
        print(f'No columns passed')
        exit
    else:
        print(args.names_list)  # Now will output: ['date_col1', 'date_col2'] 
        #usage: date_diff(df,['date_col1','date_col2'])
    
    # find match for cols_list
    col_check_flag = False
    # traverse through col list and print matched name in cols_list
    for col in df.columns.tolist():
        col_check_flag = any(list(filter(lambda cl: cl==col,cols_list)))
        if col_check_flag == True:
            pritn(f'Confirm the column name:{col}')
        
                
    
def last_day_of_month(date):
    import datetime as dt
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month+1,day=1) - dt.timedelta(days=1)