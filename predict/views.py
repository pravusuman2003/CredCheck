from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# Create your views here.

def getData(request):
    return render(request,'form.html')

def getResult(request):
    status=predict(request)
    return render(request,'result.html',{'name':request.GET['name'],'status':status})

def predict(data):
    df=pd.read_csv("loan_approval_dataset.csv")
    df.columns=df.columns.str.strip()
    df=df.drop('loan_id',axis=1)
    df['total_assets_value']=df['residential_assets_value']+df['commercial_assets_value']+df['luxury_assets_value']+df['bank_asset_value']
    df=df.drop('residential_assets_value',axis=1)
    df=df.drop('commercial_assets_value',axis=1)
    df=df.drop('luxury_assets_value',axis=1)
    df=df.drop('bank_asset_value',axis=1)
    df['education'] = df['education'].replace({' Graduate': 1, ' Not Graduate': 0})
    df['self_employed'] = df['self_employed'].replace({' Yes': 1, ' No': 0})
    df['loan_status'] = df['loan_status'].replace({' Approved': 1, ' Rejected': 0})
    X = df.drop('loan_status', axis=1)
    y = df['loan_status']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    data = {
    'no_of_dependents': int(data.GET['dependents']),
    'education': int(data.GET['education']),
    'self_employed': int(data.GET['self_employed']),
    'income_annum': int(data.GET['income_annum']),
    'loan_amount': int(data.GET['loan_amount']),
    'loan_term': int(data.GET['loan_term']),
    'cibil_score': int(data.GET['cibil_score']),
    'total_assets_value': int(data.GET['assets_value'])
    }
    input_df=pd.DataFrame(data,index=[0])
    predicted_status = model.predict(input_df)
    return predicted_status