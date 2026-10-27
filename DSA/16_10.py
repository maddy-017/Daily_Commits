# def sec_largest(values: list[int]) -> int:
#     largest = max(values)
#     second_largest = None

#     for value in values:
#         if value != largest:
#             if second_largest is None or value > second_largest:
#                 second_largest = value

#     return second_largest


# print(sec_largest([1, 2, 3, 4]))  # Output: 3
# print(sec_largest([4, 3, 2, 1]))  # Output: 3
# print(sec_largest([10, 10, 8, 7]))  # Output: 8
def duplicates( values: list[int])->list[int]:
    seen =[]
    duplicate =[]
    for value in values:
        if value not in seen:
            seen.append(value)
        else:
            duplicate.append(value)
    return duplicate
print (duplicates([1,2,3,4,4,5,5]))           
# def freq(values: list[int])->dict[int:int]:
#     counts :dict[int:int] ={}
#     for value in values:
#      counts[value] = counts.get(value, 0) + 1
#     return counts
# print(freq([1,2,2,3,4]))