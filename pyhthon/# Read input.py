# # # # def factorial(n):
# # # #     result = 1
# # # #     for i in range(1, n + 1):
# # # #         result *= i
# # # #     return result


# # # # # Read input and print result
# # # # num = int(input())
# # # # print(str(num) + "! = " + str(factorial(num)))
# # # def factorial(n):
# # #     result = 1
# # #     for i in range(1, n + 1):
# # #         result *= i
# # #     return result


# # # # Read input and print result
# # # num = int(input())
# # # print(str(num) + "! = " + str(factorial(num)))
# # def factorial(n):
# #      result = 1
# #      for i in range (1,n+1):
# #         result *= i 
# #      return result 
# # num = int (input())
# # factorial
# # print(f"{num}! = {factorial(num)}")
# # Read count
# # n = int(input())

# # Read numbers and calculate sum
# # Read count


# # Read numbers and calculate sum
# # 1. Get the total number of items first
# num_inputs = int(input())

# user_list = []

# # 2. Loop that many times
# for _ in range(num_inputs):
#     item = int(input())
#     user_list.append(item)
# sum_lst = sum(user_list)
# print("Sum:%d"%sum_lst)
    

# # Print the sum



# # Print the sum
# import math

# # Read the shape
# shape = input().strip()

# if shape ==	"rectangle":
#   b_r = input()
#   w_r = input()
  
#   print ("Area: %.2f"%(float(b_r*w_r)))
# elif shape =="circle":
#   r = float(input())
#   print ("Area: %.2f"%(float(math.pi *r*r)))

# elif shape =="triangle":
#   base = float(input())
#   height = float(input())
#   print("Area: %.2f"%(float(0.5*base*height)))
# else:
#   print("shape not matched")
# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }
# for key in person:
#     print(key)

# for k, value in person.items():
#     print(k, value) # this way we get both keys and values printed out

# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }
# for key in person:
#     if key == 'skills':
#         for skill in person['skills']:
#             print(skill)
# count = 10
# while count>-1:
#     print(count)
#     count -=1
# for i in range(10,-1):
#     print(i)

    # count = count + 1
#prints from 0 to 4
# for i in range(8):
#     for j in range(8):
#         print("#", end=" ")
#     print()
# for i in range(11):
# #     print("%d x %d = %d"%(i,i,i*i) )
# list = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for lst in list:
#     print(lst)
# t_1 =0
# t_2 =0
# for i in range(0,101,2):
#     t_1+=i
#     print(t_1,end="")
# for i in range(1,101,2):
#     t_2+=i
#     print(t_2)
# even_sum = 0
# odd_sum = 0

# for i in range(101):
#     if i%2==0:
#         even_sum += i
#     else:
#         odd_sum += i

# print("Sum of evens: %d."%(even_sum),end=" ")
# print("And the sum of odds:", odd_sum)
        
sales = [4500, 3200, 5000, 3200, 6100, 4500, 3900]
print("Total sales for the week : ",sum(sales))
# QB
highest_sale =max(sales)
highest_sale_index=sales.index(highest_sale)+1
print(f"The highest sale was on day {highest_sale_index} & it was {highest_sale}")
# Q3
sales[3] = 3800
print(sales)
# Q4
sales1=[]
for sale in sales:
    if sale not in sales1:
        sales1.append(sale)
print (sales1)   

        

        



