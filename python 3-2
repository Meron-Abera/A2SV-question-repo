import sys

n = int(input())
a = [int(i) for i in input().strip().split(' ')]
codeSwaps = 0

for i in range(n):
    currentSwap = 0

    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            currentSwap += 1
            
    codeSwaps += currentSwap
            
    if currentSwap == 0:
        break
        
print("Array is sorted in " + str(codeSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))
