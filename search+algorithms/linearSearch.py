def linearSearch(arr, targetVal):
    # Liste üzerinde döngü başlatılır
    for i in range(len(arr)):
        # Eğer eleman hedef değere eşitse, index döndürülür
        if arr[i] == targetVal:
            return i
    # Hiçbir eşleşme yoksa -1 döndürülür
    return -1


# Arama yapılacak örnek liste
mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]
x = 4  # Aranacak değer

# Linear search fonksiyonu çalıştırılır
result = linearSearch(mylist, x)

# Sonuç ekrana yazdırılır
if result != -1:
    print("Found at index", result)
else:
    print("Not found")
