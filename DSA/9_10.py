# def neg_num_find (values : list[int])->list[int]:
#    negatives =set()
# for index ,value in enumerate(values):
#         if value < 0:
#             negatives.add(value)
# print(f"these are the negative number{negatives}")
#         return -1       
# user_input = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
# neg_num_find(user_input)

# def sum_of_array(values: list[int]) :
#     total = 0

#     for value in values:
#         total = total + value
#     print(total)
    


# user_input = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
# result = sum_of_array(user_input)
# print(result)


# def sum_of_positiveonlyarray(values: list[int]):
#     total = 0

#     for value in values:
#         if value > 0:
#          total = total + value
#     print(total)
    


# user_input = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
# result = sum_of_positiveonlyarray(user_input)
# print(result)

def find_max_min(values: list[int]) -> tuple[int, int]:

    maxi = values[0]
    mini = values[0]

    for value in values[1:]:
        if value > maxi:
            maxi = value
        if value < mini:
            mini = value

    print(maxi, mini)

user_input = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
find_max_min(user_input)



            
                