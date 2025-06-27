def binarySearch(arr, targetVal):
    # Başlangıç (sol) ve bitiş (sağ) indeksleri tanımlanır
    left = 0
    right = len(arr) - 1

    # Sol indeks sağdan küçük veya eşit olduğu sürece döngü devam eder
    while left <= right:
        # Orta indeks hesaplanır
        mid = (left + right) // 2

        # Eğer orta eleman hedef değerse, index döndürülür
        if arr[mid] == targetVal:
            return mid

        # Eğer orta eleman hedef değerden küçükse, arama sağ tarafa kaydırılır
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            # Aksi halde arama sol tarafa kaydırılır
            right = mid - 1

    # Değer bulunamazsa -1 döndürülür
    return -1


# Sıralı bir liste
mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 11  # Aranacak değer

# Binary search fonksiyonu çalıştırılır
result = binarySearch(mylist, x)

# Sonuç ekrana yazdırılır
if result != -1:
    print("Found at index", result)
else:
    print("Not found")
