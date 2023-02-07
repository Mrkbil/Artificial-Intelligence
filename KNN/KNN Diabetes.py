import csv
import random
import numpy as np


class Euc:
    def __init__(self, t, euc):
        self.t = t
        self.euc = euc

    def __str__(self):
        self.t
        self.euc


file = open('Dataset/diabetes.csv')
data = csv.reader(file)
data_list = []
for row in data:
    data_list.append(row)

training_Set = []
test_set = []
validation_set = []
random.shuffle(data_list)
for i in data_list:
    prob = np.random.random()
    if 0 <= prob <= 0.7:
        training_Set.append(list(map(float, i)))
    elif 0.7 < prob <= 0.85:
        test_set.append(list(map(float, i)))
    else:
        validation_set.append(list(map(float, i)))

features = len(training_Set[0]) - 1


def avg_output(k_sample, features, K):
    sum = 0
    for i in k_sample:
        sum += i.t[features]
    avg = sum / K
    return avg


def KNN(val, train, features, K):
    t_list = []
    Error = 0
    for i in val:
        for j in train:
            sum = 0
            for k in range(features):
                sum += (i[k] - j[k]) ** 2
            euc = np.sqrt(sum)
            t_list.append(Euc(j, euc))
        t_list.sort(key=lambda x: x.euc)
        k_sample = t_list[:K]
        avg = avg_output(k_sample, features, K)
        Error = Error + (i[features] - avg)**2
    MeanSquereError = Error / len(val)
    return MeanSquereError


K = 5
error = KNN(validation_set, training_Set, features, K)
error2 = KNN(test_set, training_Set, features, K)
print("{:.2f}".format(error))
print("{:.2f}".format(error2))
