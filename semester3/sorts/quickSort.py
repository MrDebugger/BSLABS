def partition(arr,low,high): 
	border = low 		 
	pivot = arr[high]	
	for j in range(low , high): 
		if arr[j] <= pivot: 
			arr[border],arr[j] = arr[j],arr[border] 
			border = border+1
	arr[border],arr[high] = arr[high],arr[border] 
	return border  


def quickSort(arr,low,high): 
	if low < high: 
		pi = partition(arr,low,high) 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("%d" %arr[i]), 

