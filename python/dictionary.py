import pandas as pd

data = {
    "Name": ["Shivam","Saini","Rahul","John"],
    "Mobile": [6396909996,8650223615,128586764,765468566],
    "Remarks": ["ok","done","good","good"]
}

# Dictnory can't support Row wise operation So we convert it into dataFrame first


data=pd.DataFrame(data)

print(data.iloc[1:3]) #index location >> iloc
