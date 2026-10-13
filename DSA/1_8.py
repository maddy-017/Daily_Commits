# def sum_values(values: list[int]) -> int:
#     total = 0
#     for value in values:
#         total += value
#     return total

# assert sum_values([]) == 0
# assert sum_values([4, -1, 6]) == 9
# print("All tests passed")
# def mxm(values:list[int])->int:
#     if not values:
#         raise ValueError("list = empty ")
#     best = values[0]
#     for value in values:
#         if value > best:
#             value=best
#             return best

# assert mxm ([-3,-9,-7]) == -3        
# def maximum(values: list[int]) -> int:
#     if not values:
#         raise ValueError("values must not be empty")
    
#     best = values[0]
#     minimum =values[0]
    
#     for value in values:
#         if value > best:
#             best = value
    
#     return best

#     for value in values:
#         if value < minimum:
#             best = value
    
#     return minimum
  


# assert maximum([-7, -9, -3]) == -3
# assert maximum([-7, -9, -3]) == -9
def positive_number():
    user_list = list(int(x) for x in input("Enter elements separated by space: ").split())

    zero = 0
    positive = 0
    negative = 0

    for value in user_list:
        if value == 0:
            zero = zero + 1
        elif value > 0:
            positive =positive+1
        elif value < 0 :
            negative=negative+1

    return print(f"positive : {positive},negative :{negative} ,zero :{zero} ")     
result = positive_number()
print(result)





        

# # 1. Define the function with parameters
# def add_numbers(num1, num2):
#     result = num1 + num2
#     return result

# # 2. Pass values (inputs) into the function when calling it
# total = add_numbers(5, 10)
# print(total)  # Output: 15

