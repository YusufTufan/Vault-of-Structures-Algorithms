def partition(array, low, high):
    pivot = array[high]  # Listenin son öğesi pivot olarak seçilir.
    i = low - 1  # Daha küçük öğeleri takip etmek için indeks.

    for j in range(low, high):  # Listenin low'dan high'a kadar olan kısmını döngüye al.
        if array[j] <= pivot:  # Eğer öğe pivot'tan küçük veya eşitse, yer değiştirme yapılır.
            i += 1
            array[i], array[j] = array[j], array[i]  # Küçük öğeler sola kaydırılır.

    array[i + 1], array[high] = array[high], array[i + 1]  # Pivot öğesi doğru yerine yerleştirilir.
    return i + 1  # Pivot'un yeni konumu döndürülür.


def quicksort(array, low=0, high=None):
    if high is None:  
        high = len(array) - 1  # Eğer high belirtilmemişse, dizinin son indeksi atanır.

    if low < high:  # Dizi bölünebiliyorsa işlemi başlat.
        pivot_index = partition(array, low, high)  # Pivot belirlenir ve konumu alınır.
        quicksort(array, low, pivot_index - 1)  # Pivot'un sol tarafı sıralanır.
        quicksort(array, pivot_index + 1, high)  # Pivot'un sağ tarafı sıralanır.


# Örnek kullanım
mylist = [64, 34, 25, 5, 22, 11, 90, 12]  
quicksort(mylist)  # Listeyi hızlı sıralama algoritmasıyla sıralar.
print(mylist)  # Sıralanmış listeyi ekrana yazdırır: [5, 11, 12, 22, 25, 34, 64, 90]
