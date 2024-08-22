class Univariate():

    def QuanQual(dataset):
        Quan=[]
        Qual=[]
        for columnName in dataset.columns:
            print(columnName)
            if(dataset[columnName].dtypes=="O"):
                #print("Qual")
                Qual.append(columnName)
            else:
                #print("Quan")
                Quan.append(columnName)
        return Quan,Qual
    def Univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%",
                               "Q3:75%","99%","Q4:100%","IQR","1.5rule","Lesser","Greater",
                                    "Min","Max","kurtosis","skew","Var","Std"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["Mean"]=dataset[columnName].mean()
            descriptive[columnName]["Median"]=dataset[columnName].median()
            descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5rule"]=1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Min"]=dataset[columnName].min()
            descriptive[columnName]["Max"]=dataset[columnName].max()
            descriptive[columnName]["kurtosis"]=dataset[columnName].kurtosis()
            descriptive[columnName]["skew"]=dataset[columnName].skew()
            descriptive[columnName]["Var"]=dataset[columnName].var()
            descriptive[columnName]["Std"]=dataset[columnName].std()
        return descriptive
    def Finding_outliers(descriptive, Quan):
        Lesser = []
        Greater = []
        for ColumnName in Quan:
            if descriptive[ColumnName]["Min"] < descriptive[ColumnName]["Lesser"]:
                Lesser.append(ColumnName)
            if descriptive[ColumnName]["Max"] > descriptive[ColumnName]["Greater"]:
                Greater.append(ColumnName)
        return Lesser, Greater
    def Handle_outliers(dataset, descriptive, Quan):
        #Lesser, Greater = Finding_outliers(descriptive, Quan)
        for ColumnName in Lesser:
            dataset.loc[dataset[ColumnName] < descriptive[ColumnName]["Lesser"], ColumnName] = descriptive[ColumnName]["Lesser"]
        for ColumnName in Greater:
            dataset.loc[dataset[ColumnName] > descriptive[ColumnName]["Greater"], ColumnName] = descriptive[ColumnName]["Greater"]
        return dataset
    def FreqTable(ColumnName, dataset):
        FreqTable = pd.DataFrame(columns=["Unique_Values", "Frequency", "Relative_Frequency", "Cummulative_Frequency or cumsum"])
        FreqTable["Unique_Values"] = dataset[ColumnName].value_counts().index
        FreqTable["Frequency"] = dataset[ColumnName].value_counts().values
        total_count = len(dataset[ColumnName])
        FreqTable["Relative_Frequency"] = FreqTable["Frequency"] / total_count
        FreqTable["Cummulative_Frequency or cumsum"] = FreqTable["Relative_Frequency"].cumsum()
        return FreqTable
    
    