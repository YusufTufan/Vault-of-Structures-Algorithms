# Selection Sort Algoritması Örneği
# Listenin her elemanı için en küçük değeri bulup, başa taşıyoruz.

mylist = [64, 34, 25, 5, 22, 11, 90, 12]  # Sıralanacak liste
n = len(mylist)  # Listenin uzunluğu

for i in range(n-1):
  min_index = i  # O anki en küçük elemanın indeksini saklıyoruz
  for j in range(i+1, n):  # Listenin geri kalanını tarıyoruz
     if mylist[j] < mylist[min_index]:  # Daha küçük bir değer bulursak
       min_index = j  # Yeni en küçük elemanın indeksini güncelliyoruz
  
  # pop() ile küçük elemanı çıkartıp, doğru yere ekliyoruz
  min_value = mylist.pop(min_index)  
  mylist.insert(i, min_value)  

print(mylist)  # İlk sıralama işleminin sonucu

# ------------------------------------------------------------
# Daha verimli versiyon: Pop ve Insert yerine direk Swap yapıyoruz!
# Swap işlemi, diziyi gereksiz kaydırmadan elemanları değiştiriyor.

for i in range(n):
  min_index = i  # En küçük elemanın indeksini saklıyoruz
  for j in range(i+1, n):  # Geri kalan listeyi kontrol ediyoruz
     if mylist[j] < mylist[min_index]:  # Daha küçük değer bulursak güncelliyoruz
       min_index = j  

  # Elemanların yerlerini değiştirerek swap işlemini yapıyoruz
  mylist[i], mylist[min_index] = mylist[min_index], mylist[i]  

print(mylist)  # Son haliyle sıralanmış liste
