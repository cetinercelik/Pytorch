import numpy as np
import pandas as pd

print("------------Pandas Serileri ---------")
dataArr=[55,66,88,99,22]
tag=['a','b','c','d','e']


data=pd.Series(dataArr)#dataArr içindeki her bir veriye indis numarası vererk yazar
print("---------data------------")
print(data)

data=pd.Series(data=dataArr,index=tag)# datayı verdiğimiz indexlerlerle sıralar
print("------data---------------")
print(data)


data2=pd.Series(data=[11.3,'a',True,'atttt','56'],index=tag)#Datayı farklı türlerde verebiliriz
print("---------data2------------")
print(data2)


dataSet={'a':15,'b':87,'c':23,'e':45}#Veri seti ve index tanımlama başka bir yolu
dt=pd.Series(dataSet)
print("---------dataSet------------")
print(dt)

dataSet2={'a':16,'b':87,'c':23,'f':45}
dt2=pd.Series(dataSet2)
print("-----------dataSet2-----------")
print(dt2)

count=dt+dt2#indis her ikisinde varsa verilerin toplamını yoksa NOn değini atar
print("---------Toplam-----------")
print(count)

print("----------Data Frames---------")
from numpy.random import randn #Yukarıdaki değerleri etkilemesin diye burada oluşturdum
np.random.seed(54)


rand_matrix=randn(5,4)
print("---Random Matrisi-------")
print(rand_matrix)

dataMatrix=pd.DataFrame(rand_matrix)
print("---Data Frame ile Random Matrisi---")
print(dataMatrix)

dataMatrix=pd.DataFrame(data=rand_matrix,columns='veri1 veri2 veri3 veri4'.split(),index='a b c d e'.split())#Data ve kolon adlarnı veya index bilgilerini dışardan verebiliriz
print("---Data Frame ile Random Matrisi---")
print(dataMatrix)
print('---sutun değerlerini alma---')
list=['veri1','veri2']
print(dataMatrix[list])

print('---Data Frames ile Drop,loc,iloc İşlemleri---')
dataMatrix['data']=dataMatrix.veri2+dataMatrix.veri4 # Matrise yeni bir sutun ekleme
print('-----Matrise yeni sutun ekleme-------')
print(dataMatrix)
print('----Matristen sutun silme')
print(dataMatrix.drop('veri1',axis=1,inplace=True))#axis=1 olamsı sutun olduğunu belirtmek için - inplace=True olduğunda gerçek veri kalıcı olarak etkileniyor
print('---Matristen satır silme')
print(dataMatrix.drop('a'))
print('Matriste Satır bilgisine erişme')
print(dataMatrix.loc[['a','b']])
print('--Satır ve sutunların belirli değerlerini alma')
print(dataMatrix.loc[['a','b']][['veri4','data']])
print(dataMatrix.loc[['a','b'],['veri4','data']])#Aynı işlemi yapar
print('---iloc işlemleri---')
print(dataMatrix.iloc[[0,1],[2,3]])#loc ile benzer işlem yapar fakat iloc numerik index kullanır

print('--- Data Frame üzerinde koşul işlemleri----')
condMatrix=randn(5,4)
dataCondition=pd.DataFrame(data=condMatrix,columns='veri1 veri2 veri3 veri4'.split(),index='a b c d e'.split())

print('-----Başlangıç Matrisi----')
print((dataCondition))
print('--------------------------')
print(dataCondition>0)#Sıfırdan büyük değerleri True küçükleri ise False döndürür
print(dataMatrix[dataMatrix>0])#Sıfırdan büyük kendi değerlerini küçükleri ise NaN değerini atar
print('--Sutun ve Satırlara göre işlem')
print(dataCondition['veri1']>0)#Sutuna göre
print(dataCondition[dataCondition['veri1']>0]['veri4'])#İlk sutunda True olan iki satırın 4. sutundaki değerlerini alır

print('----Çoklu Şart-----')
condition1=dataCondition['veri1']<0
condition2=dataCondition['veri4']>1

print('---And Koşulu--')
andCondition1=dataCondition[(condition1) & (condition2)]
print(andCondition1)
print('---------------------------------------------')
andCondition2=dataCondition[(condition1) & (condition2)][['veri1','veri3']]#Ayrıca belirli kolonları çağırabiliyoruz
print(andCondition2)

print('----Or Koşulu----')
orCondition1=dataCondition[(condition1) | (condition2)]
print(orCondition1)
print('---------------------------------------------')
orCondition2=dataCondition[(condition1) | (condition2)][['veri1','veri3']]#Ayrıca belirli kolonları çağırabiliyoruz
print(orCondition2)


print('----------Data Frames Diğer Özellikler-----')
dtMatrix=randn(5,4)

print('-----Data Frame Matrix-----')
dataFrame=pd.DataFrame(data=rand_matrix,columns='bilgi_a bilgi_b bilgi_c bilgi_d'.split(),index='a b c d e'.split())
print(dataFrame)
print('---------------------------------------------')
print(dataFrame.reset_index(inplace=True))#İndex kolonunu ekler
print('---------------------------------------------')
print(dataFrame.columns)#Kolonları verir
print('---------------------------------------------')
dataFrame['index']='aa ab ac ad ad'.split()#index adında yeni bir kolon ekler
dataFrame.set_index('index',inplace=True)
print(dataFrame)
print('---------------------------------------------')
print(dataFrame.info())#Veri hakkında bilgi verir
print('---------------------------------------------')
print(dataFrame.describe())#istatiksel değerler
print('---------------------------------------------')
print(dataFrame.dtypes)
print('---------------------------------------------')
a=dataFrame['bilgi_c']>0
print(a.value_counts())#Her değerden kaç tane olduğunu gösterir

print('----Read_csv ve to_csv Metodları-----')
data_csv=pd.read_csv('C:\modProcess\kutu.csv')#Dosyadan veri okuma
print(data_csv)
print('-----------------------Baş----------------------')
print(data_csv.head(8))#Baştan Sekizinci sıradaki veriye kadar okur
print('-------------------------Son--------------------')
print(data_csv.tail(5))#Sondan Beşinci sıradaki veriye kadar okur
print('---------------------------------------------')

print('----------GroupBy Kavramı--------------------')
GroupBy={'firmalar':['TT','TRC','TRC','VDFN','VDFN','TT','TT','TT','TRC'],
          'ürünler':['IPHONE','SMSG','SMSG','IPHONE','SMSG','SMSG','IPHONE','SMSG','SMSG'],
          'satislar':[500,200,600,800,900,700,600,900,900]}

dataGroupBy = pd.DataFrame(GroupBy)
print(dataGroupBy)
print('----------------------Sum-----------------------')
print(dataGroupBy.groupby('firmalar').sum())#Burda Satışlar stunu numeric olduğundan direkt firmaların toplam satışlarını alır
print('-----------------------Count firmalar----------------------')
print(dataGroupBy.groupby('firmalar').count())#Satış sayısı
print('-----------------------Count ürünler----------------------')
print(dataGroupBy.groupby('ürünler').count())#Satış sayısı
print('-----------------------Descripe ürünler----------------------')
print(dataGroupBy.groupby('ürünler').describe().T)#Analiz


print('------------Önemli Metodlar----------')
dataMethod=pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','jkl']})
print(dataMethod)
print('---------------------unique----------------------------')
print(dataMethod['col2'].unique())
print('---------------------unique length----------------------------')
print(len(dataMethod['col2'].unique()))

print('------------Çarpma Metodu------------')
def carp(sayi):
    return sayi*2;

dataMethod['yeni']=dataMethod['col1'].apply(carp)#Değerleri 2 ile çarpıp yeni bir sutun oluşturur
print(dataMethod)

print('-------Sutunu silme-----')
del dataMethod['yeni']
print(dataMethod)


#CSV den veri okuma
data=pd.read_csv('C:\modProcess\kutu.csv')#Csv Dosyasındaki verileri okuma
print('----------Read csv-------------')
print(data)
data.to_csv('example.csv',index=False)#example adında yeni bir dosyaya kayıt alma