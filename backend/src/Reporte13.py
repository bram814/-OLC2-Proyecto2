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

#7
def Report13(body):

    labels = []
    poly = []
    #___________________________________________________________________________________________
    # Step 1: trainign data.
    
    label1 = body['label1'] # label1  -> filtro
    label2 = body['label2'] # label2  -> encabezado 1
    label3 = body['label3'] # label3  -> encabezado 2
    filter = body['filter'] # label5  -> encabezado de Filtro
    content = body['content'] # content -> contenido
    
    labels.append(str(label2))
    labels.append(str(label3))
    
    filtro = False
    if(label1 != ''):
        filtro = True

    df = pd.DataFrame(content)

    # df.fillna(0, inplace=True)

    infectados = df[label2] # X
    
    edad = df[label3] # Y
    
    data = pd.concat([infectados,edad],axis=1)
    data.columns = [label2,label3]
    data.fillna(0,inplace=True);
    X_TRANSF = infectados
    edad_promedio = data.groupby(by=label2).describe()
    # print(edad_promedio)
    

    x = edad_promedio.index
    print(len(x))
    X_NEW = []
    i = 0
    while(i<len(x)):
        X_NEW.append(x[i])
        i += 1
    print(len(X_NEW))
    i = 0
    while(i<len(X_NEW)):
        poly.append({
                "x":str(X_TRANSF[i]),
                "y":str(X_NEW[i])
            }) 
        i+=1
    print(poly)
    title = 'Muertes promedio por casos confirmados y edad de covid 19 en un País.'.format(label1)
    # descr = 'Para {} hay una cantidad de {} que equivale al {}% ; Para {} hay una cantidad de {} que equivale al {}%'.format(label2, MEN, MEN_NEW*100, label3, FEMALE, FEMALE_NEW*100)
    
    return poly, title, labels

