import pandas as pd

from sklearn.model_selection import train_test_split

from acquire import get_zillow_data

def wrangle_zillow(cached=True):
    #get zillow data
    df = get_zillow_data()
    #filter out properties that are not single unit
    df = df[df.propertylandusetypeid.isin([260,261])]
    #changing fips number to labeled county
    df['county'] = df.fips.replace([6037, 6059, 6111],['los_angeles', 'orange', 'ventura'])
    #drop duplicate or unnecessary columns
    df = df.drop(columns = ["id", "id.1", "propertylandusetypeid", "heatingorsystemtypeid", "propertyzoningdesc", "calculatedbathnbr", "finishedsquarefeet12", "fips"])
    #filter out bedrooms and bathrooms == 0
    df = df[(df.bedroomcnt > 0) & (df.bathroomcnt > 0)]
    #filter out houses less than 400 square feet
    df = df[df.calculatedfinishedsquarefeet > 400]
    #fill NaN units with 1
    df.unitcnt = df.unitcnt.fillna(1.0)
    #filter out all units not equal to 1
    df = df[df.unitcnt == 1]
    #dropping unitcnt since they are all the same and more unnecessary columns
    df = df.drop(columns = ["unitcnt", "propertylandusedesc", "propertycountylandusecode", "assessmentyear", "pid", "regionidcounty"])
    #filter out columns and rows with more than 40% null values
    df = handle_missing_values(df, .6, .6)
    #filling NaN heating systems with None
    df.heatingorsystemdesc = df.heatingorsystemdesc.fillna("None")
    #split into train, validate, test
    train, validate, test = zillow_split(df)
    #missing fixed values will be replaced with the mode
    cols_fixed = ['buildingqualitytypeid', 'regionidcity', 'censustractandblock', 'regionidzip', 'yearbuilt']
    for col in cols_fixed:
        mode = int(train[col].mode())
        train[col].fillna(value = mode, inplace = True)
        validate[col].fillna(value = mode, inplace = True)
        test[col].fillna(value = mode, inplace = True)
    #missing continuous values will be replaced with the median
    cols_cont = ['lotsizesquarefeet', 'structuretaxvaluedollarcnt', 'fullbathcnt', 'calculatedfinishedsquarefeet', 'taxamount', 'landtaxvaluedollarcnt', 'taxvaluedollarcnt']
    for col in cols_cont:
        median = train[col].median()
        train[col].fillna(median, inplace=True)
        validate[col].fillna(median, inplace=True)
        test[col].fillna(median, inplace=True)
    #return null free train, validate and test datasets
    return train, validate, test


def handle_missing_values(df, prop_required_column, prop_required_row):
    '''
    This function takes in a Dataframe, 
    proportion(0-1) of nulls required for a column
    and a proportion(0-1) of nulls required for rows
    then returns a dataframe without the nulls 
    under the threshold
    '''
    #setting threshold for row, only accepts integer
    thresh_row = int(round(prop_required_column*df.shape[0],0))
    #dropping nulls under threshold
    df.dropna(axis=1, thresh=thresh_row, inplace=True)
    #setting threshold for columns, only accepts integer
    thresh_col = int(round(prop_required_row*df.shape[1],0))
    #dropping nulls under threshold
    df.dropna(axis=0, thresh=thresh_col, inplace=True)
    return df 


def null_finder_columns(df):
    '''
    This function takes in a DataFrame and list 
    information about the null values in the columns
    '''
    #accepts a 'df' and creates a new one labeled 'nulls'  
    #nulls index is the df's columns
    nulls = pd.DataFrame(index = df.columns)
    #sums up the null values in the dataframes columns
    nulls['num_rows_missing'] = df.isnull().sum(axis = 0)
    #finds the percentage of null values in the df's columns
    nulls['pct_rows_missing'] = nulls.num_rows_missing / df.shape[0]
    return nulls



def null_finder_rows(df):
    '''
    This function finds the number of columns missing in a row,
    the percent of columns missing in the row
    and the number of rows that have the same amount of columns missing
    '''
    #initiate a dataframe
    rows = pd.DataFrame()
    #find the number of columns missing in the row
    rows['num_cols_missing'] = df.isnull().sum(axis=1)
    #find the percentage of columns missing in the row
    rows['pct_cols_missing'] = df.isnull().sum(axis=1) / df.shape[1]
    #group by 'num_cols_missing' and find 
    #how many rows have that number of columns missing
    num_rows = rows.groupby('num_cols_missing').count()
    #rename the column as 'num_rows'
    num_rows = num_rows.rename(columns ={'pct_cols_missing': "num_rows"})
    #group by 'num_cols_missing' and find 
    #the percentage of columns missing in the row
    pct_cols = rows.groupby('num_cols_missing').mean()
    #combine the 'pct_cols' and 'num_rows'
    result = pd.concat([pct_cols, num_rows], axis=1, sort=False)
    #take the 'num_cols_missing' out of the index
    result = result.reset_index()
    return result

def zillow_split(df):
    '''
    This function splits a dataframe into train, validate, and test sets
    '''
    train_and_validate, test = train_test_split(df, train_size=.8, random_state=123)
    train, validate = train_test_split(train_and_validate, train_size = .7, random_state=123)
    return train, validate, test