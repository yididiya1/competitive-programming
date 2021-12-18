def largestNumber(nums):
        num_string = [str(x) for x in nums ]
        result = ''
        for i in range(1,len(num_string)):
            key = num_string[i]
            j = i - 1
            while j >= 0 and int(key+num_string[j]) < int(num_string[j]+key):
                    num_string[j+1] = num_string[j]
                    j -= 1 
            num_string[j+1] = key
            
        
        final_list = num_string[::-1]
        print(final_list)
        
        for i in range(len(final_list)):
            result+=final_list[i]
            
        print(result)
        
        return result.lstrip('0') or '0'

example = largestNumber([9, 5, 34, 3, 30])
print(example)