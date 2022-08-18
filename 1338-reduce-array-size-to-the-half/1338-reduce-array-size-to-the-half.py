class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr.sort()
        my_dict = {}
        summ = 0
        size = len(arr)//2
        output = []
        
        for i in range(len(arr)):
            if arr[i] not in my_dict:
                my_dict[arr[i]] = 1
            else :
                my_dict[arr[i]] += 1
            
        #print(my_dict)
        
        sorted_dict = {k: v for k, v in sorted(my_dict.items(),reverse=True, key=lambda item: item[1])}
        
        #print(sorted_dict)
        
        for key in sorted_dict:
            if sorted_dict[key] + summ >= size:
                output.append(key)
                break
            else :
                output.append(key)
                summ+=sorted_dict[key]
        
        #print(output)
        return len(output)