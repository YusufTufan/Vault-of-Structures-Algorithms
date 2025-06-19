
# 📊 Sıralama Algoritmaları Açıklamalı Rehber

Bu klasör, bilgisayar bilimlerinde temel kabul edilen beş klasik sıralama algoritmasının Python ile yazılmış uygulamalarını içerir. Her biri algoritma mantığı, verimlilik ve gerçek hayatta kullanım alanları açısından açıklanmıştır.

---

## 🔁 1. Bubble Sort (Kabarcık Sıralama)

**Mantık:**  
- Liste boyunca tekrar tekrar dolaşır  
- Yan yana olan elemanları karşılaştırır ve gerekirse yer değiştirir  
- Büyük elemanlar "yukarıya doğru kabarır"

**Zaman Karmaşıklığı:**  
- En kötü: O(n²)  
- En iyi (sıralı dizi): O(n)

**Kullanım Alanı:**  
- Eğitim amaçlı  
- Küçük veri kümeleri

**Günlük Hayat Örneği:**  
- Basit mobil oyun skorları sıralaması

---

## 📌 2. Selection Sort (Seçmeli Sıralama)

**Mantık:**  
- Her adımda kalan diziden en küçük elemanı bulur  
- Onu dizinin başındaki sırasız elemanla değiştirir

**Zaman Karmaşıklığı:**  
- Her zaman O(n²)

**Kullanım Alanı:**  
- Bellek yazma işlemleri maliyetli olan sistemlerde

**Günlük Hayat Örneği:**  
- Gömülü sistemlerde sıralama (az RAM ile)

---

## ✍️ 3. Insertion Sort (Eklemeli Sıralama)

**Mantık:**  
- Sıralı dizi parçasını oluşturur  
- Her yeni elemanı doğru pozisyona yerleştirir

**Zaman Karmaşıklığı:**  
- En kötü: O(n²)  
- En iyi (neredeyse sıralı): O(n)

**Kullanım Alanı:**  
- Küçük ya da neredeyse sıralı veri kümeleri

**Günlük Hayat Örneği:**  
- Eldeki iskambil kartlarını sıralamak

---

## 🔀 4. Merge Sort (Birleştirmeli Sıralama)

**Mantık:**  
- Diziyi sürekli ikiye böler  
- Her yarımı sıralar  
- Daha sonra bu yarımları birleştirir

**Zaman Karmaşıklığı:**  
- Her durumda O(n log n)

**Kullanım Alanı:**  
- Büyük veri kümelerinde  
- Stabil sıralama gereken durumlar

**Günlük Hayat Örneği:**  
- Sabit diskteki dosyaları sıralamak  
- Sunucu taraflı çoklu iş parçacıklı sıralamalar

---

## ⚡ 5. Quick Sort (Hızlı Sıralama)

**Mantık:**  
- "Pivot" adında bir referans eleman seçilir  
- Dizi pivot'a göre küçük ve büyük olarak ikiye bölünür  
- Alt diziler ayrı ayrı sıralanır

**Zaman Karmaşıklığı:**  
- Ortalama: O(n log n)  
- En kötü (kötü pivot): O(n²)

**Kullanım Alanı:**  
- Bellekte hızlı sıralama gereken yerler

**Günlük Hayat Örneği:**  
- Veri tabanlarında milyonlarca kaydın sıralanması

---

## 🧠 Özet Tablo

| Algoritma       | En İyi   | Ortalama | En Kötü  | Stabil | Kullanım Alanı                    |
|-----------------|----------|----------|----------|--------|-----------------------------------|
| Bubble Sort     | O(n)     | O(n²)    | O(n²)    | Evet   | Eğitim, küçük veri setleri        |
| Selection Sort  | O(n²)    | O(n²)    | O(n²)    | Hayır  | Donanımda az bellekle sıralama    |
| Insertion Sort  | O(n)     | O(n²)    | O(n²)    | Evet   | Küçük ve neredeyse sıralı veriler |
| Merge Sort      | O(n log n)| O(n log n)| O(n log n)| Evet | Büyük veriler, stabil sıralama    |
| Quick Sort      | O(n log n)| O(n log n)| O(n²)   | Hayır  | Bellek içi hızlı sıralamalar      |

---

## 👨‍💻 Geliştirici
**Yusuf Tufan**  
