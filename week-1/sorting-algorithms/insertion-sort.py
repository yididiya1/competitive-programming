def insertionSort1(n, arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            print(' '.join(map(str, arr)))
            #print(arr)
            j -= 1           
        arr[j+1] = key
        
    print(' '.join(map(str, arr)))
        

insertionSort1(5,[2,4,6,8,3])
   