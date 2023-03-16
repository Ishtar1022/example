# %%
list1 = [100, 200, 300, 400, 500]
# %%
list2 = []
list1_orginal_length = len(list1)
list1_copy = list1[:]
for _ in range(list1_orginal_length):
    list2.append(list1_copy.pop())
list2
# %%
list1.pop?
# %%
list2.append?
# %%
list2 = []
list1_orginal_length = len(list1)
for i in range(list1_orginal_length):
    list2.append(list1[4-i])
list2
# %%
list3 = [list1[(len(list1)-1)-i] for i in range(len(list1))]
list3
# %%
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
# %%
list3 = []
for i in range(len(list1)):
    list3.append(list1[i] + list2[i])
list3
# %%
list4 = [list1[i] + list2[i] for i in range(len(list1))]
list4
# %%
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
# %%
list5 = []
for i in list1:
    for j in list2:
        list5.append(i + j)
list5
    
# %%
list5 = [i + j for i in list1 for j in list2]
list5
# %%
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
# %%
for j in range(len(list2)):
    print(f"{list1[j]} {list2[(len(list2) - 1)- j]}")
# %%
list2.reverse()
for i in range(len(list1)):
    print(f"{list1[i]} {list2[i]}")

# %%
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# %%
list2 = []
for i in list1:
    if i:
        list2.append(i)
list2

# %%
list1.remove?
# %%
list1.count?
# %%
empty_value = list1.count("")
for _ in range(empty_value):
    list1.remove("")
list1
# %%
# Exercise 7: Add new item to list after a specified item
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]