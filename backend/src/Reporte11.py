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


def Report11(body):
   
    labels = []
    value = []
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

    
    if(filtro):
        df = df[df[filter]==label1]

        MEN = df[label2]
        FEMALE = df[label3]

    else:
        MEN = df[label2]
        FEMALE = df[label3]
    print("---------")

    i =0
    MEN_NEW = 0
    while(i<len(MEN)):
        MEN_NEW += int(MEN[i])
        i += 1
    
    i =0
    FEMALE_NEW = 0
    while(i<len(FEMALE)):
        FEMALE_NEW += int(FEMALE[i])
        i += 1
    
    MEN = MEN_NEW
    FEMALE = FEMALE_NEW

    TOTAL = MEN + FEMALE 
    MEN_NEW = (MEN + 100) / TOTAL          # % MEM 
    FEMALE_NEW = (FEMALE + 100) / TOTAL    # % FEMALE

    value.append(MEN_NEW)
    value.append(FEMALE_NEW)


    title = 'Porcentaje de hombres infectados por covid-19 en el Pais de {} desde el primer caso activo.'.format(label1)
    descr = 'Para {} hay una cantidad de {} que equivale al {}% ; Para {} hay una cantidad de {} que equivale al {}%'.format(label2, MEN, MEN_NEW*100, label3, FEMALE, FEMALE_NEW*100)
    
    return value, title, labels, descr