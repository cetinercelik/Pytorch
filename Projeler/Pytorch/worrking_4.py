import numpy as np
import  torch

print("Toplama işlemelri")
a=torch.tensor([1,2,3])
b=torch.tensor([4,5,6])
print("---------------------------")
print(a)
print("----------------------------")
print(b)
print("----------------------------")
print(a+b)
print("----------------------------")

print("----Add-----")
torch_add=torch.add(a,b)#Toplam
print(torch_add)
print("------------------------")

print("------Çarpma işlemi (mul)----------")
torch_mul=torch.mul(a,b)
print(torch_mul)
print("-------------------------")

print("----Bölme işlemi (div)")
torch_div=torch.div(a,b)
print(torch_div)
print("----------------------------")


print("--------Ek bilgi--------")
a=a+b
x=a.mul_(b)#a ile b 'yi toplayıp b ile tekrardan çarpıyor(add_ ,mul_ komutları için geçerli)
print(x)
print("-------------------------")