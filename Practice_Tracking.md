# Python Exercise

## Exercise 1: Reverse a list in Python

**Given:** 
>list1 = [100, 200, 300, 400, 500]

**Expected output:**
>[500, 400, 300, 200, 100]

**Solution:**
**1. use the reverse( ) function**

    ```python
    list1 = [100, 200, 300, 400, 500]
    list1.reverse()
    print(list1)
    ```

**2. use an empty list + for loop + append( ) + pop( )**
   
    ```python
    list2 = []
    list1_orginal_length = len(list1)     🐰1
    list1_copy = list1[:]                 🐰2
    for _ in range(list1_orginal_length): 🐰3
        list2.append(list1_copy.pop())
    list2
    ```

🐰1: 这一步是为了将 list1 的长度**固定**住
🐰2: 这里是为了**不改变原 list1**
🐰3: ~~`for i in range(list1):`~~, 
     因为如果这样写的话，在每一次loop中，*list1的长度是会发生改变的*。这样写的话，程序的运行过程会变成，

>- 第一次loop，i = 100，list2 中增加 500
>
>- 第二次loop，i = 200，list1 变成 [100,200,300,400] ，list2中 append 400
>- 第三次loop，i = 300, list1 变成 [100,200,300] ，list2中 append 300
然后就不执行了

**3. algorithm**

```python 
list2 = []
list1_orginal_length = len(list1)
for i in range(list1_orginal_length):
    list2.append(list1[4-i])               🐰4
list2
```
🐰4: 除了**pop method**以外，可以将 value 从list1中，取出来的办法

**4. 用 list comprehension 写**
   
```python
list3 = [list1[(len(list1)-1)-i] for i in range(len(list1))]
list3
```
- `len(list1)` = 5
`range(len(list1))`即 `range(5)`会生成 0,1,2,3,4 五个数字
`for i in range(len(list1))`
即 i = 0, i = 1, i = 2, i = 3, i = 4 循环五次

- 这里的 **`list1[(len(list1)-1)-i]`** 其实就是 **`list1[4-i]`**
因为i = 0时，所需要取出来的 value 是 list1 中 index 为 4 的数
i = 1， index 为 3
...
相加都是4
所以，需要取出来的数字即为 `list1[4-i]`
- list comprehension 的写法就是，因为已经在一个 list 中了，所以可以先写后半句 for statement，然后再写，需要 append 到list中的 value 的运算方式。

## Exercise 2: Concatenate two lists index-wise

**Given:** 
>list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

**Expected output:**
>['My', 'name', 'is', 'Kelly']

**Solution:**

**1. for loop**

```python
   list3 = []
for i in range(len(list1)):
    list3.append(list1[i] + list2[i])
list3
```
🐰 这里用 ***index*** 来对两个 list 进行loop，而不是用 list 中的 item 来进行 loop
**i** 在这里需要循环 4 次，4 用 **`len(list1)`** 来表示

**2. list comprehension**
   
```python
list4 = [list1[i] + list2[i] for i in range(len(list1))]
list4
```

## Exercise 4: Concatenate two lists in the following order

**Given:** 
>list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

**Expected output:**
>['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

**Solution:**

**1. Nested for loop**

```python
list5 = []
for i in list1
    for j in list2:
        list5.append(i + j)
list5
```
🐰 这里用 ***item*** 来对两个 list 进行 loop 更简单
这道题有点像排列组合，本质上是 2 个loop，
>第一个loop中，`list1[0]`需要与 `list2[0]` 和 `list2[1]`分别 concatenate
第二个loop中，`list1[1]`需要与`list2[0]`和`list2[1]`分别 concatenate

所以可以用 ***nested for loop*** 来实现

**2. list comprehension**

```python
list5 = [i + j for i in list1 for j in list2]
list5
```

## Exercise 5: Iterate both lists simultaneously

**Given:** 
>list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

**Expected output:**
>10 400
20 300
30 200
40 100

**Solution:**

**1. for loop**

```python
for j in range(len(list2)):
    print(f"{list1[j]} {list2[(len(list2) - 1)- j]}")
```

🐰 这道题的关键在于 **reverse list2** 以实现 list1 与 list2_reverse 的concatenation
🐰 这里print两个需要运算的string，进行concatenation，最简单的办法就是 
`fstring`
 - **f""** - 注意里面需要运算的部分要加 **curly brackets { }**

🐰 用 ***index*** 对两个list进行loop
`list1[0]`需要与`list2[3]`进行concatenate
 - 和之前 exercise1 的 solution3 中的算法很相似，两个 index 相加等于一个固定的值 
    
  所以当 j = 0, `list1[j]` 即为 `list[0]` ; `list2[len(list2)-1-j]`即为 `list2[3]`

**2. reverse function**

```python
list2.reverse()
for i in range(len(list1)):
    print(f"{list1[i]} {list2[i]}")
```

🐰不要这样写
 - ~~list2_copy = list2.reverse()~~

注意 `list2.reverse()`是一个**IN PLACE CHANGE**, 并不会 return value，所以不能 被赋值和保存给一个 new list


## Exercise 6: Remove empty strings from the list of strings

**Given:** 
>list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

**Expected output:**
>["Mike", "Emma", "Kelly", "Brad"]

**Solution:**

**1. empty list + if statement**

```python
list2 = []
for i in list1:
    if i:   # i 为empty value时，python会判定为 False
        list2.append(i)
list2
```

**2. remove method + for loop**

```python
empty_value = list1.count("")
for _ in range(empty_value):
    list1.remove("")
list1
```

**count( )** - Return number of occurrences of value.
**remove( )** - Remove first occurrence of value.
>🍓所以，可以通过count method数空白值出现的次数，然后用 for loop和 remove method把空白值去掉。

🐰 不要这样写
 - ~~for i in list1:~~
~~if i:~~
~~____list1.remove(i)~~

>🍓因为`remove()`对 list1会造成 **IN PLACE CHANGE**，所以 list1 发生改变以后，loop的内容也会发生改变。


# Dictionary Exercise

## Exercise1: Convert two lists into a dictionary

**Given:** 
>keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

**Expected output:**
>{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

**Solution:**

**1. for loop 用相同 index 进行 loop**

```python
dict1 = {}
for i in range(len(keys)):
    dict1[keys[i]] = values[i]
dict1
```

**2. 用 **zip( )** function**

```python
dict2 = {}
for key, value in zip(keys, values):
    dict2[key] = value
dict2
```

🐰 因为`zip()`可以把两个 list 变成成对的 tuple：
>用 `list(zip(keys, values))` 可以显示 zip()
>
>[('Ten', 10), ('Twenty', 20), ('Thirty', 30)]

因为是 **tuple**，所以就可以使用**对位拆解**。

**3. 用 builtin function - dict()**
   
```python
dict(zip(keys, values))
```

🐰 dict() function 
 - docstring 中的第二条，即 mapping 部分是一个 (key, value) pair 的时候，function会自动拆解。
>dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs

## Exercise2: Merge two Python dictionaries into one

**Given:** 
>dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Fourty': 40, 'Fifty': 50}

**Expected output:**
>{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

**Solution:**

**1. 用 dict.update()这个method**

```python
dict1.update(dict2)
```

🐰 `dict.update()` 的用法是
>**Docstring:**
D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
从 dict E or 可迭代的 E 中，执行以下操作
>- If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
如果 E 是一个可以执行 .keys()的object，那么
🍓__将原 Dict中，key与E相同部分，update 为 E 中的 value
🍓__原 Dict 中如果没有，则添加 E 中的 key-value pair。
>>
>- **类似于对 E 中的 key-value pair进行了一个 for loop**
> `for key in dict2:`
>____`dic1[key] = dict2[key]`
>>
>- If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]

**2. 用 dict() 这个function**

```python
dict(**dict1, **dict2)
```
🐰 dict()的用法是
>dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)
>>
> ** 的意思，当 function()中被赋值的参数，本身就是一个集合的时候，两个 * 就会执行“拆解”的操作
> 
> 即，**dict 就会把 dict 拆解成 key-value pair

🍓 譬如，下面这个example中，
```python
    a = [1, 10]
    range(*a)

# 上面的output为 range(1, 10)，所以 a 被拆解了
```

## Exercise4: Initialize dictionary with default values

**Given:** 
>employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

**Expected output:**
>{'Kelly': {'designation': 'Developer', 'salary': 8000},
 'Emma': {'designation': 'Developer', 'salary': 8000}}

**Solution:**

**1. dict.fromkeys()**

```python
dict.fromkeys(employees, defaults)
```

🐰 `dict.fromkeys()`
>Signature: dict.fromkeys(iterable, value=None, /)
Docstring: Create a new dictionary with keys from **iterable** and **values** set to value.
>
>🍓 forward slash / 标注 method中的是 positional arguments，不用在执行的时候把 = 前面的写在 method 里面

这里不能用 ~~dict.setdefault()~~, 因为 `setdefault()` 这个method，

- ‘Insert key with a value of default if key is not in the dictionary.’
  
所添加的key **只能是一个 value值，不能是一个list / dict** （只能一对一对添加）


## Exercise5: Create a dictionary by extracting the keys from a dictionary

**Given:** 
>sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
>
> 'Keys to extract
keys = ["name", "salary"]

**Expected output:**
>{'name': 'Kelly', 'salary': 8000}

**Solution:**

**1. 用 for loop**

```python
new_dict = {}
for key in keys:
    new_dict[key] = sample_dict[key]
new_dict
```

**2. 用 comprehension 写**

```python
new_dict1 = {key: sample_dict[key] for key in keys}
new_dict1
```

🐰 与 list comprehension 很相像，记得加 **key:**

## Exercise6: Delete a list of keys from dictionary

**Given:** 
>sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
Keys to remove
keys = ["name", "salary"]

**Expected output:**
>{'name': 'Kelly', 'salary': 8000}

**Solution:**

**1. 用 `dict.pop()`**
   
```python
sample_dict.pop("name")
sample_dict.pop("salary")
sample_dict
```
🐰 dict.pop() 是指定一个 key，就可以删除对应的 value
🐰 注意不能用 ~~`dict.popitem()`~~
>因为 popitem 中的 docstring 有规定
>- Pairs are returned in LIFO (last-in, first-out) order.
是有删除的顺序的，后进先出。

## Exercise7: Check if a value exists in a dictionary

**Given:** 
>sample_dict = {'a': 100, 'b': 200, 'c': 300}

**Expected output:**
>200 present in a dict

**Solution:**

**1. 用 if statement 来进行判断**

```python
if 200 in sample_dict.values():
    print("200 present in a dict")
```

🐰 因为 `dict.values()`可以给出的output是：
dict_values([100, 200, 300])

 - 所以可以用 if statement 来判断 ‘200’ 是否在里面

## Exercise8: Rename key of a dictionary

**Given:** 
>sample_dict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}

**Expected output:**
>{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

**Solution:**

**1. 用normal的添加 key-value pair的方式 + pop method**

```python
sample_dict['location'] = sample_dict.pop('city')
```

🐰 思路是：先把旧的 key-value pair 删掉，然后再添加一对新的。
 - 但是需要把原来的 value 进行保存，在赋值到新的 key 上
  
🍓 pop() method，**会将被 pop 的 key 所对应的 value return，**
 - 所以这个 return value 是可以被保存的，
 - 直接用 ‘location’ 这个新的 key 来进行保存——就实现了 **rename**
  
>可以跟 exercise10 对比一下，8是改写 key，10是改写 value

## Exercise9: Get the key of a minimum value from the following dictionary

**Given:** 
>sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}

**Expected output:**
>Math

**Solution:**

**1. min() 的一种神奇的写法**  @#¥%?!!

```python
min(*sample_dict)
```
🐰 因为 * 是可以对 dict 进行拆解的
>`min()` 的 docstring 中最后一条写道：
With two or more arguments, return the smallest argument.

**2. min()**
   
```python
min(sample_dict, key=sample_dict.get)
```

🐰 `dict.get()` 如果 key 在 dict 中，该 method 会返回 该 key 所对应的 value
Return the value for key if key is in the dictionary, else default.

## Exercise10: Change value of a key in a nested dictionary

**Given:** 
>sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

**Expected output:**
>sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

**Solution:**

**1. 直接改写**
   
```python
sample_dict['emp3']['salary'] = 8500
sample_dict
```