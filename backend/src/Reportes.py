from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures #grado
from sklearn.metrics import r2_score, mean_squared_error

import matplotlib.pyplot as plt  # To visualize
from sklearn import preprocessing
import pandas as pd
import numpy as np


def Reporte1(body):

    poly = []
    dispers = []
    labels = []
    #___________________________________________________________________________________________
    # Step 1: trainign data.
    
    label1 = body['label1'] # label1  -> filtro
    label2 = body['label2'] # label2  -> encabezado 1
    label3 = body['label3']  # label3  -> encabezado 2
    content = body['content'] # content -> contenido
    
    filtro = False
    if(label1 != ''):
        filtro = True

    df = pd.DataFrame(content)
    

    # le = preprocessing.LabelEncoder()
    # x1_encoded = le.fit_transform(df[label2].to_numpy()) # encode por si la columan son strings.
    # x2_encoded = le.fit_transform(df[label3].to_numpy()) # no debería de ser necesario ya que la columna es int.

    # features  = list(zip(x1_encoded, x2_encoded)) # Convertir a Tupla.
    # print(f'List: {features}')
    # data = pd.DataFrame(features) # Convierte la tupla a dataFrame.
    
    
    #     X = np.asarray(df[label2]=='Guatemala')
    # else:
    X = np.asarray(df[label2])
    Y = np.asarray(df[label3]).reshape(-1,1)
    
    i = 0
    while(i<len(X)):
        # temp.append(i+1)
        X[i] = f'{(i+1)}'
        i += 1

    X_TEMP = X
    i = 0
    while(i<len(X_TEMP)):

        labels.append(X_TEMP[i])
        poly.append({
            "x":X_TEMP[i],
            "y":Y[i][0]
        })
        i += 1
    
    X = X.reshape(-1,1)
    #___________________________________________________________________________________________
    # Step 2: data preparation.
        
    nb_degree = int(body['degree']) # Grado
    polyneal_feature = PolynomialFeatures(degree=nb_degree)
    X = polyneal_feature.fit_transform(X)
    Y = polyneal_feature.fit_transform(Y)


    #___________________________________________________________________________________________
    # Step 3: define and train a model
        
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(X, Y)  # perform linear regression
    Y_pred = linear_regressor.predict(X)  # make predictions

    
    i = 0
    while(i<len(X_TEMP)):
        dispers.append({
            "x":X_TEMP[i],
            "y":Y_pred[i][1]
        })
        i += 1

  
    
    #_________________________  __________________________________________________________________
    # Step 4: calculate bias and variance
    
    rmse = np.sqrt(mean_squared_error(Y, Y_pred, squared=False))
    r2 = r2_score(Y,Y_pred)
    # print('RSEME: ', rmse)
    # print('R2: ', r2)

    title = 'Degree = {}; RMSE = {}; R2 = {}'.format(nb_degree, round(rmse,2), round(r2,2))

    return poly, dispers, rmse, r2, labels
