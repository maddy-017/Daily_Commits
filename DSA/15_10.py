# def reverse_array(values:list[int])->list[int]:
#     result = values.copy()
#     left, right = 0, len(result) - 1
#     while left < right:
#         result[left], result[right] = result[right], result[left]
#         left += 1
#         right -= 1
#     return result
# assert reverse_array([1,2,3,4])==[4,3,2,1]
def is_array_sorted (values:list[int])->bool:
    for i in range(len(values)-1):
        if values[i]>values[i+1]:
           return False
    return True

print(is_array_sorted([1,2,4,3]))

 
	

    
