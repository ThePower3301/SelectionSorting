import sys 

A = [ 95, 15, 50, 56, 87, 14, 41, 88, 84, 64, 95, 48, 75, 
      68, 71, 55, 83, 72, 84, 76, 43, 71, 71, 83, 19, 67, 
      72, 15, 63, 42, 17, 67, 52, 68, 39, 26, 30, 79, 49,
      12, 68, 17, 38, 80, 17, 25, 33, 99, 99, 47, 32, 24, 
      64, 72, 86, 39, 48, 82, 28, 68, 63, 65, 22, 58, 70, 
      24, 24, 54, 70, 82, 45, 31, 99, 15, 29, 32, 71, 37, 
      14, 60, 15, 66, 10, 50, 42, 73, 79, 52, 65]


for i in range(len(A)): 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
   
    A[i], A[min_idx] = A[min_idx], A[i] 

print ("Sorted array") 
for i in range(len(A)): 
    print("%d" %A[i]),  
