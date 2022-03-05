import torch
import numpy as np

print(torch.__version__)#version kontrolü

print("Numpy Array ")
arr=np.array([1,2,3,4,5])
print(arr)
print("--------------------------")

print("Data Type")
print(arr.dtype)
print("---------------------------")

print("Numpy arry'i torcha çevirmek ")
torch_from_np=torch.from_numpy(arr)#Tensor yapısına çevirir
torch_from_np2=torch.as_tensor(arr)#Yukardaki ile aynı şekil deçalışır
print(torch_from_np)
print(torch_from_np2)
print("-----------------------------")

print("Tensor yapsının değişikliliklerden etkilenmemesi")
arr[0]=99
print(arr)
print("-----------------------------")
print(torch_from_np)#Değişir
print(torch_from_np2)#Değişir
print("-----------------------------")
last_tensor=torch.tensor(arr)
print(last_tensor) #En üstte tanımlanan diziye bağlı kalır?
print("-----------------------------")

