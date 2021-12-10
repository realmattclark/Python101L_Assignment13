def total(values):
    sum = 0
    for i in values:
        sum += i
    return sum

def median(list):
    list = [4,3,1,5]
    list.sort()
    print(list)
    if len(list) %2 == 1:
        index = int(len(list)/2)
        return list[index]
    else:
        index = int(len(list)/2)
        sum = list[index] + list[index - 1]
        return sum/2


print(median(list))
