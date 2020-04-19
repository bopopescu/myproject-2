#------------------- 74 github -------------
print("hiiiiiii")


#-------------------72 connecting to the mysql --------------------------
# import mysql.connector as mc
# mydb = mc.connect(host='localhost',user='root',passwd='sheru007',database='sk')
#
# mycursor = mydb.cursor()
# # mycursor.execute("show databases")  # if u use it ,dont specify database in connect
# mycursor.execute("select * from student")
# # result = mycursor.fetchall()     # to fetch all data
# result  = mycursor.fetchone()     # to fetch one data
# for i in result:
#     print(i)


#------------ 71 selection sort --------------

# def selectionsort(nums):
#
#     for i in range(len(nums)-1):
#         minpos = i
#         for j in range(i,len(nums)):
#             if nums[j] < nums[minpos]:
#                 minpos = j
#
#         nums[i],nums[minpos] = nums[minpos],nums[i]
#         print(nums)
#
# nums = [2,4,3,7,5,9,6,1]
# selectionsort(nums)



# --------- 70 bubble sort -----------------

# def sort(lst):
#
#     for i in range(len(lst)-1,0,-1):
#         for j in range(i):
#             if lst[j] > lst[j+1]:
#                 lst[j],lst[j+1] = lst[j+1],lst[j]
#
# nums = [2,3,6,4,9,8,7]
# sort(nums)
# print(nums)



#---------- 69 binary search -----------------

# pos = -1
#
# def binarysearch(lst,n):
#
#     l = 0
#     u = len(lst)-1
#
#
#     while l <= u:
#         mid = (l+u) // 2
#         if lst[mid] == n:
#             globals()['pos'] = mid
#             return True
#         else:
#             if lst[mid] < n:
#                 l = mid+1
#             else:
#                 u = mid-1
#
#     return False
#
#
#
# lst = [2,4,5,6,7,89,10]
# n = 100
# lst.sort()
#
# if binarysearch(lst, n):
#     print('found at ', pos)
# else:
#     print('not found')


# ------------------------------------- 68 linear search ----------------
# pos = -1
#
# def linearsearch(lst,n):
#
#     i = 0
#
#     while i < len(lst):
#         if lst[i] == n:
#             globals()['pos']  = i         # to change in global variable
#             return True
#         i += 1
#
#     return False
#
#
#
# lst = [2,4,5,6,7,89,10]
# n = 11
#
# if linearsearch(lst, n):
#     print('found at ', pos)
# else:
#     print('not found')

# ------- 65 file handing -----------

# f = open('mydata','r')   # open in read mode
# # print(f.read())  # for full text
# print(f.readline(), end='')  # for one line and use end='' to avoid \n that is by default
# print(f.readline(),end = '') # for 2nd line

# f2 = open('writedata','w')  # to append data open it with 'a' mode
# f2.write('this is new line \nhiii i am sk \n')
#
# for data in f:
#     f2.write(data)


# p1 = open('mummy_papa.jpg','rb')
# p2 = open('parents.jpg','wb')
# for b in p1:
#     p2.write(b)
#


# ------- 64 multi thread ------------------

# from threading import *
# from time import  sleep
# # both are vhild class of thread class
# class hello(Thread):
#
#     def run(self):
#         for i in range(5):
#             print('hello')
#             sleep(1)
#
# class hii(Thread):
#     def run(self):
#         for i in range(5):
#             print('hii')
#             sleep(1)
#
# t1 = hello()
# t2 = hii()
#
# # t1.run()
# # t2.run()
# # what if we want to run them simantaneously
# t1.start()
# sleep(0.2)
# t2.start()

# wait to finish t1 and t2 thread
# t1.join()
# t2.join()

# print('byy')






# ------------- 63 exception handling ---------




# a = 5
#
# try:
#     print('file open')
#
#     b = int(input("enter a number :"))
#     print(a/b)
# except ZeroDivisionError as e:
#     print(" can not divie by zero and error : ", e)
# except ValueError as e:
#     print(" invalid input and error : " , e)
# except Exception as e:
#     print('something went wrong :  ', e)
#
# finally:
#     print("file closed")



# --------- 62 generator -used to get iterator -------

# def topten():
#
#     n = 1
#     while n <= 10:
#         sq = n*n
#         yield sq
#         n += 1
#
# values = topten()
# print(next(values))
# print(next(values))

# for i in values:
#     print(i)

# ---------- 61 iterator -------------

# class topten():
#
#     def __init__(self):
#         self.num  = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         if self.num <= 3:
#             val = self.num
#             self.num += 1
#             return val
#         else:
#             raise StopIteration
#
# values = topten()
# i = values.__iter__()
# print(i.__next__())
# print(i.__next__())
# print(next(i))
# for i in values:
#     print(i)

#------------ 58 - polymorphism -----------------

# -duck - typing

# class pycharm:
#
#     def execute(self):
#         print('compiling..')
#         print('running..')
#
# class sublime:
#
#     def execute(self):
#         print('compiling..')
#         print('running..')
#
# class laptop:
#
#     def code(self,ide):
#         ide.execute()
#
# ide = sublime()
# lap = laptop()
# lap.code(ide)

#---- operator overloading -----------------

# class student:
#
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def __add__(self, other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = student(m1,m2)
#         return s3
#
#     def __gt__(self, other):
#         if self.m1 + self.m2  > other.m1 + other.m2:
#             return True
#         else:
#             return False
#
#     def __str__(self):
#         return '{} {}'.format(self.m1,self.m2)
#
# a = 8
# b = 3
# print(a+b)    # but by default it call int.__add__(a,b)
#
# s1 = student(45,25)
# s2 = student(2,36)
#
# s3 = s1+s2         # dont work if we dont create operator overloading
# print(s3.m1 , s3.m2)
#
# if s1 > s2:         # we have to cretae it
#     print('s1 wins!!')
# else:
#     print('s2  wins!!')
#
# print(a)  # bydefault a__str__ is called and print the value not addresss
# print(s1)  # print address not value so create function

#----------56 inheritance -------
# class A:
#
#     def __init__(self):
#         print(' A - init')
#
#     def feature1(self):
#         print('feature 1-A')
#
#     def feature2(self):
#         print('feature 2-A')
#
#
# class B:
#
#     def __init__(self):
#         print(' B - init')
#
#     def feature1(self):
#         print('feature 1-B')
#
#     def feature2(self):
#         print('feature 2-B')
#
#
# class C(A,B):
#
#     def __init__(self):
#         super().__init__()
#         print(' C- INIT')
#
#     def feat(self):
#         super().feature1()   # call most left class , here A- feature 1
#
#     def feature3(self):
#         print('feature 3-C')
#
# # if we dont create init in child then it will call the parent class init(left declared class first)
# a = C()   # call A- init and then C-init
# a.feat()




# ------- 49 class and object -------
# class computer:
#
#     brand = 'hp'           # it is class variable and same for all instance
#     def __init__(self,cpu,ram,hd):
#         self.cpu = cpu
#         self.ram = ram                # there are instance variable
#         self.hd = hd
#         self.ownerr = self.owner()     # create the object of inner class here
#
#     def config(self):       # call by object
#         print('congif is : ',self.cpu,self.ram,self.hd)
#         self.ownerr.show()
#
#     # accessor method is used to access the value and mutator method is used to modify the values
#     def compare(self,other):
#         if self.cpu == other.cpu:
#             return True
#         else:
#             return False
#
#
#
#     class owner:            # inner class
#
#         def __init__(self):
#             self.name = 'sheru'
#             self.mobno = 9957961559
#
#         def show(self):
#             print(self.name,self.mobno)
#
#
#
#
#     @classmethod                 # call by class
#     def getbrand(cls):
#         return cls.brand
#
#     @staticmethod             # call by object
#     def getinfo():
#         print("hii it is static varibale")
#
# comp1  = computer('i5','8gb','1TB')
# comp2 = computer('i5','8gb','500gb')
# comp1.config()             # callling instance method by object
# comp2.config()
# if comp1.compare(comp2):
#     print('it is same cpu')
# else:
#     print('it is different cpu')
#
# print(computer.getbrand())   # calling class method
# computer.getinfo()       # calling static method by object or class
# comp1.getinfo()
#





# --------------- 46 special variable __name__ ---------
# import calc

# print(__name__)   # print __main__ if it is not module, but if it is module then it print module name ex. mycode
# print('hii i am sheru khan')








# ------ 45 module -------

# from calc import *
# print(add(3,4) , mul(3,4))









#----------------- 44 decorator- used to add extra feature in function if we r not allow to see the other part of function --

# def div(a,b):
#     print(a/b)
#
# def smart_div(func):
#
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#
#     return inner
#
# div(2,4)
# div = smart_div(div)
# div(2,4)



#------------- 41 lanbda function ----------
# f = lambda a,b:a+b
# print(f(3,4))

# from functools import reduce
# nums = [1,2,3,4,5,6,7,7,8,9]
# even = list(filter(lambda n:n%2==0,nums))
# print(even)
#
# double = list(map(lambda n:n*2,even))
# print(double)
#
# sum = reduce(lambda a,b:a+b,double)
# print(sum)


#-------------------40 recursion ----------------
# import sys
# sys.setrecursionlimit(5000)
# print(sys.getrecursionlimit())


# ------------------ 36 global variable ---------------

# a = 10
# def sth():
#     # global a  # it tell that use global variable a insteat of local variable but we can not create another a
#     a = 9
#     print('in fun', a)  # it change the global and now it is 15
#     globals()['a'] = 15   # to access the global variable
#
#
# sth()
# print('outside',a)


















# ------ 33 function ------

# def add_sub(x,y):      # defining the function
#     a = x+y
#     s = x-y
#     return a,s
#
# res1,res2 = add_sub(5,4)    # calling the function
# print(res1,res2)
# # -- list is by default call by reference , if u change there, it will change here
# # actual argument is 4 type - position , keyword,default,variable length
#
# def person(name,age=23):
#     print(name,age)
#
#
# person('sheru',28) #ok nit is positional argument
# person(24,'sheru')  # wrong, we are depent on position
# person(age = 23,name = 'sheru')  # keyword argument
# person('sheru')  # default argument


# def add(a,*b):   # *b is tuple with any number of argument and it is varivle length argument
#     print(a)
#     print(b)
#     c = a
#     for i in b:
#         c = c+i
#     print(c)
#
# add(1,2,3,4,5)
#
# def person(name,**data):  # **data is dictionary and keyword variable length argument
#     print(name)
#     for k,v in data.items():
#         print(k,v)
#
#
# person(age = 23,name = 'sheru',city = 'hydrabad',mob = 9957961559)
#
















# ---------- 31 multi dimentional array --------
# from numpy import *
#
#
# arr  = array([
#
#             [1,2,3],
#             [5,6,7],
#             [8,9,10]
#
#             ])

# print(arr)
# print(arr.ndim)     # flatten for make it single dimentional
#                     # reshape(h,l,b) or reshape(l,b) to make it multidimentional from 1D
# print(arr.shape)
# print(arr.size)
# # it is 3d array to vonvert it into matrix
# m = matrix(arr)
# print(m)
# print(diagonal(m))










# ----- ------------------------------ 29 array in numpy --------------------------------
# from numpy import *

#arr = array([1,2,3,4,5,6])
#print(arr)
# print(arr.dtype)  # but if we change an element into float then all become to float
# arr2 = array([1,2,3,4,5],float)
# print(arr2)
#
# arr3 = linspace(1,15,5)  # start , end , no. of parts(bydefault it is 50)
# print(arr3)
#
# arr4 = arange(1,15,2) # start , end , no. of step
# print(arr4)
#
# arr5 = logspace(1,40,5) # it is 10^(start,end) and no. of parts
# print("%.2f" %arr5[1])
#
# print(zeros(5))
# print(ones(5))
#
# arr6 = arr + 5   #add a constant to all element
# print(arr6)
#
# print(sin(arr) ,'\n' , cos(arr) ,'\n', sqrt(arr) , log(arr)) # max, sum , concate

# copy the array
# arr7 = arr.copy()   # it is shallow copy. address is diff but change in one will change in another.
#                      # for deep copy use arr.copy() method
# arr7[1] = 98
# print(arr)
# print(arr7)
# print(id(arr))
# print(id(arr7))


















# --------- 26 array in python -----------------
# from array import *
# vals = array('i',[4,2,-5,6,9,3])
# print(vals.buffer_info())
# print(vals.typecode)
# vals.reverse()
# print(vals)
#
# for i in range(len(vals)):
#     print(vals[i],end = " ")
#
# print()
# for e in vals:
#     print(e,end=" ")
#
# newarray = array(vals.typecode,(a for a in vals))
# print(newarray)
#
#
# aa = array('i',[])
# n = int(input("enter the length of array"))
#
# for i in range(n):
#     x = int(input("enter the number "))
#     aa.append(x)
#
# print(aa)
#
# s = int(input("enter the value to besearch "))
#
# k = 0
# for e in aa:
#     if e == s:
#         print(k)
#         break
#     k += 1
# else:
#     print("element not fount !!")
#
# print(aa.index(s))

#-------------- 25 prime number --------------
# num = int(input('enter the number to be check for prime '))
# for i in range(2,num):
#
#     if num%i == 0:
#         print('not prime')
#         break
# else:
#     print('prime')


# ---------------- 24 for else -----------------

# nums = [23,14,46,76,83]
#
# for num in nums:
#
#     if(num%5 == 0):
#         print(num)
#         break
#
# else:
#     print('not found')






# ----------- 21 for loop ----------------------

# x = ['sheru','heena','papa','mummy']
# for i in x:
#     print(i)



# -------- 20 while loop ---------
# i = 1
# while i <= 5:
#     print(i , 'sheru ',end='')
#     j = 1
#     while j <= 3:
#         print('rocks ',end = '')
#         j += 1
#     i += 1
#     print()

# -------------- 18 print and user input  ---------------
# x = int(input("enter 1st number "))
# y = int(input("enter 2nd number "))
# z = x+y
# print(z)
#
# ch = input("enter a char ")[0]
# print(ch)
#
# result = eval(input('enter the expr'))
# print(result)


