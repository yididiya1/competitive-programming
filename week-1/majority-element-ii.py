def majorityElement(nums):
    
    my_dict = {}
    result = []
    rep = (len(nums)//3)+1
    
    for num in nums:
        key_list = list(my_dict.keys())   
        if num in key_list:
            my_dict[num]+=1
        else:
            my_dict[num] = 1
    
    
    key_list = list(my_dict.keys())
    val_list = list(my_dict.values())
    
    print(my_dict,rep)

    result = [k for k,v in my_dict.items() if v >= rep]
    
    #print(result)
    return result


example = majorityElement([-1,-1,-1])
print(example)