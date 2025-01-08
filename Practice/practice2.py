# str1="NAABBCCPCADDNCCNBBNBDDDPMMMM"
#
# dict1={}
# for i in str1:
#     if i in dict1:
#         dict1[i]+=1
#     else:
#         dict1[i]=1
# print(dict1)
# most_frequent=max(dict1.values())
#
# filtered_counts=[count for count in dict1.values() if count!=most_frequent]
#
# if filtered_counts:
#     second_frequent_count=max(filtered_counts)
#
#     second_frequent_char=[char for char,count in dict1.items() if count==second_frequent_count]
#     print(f"second most frequent char and count{second_frequent_char}:{second_frequent_count} ")
# else:
#     print("no second frequent element")
import time

# str1="AABBBAAACCDDD"
# first_element=str1[0]
# count=1
# result=""
# len_str1=len(str1)
# for i in str1[1:len_str1]:
#     if i==first_element:
#         count+=1
#     else:
#         result=result+first_element+str(count)
#         first_element=i
#         count=1
# result=result+first_element+str(count)
#
# print(result)


# def reverse(number1):
#     result=0
#     while number1>0:
#         last_digit=number1%10
#         result=result*10+last_digit
#         number1=number1//10
#     return result
#
# r=reverse(5496)
# print(r)

# n!=n*(n-1)!
# def factoial(number):
#     result=1
#     while number>0:
#         result=result*number
#         number=number-1
#
#     return result
# f=factoial(5)
# print(f)


# def factorial(number):
#     if number==0 or number==1:
#         return 1
#     else:
#         return number* factorial(number-1)
#
# f=factorial(5)
# print(f)


# def Palindrome(number):
#     number1=number
#     result=0
#     while number>0:
#         last_digit =number%10
#         result=result*10+last_digit
#         number=number//10
#
#     if result==number1:
#         print("number is palindrome")
#     else:
#         print("number is not palindrome")
#
# r=Palindrome(1224)

# number=6
# for i in range(2,number):
#     if number%i==0:
#         print("number is not prime")
#         break
# else:
#     print("number is prime")


# def decor(fun):
#     def wrap():
#         print("hey guest")
#         fun()
#         print("How are you")
#     return wrap
#
#
# @decor
# def greeting():
#     print("hello good morning")
#
#
# g=greeting()

# f=open("manish.txt","a")
# f.write("Hello buddy how are you")
# f.close()
#
# f=open("manish.txt","r")
# text=f.read()
# print(text)

# f=open("manish.txt","w")
# f.write("Hey new buddy\nyou are noob")
# f.close()


# def divide(x,y):
#     try:
#         result=x/y
#         return result
#     except Exception as e:
#         return e
#
# d=divide(5,0)
# print(d)
#
#
# str1="B4A1D3"
# list1=[]
# list2=[]
#
# for i in str1:
#     if i.isalpha():
#         list1.append(i)
#     else:
#         list2.append(i)
#
#
# list1.sort()
# list2.sort()
#
# print("".join(list1) + "".join(list2))

# str1="a4b3c2"
# output=""
# for i in str1:
#     if i.isalpha():
#         output=output+i
#         previous=i
#     else:
#         output=output+previous*(int(i)-1)
#
# print(output)

# str1="AAABBCCAADDCC"
#
# first_element=str1[0]
# result=""
# count=1
#
# for i in str1[1:len(str1)]:
#     if first_element==i:
#         count=count+1
#     else:
#         result=result+first_element+str(count)
#         first_element=i
#         count=1
#
# result=result+first_element+str(count)
#
# print(result)

# str1="AABBCCDCGJJLJGGJKYTRJKOOHN"
#
# dict1={}
#
# for i in str1:
#     if i in dict1:
#         dict1[i]+=1
#     else:
#         dict1[i]=1
#
# for x,y in dict1.items():
#     print("".join(x+str(y)), end="")


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//button[@id='openwindow']").click()
# windows=driver.window_handles
#
# driver.switch_to.window(windows[1])
# print(driver.title)
# driver.switch_to.window(windows[0])
# print(driver.title)

# num1=8
#
# for i in range(2,num1):
#     if num1%i==0:
#         print("not a prime number")
#         break
# else:
#     print("prime number")

# def Prime():
#     for i in range(1,101):
#         for y in range(2,i):
#             if i%y==0:
#                 break
#         else:
#             print(i,end=' ')
#
# p=Prime()












# str1="This is the sample test"
#
# str2=str1.lower().replace(" ","")
#
# dict1={}
#
# for i in str2:
#     if i in dict1:
#         dict1[i]+=1
#     else:
#         dict1[i]=1
#
# print(dict1)

# number1=35257

# def Reverse(num):
#     result=0
#     while num>0:
#         last_digit=num%10
#         result=result*10+last_digit
#         num=num//10
#     return result
#
# r=Reverse(35257)
# print(r)

# list1 = [11, 2, 3, 14, 5, 6, 10, 7]
#
# # Initialize the first element as the maximum
# max_element = list1[0]
#
# for i in list1[1:]:
#     if max_element < i:
#         max_element = i
#
# print("Max element:", max_element)

# list1 = [11, 2, 3, 14, 5, 6, 10, 7]
# first_element = list1[0]  # Initialize the first element
#
# # Iterate over the list starting from the second element
# for i in list1[1:]:
#     if first_element > i:
#         continue  # Continue if the current first_element is larger
#     else:
#         first_element = i  # Update first_element to the larger value
#
# print("Max element:", first_element)

# class Parent:
#     def __init__(self,standard,school):
#         self.standard=standard
#         self.school=school
#
#     def output(self,name):
#         print(f"the details of person is name:{name} and class and school is {self.standard} and {self.school}")
#
#
# class Child(Parent):
#     def __init__(self,place,standard,school):
#         super().__init__(standard,school)
#         self.place=place
#
#     def output(self,fname,lname):
#         print(f"the details of the person is firstname:{fname} lastname:{lname} place:{self.place} standard:{self.standard} school:{self.school}")
#
#
# c=Child("kanda",12,"GGIC")
# c.output("Manish","Pandey")


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.implicitly_wait(2)
# driver.maximize_window()
# driver.get("https://www.zoho.com/signup.html")
# driver.find_element(By.XPATH,"//input[@id='rmobile']/preceding::input[@name='email']").send_keys("Hey")
# driver.find_element(By.XPATH,"//input[@id='rmobile']").send_keys("12345")
# time.sleep(5)

# str1="MaUUunishouChanIdraKanOAdpalA"
# vowels="aeiouAEIOU"
# vowel_count=0
# consonant_count=0
# for i in str1:
#     if i in vowels:
#         vowel_count+=1
#     else:
#         consonant_count+=1
#
# print(vowel_count,consonant_count)
# print(len(str1))

#
# str1="my name is manish kandpal"
# str2=str1.replace(" ","")
# print(str2)
# vowels="aeiouAEIOU"
# vowel_count=0
# consonant_count=0
#
# for i in str2:
#     if i in vowels:
#         vowel_count+=1
#     else:
#         consonant_count+=1
#
# print(vowel_count,consonant_count)
# //input[@name='email']/ancestor::form//button[@name='login']
#1234

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("this is Person class construtor call")

    def Eat(self):
        print("eat")

    def Sleep(self):
        print("sleep")


# class Engineer(Person):
#
#     def __init__(self, salary,name,age):
#         super().__init__(name,age)
#         self.salary = salary
#         print(f"this is Engineer class construtor ")
#
#     def Work(self):
#         print(f"do some problem solving of world and your salary will be {self.salary}")
#
#
# class Doctor:
#     def Work(self):
#         print("do some trement of patient")
#
#
# engineerObj = Engineer(15000)
# engineerObj.Work()


class A:
    def Method(self):
        print("this is class A")

class B(A):
    def Method(self):
        print("this is class B")

class C(A):
    def Method(self):
        print("this is class C")


class D(B,C):
    def Method(self):
        print("this is class D")

dObj=D()
dObj.Method()

















































































