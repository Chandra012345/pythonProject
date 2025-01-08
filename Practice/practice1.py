# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='root')
# cur=mydb.cursor()
# cur.execute("CREATE DATABASE db1")
import time

from selenium.webdriver.support.wait import WebDriverWait

# creating a new table
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',
#                              user='root',
#                              password='root',
#                              database='db1')
# cur=mydb.cursor()
# s="create table book(bookid integer(4), title varchar(25), price float(5,2))"
# cur.execute(s)

# inserting data into tables

# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',
#                              user='root',
#                              password='root',
#                              database='db1')
# cur=mydb.cursor()
# s="insert into book(bookid,title,price) values(%s,%s,%s)"
# bookid=int(input("enter the value of book id"))
# title=str(input("enter the value of string"))
# price=float(input("enter the value of book price"))
# bookdata=(bookid,title,price)
# cur.execute(s,bookdata)
# mydb.commit()
# cur.close()
# mydb.close()

#inserting multiple data inside table

# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',
#                              username='root',
#                              password='root',
#                              database='db1')
# cur=mydb.cursor()
# s="insert into book(bookid,title,price) values (%s,%s,%s)"
# books=[(5,'java',500),(45,'c##',450),(67,'C',890)]
# cur.executemany(s,books)
# mydb.commit()
# print(type(books))
# mydb.rollback()


# facthing the data from database:

# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',
#                              username='root',
#                              password='root',
#                              database='db1')
# cur=mydb.cursor()
# s="select * from book"
# cur.execute(s)
# result=cur.fetchall()
# for rec in result:
#     print(rec)
#     print(type(rec))

# Write a program to find the sum of digits of a given number


# input = "B4A1D3"
# list1 = []
# list2 = []
#
# for i in input:
#     if i.isalpha():
#         list1.append(i)
#     else:
#         list2.append(i)
#
# print(list1)
# print(list2)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.implicitly_wait(4)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
# driver.find_element(By.XPATH,"//label[@for='radio1']").click()
# time.sleep(5)
# driver.close()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# driver=webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# dropdown=driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']")
# select=Select(dropdown)
# select.select_by_index(1)
# time.sleep(5)
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
#
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.implicitly_wait(5)
# checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
# print(len(checkboxes))
# for i in checkboxes:
#     i.click()
# time.sleep(5)
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.implicitly_wait(4)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.XPATH,"//button[@id='openwindow']").click()
# windows=driver.window_handles
# print(windows)
# driver.switch_to.window(windows[1])
# print(driver.title)
# driver.switch_to.window(windows[0])
# print(driver.title)
# driver.close()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
#
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.implicitly_wait(4)
# driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Manish")
# driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
# alerts=driver.switch_to.alert
# alerts.accept()
# time.sleep(5)
# driver.close()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# driver=webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# drop_down=driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']")
# drop_down_menu=Select(drop_down)
# drop_down_menu.select_by_index(1)
# time.sleep(5)
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
# checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
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
# driver.maximize_window()
# driver.find_element(By.ID,"openwindow").click()
# print(driver.current_window_handle)
# windows=driver.window_handles
# driver.switch_to.window(windows[1])
# print(driver.current_window_handle)
# time.sleep(4)
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.ID,"name").send_keys("Manish")
# time.sleep(5)
# driver.find_element(By.ID,"alertbtn").click()
# alerts=driver.switch_to.alert
# alerts.accept()
# driver.close()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# iframe=driver.find_element(By.ID,"courses-iframe")
# driver.switch_to.frame(iframe)
# driver.find_element(By.LINK_TEXT,"Courses").click()
# time.sleep(5)
# driver.close()



# def prime(number):
#     for i in range(2,number):
#         if number%i==0:
#             print("number is not prime number")
#             break
#     else:
# #         print("number is prime number")
#
# list1=[]
# list2=[]
# for i in range(2,101):
#     for y in range(2,i):
#         if i%y==0:
#             list1.append(i)
#             break
#     else:
#         list2.append(i)
#
# print(list2)

# def armstrong(number):
#
#     list1=[ int(i)*int(i)*int(i )for i in str(number)]
#     result=sum(list1)
#     if result==number:
#         print("number is armstrong")
#     else:
#         print("number is not armstrong")
#
# a=armstrong(153)

# import copy
# list1=[2,5,[10,30]]
#
# list2=copy.deepcopy(list1)
#
# list2[2][1]=50
#
# print(list1)
# print(list2)
# 1234
# def palindrome(number):
#     number1=number
#     last_element=number%10
#     result=0
#     while number>0:
#         result=result*10+last_element
#         number=number//10
#         last_element=number%10
#     if result==number1:
#         print("number is palindrome")
#     else:
#         print("number is not palindrome")
#
#
# p=palindrome(1221)

# f=open("manish.txt","r")
# result=f.read()
# print(result)
# f.close()

# file=open("manish.txt", "w")
# result=file.write("I am groot\n")
# file.close()

# f=open("manish.txt","a")
# result=f.write("I am second grood\n")
# f.close()

# s="AAABBCCCDDAA"
# first_element=s[0]
# count=1
# result=""
# for i in range(1,len(s)):
#     if first_element==s[i]:
#         count+=1
#     else:
#         result+=first_element+str(count)
#         first_element = s[i]
#         count=1
#
#
# result+=first_element+str(count)
#
# print(result)
# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             print("number is not prime")
#             break
#     else:
#         print("number is prime ")
#
# p=prime(7)

# list1=[]
# list2=[]
# for i in range(2,101):
#     for y in range(2,i):
#         if i%2==0:
#             list1.append(i)
#             break
#     else:
#         list2.append(i)
#
#
# print(list2)


# def fact(number):
#     if number<=1:
#         return 1
#     else:
#         return number*fact(number-1)
#
# f=fact(5)
# print(f)

# def fact(number):
#     result=1
#     while number>0:
#         result=result*number
#         number=number-1
#
#     print(result)
#
# f=fact(5)

# def armstrong(number):
#     number1=number
#     list1=[int(i)* int(i)* int(i) for i in str(number)]
#     result=sum(list1)
#
#     if result==number1:
#         print("number is armstrong")
#     else:
#         print("number is not armstrong")
#
# a=armstrong(157)

# 1234
# def reverse(number):
#     result=0
#     number1=number
#     while number>0:
#         last_digit=number%10
#         result=result*10+last_digit
#         number=number//10
#
#     if result==number1:
#         print(f'{number1} is palindrome')
#     else:
#         print(f'{number1} is not palindrome')
#
# r=reverse(1221)


# def hcf(number1,number2):
#     if number1>number2:
#         min=number2
#     else:
#         min=number1
#     for i in range(1,min+1):
#         if number1%i==0 and number2%i==0:
#             gcd=i
#
#     return gcd
#
# h=hcf(10,20)
# print(h)



# first_element=input[0]
# count=1
# result=""
#
# for i in range(1,len(input)):
#     if first_element==input[i]:
#         count+=1
#     else:
#         result=result+first_element+str(count)
#         count = 1
#         first_element = input[i]
#
#
#
#
# result=result+first_element+str(count)
#
# print(result)


# s="AAABBCCCDDAA"
# first_element=s[0]
# count=1
# result=""
# for i in range(1,len(s)):
#     if first_element==s[i]:
#         count+=1
#     else:
#         result+=first_element+str(count)
#         first_element = s[i]
#         count=1
#
#
# result+=first_element+str(count)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.find_element(By.XPATH,"//input[@value='radio1']").click()
# time.sleep(2)
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# driver=webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# select=driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']")
# dropdown=Select(select)
# dropdown.select_by_index(2)
# time.sleep(5)
# driver.close()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
#
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.CSS_SELECTOR,"#openwindow").click()
# print(driver.title)
# windows=driver.window_handles
# driver.switch_to.window(windows[1])
# print(driver.title)
# driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver=webdriver.Chrome()
#
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# driver.find_element(By.ID,"autocomplete").send_keys("In")
# wait= WebDriverWait(driver,10)
# content=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//li[@class='ui-menu-item']//div")))
# print(len(content))
#
# for i in content:
#     if i.text== "India":
#         i.click()
# time.sleep(5)
#
# driver.close

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.get("https://www.livecareer.com/cv/templates?utm_source=qa")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//img[@title='CV Template Free Notable Orange CV Brown 1']//ancestor::div[@class='col-4 eq-col sort default viewed active']//span[@class='zoom-icon']").click()
# time.sleep(5)


# f=open("manish.txt","r")
# text=f.read()
# print(text)

# Write a program to find the Fibonacci series up to a given number of terms
# 01123581321


# a = 0
# b = 1
# for i in range(10):
#
#     c = a + b
#     print(a)
#     a,b=b,c


# def fibonacci(number):
#
#     a,b=0,1
#     fibonacci_sequence=[]
#     for i in range(number):
#         fibonacci_sequence.append(a)
#         a,b=b,a+b
#
#     return fibonacci_sequence
#
# fObj=fibonacci(10)
# print(fObj)

# list1=[1,2,3,4,5]
#
# def Left_shift(number):
#     eff_left_shift=number%len(list1)
#     list2=list1[eff_left_shift:]+list1[:eff_left_shift]
#     return list2
#
# lShift=Left_shift(2)
# print(lShift)
#
# def Right_shift(number):
#     eff_right_shift=number%len(list1)
#     list3=list1[-eff_right_shift:]+list1[:-eff_right_shift]
#     return list3
#
# r=Right_shift(2)
# print(r)

a=5
# b=2
#
# try:
#     print("file open")
#     print(a/b)
#
# except Exception as e:
#     print("number cant be divided:", e)
#
# finally:
#     print("file close")

# from abc import ABC, abstractmethod
#
# class Person(ABC):
#     def __init__(self,n):
#         self.n=n
#
#     @abstractmethod
#     def Eye(self):
#         pass
#
#     @abstractmethod
#     def Ear(self):
#         pass
#
# class Doctor(Person):
#
#     def Eye(self):
#         print("the number of eyes a doctor have", self.n)
#
#
# dObj=Doctor(2)
# dObj.Eye()


# list1 = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 2, 4, 2, 5]
#
# for i in range(len(list1)-1, -1,-1):
#     if list1[i]==2:
#         del list1[i]
#         break
# print(list1)


# def Remove_last_iteration(lst,number):
#     n=len(lst)-1
#     for i in range(n,-1,-1):
#         if lst[i]==number:
#             del lst[i]
#             break
#     return lst
#
# lst=[1,2,3,4,2,5]
# number=2
# r=Remove_last_iteration(lst,number)
# print(r)
# input:
# list1=[2,10,5,2,7,2,5,7,8,9,2]
# number=2
# output:
# [0,10]
# 
# def Index_finder(lst,number):
#     for i in range(len(list1)):
#         if list1[i]==2:
#             print(f"index : {i} and value {list1[i]}")
#
# Index_finder(list1,2)



from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()
try:
    element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"id")))
    element.click()
except Exception as e:
    driver.refresh()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id")))
    element.click()
    print(e)







































