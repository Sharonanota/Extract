


# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('google.com'))
# from curses.ascii import isblank
# from turtle import clone


# a=[1,3,4,5,6,7,7,8]
# for x in a:
#     print(x*5)
    
    
# b=[4,5,6,7,8,8,9]
# print(len(b))    

# c= [2,3,5,6,7,8,8,9,0] 

# print(max(c))

# d=[1,2,3,4,5,5,6,7,8,8]
# print(min(d))


# def match_words(words):
#   ctr = 0

#   for word in words:
#     if len(word) > 1 and word[0] == word[-1]:
#       ctr += 1
#   return ctr

# print(match_words(['abc', 'xyz', 'aba', '1221']))    

# x= [1,2,3,3,4,5,5,6,7,7]
# x = list(dict.fromkeys(x))
# print(x)

# m = ["a", "b", "a", "c", "c"]
# m = list(dict.fromkeys(m))
# print(m)

# # y= ["a", "b", "a", "c", "c",""]
# # print(isblank(y))

# y =['']
# if len(y) == 0:
#     print("is empty")
# else:
#     print("is not empty")     
# s= [1,2,3,3,4,5,5,6,7,7]      
# print(clone(s))
# a = [1,2]
# b = a.clone()
# # a.append(3)
# print(b) # [1,2,3] [1,2]

# def long_words(n, str):
#     word_len = []
#     txt = str.split(" ")
#     for x in txt:
#         if len(x) > n:
#             word_len.append(x)
#     return word_len	
# print(long_words(3, "The quick brown fox jumps over the lazy dog"))
# from posixpath import split


# n=("I love you ochwada")
# print(split(n))


# string = "age, uNiVeRsItY, naMe, gRaDeS"
# lst = string.split(',')
# print(lst)


# def common_data(list1, list2):  
#      result = False  
#      for x in list1:  
#          for y in list2:  
#              if x == y:  
#                  result = True  
#                  return result  
# print(common_data([1,2,3,4,5], [5,6,7,8,9]))  
# print(common_data([1,2,3,4,5], [6,7,8,9]))   



# 1a) Create a class Vehicle with the following attributes:name, max_speed,mileage. Define attribute color to be “White” for all the vehicles.
#  Create two instances to confirm it works.
# b) Create a method that congratulates the owner  for buying that kind of a car. Include the car’s name, color,max_speed,mileage.
# c)Create a method that returns the car name and its capacity.
   
from unicodedata import name


class Vehicle:
    color = "Black"
    def __init__ (self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
       
    

    def congradulate(self):
        return f"hello, congradulation for buying {self.name},with a beautiful Aesthetic  {self.color}color,and a maximum speed of {self.max_speed},with {self.mileage} "
    
    
    def capacity(self,capacity):
        return f"Hello John you bought {self.name} With capacity of {capacity}"  
       

