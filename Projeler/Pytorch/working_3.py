import numpy as np
import torch

print("torch arange")
x=torch.arange(6).reshape(3,2)#0-5 kadar 3x2 matris
print(x)
print("--------------------------")

print("indislere ulaşma")
print(x[1,1])#Birinci satır birinci sutundaki elemana ulaşır
print(x[:,1:])#ikinci sütunun tamamını alır
print("----------------------------")

print("View Metodu")
a=torch.arange(10)
print(a)
print("---------------------------")
b=a.view(5,2)# a 'dan aldığı değerleri 5x2 lik matrise ayırır
print(b)
print("----------------------------")

print(a.view(5,-1))#5 tane satır geriye klan sutunları otomatik tamamla
print(2,-1)#2 satır geriye kalan sutunları otomatik tamamla
