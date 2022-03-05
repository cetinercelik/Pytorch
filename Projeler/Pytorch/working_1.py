import numpy as np
import torch

arr=np.array([1,3,5,7,9])
new_arr=torch.tensor(arr)

print("Tensor dizisi")
print(new_arr)
print("--------------------------")

print("Büyük harf kullanarak Tensor yazmak")
new_arr2=torch.Tensor(arr)#Değerleri Floata çevirir(FloatTensor diyerej de aynı işlemi yapabiliriz)
print(new_arr2)
print(new_arr2.dtype)
print("---------------------------")

print("--placeholder(bellek tutucular)")
torch_empty=torch.empty(2,3)#O değerine yakın 2x3 lük matris oluşturur
print(torch_empty)
print("----------------------------------")
torch_zeros=torch.zeros(3,3,dtype=torch.int32)# Data type'ını verebilirsiniz
print(torch_zeros)
print("-----------------------------------")
torch_ones=torch.ones(3,2)
print(torch_ones)
print("-----------------------------------")

print("Arange komutu")
torch_arange=torch.arange(0,18,2)#0 - 18 'e 2 ' li arttır
print(torch_arange)
print("----------------------------")
print(torch_arange.reshape(3,3))#3x3 'lük bir tensor oluşturur
print("------------------------------")

print("Linspace komutu")
torch_lines=torch.linspace(1,10,12)#1 - 10 arasında 12 tane sayı oluşturu
print(torch_lines)
print("--------------------------------")
print(torch_lines.reshape(4,3))#4x3 lük matris oluşturur
print("--------------------------------")

print("Type Dönüşümü ")
my_tensor=torch.tensor([5,6,8,4,6])
data_type_reverse=my_tensor.type(torch.float16)
print(data_type_reverse)
print("-----------------------------")