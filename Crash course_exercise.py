# %%
# Exercise 2-3
a = 'Eric'

print("Hello " + a + ", would you like to learn some Python today?")
# %%
# Exercise 2-4
a = 'mark'
print(a.lower())
# %%
print(a.upper())
# %%
print(a.title())
# %%
# Exercise 2-6
famous_person = 'Albert Einstain'
quote_1 = r' "A person who never made a mistake never tried anything new."'
message = famous_person + ' once said,' + quote_1
print(message)
# %%
# Exercise 2-7
a = ' Aiden '
print(a.lstrip())
print(a.rstrip())
print(a.strip())
# %%
# Exercise 2-9
b = 9
message_1 = "My favourate number is " + str(b)
print(message_1)
# %%
# Exercise 3-1 
names = ['dorisky', 'Ouni', 'Jie', 'Wanlin']
message_2 = "I miss u, " + names[0].title()
print(message_2)

# %%
# Exercise 3-4
guest_list = ['dorisky', 'ouni', 'jie', 'miao']
message_3 = 'Let us eat dinner together, ' + guest_list[-1]
print(message_3)
# %%
guest_list[1] = 'wanlin'
print(guest_list)
# %%
guest_list.insert(2, 'Babe')
print(guest_list)
# %%
guest_list.append('ting')
print(guest_list)
# %%
message_4 = "Hello " + guest_list[2] + ", I found a bigger table for dinner. "
print(message_4)
# %%
not_come1 = guest_list.pop()
print(not_come1)
print(guest_list)
message_5 = "Sorry " + not_come1 + ", we can meet next time."
print(message_5)
# %%
del guest_list[0]
print(guest_list)
# %%
guest_list.pop()
print(guest_list)



# %%
rivers = {'Nile': 'egypt', 'missipi': 'usa', 'thames': 'uk'}
for key in rivers.keys():
    print("The " + key.title() + " runs through " + rivers[key] + ".")
# %%
for key, value in rivers.items():
    print("The " + key.title() + " runs through " + value + ".")
# %%
