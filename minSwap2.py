def __init__(self):
    pass

  def minSwaps2(self, arr):
    i=0
    minN = 0
    count = 0
    temp = 0
    arrN = []

    while i < len(arr) - 1:
        arrN = arr[i+1:]
        minN =  min( arrN)
       
        if arr[i] > minN :
            temp = arr[i]
            print(temp)
            arr[i] = minN
            # print(arr[i])
            arr[arr.index(minN)] = temp
            print(arr[arr.index(minN)])
            count += 1
            print(arr[i])
        i+= 1
    return count

    # pseudocode
# ----------
# 1. create a function that takes an array of numbers 
# 2. create a variable minN, count and temp 
# 3. loop through the array
# 4. get the minN of the rem of the array
# 5. check to see if the minN is smaller than f
# 6. if it is wap the values and increment count by 1
# 7. else do nothing
# 8, return count