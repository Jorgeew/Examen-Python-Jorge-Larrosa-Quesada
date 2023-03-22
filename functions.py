import csv

def read_data():
    dict = {}
    with open('winequality.csv', 'r') as file:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            dict['dato' + str(i)] = {'type': row[0], 'fixed acidity': row[1], 'volatile acidity': row[2], 'citrid acid': row[3], 'residual sugar': row[4], 'chlororides': row[5], 'free sulfur dioxide' : row[6], 'total sulfur dioxide': row[7], 'density': row[8], 'PH': row[9], 'sulphates': row[10], 'alcohol': row[11], 'quality': row[12]}
            i+=1
    dict.pop('dato0')
    return dict

def split(dict1):
    dictWhite = {}
    dictRed = {}
    for i in dict1.keys():
        for key, value in dict1[i].items():
            if(key == 'type'):
                if(dict1[i]['type'] == 'white'):
                    dictWhite[i] = dict1[i]
                else:
                    if(dict1[i]['type'] == 'red'):
                        dictRed[i] = dict1[i]

    return dictWhite, dictRed

def reduce(dict1, atributo):
    #print(dict1.items())
    for i in dict1.keys():
        for key, values in dict1[i].items():
            if(key == atributo):
                print(dict1[i][atributo])




   
   
        
    


