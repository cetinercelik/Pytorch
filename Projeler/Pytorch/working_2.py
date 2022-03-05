import  torch

print("Torch random Matrix")
torch_rand=torch.rand(4,4)
print(torch_rand)
print("-------------------------------------")

print("Integer Torch matris")
torch_int=torch.randint(low=2,high=11,size=(5,5))#2-10 arasında 5x5 'lik random matris(int tipinde)
print(torch_int)
print("----------------------------------------")

print("")
x=torch.zeros(2,5)
print(x)
print("------------------------------------------")
torch_like=torch.rand_like(x)#x 'in boyutunu alıp (0,1)arasında bir random sayı alır
print(torch_like)
print("-------------------------------------------")
torch_like1=torch.randn_like(x)#x 'in özelliklerini alan standart sapması 1 ortalaması 0 olan random bir matris
print(torch_like1)
print("--------------------------------------------")

print("Seed komutu ")
torch_seed=torch.manual_seed(45)#Bu komut ile sürekli aynı random değerleri alır
print(torch_seed)
torch_radint=torch.randint(low=2,high=11,size=(5,5))
print(torch_radint)
print("---------------------------------------------")