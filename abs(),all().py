# all built-in function in python

#Return the absolute value of a number:
x=abs(-15.375)
print(x)


#Return absolute value of complex number:
x=abs(5+2j)
print(x)

"""
The all() function returns True
 if all items in an iterable are true,
 otherwise it returns False.
"""
#Check if all items in a list are True:
my_list =[True,True,True]
x=all(my_list)
print(x)


#If the iterable object is empty,
#the all() function also returns True.
my_list =[]
x=all(my_list)
print(x)


#Check if all items in a list are True:

mylist=[0,1,1]
x=all(mylist)
print(x)


#Check if all items in a tuple are True:

mytuple=(0,True,False)
x=all(mytuple)
print(x)

#Check if all items in a set are True:

myset ={0,1,0}
x =all(myset)
print(x)

#Check if all items in a dictionary are True:

mydict ={0:"Apple",1:"Orange"}
x =all(mydict)
print(x)
#When used on a dictionary,the all()checks 
#if all the keys are true, not the values.



