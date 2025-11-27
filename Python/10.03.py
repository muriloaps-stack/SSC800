import numpy as np

n = int(input())

A = map(int, input().split())
B = map(int, input().split())

a = np.array(list(A))
b = np.array(list(B))   

veta = np.dot(a, b)

print(veta)