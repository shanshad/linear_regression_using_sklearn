
# This code is to create a single feature linear regression model
# using sklearn library
# -------------------------------------------------

# basic info
# features=inputs or independent variables
# labels=outputs or dependent variables
# parametric form for single feature linear regression problem : y=ax+b
# we have two data sets,
# 1, with two columns, with titles 'area' and 'price' and named as house price monore.xlsx
#     area	price
#     2600	550000
#     3000	565000
#     3200	610000
#     3600	680000
#     4000	725000
#
#     this contains our datas. from this data set we want to find out
#     how the output (prices) is related to input (area),
#     and utilise this relation to find out the prices of another set of data
#     where only area is given.
# 2,    area      named as area only dataset.xlsx
#       1000
#       1500
#       2300
#       3540
#       4120
#       4560
#       5490
#       3460
#       4750
#       2300
#       9000
#       8600
#       7100

import pandas as pd
from sklearn import linear_model

reg=linear_model.LinearRegression()
df=pd.read_excel(r"C:\Users\LENOVO\Desktop\Datasets for machine lerning\house price monore.xlsx")

# here we are reading the data which is in an excel sheet. if data was in csv format, you could have used read_csv command.
# if you are using excel and an IDE you might face issues with reading excel files. i would recommend you to install openpyxl
# Use pip or conda to install openpyxl

reg.fit(df[['area']],df['price'])

# reg.fit(features,labels) is used to train the model. while providing features be careful that you are providing it in a 2D matrix
# format. ie. [[]], if you had multiple features then you can input like this: df[['area','rooms','doors']]. and labels should be in a series of order (n,)
# so you can either write df.price or df['price'].
#
# since we have already trained our data, we can test it. use predict function.
# !! careful that you also give input to predict function in 2D matrix form only

print(reg.predict([[3300]]))

# you will be getting an output "[628715.75342466]" which lies between 610000 and 68000 as 3300 lies between 3200 and 3600.
# you can also get the parameters and intercepts of the linear regression model for this dataset

print(f"the coefiicients of regression is {reg.coef_}")
print(f"the intercept of regression is {reg.intercept_}")

# output: "the coefiicients of regression is [135.78767123]"
# output: "the intercept of regression is 180616.43835616432"
# since we got the relation between features and labels we can use this relation to predict the labels of a new dataset which only have features
# !! make sure that second datasets column titles also matches with first datasets features titles

out_put_needed=pd.read_excel(r"C:\Users\LENOVO\Desktop\Datasets for machine lerning\area only dataset.xlsx")

# here we are reading and storing our second dataset into a variable named out_put_needed

k=reg.predict(out_put_needed)

# here k contains an array of predicted prices of area only dataset

out_put_needed['price']=k

# this line is uesd to put that array into the out_put_needed dataframe by creating a new column named price
#now data frame is updated with area and price columns, but it is only in the python memmory.we need to update the excel sheet also.

out_put_needed.to_excel(r"C:\Users\LENOVO\Desktop\Datasets for machine lerning\area only dataset.xlsx")

#!! before running the code make sure that you have not kept the second excel sheet open while running the program
# if it is open python won't be able to modify the sheet and update it
# after running the code you can check the area only data set.xlsx,it will be updated