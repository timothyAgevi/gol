
  def __init__(self):
    pass
  def reverseInArray(self,arr):
    x = 0 
    y = len(arr) - 1
    temp = 0
    while y > x :
      temp = arr[x]
      arr[x] = arr[y]
      arr[y] = temp
      x += 1
      y -= 1
    return arr

    #  pseudocode
# 1. create a fxn 
# 2. create three variables, x to point at 0, temp,  and y to point at the end of the array
# 3. loop through the array until y = or less than x
# 4. each time you loop, increase x by 1 and reduce y by 1
# 5. also change values for array
# 6. return array
#  https://github.com/timothyAgevi/gol/blob/master/reverseArray
# github links

