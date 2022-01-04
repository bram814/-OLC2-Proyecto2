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


def Report12(body):

    poly = []
    dispers = []
    labels = []

    poly_new = []
    dispers_new = []
    labels_new = []
    #___________________________________________________________________________________________
    # Step 1: trainign data.
    
    label1 = body['label1'] # label1  -> filtro
    label2 = body['label2'] # label2  -> encabezado 1
    label3 = body['label3'] # label3  -> encabezado 2
    isTime = body['isTime'] # label4  -> encabezado Tiempo
    filter = body['filter'] # label5  -> encabezado de Filtro
    content = body['content'] # content -> contenido
    compararPais = body['compareCountry'] # comparativo
    
    filtro = False
    if(label1 != ''):
        filtro = True

    df = pd.DataFrame(content)

    if(isTime == '1'): # el encabezado 1 es fecha
      
        df[f'{label2}_ordinal'] = pd.to_datetime(df[label2], dayfirst = True).apply(lambda date: date.toordinal())
        label2 = f'{label2}_ordinal'
    
    if(filtro):
        X = np.asarray(df.loc[df[filter]==label1, [label2]])
        Y = np.asarray( df.loc[df[filter]==label1, [label3]]).reshape(-1,1)


        X_NEW = np.asarray(df.loc[df[filter]==compararPais, [label2]])
        Y_NEW = np.asarray( df.loc[df[filter]==label1, [label3]]).reshape(-1,1)

    else:
        X = np.asarray(df[label2])
        Y = np.asarray(df[label3]).reshape(-1,1)

        X_NEW = np.asarray(df[label2])
        Y_NEW = np.asarray(df[label3]).reshape(-1,1)

    i = 0
    if(isTime=='0' or isTime==''):
        while(i<len(X)):

            X[i] = f'{(i+1)}'
            i += 1


    i = 0
    if(isTime=='0' or isTime==''):
        while(i<len(X_NEW)):

            X_NEW[i] = f'{(i+1)}'
            i += 1


    X_TEMP = X
    X_TEMP_NEW = X_NEW
    
    
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

    
    i = 0
    while(i<len(X_TEMP_NEW)):

        if(filter):
            labels_new.append(str(X_TEMP_NEW[i][0]))
            poly_new.append({
                "x":str(X_TEMP_NEW[i][0]),
                "y":str(Y_NEW[i][0])
            })
            
        else:
            labels_new.append(str(X_TEMP_NEW[i]))
            poly_new.append({
                "x":str(X_TEMP_NEW[i]),
                "y":str(Y_NEW[i][0])
            })
        i += 1


    if(isTime == '1'):
        Y = Y.reshape(-1,1)
        Y_NEW = Y_NEW.reshape(-1,1)

    X = X.reshape(-1,1)
    X_NEW = X_NEW.reshape(-1,1)
    
    #___________________________________________________________________________________________
    # Step 2: data preparation.
        
    nb_degree = int(body['degree']) # Grado
    polyneal_feature = PolynomialFeatures(degree=nb_degree)
    X = polyneal_feature.fit_transform(X)
    Y = polyneal_feature.fit_transform(Y)

    polyneal_feature_new = PolynomialFeatures(degree=nb_degree)
    X_NEW = polyneal_feature_new.fit_transform(X)
    Y_NEW = polyneal_feature_new.fit_transform(Y)

    #___________________________________________________________________________________________
    # Step 3: define and train a model
        
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(X, Y)  # perform linear regression
    Y_pred = linear_regressor.predict(X)  # make predictions
    
        
    linear_regressor_new = LinearRegression()  # create object for the class
    linear_regressor_new.fit(X_NEW, Y_NEW)  # perform linear regression
    Y_pred_new = linear_regressor_new.predict(X_NEW)  # make predictions
    

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
    
    i = 0
    while(i<len(X_TEMP_NEW)):
        if(filtro):
           dispers_new.append({
                "x":str(X_TEMP_NEW[i][0]),
                "y":str(Y_pred_new[i][1])
            }) 
        else:
            dispers_new.append({
                "x":str(X_TEMP_NEW[i]),
                "y":str(Y_pred_new[i][1])
            })
        i += 1

    #_________________________  __________________________________________________________________
    # Step 4: calculate bias and variance
    
    rmse = np.sqrt(mean_squared_error(Y, Y_pred, squared=False))
    r2 = r2_score(Y,Y_pred)
    # print('RSEME: ', rmse)
    # print('R2: ', r2)
    
    rmse_new = np.sqrt(mean_squared_error(Y_NEW, Y_pred_new, squared=False))
    r2_new = r2_score(Y_NEW,Y_pred_new)
    # print('RSEME: ', rmse)
    # print('R2: ', r2)
    

    title = 'Ánalisis Comparativo entre el País {}: \n Degree = {}; RMSE = {}; R2 = {}, {}: \n Degree = {}; RMSE = {}; R2 = {}  '.format(label1, nb_degree, round(rmse,2), round(r2,2), compararPais, nb_degree, round(rmse_new,2), round(r2_new,2))

    NEW_POLY = []
    NEW_POLY.append(poly)
    NEW_POLY.append(poly_new)

    NEW_DISPERS = []
    NEW_DISPERS.append(dispers)
    NEW_DISPERS.append(dispers_new)

    NEW_LABELS = []
    NEW_LABELS.append(labels)
    NEW_LABELS.append(labels_new)
    
    i = 0 
    print("----------------")
    while(i<len(poly_new)):
        poly.append(poly_new[i])
        i+=1

    print("----------------")

    
    i = 0 
    while(i<len(dispers_new)):
        dispers.append(dispers_new[i])
        i+=1
        
    i = 0 
    while(i<len(labels_new)):
        labels.append(labels_new[i])
        i+=1


    return NEW_POLY, NEW_DISPERS, title, r2, NEW_LABELS


