def wrangle_cols(df, col_dict, units = None, col_ind = 'col'):
    '''
    Select columns that are dictionary keys and rename these to given values
    add units as multiindex
    '''

    import pandas as pd
    
    # select columns rename
    if col_ind == 'col':
        df = df[list(col_dict.keys())]
        df = df.rename(columns = col_dict)
    elif col_ind == 'ind':
        df = df.loc[list(col_dict.keys())]
        df = df.rename(index = col_dict)
    #add units
    if units is not None:
        if col_ind == 'col':
            site_cols_units = pd.MultiIndex.from_arrays([list(df.columns), units])
            df.columns = site_cols_units
        elif col_ind == 'ind':
            df['units'] = units

    return df

def save_to_csv(df, file_dir, file_name, header = True, index = False):
    '''
    save a pandas dataframe to csv
    '''
    import os
    if os.path.exists(file_dir) == False:
        os.makedirs(file_dir)
    file_path = os.path.join(file_dir, file_name)
    if len(df) > 0:
        df.to_csv(file_path, header = header, index = index)
