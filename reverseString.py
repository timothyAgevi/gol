 def reverseSentenceInPlace(self, A):
    f=0
    l= len(A) - 1
    temp= ''
    # for i in range(len(A)-1):
    while f < l :
      if A[f + 1].isspace() and A[l - 1].isspace():
        temp= A[0:f + 1]
        A[0:len(A)- l]  = A[l: len(A)]
        A[l:len(A)] = temp
        break
      else:
        f += 1
        l -= 1
    return A

    # https://github.com/timothyAgevi/gol/blob/master/reverseString.py
    # question
    # Write a function reverseArray(A) that takes in an array A and reverses it, 
    # without using another array or collection data structure; in-place.