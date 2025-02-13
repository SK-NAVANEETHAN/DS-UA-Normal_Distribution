class Univariate():

      def QuanQual(dataset):
          quan=[]
          qual=[]
          for columnName in dataset.columns:
              #print(columnName)
              if (dataset[columnName].dtype=="O"):
                  #print("qual")
                  qual.append(columnName)
              else:
                  #print("quan")
                  quan.append(columnName)
          return quan,qual

      def freqTable(columnName,dataset):
          freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative_Frequency","Cusum"])
          freqTable["Unique_Values"]=dataset[columnName].value_counts().index
          freqTable["Frequency"]=dataset[columnName].value_counts().values
          freqTable["Relative_Frequency"]=(freqTable["Frequency"]/103)
          freqTable["Cusum"]=freqTable["Relative_Frequency"].cumsum()
          return freqTable

      def Univariate(dataset,quan):
          descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR","1.5Rule","Lesser","Greater","Min","Max","kurtosis","skew","var","std"],columns=quan)
          for columnName in quan:
              descriptive.loc["Mean",columnName]=dataset[columnName].mean()
              descriptive.loc["Median",columnName]=dataset[columnName].median()
              descriptive.loc["Mode",columnName]=dataset[columnName].mode()[0]
              descriptive.loc["Q1:25%",columnName]=dataset[columnName].quantile(0.25)
              descriptive.loc["Q2:50%",columnName]=dataset[columnName].quantile(0.50)
              descriptive.loc["Q3:75%",columnName]=dataset[columnName].quantile(0.75)
              descriptive.loc["Q5:99%",columnName]=dataset[columnName].quantile(0.99)
              descriptive.loc["Q4:100%",columnName]=dataset[columnName].max()
              descriptive.loc["IQR",columnName]=descriptive.loc["Q3:75%",columnName]-descriptive.loc["Q1:25%",columnName]
              descriptive.loc["1.5Rule",columnName]=1.5*descriptive.loc["IQR",columnName]
              descriptive.loc["IQR",columnName]=descriptive.loc["Q3:75%",columnName]-descriptive.loc["Q1:25%",columnName]
              descriptive.loc["1.5Rule",columnName]=1.5*descriptive.loc["IQR",columnName]
              descriptive.loc["Lesser",columnName]=descriptive.loc["Q1:25%",columnName]-descriptive.loc["1.5Rule",columnName]
              descriptive.loc["Greater",columnName]=descriptive.loc["Q3:75%",columnName]+descriptive.loc["1.5Rule",columnName]
              descriptive.loc["Max",columnName]=dataset[columnName].max()
              descriptive.loc["Min",columnName]=dataset[columnName].min()
              descriptive.loc["kurtosis",columnName]=dataset[columnName].kurtosis()
              descriptive.loc["skew",columnName]=dataset[columnName].skew()
              descriptive.loc["var",columnName]=dataset[columnName].var()
              descriptive.loc["std",columnName]=dataset[columnName].std()
          return descriptive    

     def outlier_columnName(columnName,dataset):
         Lesser=[]
         greater=[]
         for columnName in quan:
             if(descriptive[columnName]["Min"]<descriptive[columnName]["Lesser"]):
                 Lesser.append(columnName)
             if(descriptive[columnName]["Max"]>descriptive[columnName]["Greater"]):
                 greater.append(columnName)
         return Lesser, greater

     def replacing_outlier(columnName,dataset):
         for columnName in Lesser:
             dataset[columnName][dataset[columnName]<descriptive[columnName]["Lesser"]]=descriptive[columnName]["Lesser"]
         for columnName in greater:
             dataset[columnName][dataset[columnName]>descriptive[columnName]["Greater"]]=descriptive[columnName]["Greater"]
         return Lesser, greater






