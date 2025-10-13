import heapq as hq

arr = [2,4,5,12,453,344,52,57,876,53]
#Heapify method sorts the list , this is min heap

hq.heapify(arr)
print("1: ", arr) # [2, 4, 5, 12, 53, 344, 52, 57, 876, 453]

hq.heappush(arr, 100)
print("2: ", arr) # [2, 4, 5, 12, 53, 344, 52, 57, 876, 453, 100]

hq.heappop(arr)
print("4: ", arr)

# Used to pop and push the element in same time
print ("Element: ", hq.heappushpop(arr, 5))
print("5: ",arr)

#Used to get n largest elements in heap
print("6: ", hq.nlargest(4,arr))

#Used to get n smallest elements in heap
print("7: ", hq.nsmallest(4,arr))

