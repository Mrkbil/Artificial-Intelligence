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


file = open('Dataset/iris.csv')
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


def find_majorClass(sample, features, n):
    major = []
    for i in range(n):
        major.append(0)
    for i in sample:
        index = int(i.t[features])
        print("index: ",index)
        major[index] += 1
    return major.index(max(major))


def KNN(val, train, features, K):
    t_list = []
    currect = 0
    for i in val:
        for j in train:
            sum = 0
            for k in range(features):
                sum += (j[k] - i[k]) ** 2
            euc = np.sqrt(sum)
            t_list.append(Euc(j, euc))
            # print("Euc: ",j,euc)
        t_list.sort(key=lambda x: x.euc)
        k_sample = t_list[:K]
        for z in k_sample:
            print(z.euc,z.t)
        majority = find_majorClass(k_sample, features, 3)
        print(i)
        print("Majority: ",majority,i[features])
        if i[features] == majority:
            print("true")
            currect += 1
    return currect / len(val)


K = 5
accuracy = KNN(validation_set, training_Set, features, K)
accuracy2 = KNN(test_set, training_Set, features, K)
print("{:.2f}%".format(accuracy * 100))
print("{:.2f}%".format(accuracy2 * 100))
