#Creating a queue using an Linked-List.
class Node:
  def __init__(self, data):
    self.data = data          # Düğümün değeri
    self.next = None          # Bir sonraki düğümü gösterir

class Queue:
  def __init__(self):        #constructor
    self.front = None        #Kuyruğun başını (ilk elemanı) tutar.
    self.rear = None         #Kuyruğun sonunu (son eklenen elemanı) tutar.
    self.length = 0          #Kuyruğun uzunluğunu tutar.

  def enqueue(self, element): #Kuyruğa yeni eleman ekler.
    new_node = Node(element)
    if self.rear is None:
      self.front = self.rear = new_node
      self.length += 1
      return
    self.rear.next = new_node
    self.rear = new_node
    self.length += 1

  def dequeue(self):         #Kuyruğun ilk Elemanını Çıkarır
    if self.isEmpty():
      return "Queue is empty"
    temp = self.front
    self.front = temp.next
    self.length -= 1
    if self.front is None:
      self.rear = None
    return temp.data

  def peek(self):           #Kuyruğun son Elemanını Gösterir (Silmeden)
    if self.isEmpty():
      return "Queue is empty"
    return self.front.data

  def isEmpty(self):        #Kuyruğun Boş Olup Olmadığını Kontrol Eder
    return self.length == 0

  def size(self):           #Kuyruktaki Eleman Sayısını Döndürür
    return self.length

  def printQueue(self):      #Kuyruğu Baştan Sona Yazdırır
    temp = self.front
    while temp:
      print(temp.data, end=" -> ")
      temp = temp.next
    print()