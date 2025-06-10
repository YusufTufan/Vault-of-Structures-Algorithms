class Node:
    def __init__(self, data):
        self.data = data  # Düğümün (node) içine veri atılır
        self.next = None  # Düğümün sonraki düğüme bağlantısı başlangıçta yok

class LinkedList:
    def __init__(self):
        self.head = None  # Bağlı listenin ilk elemanı (başlangıç noktası)

    def insert(self, data):
        """Listenin sonuna yeni bir düğüm ekler"""
        new_node = Node(data)  # Yeni düğüm oluştur
        if not self.head:  # Eğer liste boşsa, yeni düğüm baş olur
            self.head = new_node
        else:
            temp = self.head
            while temp.next:  # Listenin sonuna kadar ilerle
                temp = temp.next
            temp.next = new_node  # Son düğümün "next" bağlantısını yeni düğüme bağla

    def delete(self, key):
        """Belirtilen değere sahip düğümü siler"""
        temp = self.head

        # Eğer silinecek düğüm baştaysa, başı güncelle
        if temp and temp.data == key:
            self.head = temp.next  # Başı bir sonraki düğüme kaydır
            temp = None  # Belleği temizle
            return

        # Listeyi tarayarak uygun düğümü bul
        prev = None
        while temp and temp.data != key:
            prev = temp  # Bir önceki düğümü sakla
            temp = temp.next  # İleri git

        # Eğer anahtar bulunamadıysa çık
        if temp is None:
            return

        prev.next = temp.next  # Önceki düğümün bağlantısını silinen düğümün sonrasına bağla
        temp = None  # Belleği temizle

    def display(self):
        """Listeyi ekrana yazdırır"""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")  # Veriyi yazdır ve bağlantıyı göster
            temp = temp.next
        print("None")  # Listenin sonunu belirt

# Örnek kullanım
llist = LinkedList()
llist.insert(10)  # 10 eklenir
llist.insert(20)  # 20 eklenir
llist.insert(30)  # 30 eklenir
llist.display()  # 10 -> 20 -> 30 -> None

llist.delete(20)  # 20 silinir
llist.display()  # 10 -> 30 -> None