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

🐰1: 这一步是为了将 list1 的长度 **固定** 住
🐰2: 这里是为了==不改变原 list1==
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
`range(len(list1))`即`range(5)`会生成 0,1,2,3,4 五个数字
`for i in range(len(list1))`
即 i = 0， i = 1, i = 2, i = 3, i = 4 循环五次

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
>**f""** - 注意里面需要运算的部分要加 **curly brackets { }**

🐰 用 ***index*** 对两个list进行loop
`list1[0]`需要与`list2[3]`进行concatenate
>和之前 exercise1 的 solution3 中的算法很相似，两个 index 相加等于一个固定的值 
    
 - 所以当 j = 0, `list1[j]` 即为 `list[0]` ; 
  `list2[len(list2)-1-j]`即为 `list2[3]`

**2. reverse function**

```python
list2.reverse()
for i in range(len(list1)):
    print(f"{list1[i]} {list2[i]}")
```
🐰 ~~list2_copy = list2.reverse()~~ 
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
>🍓所以可以通过count method数空白值出现的次数，然后用for loop和remove method把空白值去掉。

🐰 不要这样写
|||
|:-|:-|
|~~for i in list1:~~|| 
|~~if i:~~||
||~~list1.remove(i)~~|

>🍓因为`remove()`对 list1会造成 **IN PLACE CHANGE**，所以 list1 发生改变以后，loop的内容也会发生改变。