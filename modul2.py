def donenVarliklar(a,b,c,d,e):
    donenVarliklar=a+b+c+d+e
    print(donenVarliklar)

def duranVarliklar(a,b,c):
    duranVarliklar=a+b+c
    print(duranVarliklar)

def kisaVadeliYabanciKaynak(a,b):
    kisaVadeliYabanciKaynak=a+b
    print(kisaVadeliYabanciKaynak)

def uzunVadeliYabanciKaynak(a,b):
    uzunVadeliYabanciKaynak=a+b
    print(uzunVadeliYabanciKaynak)

def ozKaynaklar(a):
    ozKaynaklar=a
    print(ozKaynaklar)



print("BİLANÇONUN AKTİFİ")
from soru2cevap import donenVarliklar
print("1.Dönen Varlıkları hesaplamak için;")
x=int(input("100 Kasa hesabını giriniz:"))
y=int(input("101 Alınan çekler hesabını giriniz:"))
z=int(input("102 Bankalar hesabını giriniz:"))
t=int(input("121 Alacak senetleri hesabını giriniz:"))
k=int(input("153 Ticari mallar hesabını giriniz:"))
donenVarliklar(x,y,z,t,k)

from soru2cevap import duranVarliklar
print("2.Duran Varlıkları hesaplamak için;")
g=int(input("252 Binalar hesabını giriniz:"))
l=int(input("254 Taşıtlar hesabını giriniz:"))
m=int(input("255 Demirbaşlar hesabını giriniz:"))
duranVarliklar(g,l,m)

print("BİLANÇONUN PASİFİ")
from soru2cevap import kisaVadeliYabanciKaynak
print("3.Kısa Vadeli Yabancı Kaynakları hesaplamak için;")
n=int(input("300 Banka kredileri hesabını giriniz:"))
j=int(input("320 Satıcılar hesabını giriniz:"))
kisaVadeliYabanciKaynak(n,j)

from soru2cevap import uzunVadeliYabanciKaynak
print("4.Uzun Vadeli Yabancı Kaynakları hesaplamak için;")
h=int(input("400 Banka kredileri hesabını giriniz:"))
s=int(input("421 Borç senetleri hesabını giriniz:"))
uzunVadeliYabanciKaynak(h,s)

from soru2cevap import ozKaynaklar
print("5.Öz Kaynakları hesaplamak için;")
v=int(input("500 Sermaye hesabını giriniz:"))
ozKaynaklar(v)

if ((donenVarliklar and duranVarliklar)==(kisaVadeliYabanciKaynak and uzunVadeliYabanciKaynak and ozKaynaklar)):
    print("Kapanış bilançosu doğru hesaplanmıştır.")
else:
    print("Kapanış bilançosu yanlış hesaplanmıştır.")
