import numpy as np #Numpy kütüphanesini dahil ediyoruz

#Tek boyutlu dizi
oneArr=[1,2,3,4,5]# Diziyi tanımlıyoruz()
n_oneArr=np.array(oneArr)#Diziyi ekrana yazdırıyoruz

print("Tek boyutlu dizi")
print("--------------------------------")
print(oneArr)# Liste olarak alıyor
print("--------------------------------")
print(n_oneArr)# Numpy dizisi türünde alıyor
print("--------------------------------")

# Çok boyutlu dizi
manyArr=[[1,2,3],[4,5,6],[7,8,9]]#Düz iç içe bir liste halinde sıralanır
n_manyArr=np.array(manyArr)#Matris halinde sıralanır

print("Çok boyutlu dizi")
print("--------------------------------")
print(manyArr)
print("--------------------------------")
print(n_manyArr)
print("--------------------------------")
print(n_manyArr.shape)#Boyutunu verir
print("--------------------------------")
print(n_manyArr.size)#Elaman sayısımı verir(Numpy kütüphanesinden bunlara benzer bir çok metod bulunmaktadır)
print("--------------------------------")

data=np.arange(1,10)#İlk elamanı alır son elamanı almaz
dataShape=data.shape# Elaman sayısını verir
dataReShape=data.reshape(3,3)#  (5,5) lik matrise çevirir
dataReShape1=data.reshape(3,-1)#  Matrisin kaça kaçlık olacağına hesaplayamadığımza bu komutu kullnırız

print("Arange----")
print("--------------------------------")
print(data)
print("Shape")
print("--------------------------------")
print(dataShape)
print("--------------------------------")
print("Reshape")
print("--------------------------------")
print(dataReShape)

data1=np.arange(1,10,2)#İkili artırarak diziyi alır
print("Arange iki işlem----")
print("--------------------------------")
print(data1)

oneZeros=np.zeros(5)#beştane sıfırdan oluşan (1,5) lik bir matris oluşturur (np.one()) aynı şekilde matrisi 1lerden oluşturu
manyOne=np.ones((4,10))/4 #(4,10) luk birden oluşan bir matris oluşturup 4 böler veya dört işlem uygulayabilirsiniz

print("One zero")
print("--------------------------------")
print(oneZeros)
print("Many One")
print("--------------------------------")
print(manyOne)

space=np.linspace(1,10,3)# 1 ile 10 arsaında tam veya virgülü olacak şekide 3 tane sayı alır

print("Linspace")
print("--------------------------------")
print(space)

eye=np.eye(5) # 5*5 lik köşegeni bir olan bir kare matris alır

print("Eye")
print("--------------------------------")
print(eye)

# randSeed=np.random.seed(60) # ==>>Bu komutu çalıştıdığınız anda süekli aynı random sayıları yazdıracaktır onun için kapattım
rand=np.random.rand(3)# 3 tane random sayı oluşturur sayıları istediğiniz gibi değiştirebilisiniz
randNorm=np.random.normal(2,2,6)#Baştaki sayı ortalama ikinci sayı standart sapma üçüncü sayı ise boyutu
randInt=np.random.randint(1,50,10)# 1 den 50 kadar 10 tane integer sayı oluşturur(yukarıdaki ile karıştırmayın)

print("Random ----")
print("--------------------------------")
print(rand)
print("Random Normal")
print("--------------------------------")
print(randNorm)
print("Random Integer")
print("--------------------------------")
print(randInt)

dataMatrix=np.random.rand(4,3,2) # 4 tane (3,2) boyutunda matrisler oluşturur

print("------Data Matrix------")
print("--------------------------------")
print(dataMatrix)

dataAnaliz=np.random.randn(5)

print("--Data----")
print(dataAnaliz)
print("-----Max----")
print(dataAnaliz.max())
print(dataAnaliz.argmax())
print("-----Min-----")
print(dataAnaliz.min())
print("--------------------------------")
print(dataAnaliz.argmin())
print("--------------------------------")

print("İndislere ulaşma yöntemi")
print("--------------------------------")
dataSet=np.arange(1,30)

print(dataSet[5])#5.ci indise ulaşır
print("--------------------------------")
print(dataSet[1:10])# 1 ile 10 arasındaki verileri alır
print("--------------------------------")
print(dataSet[:10])# 1 ile 10 arasında ki verileri alır
print("--------------------------------")

newData=dataSet[:10]#dataSet veris setinin ilk 10 indisini alıyoruz
newData[:]=500#Aldığımız indislere 500 değerini atıyoruz

newData=newData/100

print("new Data veri seti")
print("--------------------------------")
print(newData)
print("dataSet veri seti")
print("--------------------------------")
print(dataSet)


dataSet1=np.arange(30)
dataSetCopy=dataSet1.copy()

print("Kopyalanan veri ")
print("--------------------------------")
print(dataSetCopy)

dataSetCopy=dataSetCopy[:10]#Bu yaptığımız işelemler yukarıdakinden farkı asıl verini üzerinden yapılan işlemlerin asıl veri bütünlüğünü bozmamasıdır
dataSetCopy[:]=100
print("Kopyalanıp değiştirilen veri")
print("--------------------------------")
print(dataSetCopy)
print("Asıl veri")
print("--------------------------------")
print(dataSet)

print("Matris işlemleri")
print("--------------------------------")
arr_2d=np.array([[5,6,7],[2,8,9],[1,6,9]])

print(arr_2d)
print("--------------------------------")
print(arr_2d[1])#ilk üçlü elamanı alır
print("--------------------------------")
print(arr_2d[1,1])#ilk üçlü elaman içinde ilk indisi alır
print("--------------------------------")
print(arr_2d[:2])#ilk iki satırı alır
print("--------------------------------")
print(arr_2d[:2,1:])#ilk iki satır ve ilk iki sutunu alır
print("--------------------------------")
print(arr_2d[:2,2])#ilk iki satırın son iki sutununu alır

print("Koşul işlemleri---------")
dataArange=np.arange(1,11)

print(dataArange)
print("--------------------------------")
condition=dataArange>5
print(condition)#Bu şekide ki yazımda sadece True veya False döner
print("--------------------------------")
print(dataArange[condition])# Burada ise şartı sağlayan sayıları döndürür

print("Matamatiksel işlemler-------------")
matArange=np.arange(0,10)


print(matArange+matArange)#Bütn indisleri kendi değerleri ile toplar
print("--------------------------------")
print(np.sqrt(matArange))#Her bir indisin karekökünü alır
print("--------------------------------")
#print(np.log(matArange))#Her bir elamanın idisinin loaritmasını alır
print("--------------------------------")
print(matArange.sum())#Bütün elemanların toplamını alır
print("--------------------------------")

print("Dizilerde Matamatiksel işlemeler--------------")
matArray=np.array([[5,6,7],[2,8,9],[1,6,9]])

print("---------------Boyut-----------------")
print(matArray.shape)#Boyut
print("---------------Toplam-----------------")
print(matArray.sum())#Toplam
print("----------------sutunlardaki Toplam----------------")
print(matArray.sum(axis=0))#Bütün sutunlardaki saayıların sütün sütun ayrı toplamı
print(matArray.mean(axis=0))#Bütün sutunların ortalamasını alır
print("--------------satırlardaki Toplam------------------")
print(matArray.sum(axis=1))#Bütün satırlardaki sayıların satı satır toplamı
print(matArray.mean(axis=1))#Satırların ortalamasını alır