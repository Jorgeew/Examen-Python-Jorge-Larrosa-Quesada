import csv

def read_data():
    dict = {type}
    with open('winequality.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dict += {'type': row[0], 'fixed acidity': row[1], 'volatile acidity': row[2], 'citrid acid': row[3], 'residual sugar': row[4], 'chlororides': row[5], 'free sulfur dioxide' : row[6], 'total sulfur dioxide': row[7], 'density': row[8], 'PH': row[9], 'sulphates': row[10], 'alcohol': row[11], 'quality': row[12]}
    print(dict)

read_data()