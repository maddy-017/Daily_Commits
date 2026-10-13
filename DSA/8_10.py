# def duplicates(values: list[int]) -> bool:
#     seen: set[int] = set()
#     for value in values:
#         if value in seen:
#             return value
#         seen.add(value)
        
#     return False

# print(duplicates([2, 2, 1]))
# def duplicates(values: list[int]) -> list[int]:
#     seen: set[int] = set()
#     dup : list[int]=[]
#     for value in values:
#         if value in seen:
#             dup.append(value)
#         else:
#             seen.add(value)
#     return dup


# print(duplicates([2, 2, 1,4,1]))
# def duplicates(values: list[int]) -> bool:
#     seen :list[int]=[]
#     for i in range(len(values)):
#         for j in range(i+1,len(values)):
#             if values[i]==values[j]:
#                 return True
            
                
#     return False        
# print(duplicates([4,3,2,2]))
# def duplicates(values: list[int],k:int) -> bool:
#     for i in range(len(values)):
#         for j in range(i+1,len(values)):
#             if values[i]==values[j]:
#                 return True
            
                
#     return False        
# print(duplicates([4,3,2,2]))

def duplicate_within_k(values: list[int], k: int) -> bool:
    for i in range(len(values)):
        for j in range(i + 1, min(i + k + 1, len(values))):
            if values[i] == values[j]:
                return True

    return False
print(duplicate_within_k([2,1,3,4,2],3))