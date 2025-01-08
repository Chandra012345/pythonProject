# How would you determine if one string is a rotation of another using Python? Provide an algorithm with O(n) time complexity.
#
# Input:
# "waterbottle", "erbottlewat"
#
# Output:
# True
# import time


# def function(str1,str2):
#     if len(str1)!=len(str2) or len(str1)==0:
#         return False
#
#     str3=str1+str1
#     if str2 in str3:
#         return True
#     else:
#         return False
#
#
# f=function("","")
# print(f)


# Question:
# Describe an efficient algorithm to find the length of the longest substring without repeating characters in a given string using Python.
#
# Input:
# "abcabcbb"
#
# Output:
# 3

# def function(str1):
#     dict1={}
#     for i in str1:
#         if i in dict1:
#             dict1[i]+=1
#         else:
#             dict1[i]=1
#     max_value=max(dict1.values())
#     for key,value in dict1.items():
#         if value==max_value:
#             print(key,":", value)
#
# function("AABBCCDDD")

# Explain how you would find the first non-repeating character in a string and return its index using Python. Optimize for both time and space complexity.
#
# Input:
# "leetcode"
#
# Output:
# 0

# def function(str1):
#     list1=[]
#     for i in list1:
#         if i in list1:
#             count=count+1
#         else:
#             count


# aaabbbcc


# def function(str1):
#     dict1={}
#     result=""
#     for i in str1:
#         if i in dict1:
#             dict1[i]+=1
#         else:
#             dict1[i]=1
#
#
#     for key, value in dict1.items():
#         if value>1:
#             result=result+key+str(value)
#         else:
#             result=result+key
#
#     return result
#
# f=function("AAABBCDDDD")
# print(f)


# def function(str1):
#     l=len(str1)
#     result=""
#     while l>0:
#         result+=str1[l-1]
#         l=l-1
#
#     return result
#
# f=function("Manish")
# print(f)


# def function(str1):
#     result=""
#     l=len(str1)
#     for i in range(l-1,-1,-1):
#         result+=str1[i]
#
#     return result
#
# f=function("Manish")
# print(f)

# def function(str1):
#     str2=str1.strip().lower()
#     if str2==str2[::-1]:
#         print("This string is palindrome string")
#     else:
#         print("this string is not palindrome")
#
# f=function("Lebcel")


# 3.	How would you find the first non-repeated character in a string using Python?
#
# def function(str1):
#     for i in str1:
#         if str1.count(i)==1:
#             print(i)
#             break
#
#
# f=function("AABBCCADFFH")


# str1="listen"
# str2="silent"

# def function(str1,str2):
#     str1=str1.strip().lower()
#     str2=str2.strip().lower()
#     if str1==


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# ser_obj=Service("C:\\Users\\hp\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
# driver=webdriver.Chrome(service=ser_obj)
# driver.maximize_window()
#
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# radio_button=driver.find_elements(By.CSS_SELECTOR,".radioButton")
# for i in radio_button:
#     i.click()
# time.sleep(5)
# print(len(radio_button))
# driver.close()

# dropdown=driver.find_element(By.CSS_SELECTOR,"#dropdown-class-example")
#
# select=Select(dropdown)
# select.select_by_index(1)
# time.sleep(4)
# driver.close()


# driver.find_element(By.ID,"openwindow").click()
# all_window=driver.window_handles
# print(len(all_window))
# driver.switch_to.window(all_window[1])
# driver.find_element(By.LINK_TEXT,"Courses").click()
# driver.switch_to.default_content()
# print(driver.title)
# driver.close()

# driver.find_element(By.XPATH,"//input[@name='enter-name']").send_keys(("Manish"))
# driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
# driver.switch_to.alert.
# driver.close()

# input="durga"
# print(input[::-1])
#
# l=len(input)
# result=""
# while l>0:
#     result=result+input[l-1]
#     l=l-1
#
# print(result)

# input="Manish Kandpal"
# list1=input.split()
# list2=[]
# print(list1)
# for i in list1[::-1]:
#     list2.append(i[::-1])
#
# print(" ".join(list2))

# s1="Ravi"
# s2="Teja"
#
# output=""
# for i,j in zip(s1,s2):
#     output+=i+j
#
# print(output)

# input="B4A1D3"
# l1=[]
# l2=[]
#
# for i in input:
#     if i.isalpha():
#         l1.append(i)
#     else:
#         l2.append(i)
#
# print("".join(sorted(l1)+sorted(l2)))


# input="ABBCCCDDEGGFFHKKKIUBNKKK"
# dict1={}
# result=""
# for i in input:
#     if i in dict1:
#         dict1[i]+=1
#     else:
#         dict1[i]=1
#
# for key,value in dict1.items():
#     result+=key+str(value)
#
# print(result)

# class Login:
#     def __init__(self):
#         print("this is parent constructor")
#
#
# class Homepage(Login):
#     def __init__(self):
#         super().__init__()
#         print("this is base constrctor")
#
# h=Homepage()

# s=lambda a,b:a+b
# print(s(2,3))

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# ser_obj=Service("C:\\Users\\hp\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
# driver=webdriver.Chrome(service=ser_obj)
# driver.maximize_window()
# driver.get("https://www.makemytrip.com/")
# tag_name=driver.find_elements(By.TAG_NAME,"a")
# print(len(tag_name))
# for i in tag_name:
#     print(i.text)


# import copy
# orginal_list=[1,2,[3,4]]
# new_list=copy.copy(orginal_list)
# print(new_list)
# new_list[2][1]=5
# print(orginal_list)
# print(new_list)

# import copy
# original_list=[1,2,[3,4]]
# new_list=copy.deepcopy(original_list)
# print(new_list)
# new_list[2][1]=5
# print(original_list)
# print(new_list)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# ser_obj=Service("C:\\Users\\hp\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
# driver=webdriver.Chrome(service=ser_obj)
#
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.switch_to.frame("courses-iframe")
# print(driver.title)
# driver.find_element(By.LINK_TEXT,'Mentorship').click()
# driver.switch_to.default_content()
# print(driver.title)
# driver.close()


# s='ABAABBCA'
# dict1={}
# result=""
# for i in s:
#     if i in dict1:
#         dict1[i]+=1
#     else:
#         dict1[i]=1
#
# for key,value in dict1.items():
#     result+=str(value)+key
#
# print(result)
#
# print(dict1)

# str1="My name is manish and i am from uttarakhand"
#
# str2="aeiouAEIOU"
# count=0
# for i in str1:
#     if i in str2:
#         count+=1
#
# print(count)


# f=open("manish.txt","w")
# f.write("My name is manish")
# f.close()

# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.makemytrip.com/")
# time.sleep(5)

# input="AABBCCAAAFFFEEE"
# output="A2B2C2A3F3E3"
# dict1={}
# result=""
#
# for i in input:
#     if i in dict1:
#         dict1[i]+=1
#     else:
#         dict1[i]=1
#
# for key,value in dict1.items():
#     result+="".join(key+str(value))
#
# print(result)
# list1=[]
# for i in range(1,100):
#     if i%i
#
# print(list1)

# a=1234
#
# x=(a//1000)
# y=(a//100)%10
# z=(a//10)%10
# b=a%10
# print(x+y+z+b)


# digit=1234
# for sum in str(digit)

# str1="My name is Manish"
#
# list1=str1.split()
# list2=[]
# for i in list1:
#     list2.append(i[::-1])
#
# print(" ".join(list2))

# class Practice:
#     count=0
#     def __init__(self,str1):
#         self.str1=str1
#
#
#     def Function1(self):
#         list1 = self.str1.split()
#         list2 = []
#         for i in list1:
#             list2.append(i[::-1])
#             Practice.count = Practice.count + 1
#
#
#
#         result=(" ".join(list2))
#         print(Practice.count)
#         return result
#
#
# p=Practice("My name is Manish")
# print(p.Function1())


# a=1234
# count=0
# for i in str(a):
#     count+=int(i)
# print(count)
# num=7
# for i in range(2,num):
#     if num%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")

# Write a program to find the sum of digits of a given number
# def function(num):
#     count=0
#     for i in str(num):
#         count=count+int(i)
#
#     return count
#
# f=function(1234)
# print(f)

# Write a program to check if a number is prime or not
# num=7
# for i in range(2,num):
#     if num%i==0:
#         print("not prime")
#         break
# else:
#     print("Prime")

# list1=[]
# list2=[]
# for i in range(1,101):
#     if i==1:
#         continue
#     for j in range(2,i):
#         if i%j==0:
#             list1.append(i)
#             break
#     else:
#         list2.append(i)
#
# print("prime number",list2)


# def factorial(num):
#     if num==1:
#         return 1
#     else:
#         return num*factorial(num-1)
#
# f=factorial(10)
# print(f)


# def factorial(n):
#     result=1
#     for i in range(1,n+1):
#         result=result*i
#     return  result
#
# f=factorial(10)
# print(f)

# n=153
# result=0
# for i in str(n):
#     result=result+(int(i)*int(i)*int(i))
# print(result)
# if result==n:
#     print("armstrong number")
# else:
#     print("Not armstrong")


# Write a program to reverse a given number

# n=1234
# output=4321
#
# n1=str(n)
# n2=n1[::-1]
# print(type(int(n2)))


# Function to reverse a number
# def reverse_number(number):
#     reverse = 0
#     while number != 0:
#         # Extract the last digit of the number
#         digit = number % 10
#         # Append the digit to the reverse number
#         reverse = reverse * 10 + digit
#         # Remove the last digit from the number
#         number = number // 10
#     return reverse
#
# # Taking input from the user
# number = int(input("Enter a number: "))
#
# # Calling the function to reverse the number
# reversed_number = reverse_number(number)
#
# # Displaying the reversed number
# print("Reversed number:", reversed_number)


# def Reverse(number):
#     reversed_number=0
#     while number!=0:
#         last_digit=number%10
#
#         reversed_number=reversed_number*10+last_digit
#
#         number=number//10
#
#     return reversed_number
#
# number=(int(input("Enter a number:")))
#
# r=Reverse(number)
# print(r)


# Write a program to find the largest among three numbers.


# a,b,c=10,12,11


# def function(*n):
#     print(max(n))
#
# f=function(10,8,9)

# Write a program to find the Fibonacci series up to a given number of terms

# def compress_string(input_string):
#     compressed_string = ""
#     current_char = input_string[0]
#     count = 1
#
#     for i in range(1, len(input_string)):
#         if input_string[i] == current_char:
#             count += 1
#         else:
#             compressed_string += current_char + str(count)
#             current_char = input_string[i]
#             count = 1
#
#     # Append the last character and its count
#     compressed_string += current_char + str(count)
#
#     return compressed_string
#
#
# # Test the function with the given input
# input_string = "AAABBAACC"
# output_string = compress_string(input_string)
# print(output_string)


# list1 = []
# list2 = []
# for i in range(1, 101):
#     if i == 1:
#         continue
#     for j in range(2, i):
#         if i % j == 0:
#             list1.append(i)
#             break
#     else:
#         print(i, end=" ")


# input="AAABBCCAADD"
# first_char=input[0]
# result=""
# count=1
# for i in range(1,len(input)):
#     if input[i]==first_char:
#         count = count + 1
#     else:
#         result = result + first_char + str(count)
#         first_char=input[i]
#         count = 1
#
# result=result+first_char+str(count)





# print(result)



# input="AAABBCCDDEEAA"
#
# first_char=input[0]
# result=""
# count=1
#
# for i in range(1,len(input)):
#     if input[i]==first_char:
#         count+=1
#     else:
#         result=result+first_char+str(count)
#         first_char=input[i]
#         count=1
#
# result+=first_char+str(count)
#
# print(result)
# list1=[]
# list2=[]
# count=0
# for y in range(1,101):
#     if y==1:
#         continue
#     for i in range(2,y):
#         if y%i==0:
#             list1.append(y)
#             break
#     else:
#         list2.append(y)
#         count+=1
#
# print(list2)
# print(count)
# print(len(list2))

#
# def function(n):
#     result = 1
#     for i in range(1,n+1):
#         result=result*i
#
#     return result
#
# f=function(5)
# print(f)


# def function(n):
#     if n==0:
#         return 1
#     else:
#         return n*function(n-1)
#
# f=function(5)
# print(f)

# n=153
#
# count=0
# list1=[int(i)*int(i)*int(i) for i in str(n)]
# print(list1)
#
# for i in list1:
#     count=count+i
# if count==n:
#     print("aramstorng number")
# else:
#     print("not armstrong number")

# Write a program to reverse a given number.

# def Reverse(number):
#     result=0
#     while number>0:
#         last_digit=number%10
#         result=result*10+last_digit
#         number=number//10
#
#     return result
#
# r=Reverse(1234)
# print(r)

# print(1//10)

# def Fibonacci(number):
#
#
#     while


# class Practice:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def Assigment(self,cls):
#         print(f"My name is: {self.name} and my age is :{self.age} and class is {cls}",)
#
#
#
# p=Practice("Manish",30)
#
# p.Assigment(15)


# o 1 1 2 3 5

# a=0
# b=1
# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(1,n+1):
#         if a<=100:
#             print(a)
#             c=a+b
#
#             a=b
#             b=c
#
#
# fibonacci(20)

# n=153

# def armstrong(n):
#     list1=[int(i)*int(i)*int(i)for i in str(n)]
#     total_digits=sum(list1)
#     if total_digits==n:
#         print("arm strong number")
#     else:
#         print("Not arm strong number")
#
# armstrong(143)

# def Lcm(a,b):
#     for i in range(1,10000):
#         if i%a==0 and i%b==0:
#             print(i)
#             break
#
# Lcm(40,30)

# def HCF(num1,num2):
#     if num1>num2:
#         min=num2
#     else:
#         min=num1
#     for i in range(1,min+1):
#         if num1%i==0 and num2%i==0:
#             hcf=i
#
#     return hcf
#
# h=HCF(80,40)
# print(h)



# Write a program to find the sum of digits of a given number.

# def Function(number):
#     Result=0
#     list1=[int(i) for i in str(number)]
#     for i in list1:
#         Result+=i
#     return Result
#
#
# f=Function(1234)
# print(f)

#
# def Reverse(number):
#     reverse_digit=0
#     while number>0:
#         last_digit=number%10
#         reverse_digit=reverse_digit*10+last_digit
#         number=number//10
#
#     return reverse_digit
#
# r=Reverse(1234)
# print(r)

# def Prime():
#     list1=[]
#     list2=[]
#     for y in range(1,101):
#         if y==1:
#             continue
#         else:
#             for i in range(2,y):
#                 if y%i==0:
#                     list2.append(y)
#                     break
#             else:
#                 list1.append(y)
#
#     return list1
#
# p=Prime()
# print(p)


# def factorial(number):
#     result=1
#     while number>0:
#         result=result*number
#         number=number-1
#
#     return result
#
# f=factorial(5)
# print(f)

# def factorial(number):
#     if number==1:
#         return 1
#     else:
#         return number*factorial(number-1)
#
# f=factorial(5)
# print(f)

# def Armstrong(number):
#     list1=[int(i)*int(i)* int(i)for i in str(number)]
#     result=sum(list1)
#     if result==number:
#         print("number is armstrong")
#
#     else:
#         print("number is not armstrong")
#
#
# a=Armstrong(153)

# def Fibonacci(number):
#     a=0
#     b=1
#     for i in range(1,number+1):
#         if a<100:
#             print(a)
#             c=a+b
#             a=b
#             b=c
#
# f=Fibonacci(20)



# def HCF(num1,num2):
#     hcf=1
#     min_num=min(num1,num2)
#     for i in range(1,min_num+1):
#         if num1%i==0 and num2%i==0:
#             hcf=i
#
#     return hcf
#
# h=HCF(4,10)
# print(h)


# def LCM(num1,num2):
#     for i in range(1, 10000):
#         if i%num1==0 and i%num2==0:
#             print(i)
#             break

# Write a program to check if a number is a palindrome or not

# def Palindrome(number):
#     original_number=number
#     reverse_number=0
#     while number>0:
#         last_digit=number%10
#         reverse_number=reverse_number*10+last_digit
#         number=number//10
#
#     if reverse_number==original_number:
#         print("number is palindrome")
#     else:
#         print("number is not palindrome")
#
# p=Palindrome(1341)

# Find the maximum element in an array



# Find the second largest element in an array

# list1=[1,5,10,56,25,78,36,24,15]
# first_element=list1[0]
# max_element=0
# for i in list1:
#     if i>first_element:
#         max_element=i
#
# print(max_element)



# def Function(array):
#     max_element=array[0]
#     for i in array[1:]:
#         if i>max_element:
#             max_element=i
#
#     return max_element
#
# f=Function([1,2,4,10,78,36,15])
# print(f)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"input[id=alertbtn]").click()
# alert_window=driver.switch_to.alert
# alert_window.dismiss()
# driver.close()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.CSS_SELECTOR,"#openwindow").click()
# print(driver.current_window_handle)
# all_windows=driver.window_handles
# print(all_windows)
# driver.switch_to.window(all_windows[1])
# print(driver.current_window_handle)
# driver.find_element(By.LINK_TEXT,"Home").click()
# driver.switch_to.default_content()
# print(driver.current_window_handle)
# driver.close()





# def Function(n):
#     if n<=1:
#         return n
#     else:
#         return Function(n-1)*Function(n-2)
#
#
# for i in range(10):
#     print(Function(i))



# def fibonacci(n):
#     if n <= 1:
#         return n  # Base case: Return n if it's 0 or 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)  # Recursive case: Sum of the two preceding Fibonacci numbers
#
# # Example usage:
# n_terms = 10
# print("Fibonacci sequence:")
# for i in range(n_terms):
#     print(fibonacci(i))




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver=webdriver.Chrome()
#
# opentab_link="Open Tab"
#
# dynamic_element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,opentab_link)))














# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver=webdriver.Chrome()
#
# element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"")))






# def my_decorator(func):
#     def wrapper():
#         print("before the function execution")
#         func()
#         print("After the function execution")
#     return wrapper
#
# @my_decorator
# def gretting():
#     print("hello Manish")
#
#
# g=gretting()

# decor=my_decorator("Hello Manish")
# print(decor)


# input="AAABBCCDDAAEE"
#
# first_element=input[0]
# result=""
# count=1
# for i in range(1,len(input)):
#     if first_element==input[i]:
#         count+=1
#     else:
#         result=result+first_element+str(count)
#         first_element=input[i]
#         count=1
#
# result=result+first_element+str(count)
#
# print(result)

# def dec_function(func):
#     def wrapper():
#         print("before the base function execution")
#         func()
#         print("after the base function execution")
#
#     return wrapper
#
# @dec_function
# def greeting():
#     print("hello sir")
#
# g=greeting()

# from abc import ABC , abstractmethod
#
# class Car(ABC):
#     @abstractmethod
#     def mileage(self):
#         pass
#
# class Maruti(Car):
#     def mileage(self):
#         print("the mileage of maruti car is 35-45 km")
#
# featuers=Maruti()
# featuers.mileage()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://www.w3schools.com/html/html_iframe.asp")
# driver.maximize_window()
# iframe_locator=driver.find_element(By.XPATH,"//iframe[@title='W3Schools HTML Tutorial']")
# driver.switch_to.frame(iframe_locator)
# driver.find_element(By.PARTIAL_LINK_TEXT,"Sign Up").click()
# time.sleep(5)
# driver.switch_to.default_content()
# driver.close()







# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver=webdriver.Chrome()
#
# driver.get("https://www.facebook.com/")
#
# element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#email")))
#
# element.send_keys("ABC")
# time.sleep(2)
# driver.close()






# import copy
#
# list1=[1,3,[5,4],6]
# list2=copy.copy(list1)
# list2[2][1]=10
# print(list1)
# print(list2)

# import copy
# list1=[1,3,[5,4],6]
# list2=copy.deepcopy(list1)
# list2[2][1]=10
# print(list1)
# print(list2)



# class Test:
#     x=5
#     y=10
#     def __init__(self,a):
#         self.a=a
#
#
# t1=Test(4)
# print(t1.a)
# print(t1.x)
# print(t1.y)
# t1.a=55
# print(t1.a)
# print(Test.x)
# Test.x=67
# print(Test.x)


# class Test:
#     x=5
#     y=10
#     def __init__(self,a):
#         self.a=a
#         Test.c=209
#
#     def f1(self):
#         self.b=105
#         Test.m=208
# t=Test(108)
# t.f1()
# print(t.__dict__)
# print(Test.__dict__)


# def func_decor(func):
#     def wrapper():
#         print("before the decore function")
#         func()
#         print("after the decore function")
#     return wrapper
#
#
# def greeting():
#     print("hello")

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"XPATH")))
# element.click()


# //span[text()='Home & Furniture']/parent::span//preceding-sibling::div/parent::div/parent::div/parent::div/preceding-sibling::div[2]
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://www.flipkart.com/")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//span[text()='Home & Furniture']/parent::span//preceding-sibling::div/parent::div/parent::div/parent::div/preceding-sibling::div[2]").click()
# time.sleep(5)
# driver.close()

# from selenium import   webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://www.hyrtutorials.com/p/add-padding-to-containers.html")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//input[@type='password'][1]").send_keys("ABC")
# driver.find_element(By.XPATH,"//input[@type='password'][1]/parent::div[1]/child::input[3]").send_keys("Mango")
# time.sleep(5)
# driver.close()

# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
# driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
# admin=driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']")
# user_mangement=driver.find_element(By.XPATH,"//span[text()='User Management ']")


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://www.facebook.com/")
# driver.find_element(By.CLASS_NAME,"inputtext").send_keys("ABC@gmail.com")
# driver.refresh()
# driver.find_element(By.CLASS_NAME,"inputtext").send_keys("ABC@gmail.com")

# from selenium import webdriver
#
# driver=webdriver.Chrome()
#
# driver.execute_script("window.location.href='https://www.facebook.com/';")
# time.sleep(5)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# driver=webdriver.Chrome()
#
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.implicitly_wait(5)
# driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
# driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# admin_xpath=driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']")
# user_mgmt_xpath=driver.find_element(By.XPATH,"//span[normalize-space()='User Management']")
# users_xpath=driver.find_element(By.XPATH,"//ul[@role='menu']//li")
#
# act=ActionChains(driver)
# act.move_to_element(admin_xpath).move_to_element(user_mgmt_xpath).move_to_element(users_xpath).click().perform()
# act.move_to_element(admin_xpath).context_click().perform()
# time.sleep(5)
# driver.close()

# from selenium import webdriver
#
# driver=webdriver.Chrome()
# driver.execute_script("window.location.href='https://www.facebook.com/';")
# list1=[]
# list2=[]
# for y in range(1,101):
#     if y ==1:
#         continue
#     for i in range(2,y):
#         if y%i==0:
#             list1.append(y)
#             break
#     else:
#         list2.append(y)



# Write a program to find the sum of digits of a given number.

# n=1234
# def Add(number):
#     list1=[int(i) for i in str(number)]
#     result=0
#     for i in list1:
#         result=result+i
#     return result
#
# a=Add(1234)
# print(a)


# def Add(number):
#     result=0
#     while number>0:
#         last_digit=number%10
#         result=result+last_digit
#         number=number//10
#
#     return result
#
# a=Add(123456)
# print(a)

# Write a program to find the factorial of a number
# def factorial(num):
#     if num==1:
#         return 1
#     else:
#         return num*factorial(num-1)
#
# f=factorial(4)
# print(f)

# def factorial(num):
#     result=1
#     while num>0:
#         result=result*num
#         num=num-1
#     return result
#
#
# f=factorial(5)
# print(f)
# Write a program to check if a number is Armstrong or not

# def Armstrong(number):
#     list1=[int(i)* int(i)* int(i) for i in str(number)]
#     total=sum(list1)
#     if number==total:
#         print("number is armstrong")
#     else:
#         print("number is not armstrong")
#
# a=Armstrong(152)

# Write a program to reverse a given number

# def reverse(number):
#     result=0
#     while number>0:
#         last_digit=number%10
#         result=result*10+last_digit
#         number=number//10
#     return result
#
# r=reverse(1234)
#
# print(r)
# Write a program to find the Fibonacci series up to a given number of terms
# a = 0
# b = 1
#
# for i in range(20):
#     if a<100:
#         c = a + b
#         print(a)
#         a = b
#         b = c

# Write a program to find the GCD (Greatest Common Divisor) of two numbers
# def GCD(num1,num2):
#     min_num=min(num1,num2)
#     result=1
#     for i in range(1,min_num+1):
#         if num1%i==0 and num2%i==0:
#             result=i
#
#     return result
# hcf=GCD(10,20)
# print(hcf)

# Write a program to check if a number is a palindrome or not

# def palindrome(num):
#     new_num=num
#     result=0
#     while num>0:
#         last_digit=num%10
#         result=result*10+last_digit
#         num=num//10
#
#     if result==new_num:
#         print("number is palindrome")
#     else:
#         print("number is not palindrome")
#
#
# p=palindrome(1221)

# def decor_function(fun):
#     def wrapper():
#         print("befor decorator")
#         fun()
#         print("after decorator")
#
#     return wrapper
#
# @decor_function
# def greeting():
#     print("hello guest")
#
# greeting()
# list1=[1,2,3,4,5]
#
# # n=4
# #
# # sort_element=n%len(list1)
# #
# # result=list1[-sort_element:]+list1[:-sort_element]
# #
# # print(result)
# n=3
# sort_element=n%len(list1)
#
# result=list1[sort_element:]+list1[:sort_element]
# print(result)

from abc import ABC , abstractmethod
from datetime import datetime


# class Car:
#     @abstractmethod
#     def mileage(self):
#         pass
#
# class Honda(Car):
#     def mileage(self):
#         print("honda car mileage")
#
# h=Honda()
# h.mileage()

# for i in range(1,6):
#     for y in range(1,i+1):
#         print("*", end=" ")
#     print()



# from selenium import webdriver
#
# driver=webdriver.Chrome()
# driver.execute_script("window.location.href='https://www.onlinegdb.com/';")



#

# first_element=input[0]
# result=""
# count=1
# for i in range(1,len(input)):
#     if first_element==input[i]:
#         count=count+1
#     else:
#         result+=first_element+str(count)
#         first_element=input[i]
#         count=1
#
# result=result+first_element+str(count)
# print(result)

# input="AABBCCAAADDEE"
# result=""
# dict1={}
# for i in input:
#     if i in dict1:
#         dict1[i]+=1
#     else:
#         dict1[i]=1
#
# for key,value in dict1.items():
#     result=result+key+str(value)
# print(result)

# list1=[]
# for i in input:
#     if i not in list1:
#         list1.append(i)
#
# print(list1)

# def isEven(x):
#     if x%2==0:
#         return True
#     else:
#         return False
#
# list1=[1,2,3,4,5,6,7,8,9,10]
#
# result=list(filter(isEven,list1))
# print(result)

# def double(x):
#     return 2*x
#
# list2=[2,3,4,5]
#
# result=list(map(double,list2))
# print(result)


# set1={10,20,30,40}
# set2={30,40,50,60}
#
# print(set1.union(set2))
# print(set1.intersection(set2))

# input="B4A1D3"
# list1=[]
# list2=[]
# for i in input:
#     if i.isalpha():
#         list1.append(i)
#     else:
#         list2.append(i)
#
# print(list1)
# print(list2)
#
# print("".join(sorted(list1)+sorted(list2)))

# input="a4b3c2"
# result=""
# for i in input:
#     if i.isalpha():
#         result=result+i
#         previous=i
#     else:
#         result=result+previous*(int(i)-1)
#
# print(result)

# input="AABBCCCDDAAFG"
#
# dict1={}
# for i in input:
#     if i in dict1.keys():
#         dict1[i]=dict1[i]+1
#     else:
#         dict1[i]=1
#
# for key,value in dict1.items():
#     result=result

# def decor_fun(fun):
#     def wrapper():
#         print("before decorating function")
#         fun()
#         print("after decorating function")
#     return wrapper
# @decor_fun
# def greetings():
#     print("hello guest")
#
# greetings()

# CREATE TABLE IF NOT EXISTS rcdcs (
#   day INTEGER NOT NULL,
#   is_rc TINYINT NOT NULL,
#   msn VARCHAR(255) NOT NULL,
#   start_time_ist DATETIME NOT NULL,
#   end_time_ist DATETIME,
#   elapsed_seconds INTEGER,
#   status TINYINT,
#   PRIMARY KEY (day, is_rc, msn)
# )
# PARTITION BY RANGE (day) (
#   PARTITION p00000000 VALUES LESS THAN (0)
# );

# def dt_gmt_to_ist(dt):
#   assert dt.tzinfo is None
#   return dt + datetime.timedelta(minutes=330)
# Write a program to find the sum of digits of a given number

# print(1234%10)
# def add(number):
#   result=0
#   while number>0:
#     last_digit = number % 10
#     result=result*10+last_digit
#     number=number//10
#
#   return result
# a=add(1234)
# print(a)

# Write a program to check if a number is prime or not.
# def Prime(number):
#   for i in range(2,number):
#     if number%i==0:
#       print("number is not prime")
#       break
#   else:
#     print("number is prime")
# Write a program to find the factorial of a number

# def fact(number):
#   if number==0:
#     return 1
#   else:
#     return number* fact(number-1)
#
# f=fact(4)
# print(f)

# def fact(number):
#   result=1
#   while number>0:
#     result=result*number
#     number=number-1
#
#   return result
# f=fact(6)
# print(f)

# def add(number):
#   result=0
#   while number>0:
#     last_digit=number%10
#     result=result+last_digit
#     number=number//10
#
#   print(result)
#
# add(12345)

# Write a program to check if a number is Armstrong or not 153

# def armstrong(number):
#     list1=[int(i)*int(i)*int(i) for i in str(number)]
#     result=sum(list1)
#     print(list1)
#     print(result)
#     if result==number:
#         print("number is armstrong")
#     else:
#         print("number is not armstrong")
#
# a=armstrong(371)

# Write a program to reverse a given number
#
# def reverse(number):
#     result=0
#     while number>0:
#         last_digit=number%10
#         result=result*10+last_digit
#         number=number//10
#
#     return result
#
#
# r=reverse(1234)
# print(r)



# def palindrome(number):
#     number1=number
#     result=0
#     while number>0:
#         last_digit=number%10
#         result=result*10+last_digit
#         number=number//10
#     print(result)
#
#     if number1==result:
#         print("number is palindrome")
#     else:
#         print("number is not palindrome")
#
# p=palindrome(1221)

# Write a program to find the sum of all prime numbers up to a given number.

# for i in range(1,101):
#     if i==1:
#         continue
#     else:
#         for y in range(2,i):
#             if i%y==0:
#                 break
#         else:
#             print(i)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.implicitly_wait(5)
# driver.find_element(By.XPATH,"//input[@value='radio1']").click()
# time.sleep(5)
# driver.close()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# driver=webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
# dropdown=Select(driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']"))
# dropdown.select_by_index(2)
# time.sleep(2)
# driver.close()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# driver=webdriver.Chrome()
#
# driver.implicitly_wait(5)
#
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# dropdown=driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']")
# dropdown_menu=Select(dropdown)
# dropdown_menu.select_by_index(2)
# time.sleep(2)
# driver.close()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
# checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
#
# for i in checkboxes:
#     i.click()
#
# time.sleep(5)
# driver.close()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# print(driver.title)
# driver.implicitly_wait(5)
#
# driver.find_element(By.CSS_SELECTOR,"#openwindow").click()
# windows=driver.window_handles
# driver.switch_to.window(windows[1])
# print(driver.title)
# driver.switch_to.window(windows[0])
# driver.find_element(By.XPATH,"//input[@value='radio1']").click()
# print(driver.title)
# print(windows)
# time.sleep(5)
# driver.switch_to.default_content()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
# driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Manish")
# driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
#
# alerts=driver.switch_to.alert
# alerts.accept()
# time.sleep(4)
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver=webdriver.Chrome()
#
# driver.get("https://www.facebook.com/")
#
# element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#email")))
#
# element.send_keys("ABC")
# time.sleep(2)
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.facebook.com/")
# element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@type='text']")))
#
# element.send_keys("Hello")
# time.sleep(5)
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"input[value='radio1']").click()
# driver.close()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
drop_down=driver.find_element(By.ID,"dropdown-class-example")
select=Select(drop_down)
select.select_by_index(1)
time.sleep(5)
driver.close()













































