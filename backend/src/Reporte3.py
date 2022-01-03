import sklearn

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures #grado
from sklearn.metrics import r2_score, mean_squared_error

# import matplotlib.pyplot as plt  # To visualize
from sklearn import preprocessing
from datetime import date   
import datetime as dt
import pandas as pd
import numpy as np


def Report3(body):

    poly = []
    dispers = []
    labels = []
    #___________________________________________________________________________________________
    # Step 1: trainign data.
    
    label1 = body['label1'] # label1  -> filtro
    label2 = body['label2'] # label2  -> encabezado 1
    label3 = body['label3'] # label3  -> encabezado 2
    isTime = body['isTime'] # label4  -> encabezado Tiempo
    filter = body['filter'] # label5  -> encabezado de Filtro
    content = body['content'] # content -> contenido
    
    filtro = False
    if(label1 != ''):
        filtro = True

    df = pd.DataFrame(content)

    if(isTime == '1'): # el encabezado 1 es fecha
      
        df[f'{label2}_ordinal'] = pd.to_datetime(df[label2], dayfirst = True).apply(lambda date: date.toordinal())
        label2 = f'{label2}_ordinal'

    # le = preprocessing.LabelEncoder()
    # x1_encoded = le.fit_transform(df[label2].to_numpy()) # encode por si la columan son strings.
    # x2_encoded = le.fit_transform(df[label3].to_numpy()) # no debería de ser necesario ya que la columna es int.

    # features  = list(zip(x1_encoded, x2_encoded)) # Convertir a Tupla.
    # print(f'List: {features}')
    # data = pd.DataFrame(features) # Convierte la tupla a dataFrame.
    
    if(filtro):
        X = np.asarray(df.loc[df[filter]==label1, [label2]])
        Y = np.asarray( df.loc[df[filter]==label1, [label3]]).reshape(-1,1)

    else:
        X = np.asarray(df[label2])
        Y = np.asarray(df[label3]).reshape(-1,1)

    i = 0
    if(isTime=='0' or isTime==''):
        while(i<len(X)):

            X[i] = f'{(i+1)}'
            i += 1

    X_TEMP = X
    
    i = 0
    while(i<len(X_TEMP)):

        if(filter):
            labels.append(str(X_TEMP[i][0]))
            poly.append({
                "x":str(X_TEMP[i][0]),
                "y":str(Y[i][0])
            })
            
        else:
            labels.append(str(X_TEMP[i]))
            poly.append({
                "x":str(X_TEMP[i]),
                "y":str(Y[i][0])
            })
        i += 1
    if(isTime == '1'):
        Y = Y.reshape(-1,1)

    X = X.reshape(-1,1)
    # plt.scatter(X,Y)
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
        if(filtro):
           dispers.append({
                "x":str(X_TEMP[i][0]),
                "y":str(Y_pred[i][1])
            }) 
        else:
            dispers.append({
                "x":str(X_TEMP[i]),
                "y":str(Y_pred[i][1])
            })
        i += 1
    
    #_________________________  __________________________________________________________________
    # Step 4: calculate bias and variance
    
    rmse = np.sqrt(mean_squared_error(Y, Y_pred, squared=False))
    r2 = r2_score(Y,Y_pred)
    # print('RSEME: ', rmse)
    # print('R2: ', r2)
   

    title = 'Indice de Progresión de la pandemia en {} \n Degree = {}; RMSE = {}; R2 = {}'.format(label1, nb_degree, round(rmse,2), round(r2,2))
    # plt.scatter(X, Y)
    # plt.plot(X, Y, color='red')
    # plt.plot(X, Y_pred, color='blue')
    # plt.savefig("reporte1.pdf")
    # plt.show()
    print(title)
    return poly, dispers, title, r2, labels


