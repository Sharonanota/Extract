#Exercise 1: Write a program to check whether a given key exists in a dictionary or not.
from optparse import Values


a={'o':1,'1':2,'2':3}
    
x=(int(input("Enter value:")))
if x in a.keys():
     print(True)
else:
     print(False)  
     
#Exercise 2: Write a program to iterate over dictionary items using for loop.  
c={0:'Value',1:'value2'}   
for v in c.keys():
    print(f"value of key{0},is {1}")
#Exercise 3: Write a program to print only keys of a dictionary.    
k={0:'value', 1:'value 2' , 2:'value 3'}
print(k.keys())
print(k.items())

#Exercise 4: Write a program to print values of dictionary.
z={0:'value', 1:'value 2' , 2:'value 3'}
print(z.values())

#Exercise 5: Write a program in python to map 2 lists into a dictionary.
ke=[1,2,3] 
V=['value1','value2', 'value3']
new_dict = dict(zip(ke,V))
print(new_dict)

#Exercise 6: Python program to remove a set of keys.
j={0:'value', 1:'value 2' , 2:'value 3'}
for k in j.keys():
    del k(0,1)


print(k)