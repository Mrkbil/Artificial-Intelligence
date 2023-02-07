import time
import numpy as np


def compute_cost(list):
    cost = 0
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                cost += 1
    return cost

def goal_test(list):
    cost=compute_cost(list)
    if(cost==0):
        return True
    else:
        return False

def generate_sequence(list):
    print("Initial List: ", list)
    cost = compute_cost(list)
    arr = list.copy()
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            tmp_list = list.copy()
            tmp = tmp_list[i]
            tmp_list[i] = tmp_list[j]
            tmp_list[j] = tmp
            tmp_cost = compute_cost(tmp_list)
            # print("TmpList & TmpCost: ",tmp_list,tmp_cost)
            if(goal_test(tmp_list)):
                return tmp_list,tmp_cost
            if tmp_cost < cost:
                cost = tmp_cost
                arr = tmp_list.copy()
    print("Min Cost list on iteration: ", arr, cost)
    return arr, cost


list=[2, 1, 5, 0, 8, 4, 10, 0, 20, 10]
list1 = [2, 1, 5, 0]
list2 = np.random.randint(100, size=(10))
print(list)
cost = compute_cost(list)
start = time.time()
while cost != 0:
    list, cost = generate_sequence(list)
end = time.time()
print("Result list & cost: ", list, cost)
print("Time taken:",end - start)
# 1267 sec
