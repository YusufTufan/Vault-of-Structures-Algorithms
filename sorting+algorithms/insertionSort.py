mylist = [64, 34, 25, 12, 22, 11, 90, 5]  # Sıralanacak liste

n = len(mylist)  # Listenin uzunluğunu alıyoruz

# İlk Insertion Sort uygulaması
for i in range(1, n):  # 1'den başlayarak her elemanı sıralı hale getirmeye çalışıyoruz
    insert_index = i  # Elemanın yerleştirileceği indeks
    current_value = mylist.pop(i)  # Elemanı listeden çıkarıyoruz (Bu hata yaratabilir!)
    
    # Elemanın doğru konumunu bulmak için geriye doğru kontrol ediyoruz
    for j in range(i-1, -1, -1):  
        if mylist[j] > current_value:  # Eğer önceki eleman daha büyükse
            insert_index = j  # Yerleştirme indeksini güncelliyoruz
    
    mylist.insert(insert_index, current_value)  # Elemanı doğru yere ekliyoruz

print(mylist)  # Sıralanmış listeyi yazdırıyoruz

# ------------------------------------------------------------------------------

# İkinci Insertion Sort uygulaması
for i in range(1, n):  # 1'den başlayarak her elemanı sıralı hale getirmeye çalışıyoruz
    insert_index = i  # Elemanın yerleştirileceği indeks
    current_value = mylist[i]  # Elemanı saklıyoruz (pop kullanılmıyor, bu daha doğru)

    # Elemanın doğru konumunu bulmak için geriye doğru kontrol ediyoruz
    for j in range(i-1, -1, -1):  
        if mylist[j] > current_value:  # Eğer önceki eleman daha büyükse
            mylist[j+1] = mylist[j]  # Büyük olanı sağa kaydırıyoruz
            insert_index = j  # Yerleştirme indeksini güncelliyoruz
        else:
            break  # Daha küçük bir eleman bulunduğunda duruyoruz

    mylist[insert_index] = current_value  # Elemanı doğru yere yerleştiriyoruz

print(mylist)  # Sıralanmış listeyi yazdırıyoruz
