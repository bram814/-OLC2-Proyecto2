import pandas as pd  # To read data

def csvToJson(csv): # si es un csv lo convierte a json

    lines = csv.split('\n') # separa por fila
    header = lines[0].split(',') # obtiene las cabeceras
   
    result = {} # guarda en un diccionario cada cabecera con su objeto.
    
    i = 0
    while(i<len(header)): # recorre todas las cabeceras
        j = 1
        obj = [] # array temporal
        
        while(j<len(lines)):

            currentLine = lines[j].split(',') # crea un objeto de la fila.
            z = 0
            if(len(currentLine)==1): # por si da error y aumenta un objeto.
                break
            
            while(z<len(currentLine)):
                if(header[i] == header[z]): # si es el mismo encabezado lo guarda en un array temporal.
                    obj.append(currentLine[z])
                    
                z += 1
            
            j += 1
       
        result[header[i]] = obj # guarda su header con su respectivo objeto.
        i += 1


    data = pd.DataFrame(result) # se convierte.
    return data, header
