class Solution(object):
    def lengthOfLongestSubstring(self, s):
        chars = list(str(s))
        newlist = []
         
        longest = 0
            
        for i in range(len(chars)):
            new_list = []
            new_list.append(chars[i])
            for j in range (i+1,len(chars)):
                if chars[j] not in new_list:
                    new_list.append(chars[j])
                else:
                    break
            #print(new_list)
            
            if len(new_list) > len(newlist):
                newlist = new_list
            
                
                
         
        return len(newlist)
        