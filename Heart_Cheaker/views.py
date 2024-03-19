from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    df = pd.read_csv(r'C:\Users\User\3D Objects\ML poject\df_ful.csv')
    x = df.drop(['Unnamed: 0','Class'], axis=1)
    y = df['Class']
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=.20, random_state=1)
    Rfc = RandomForestClassifier()
    Rfc.fit(xtest, ytest)

    v1 = int(request.GET['n1'])
    v2 = str(request.GET['n2'])
    v3 = str(request.GET['n3'])
    v4 = str(request.GET['n4'])
    v5 = str(request.GET['n5'])
    v6 = str(request.GET['n6'])
    v7 = int(request.GET['n7'])
    v8 = str(request.GET['n8'])
    v9 = float(request.GET['n9'])
    v10 = str(request.GET['n10'])
    v11 = int(request.GET['n11'])
    v12 = int(request.GET['n12'])

    pre = Rfc.predict(np.array([v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12]).reshape(1,-1))
    pred=""
    if pre==[0]:
        pred='You are away from thyroid'
    else:
        pred='You have to visit a doctor'
    return render(request, 'predict.html', {"result2":pred})