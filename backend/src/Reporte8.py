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

def Report8(body):

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
    predict = body['predict'] # label7 -> predict
    isPredict = body['isPredict'] # label8 -> si es fecha la predicción
    content = body['content'] # content -> contenido
    
    filtro = False
    if(label1 != ''):
        filtro = True

    df = pd.DataFrame(content)

    if(isTime == '1'): # el encabezado 1 es fecha
        temp = label2
        df[f'{label2}_ordinal'] = pd.to_datetime(df[label2], dayfirst = True).apply(lambda date: date.toordinal())
        label2 = f'{label2}_ordinal'

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
    
    #___________________________________________________________________________________________
    # Step 4: calculate bias and variance
    
    rmse = np.sqrt(mean_squared_error(Y, Y_pred, squared=False))
    r2 = r2_score(Y,Y_pred)
    # print('RSEME: ', rmse)
    # print('R2: ', r2)
    title = 'Tendencia del número de infectados por día del País {}  \n Degree = {}; RMSE = {}; R2 = {}'.format(label1, nb_degree, round(rmse,2), round(r2,2))
    title += '\n| Y =' + str(linear_regressor.coef_[1][1]) + 'X+ (' + str(linear_regressor.intercept_[1])+ ')'
    #___________________________________________________________________________________________
    # Step 5: prediction
    

    if(isPredict == '1'):
        d = pd.to_datetime(predict, dayfirst = True)
        predict = d.toordinal()

        new_predict = linear_regressor.predict(polyneal_feature.fit_transform([[predict]]))[0][1]
    else:
        
        d = pd.to_datetime(df[temp].max(), dayfirst = True).toordinal() + 365

    predict = d

    new_predict = linear_regressor.predict(polyneal_feature.fit_transform([[predict]]))[0][1]


   
    return poly, dispers, title, new_predict, labels