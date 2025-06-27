## 🔍 Linear Search (Doğrusal Arama)

**Ne işe yarar?**  
Küçük veya sıralanmamış listelerde aranan değeri bulmak için kullanılır.

### ⚙️ Nasıl çalışır?
1. Liste baştan sona gezilir.
2. Her eleman, aranan değer ile karşılaştırılır.
3. Eşleşme varsa indeks döndürülür.
4. Bulunamazsa `-1` döner.

### ⏱️ Zaman Karmaşıklığı
- En iyi durum: **O(1)** — Aranan değer ilk sıradaysa  
- Ortalama ve en kötü durum: **O(n)** — Aranan değer sonda ya da yoksa  
- Alan karmaşıklığı: **O(1)**

### 🔧 Günlük Kullanım
- Küçük listelerde hızlı kontrol
- Değerin olup olmadığını kontrol etme
- İndeks bilgisine ihtiyaç duyulduğunda tercih edilir

---

## 🔎 Binary Search (İkili Arama)

**Ne işe yarar?**  
Sıralı listelerde yüksek verimle arama yapmak için kullanılır.

### ⚙️ Nasıl çalışır?
1. Listenin ortası hesaplanır.
2. Aranan değer ortadaki elemanla karşılaştırılır.
3. Daha büyükse sağ yarıya, küçükse sol yarıya geçilir.
4. Değer bulunana kadar işlem tekrarlanır.
5. Bulunamazsa `-1` döner.

### ⏱️ Zaman Karmaşıklığı
- En iyi durum: **O(1)** — Aranan değer tam ortadaysa  
- Ortalama ve en kötü durum: **O(log n)**  
- Alan karmaşıklığı: **O(1)**

### 🔧 Günlük Kullanım
- Sıralı büyük veri setlerinde hızlı arama
- Veritabanlarında, arama motorlarında, sözlük uygulamalarında
- Performansın kritik olduğu uygulamalarda tercih edilir

---

## 📋 Özet Tablo

| Algoritma       | Kullanım Durumu       | En İyi | Ortalama/Kötü | Alan |
|-----------------|------------------------|--------|----------------|------|
| Linear Search   | Sıralı olmayan listeler | O(1)   | O(n)           | O(1) |
| Binary Search   | Sıralı listeler         | O(1)   | O(log n)       | O(1) |

---

## 🧠 Kullanım Örnekleri

```python
# Linear Search
linearSearch([3, 7, 2, 9], 9)  # çıktı: 3

# Binary Search
binarySearch([1, 3, 5, 7, 9], 5)  # çıktı: 2
