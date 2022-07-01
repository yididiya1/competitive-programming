class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x:x[1],reverse=True)
        total_units = 0
        
        for box in boxTypes:
            if truckSize == 0:
                break
                
            boxNo = box[0]
            boxUnit = box[1]
            
            if boxNo > truckSize:
                total_units += truckSize * boxUnit
                truckSize = 0
            else:
                total_units += boxNo * boxUnit
                truckSize -= boxNo
                
        return total_units
            
        