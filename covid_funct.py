def drop_constant_columns(dataframe):
    """
    Drops constant value columns of pandas dataframe.
    """
    keep_columns = [col for col in dataframe.columns if len(dataframe[col].unique()) > 1]
    return dataframe[keep_columns].copy()




def correlation_mat(dataset):
    corr_matrix = dataset.corr()
    print(corr_matrix)



def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
      max_value = df[feature_name].max()
      min_value = df[feature_name].min()
      result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result



def highcorr(dataset, threshold):
    col_corr = set() # Set of all the names of deleted columns
    corr_matrix = dataset.corr()
    corr_matrix = abs(corr_matrix)
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if (corr_matrix.iloc[i, j] >= abs(threshold)) and (corr_matrix.columns[j] not in col_corr):
                colname = corr_matrix.columns[i] # getting the name of column
                col_corr.add(colname)

    print(col_corr)



# remove all columns with < 0.5 correlation with Price
def del_lowcorr(dataset_in, threshold):
    col_corr = set() # Set of all the names of deleted columns
    dataset = dataset_in.copy()
    corr_matrix2 = abs(dataset.corr())
    corr_matrix2 = corr_matrix2["DailyDeaths"]


    for i in range(len(corr_matrix2)):        
        if (corr_matrix2.iloc[i] <= threshold):
                colname = corr_matrix2.index[i] # getting the name of features to remove 
                col_corr.add(colname)
                if (colname in dataset.columns) and (colname != "day_of_year")  and (colname != "avg_pred")  :
                    del dataset[colname] # deleting the column from the dataset
    return(dataset)

