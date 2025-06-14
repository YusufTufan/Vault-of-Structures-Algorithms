# Merge Sort algoritması: Diziyi bölerek sıralar ve sonra birleştirir.
def mergeSort(arr):
    if len(arr) <= 1:  # Eğer dizinin uzunluğu 1 veya daha azsa, zaten sıralıdır.
        return arr

    mid = len(arr) // 2  # Diziyi ortadan ikiye böl
    leftHalf = arr[:mid]  # Sol yarıyı al
    rightHalf = arr[mid:]  # Sağ yarıyı al

    sortedLeft = mergeSort(leftHalf)  # Sol yarıyı sıralamak için tekrar çağır
    sortedRight = mergeSort(rightHalf)  # Sağ yarıyı sıralamak için tekrar çağır

    return merge(sortedLeft, sortedRight)  # İki sıralı yarıyı birleştir

# İki sıralı listeyi birleştiren fonksiyon
def merge(left, right):
    result = []  # Sonuç dizisi
    i = j = 0  # İki listeyi karşılaştırmak için indeksler

    while i < len(left) and j < len(right):  # Her iki listeyi karşılaştır
        if left[i] < right[j]:  # Küçük olanı ekle
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])  # Kalan elemanları ekle
    result.extend(right[j:])  # Kalan elemanları ekle

    return result  # Sıralı listeyi döndür

# Örnek bir listeyi sıralama
mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergeSort(mylist)
print("Sorted array:", mysortedlist)  # Sıralı diziyi ekrana yazdır

# ------------------------------------------------------------------------------

# Alternatif Merge Sort yöntemi: Döngü kullanarak sıralama yapar
def mergeSort(arr):
    step = 1  # Başlangıçta alt diziler 1 elemanlıdır
    length = len(arr)

    while step < length:  # Alt dizilerin boyutunu artırarak sıralama yap
        for i in range(0, length, 2 * step):  # İki alt diziyi birleştir
            left = arr[i:i + step]  # Sol alt dizi
            right = arr[i + step:i + 2 * step]  # Sağ alt dizi

            merged = merge(left, right)  # İki alt diziyi birleştir

            # Birleştirilmiş diziyi orijinal dizinin içine yerleştir
            for j, val in enumerate(merged):
                arr[i + j] = val

        step *= 2  # Alt dizi boyutunu iki katına çıkar

    return arr  # Sıralı diziyi döndür

# Örnek bir listeyi sıralama
mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergeSort(mylist)
print(mysortedlist)  # Sıralı diziyi ekrana yazdır