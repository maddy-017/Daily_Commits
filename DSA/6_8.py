# def frequencies(values: list[str]) -> dict[str:int]:
#     counts: dict[str, int] = {}

#     # Step 1: Count every number
#     for value in values:
#         counts[value] = counts.get(value, 0) + 1
#     return counts
    

   


# print(frequencies(["tiger","lion","lion"]))
# def freq(values:list[str])->list[int]:
#     result =[]
#     for value in values:
#        count = 0 
#        for x in values:
#            if x==value:
#                count+=1
#        if count == 1:
#            result.append(value)

#     return result
# print(freq([12,12,2]))      
def duplicate (values:list[int])->list[int]:
    seen =[]
    
    for value in values:
        if value in seen:
            return value
        seen.append(value)
        
print(duplicate([3,1,3]))
