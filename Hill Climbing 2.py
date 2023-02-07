def cal_cost(arr):
    n=len(arr)
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                c += 1
    return c

def State_generate(list):
    n=len(list)
    cost = cal_cost(list)
    arr = list.copy()
    for i in range(n):
        for j in range(i + 1, n):
            tmp = list.copy()
            temp = tmp[i]
            tmp[i] = tmp[j]
            tmp[j] = temp
            tmp_cost = cal_cost(tmp)
            if tmp_cost < cost:
                cost = tmp_cost
                arr = tmp.copy()
    return arr, cost


list=[2, 1, 5, 0, 8, 4, 10, 0, 20, 10]
cost = cal_cost(list)
while cost != 0:
    list, cost = State_generate(list)
print("Result:")
print("list: ", list)
print("cost: ", cost)
