def selectionSort(arr,n):
        for i in range(n-1):
            smallest_no_index = i
            for j in range(i+1,n):
                if arr[j] < arr[smallest_no_index]:
                    smallest_no_index = j
            arr[i], arr[smallest_no_index] = arr[smallest_no_index], arr[i]
        return arr

example = selectionSort([1 ,4 ,3 ,9 ,7],5)
print(example)
