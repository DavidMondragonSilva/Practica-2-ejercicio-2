import matplotlib.pyplot as plt
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score



import numpy as np
import csv

def euclidean_distance(x1, x2):
    distance = np.sqrt(np.sum((x1-x2)**2))
    return distance
def accuracy(y_pred, y_test):
    return np.sum(y_pred==y_test)/len(y_test)

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions

    def _predict(self, x):
        #Calcular distancias
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        #Obtener la k mas cercana
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        #Mayoria
        most_common = Counter(k_nearest_labels).most_common()
        return most_common[0][0]
        

print("K nearest neighbors")
print("Cual dataset vas a usar? (1 a 3)")
dataset = int(float(input()))
if(dataset == 1):
    X = np.ndarray(shape=(63,1), dtype=float, order='F')
    y = np.ndarray(shape=(63), dtype=float, order='F')
    cont = 0
    with open("./Dataset1.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            X[cont][0] = row[0]
            y[cont] = row[1]
            cont = cont +1
        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state=1234)
        clf = KNN(k=5)
        clf.fit(X_train, y_train)
        predictions = clf.predict(X_test)
        acc = accuracy(predictions, y_test)
        print("Accuracy:")
        print(acc)

elif(dataset == 2):
    X2 = np.ndarray(shape=(4898,11), dtype=float, order='F')
    y2 = np.ndarray(shape=(4898), dtype=float, order='F')
    cont = 0
    with open("./Dataset2.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            X2[cont][0] = row[0]
            X2[cont][1] = row[1]
            X2[cont][2] = row[2]
            X2[cont][3] = row[3]
            X2[cont][3] = row[3]
            X2[cont][4] = row[4]
            X2[cont][5] = row[5]
            X2[cont][6] = row[6]
            X2[cont][7] = row[7]
            X2[cont][8] = row[8]
            X2[cont][9] = row[9]
            X2[cont][10] = row[10]
            y2[cont] = row[11]
            cont = cont +1
        X_train, X_test, y_train, y_test = train_test_split(X2,y2, test_size = 0.2, random_state=1234)
        clf = KNN(k=5)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        acc = accuracy(y_pred, y_test)
        print("Accuracy:")
        print(acc)
        precision = precision_score(y_test, y_pred,average='macro', zero_division=1)
        print("Precision:")
        print(precision)
        sensitivity = recall_score(y_test, y_pred,average='macro', zero_division=1)
        print("Sensitivity:")
        print(sensitivity)
        f1 = f1_score(y_test, y_pred,average='macro', zero_division=1)
        print("F1 score:")
        print(f1)
        
elif(dataset == 3):
    X3 = np.ndarray(shape=(768,8), dtype=float, order='F')
    y3 = np.ndarray(shape=(768), dtype=float, order='F')
    cont = 0
    with open("./Dataset3.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            X3[cont][0] = row[0]
            X3[cont][1] = row[1]
            X3[cont][2] = row[2]
            X3[cont][3] = row[3]
            X3[cont][3] = row[3]
            X3[cont][4] = row[4]
            X3[cont][5] = row[5]
            X3[cont][6] = row[6]
            X3[cont][7] = row[7]
            y3[cont] = row[8]
            cont = cont +1
        X_train, X_test, y_train, y_test = train_test_split(X3,y3, test_size = 0.2, random_state=1234)
        clf = KNN(k=5)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        acc = accuracy(y_pred, y_test)
        print("Accuracy:")
        print(acc)
        precision = precision_score(y_test, y_pred,average='macro', zero_division=1)
        print("Precision:")
        print(precision)
        sensitivity = recall_score(y_test, y_pred,average='macro', zero_division=1)
        print("Sensitivity:")
        print(sensitivity)
        tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
        specificity = tn / (tn + fp)
        print("Specifity:")
        print(specificity)
        f1 = f1_score(y_test, y_pred,average='macro', zero_division=1)
        print("F1 score:")
        print(f1)

else:
    print("Opcion invalida")
print("Programa terminado, presiona enter para terminar")
input()

