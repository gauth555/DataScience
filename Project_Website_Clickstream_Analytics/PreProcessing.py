import pandas as pd
from sklearn.feature_extraction import DictVectorizer


d = pd.read_csv("Analytics Challenge Data_Calculated.csv")

matrix = d.transpose().to_dict().values()
dv = DictVectorizer(sparse=False)
x = dv.fit_transform(matrix)
names = dv.get_feature_names()

data_frame = pd.DataFrame(x, columns = names)
#print(data_frame)

data_frame.to_csv("Test_Correlation_transform_weka.csv", index = False)
