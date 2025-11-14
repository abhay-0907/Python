item1 = 5
item2 = 5.0
item3 = "5"
item4 = True
item5 = [1,2]
item6 = (1,2)
item7 = {1,2}
item8 = {"a":1}
print(type(item1)) # <class 'int'>
print(type(item2)) # <class 'float'>
print(type(item3)) # <class 'str'>
print(type(item4)) # <class 'bool'>
print(type(item5)) # <class 'list'>
print(type(item6)) # <class 'tuple'>
print(type(item7)) # <class 'set'>
print(type(item8)) # <class 'dict'>

string = "5"
num = int(string) + 10
print(num)

myString = "Python Programming"

print(len(myString))
myString = myString.lower()

nums = 10;
print(nums%2==0)



ls = [1,2,3]
print(ls)
ls.append(4)
print(ls)
ls.remove(2)
print(ls)
ls[0] = 5
print(ls)

ls.insert(1,10)
print(ls)

myTuple = (10,20,30,40,40)
print(myTuple)

mySet = set(myTuple)
print(set)

dict = {"name":"John Doe", "age":30, "city":"New York"}

dict.update({"skills":["Python", "Java", "C++"]}) #{"skills":["Python", "Java", "C++"]
print(dict)


