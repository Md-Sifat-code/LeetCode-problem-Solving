def binary_search (arr,items):
    low =0;
    high = len(arr)-1
    while(low<=high):
        mid = (low+high)/2
        guess =arr[mid]
        if(guess == items):
            return mid
        elif(guess>items):
            high =mid-1
        else:
            low = mid+1
    return None