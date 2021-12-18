def checkArithmeticSubarrays(nums,l,r):
        result = []
        for i in range(len(l)):
            sub_array = nums[l[i]:r[i]+1]
            sub_array.sort()
            print(sub_array)
            count = 0
            for j in range(len(sub_array)-1):         
                if sub_array[j+1] - sub_array[j] == sub_array[1]-sub_array[0]:
                    count+=1
            if count == len(sub_array) - 1:
                result.append(True)
            else:
                result.append(False)
                
        return result
                    

example = checkArithmeticSubarrays([4,6,5,9,3,7],[0,0,2],[2,3,5])
print(example)