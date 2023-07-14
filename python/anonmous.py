
# my=lambda x,y: x+y
# print(my(10,90))


# a=filter(lambda x: x%2==0 , [1,2,3,4,5])

# print(tuple(a))

# email=['shivam@gmail.com','saini@gmail.com','amit@gaml']


# print(list(filter(lambda x:x.split("@")[1]=='gmail.com',email )))


import pandas as pd 
dataset={
     "name":["vimal","jack","Saini"],
     "id": [1,2,3]
}
db=pd.DataFrame(dataset)
# print(db["name"])

print(list(map(lambda x: x + "@gmail.com",db["name"])))
