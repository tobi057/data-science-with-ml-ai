# print("hello")
# print("world")

# a = 2 
# b = 3 
# print(a)
# print(b)

# name = "John"
# age = 36
# print(name)
# print(age)
# 5 = 5
# @ = "rtfgyhuij"
# % = "rtfgyhuij"
# * = "rtfgyhuij"

# print(5)
# print = "hello python"
# print(print)
# print("hello python") ### 


# print("hello world")

# if = ""
# name = "John"
# print(name)
# print(type(name))
# lastname = "Smith"
# print(name+" "+lastname)


# astname = "Saini"
# firstname = "Hemant "

# print(firstname  + lastname)

# name="kanchan "
# print(name)
# print(type(name))
# lastname= "kumari"
# print(name+ lastname)



# name = "John Smith"
# indexing
# print(name[0]) 
# print(name[2])

# slicing
# print(name[0:3])
# city = "Jaipur"
# company_name = "upflair"

# print(f"hello i am from {city} , my company name is {company_name}")

# company_name = "upflair"
# print("length of company name:-",len(company_name))
# print(company_name.lower())
# print("upper case",company_name.upper())
# print("title case",company_name.title())
# print("capital case",company_name.capitalize())
# print("swapcase",company_name.swapcase())
# print("count of a",company_name.count("a"))
# city = "Jaipur"
# print(company_name- city)



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.list >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>





# ls = [1,2,5,8,47,5,2,5,5,4,5,4,4,5]
# print(ls)
# print("length of ls:-",len(ls))
# print("type of ls:-",type(ls))
# ls = [3,4,5,5,55,5,5,5,5,5,5,5,5,5,5,]
## array or list 

#indexing 

# print(ls[0])
# print(ls[1])
# print(ls[2])
# print(ls[3])
# print(ls[4])
# print(ls[5])
# print(ls[6])

## slicing
# print(ls[0:7])
# print(ls[5:10])

# ls.append(500)
# print(ls)
# ls.pop()
# print(ls)

# ls.pop(3)
# print(ls)
# ls.insert(2 , 1000)
# print(ls)

# ls.remove(5)
# print(ls)


# ls.clear()
# print(ls) 

# ls.reverse()
# print(ls)  

# print(ls.count(5))
# print(ls)


# ls.sort()
# print(ls)
# print(ls)
# ls2=ls.copy()

# ls2.pop()
# print(ls2)
# print(ls)




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.tuple >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
## ordered and unchangeable
# heterogenous
# allow duplicate values

# tpl = (1,2,3,4,5, "hello", "world", 2.5)
# print(tpl)
# print("types of tpl:-",type(tpl))
# print("oth element of tpl:-",tpl[0])
# print("oth element of tpl:-",tpl[1])
# print("oth element of tpl:-",tpl[2])
# print("oth element of tpl:-",tpl[3])
# print("oth element of tpl:-",tpl[4])
# print("oth element of tpl:-",tpl[5])
# print("oth element of tpl:-",tpl[6])
# print("oth element of tpl:-",tpl[7])
# print("length of tpl:-",len(tpl))

## slicing 
# print(tpl[0:5])
# print(2 in tpl)
# print("hello" in tpl)


# max 
# min
# sum
# tpl = (1,2,3,54,5)
# print("max of tpl:-",max(tpl))
# print("min of tpl:-",min(tpl))
# print("sum of tpl:-",sum(tpl))


# tpl = 1,2,5,54,5,5,5
# print(tpl)  ## out 1,2,5,54,5,5,5
# print("length of tpl:-",len(tpl))
# print(type(tpl))

## tuple unpacking
# kapil= 1,2,3
# print(kapil)
# a , b ,c = kapil
# print("a:-",a)
# print("b:-",b)
# print("c:-",c) 



# t1 = (1,2)
# t2 = (3,4,2)
# print(t1+t2)
# print(t2*3)

# t2 = (3,4,2,(1,2))
# print(len(t2))

# print(t2[3][0])


t = (1,2,3,4,5,5,[45,7,8,8])
# print(t.index(2))
# print(t.count(5))/
# t[0]=100
# print(t)


## task 1 ::: ek tpl us list   :-t = (1,2,3,4,5,5,[45,7,8,8])



# >>>>>>>>>>>>>>>>>>>>>>>>>...dict >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## unordered and changeable
## heterogenous
## allow duplicate values


# person = {
#     "name" : "Hemant",
#     "age": 22,
#     "city": "Jaipur"
# }

# data = {'name': 'Hemant', 'age': 22, 'city': 'Jaipur'}

# print("first dict:-",person)
# print("types of dict:-",type(person))

# print("access dict value:-",person['name'])
# print("access dict value:-",person['age'])
# print("access dict value:-",person['city'])


### adding new key value pair 

# person['country'] = "India"
# print(person)

## task 1 ::: ek tpl us list   :-t = (1,2,3,4,5,5,[45,7,8,8])
## task 2  updating values of dict



### removing key value pair from dict
# del person['country']
# print(person)

# person.pop("country")
# print(person)


# dict methods 

# print("keys of dict:-",person.keys())
# print("values of dict:-",person.values())
# print("items of dict:-",person.items())


### checking for a key 

# print("name" in person)
# print("helllo" in person)


# empty_dict = { }
# print(empty_dict)
# print(type(empty_dict))



# >>>>>>>>>>>>>>>>>>>set >>>>>>>>>>>>>>>>>>>>

## unordered and unindexed
## heterogenous
## no duplicate values
## fast membership test 

# my_set = {1,2,3,4,5}
# print(my_set)
# # print(type(my_set))

# my_set = {1,2,3,4,5,5}
# print(my_set)


# my_set =set()
# print(my_set)
# print(type(my_set))


# my_set = {1,2,3,4,5}
# # my_set.add(6)
# # print(my_set)
# # my_set.remove(6)
# # print(my_set)
# my_set.discard(6)
# print(my_set)
# a = {1,2,3}
# b = {3,4,5}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(b.difference(a))

# my_set = {1,2,3,4,5}
# my_set.clear()
# print(my_set)


# membership in set 
# print(1 in my_set)
# print(5 in my_set)


# type casting 
# name = [1,2,3,4,5,5]
# print(name)
# print(type(name))
# # convert into set
# name=set(name)
# print(name)
# print(type(name))



