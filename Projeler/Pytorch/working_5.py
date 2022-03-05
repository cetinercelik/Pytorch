import numpy as np
import torch

c=torch.tensor([4,5,6])
a=torch.tensor([[1,2,3],[4,5,6]])
b=torch.tensor([[4,5],[5,6],[8,9]])

print("---- a matrisi ----")
print(a)
print("---------b matrisi-----")
print(b)
print("-------c matrisi-------")
print(c)
print("------------------------")

print("----- Üs alma işlemi-----")
torch_pow=c.pow(2)
print(torch_pow)
print("--------------------------")

print("------- Bir sayı ile toplama veya çarpma ----")
tr_sum=c+22
tr_mul=c*5
print(tr_sum)
print(tr_mul)
print("-------------------------------")

print("----İki matrsin çarpımı----")
torch_mm=torch.mm(a,b)#satır ve sutunlarının eşit olması gerekiyor.
print(torch_mm)
print("-------------------------")
print(a@b)#iki matrisin çarpımı

