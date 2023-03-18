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
# %%
list1[2]
# %%
list1[2][2]
# %%
list1[2][2][1]

# %%
list1.append?
# %% # The answer!
list1[2][2].append(7000)
# %%
list1
# %%
# Exercise 8: Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

# %%
list.append?
# %%
list1[2][1][2]
# %%
list1[2][1][2].append(sub_list)
# %%
list1
# %%
list1.extend?
# %%
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# %% The answer!
list1[2][1][2].extend(sub_list)
# %%
list1
# %%
# Exercise 9: Replace list’s item with new value if found
list1 = [5, 10, 15, 20, 25, 50, 20]
# %%
list.count?
# %%
list1.count(20)
# %%
dir(list)
# %% The answer!
list1[list1.index(20)] = 200
# %%
list1
# %%
# Exercise 10: Remove all occurrences of a specific item from a list.
list1 = [5, 20, 15, 20, 25, 50, 20]

# %%
list1.count(20)
# %%
list1.remove?
# %% The answer!
for _ in range(list1.count(20)):
    list1.remove(20)
list1
# %% 
# Dictionary exercise1: Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# %%
# solution1
dict1 = {}
for i in range(len(keys)):
    dict1[keys[i]] = values[i]
dict1
# %%
zip?
# %%
list(zip(keys, values))
# %%
# solution2
dict2 = {}
for key, value in zip(keys, values):
    dict2[key] = value
dict2
# %%
dict?
# %%
# solution3
dict(zip(keys, values))
# %%
dict(one=1, two=2)
# %%
# Dictionary exercise2: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Fourty': 40, 'Fifty': 50}
# %%
dict1 + dict2
# %%
dir(dict)
# %%
dict.fromkeys?
# %%
dict.keys?
# %%
dict.update?
# %%
# solution1
dict1.update(dict2)
# %%
dict1
# %%
dict?
# %%
# solution2
dict(**dict1, **dict2)
# %%
a = [1, 10]
# %%
range(*a)
# %%
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
# %%
# Exercise3
sampleDict["class"]["student"]["marks"]["history"]
# %%
dict.setdefault?
# %%
## Exercise4: Initialize dictianry with default values
employees_dict = {}
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
# %%
employees_dict.setdefault(employees, defaults)
# %%
dict.fromkeys?
# %%
dict.fromkeys(employees, defaults)
# %%
## Exercise5: Create a dictionary by extracting the keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
# %%
new_dict = {}
for key in keys:
    new_dict[key] = sample_dict[key]
new_dict
# %%
new_dict1 = {key: sample_dict[key] for key in keys}
new_dict1
# %%
## Exercise6: Delete a list of keys from dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
# %%
dict.pop?
# %%
dict.popitem?
# 
# %%
sample_dict.pop("name")
sample_dict.pop("salary")
sample_dict
# %%
list1 = [1, 2, 3, 4]
list2 = [1, 2]
list1 - list2
# %%
sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
# %%
sample_dict
# %%
sample_dict.keys?
# %%
sample_dict.keys()
# %%
# Exercise7: Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
# %%
sample_dict.values()
# %%
200 in sample_dict.values()
# %%
if 200 in sample_dict.values():
    print("200 present in a dict")
# %%
# Exercise8: Rename key of a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
# %%
dict.pop?
# %% 
# solution
sample_dict['location'] = sample_dict.pop('city')
sample_dict
# %%
# Exercise9: Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
# %%
sample_dict.values()
# %%
min(sample_dict.values())
# %%
min?
# %%
sample_dict.get
# %%
sample_dict.get?
# %%
# solution
min(*sample_dict)
# %%
# Exercise10: Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
# %%
sample_dict['emp3']['salary'] = 8500
sample_dict
# %%
zip?