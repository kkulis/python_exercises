

def Bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return(arr)



L = [1, 2, 5, 7, 10, 15, 20, 45, 3, 4, 5, 6, 7, 8, 8, 8, 66]

print(Bubble_sort(L))
