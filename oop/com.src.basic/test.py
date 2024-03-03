lst=[1,3,5,7,9,2,4,6,8,10]
print(lst[1:])
print(list(zip(lst,lst[1:])))

mac = max([j-i for i, i in zip(lst,lst[1:])])
