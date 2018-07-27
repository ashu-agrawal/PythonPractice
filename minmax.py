
arr=[]
i = int(input())
for j in range(0,i,1):
    arr.append(int(input()))
def miniMaxSum(arr):
    for b in arr:
        for j in range(0,len(arr)-1,1):
            if arr[j]<arr[j+1]:
                a=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=a
            else:
                continue
    print(arr)
    suma=0
    sumb=0
    for i in range(0,4,1):
        suma=suma+arr[i]
    for i in range(-1,-5,-1):
        sumb=sumb+arr[i]
    return suma,sumb

suma,sumb=miniMaxSum(arr)
print(suma,sumb)

"""
import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    for b in arr:
        for j in range(0,len(arr)-1,1):
            if arr[j]<arr[j+1]:
                a=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=a
            else:
                continue
    suma=0
    sumb=0
    for i in range(0,4,1):
        suma=suma+arr[i]
    for i in range(-1,-5,-1):
        sumb=sumb+arr[i]
    return suma,sumb

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    suma,sumb = miniMaxSum(arr)
    print(suma,sumb)
"""
