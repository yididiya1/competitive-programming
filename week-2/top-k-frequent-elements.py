
def topKFrequent(nums):
    nums.sort()
    my_dict = {}
    key_list = list(my_dict.keys())
    val_list = list(my_dict.values())
    for i in range(len(nums)):
        #print(nums[i],my_dict)
        if nums[i] not in key_list:
            my_dict[nums[i]] = 1
            key_list.append(nums[i])
        else :
            my_dict[nums[i]] += 1
            
    #key_list = list(my_dict.keys())
    #val_list = list(my_dict.values())
    #key_list.sort(reverse = True)

    result = []
    

    key_list = list(my_dict.keys())
    val_list = list(my_dict.values())
    
    
    
    
    val_list.sort(reverse = True)
    print(my_dict)
    print(key_list)
    print(val_list)
    
    for i in range(k):
        
        val = val_list[i]
        key = list(my_dict.keys())[list(my_dict.values()).index(val)]
        result.append(key)
        print(i,val,key)
        del my_dict[key]
        
        
    #print(val_list[k-1])

    #result =  [k for k,v in my_dict.items() if v >= val_list[k-1]]
    # result = [k for k,v in mydict.items() if float(v) >= 17]
    #print(result)    
    return result

    