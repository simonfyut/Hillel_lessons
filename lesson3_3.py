# list1 = [12, 3, 4, 10]
# x = list1[-1]       # x = 10
# y = [x]             # y = [10]



list1 = [1, 2, 3, 4, 5, 6]
my_list1 =[list1[0:3]] + [list1[3:]]
print(my_list1)

list2 = [1, 2, 3]
my_list2 = [list2[0:2]] + [list2[2:]]
print(my_list2)

list3 = [1, 2, 3, 4, 5]
my_list3 = [list3[0:3]] + [list3[3:]]
print(my_list3)

list4 = [1]
list4_1 = []
list_summ = [list4] + [list4_1]
print(list_summ)


list5 = []
list6 = []
list_sum = [list5] + [list6]
print(list_sum)
