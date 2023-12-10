from functools import reduce


list1 = [[1, 2, 3],[2, 8, 9],[7, 123, 8]]
list2 = [[1], [2], [3, 4, 4, 4], [123456789]]
list3 = [[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]]


def find_sum(lists):
    list_fin = set([])
    repeat = set([])
    
    for cur_list in lists:
        cur_list = set(cur_list)
        for i in cur_list:
            if i in repeat:
                list_fin.add(i)
            else:
                repeat.add(i)

    return reduce(lambda sum, x: sum+x, list_fin, 0)

print(find_sum(list1))
print(find_sum(list2))
print(find_sum(list3))

