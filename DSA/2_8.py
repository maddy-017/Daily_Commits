def freq(values:list[int])->dict[int,int]:
    count:dict[int,int]={}
    for value in values:
        count[value]=count.get(value,0)+1
    return count
assert freq([4,2,4])==  {4:2,2:1}
    
