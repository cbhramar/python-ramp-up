def regular(arr,low,high,key):
	if arr[low]==key:
		return low
	while low<high:
		mid=int((low+high)/2)
		if arr[mid]==key:
			return mid
		elif arr[mid]<key:
			return regular(arr,mid+1,high,key)
		else:
			return regular(arr,low,mid-1,key)
	return -1

def first(arr,low,high,key):
	if arr[low]==key:
		return low
	while low<high:
		mid=int((low+high)/2)
		if arr[mid]<key:
			return first(arr,mid+1,high,key)
		else:
			return first(arr,low,mid,key)
	return -1

def last(arr,low,high,key):
	if arr[high]==key:
		return high
	while low<high:
		mid=int((low+high)/2)
		if arr[mid]>key:
			return last(arr,low,mid-1,key)
		else:
			return last(arr,mid+1,high,key)
	return -1

arr=[1,2,2,3,3,3,3,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6]
n = len(arr)
k = 2
print(arr)

regular_index = regular(arr,0,n-1,k)
first_index = first(arr,0,n-1,k)
last_index = last(arr,0,n-1,k)

print("Regular Binary Search: " + str(regular_index)) 
print("First Occurence:       " + str(first_index)) 
print("Last Occurence:        " + str(last_index)) 
