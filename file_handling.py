file = open("test.txt", "r")
l = list(file)

pass
list_of_name = []
list_of_number = []
list_of_address = []

z = ""
a = ""
first = list(l[0])
for y in first:
    if y == " ":
        break
    else:
        z = z + y

for y in first:
    if y.isdigit():
        a = a + y

n_address_1 = ""
for y in first:
    if not y.isdigit():
        n_address_1 = n_address_1 + y
name_1 = n_address_1.split()

############Two#########

c = ""
n = ""
second = list(l[1])
for y in second:
    if y == " ":
        break
    else:
        c = c + y

for y in second:
    if y.isdigit():
        n = n + y

n_address_2 = ""
for y in second:
    if not y.isdigit():
        n_address_2 = n_address_2 + y
name_2 = n_address_2.split()

########Third#########

h = ""
m = ""
third = list(l[2])
for y in third:
    if y == " ":
        break
    else:
        h = h + y

for y in third:
    if y.isdigit():
        m = m + y
n_address_3 = ""
for y in third:
    if not y.isdigit():
        n_address_3 = n_address_3 + y
name_3 = n_address_3.split()

list_of_name.append(z)
list_of_name.append(c)
list_of_name.append(h)
list_of_number.append(a)
list_of_number.append(n)
list_of_number.append(m)
list_of_address.append(name_1[1])
list_of_address.append(name_2[1])
list_of_address.append(name_3[1])
print(list_of_name)
print(list_of_number)
print(list_of_address)
