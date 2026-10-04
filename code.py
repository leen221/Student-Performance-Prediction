import pandas as pd 
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
data=pd.read_csv("student_data.csv")
#d1=data.isnull().sum() #انها تستخدم ل فحص الناقص من البيانات ان كان هنالك نقص يخرج 1 
data=data.drop(columns=["school","address","sex","romantic","nursery","reason","guardian","famsize"])
data["Pstatus"]=data["Pstatus"].map({"T":1,"A":0})
data["schoolsup"]=data["schoolsup"].map({"yes":1,"no":0})
data["famsup"]=data["famsup"].map({"yes":1,"no":0})
data["paid"]=data["paid"].map({"yes":1,"no":0})
data["activities"]=data["activities"].map({"yes":1,"no":0})
data["higher"]=data["higher"].map({"yes":1,"no":0})
data["internet"]=data["internet"].map({"yes":1,"no":0})
data["Mjob"]=data["Mjob"].map({"at_home":0,"health":1,"services":2,"teacher":3,"other":4})
data["Fjob"]=data["Fjob"].map({"teacher":0,"other":1,"services":2})
x=data[["studytime","failures","schoolsup","famsup","paid","activities","higher","internet","famrel","freetime","goout","health","absences","G1","G2"]]
y=data[["G3"]]
#print(x.dtypes)
#print(x.isnull().sum())

#print(data.dtypes)
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3, random_state=23)
model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
mae=mean_absolute_error(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R-squared:", r2)


