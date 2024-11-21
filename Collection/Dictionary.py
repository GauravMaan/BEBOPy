#based on key value pair.
# it preserve the order of insertion.
# key are not changeable(immutable) and it must be unique

mydict={}
print(type(mydict))

mydict1={"name":"bob","age":27}
print(mydict1)
print("===============================================")
mydict2=dict([("name","bob"),("age",27)])
print(mydict2["name"])
print(mydict2.get("age"))
print(mydict2)
print("===============================================")
mydict3=dict(name="gaurav",age=24)
print(mydict3)
print("===============================================")
#adding or update
mydict4=dict(name="bob",age=24)
mydict4["age"]=23
mydict4["city"]="Panchkula"
mydict4["state"]="Haryana"
mydict4["food"]="FOOD"
print(mydict4)
print("===============================================")
#deleting
del mydict4["age"]
print(mydict4)
mydict4.pop("city")
print(mydict4)
print("===============================================")
mydict5=dict([("name","bob"),("age",27)])
mydict5.clear()
print(mydict5)
print("===============================================")
print(mydict4.keys())#return object of all the key/only set of key
print(mydict4.values())
print(mydict4.items())#all key value pair as tuple
print("===============================================")
mydict6=dict(pin=123456,Road="stone")
mydict6.update(mydict1)
print(mydict6)
print("===============================================")
mydict=mydict4.copy()
print(mydict)
print("===============================================")
key=[1,2,3,4]
key1=dict.fromkeys(key,"Gaurav")
print(key1)
print("===============================================")
mydict7=dict(name="gaurav")
mydict7.setdefault("age",23)
print(mydict7)
print("===============================================")
for i in mydict4:
    print(i)
for i in mydict4.values():
    print(i)
for i,j in mydict4.items():
    print(i,j)
print("===============================================")
square={x:x**2 for x in range(0,5)}
print(square)
print("===============================================")
mydict8 = {
    'Person1': dict(name="gaurav"),
    'Person2': dict(age=23)
}
print(mydict8['Person1']['name'])
print(mydict8['Person2']['age'])
print("===============================================")
print(mydict7|mydict4)
print("===============================================")
mydict9=set(mydict1.values()) & set(mydict4.values())
print(mydict9)
print("===============================================")
mydict10=set(mydict1.values()) ^ set(mydict4.values())
print(mydict10)
print("===============================================")
Mydict11 = {"a": 10, "b": 10, "c": 20}
target = 10
for key, value in Mydict11.items():
    if value == target:
        print(f"Key: {key}, Value: {value}")
print("===============================================")


