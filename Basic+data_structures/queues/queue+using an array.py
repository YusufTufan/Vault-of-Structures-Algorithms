#Creating a queue using an array.
class Queue:
#constructor-------------------------------------------------------------------------------------------
  def __init__(self):
    self.queue = []
#Kuyruğa yeni bir eleman ekler.------------------------------------------------------------------------    
  def enqueue(self, element):
    self.queue.append(element)
#Kuyruğun en üstündeki elemanı çıkarır ve döndürür.Eğer kuyruk boşsa, hata mesajı döndürür.-------------
  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue.pop(0)
#Kuyruğun en üstündeki elemanı döndürür ama çıkartmaz.Eğer kuyruk boşsa, hata mesajı döndürür.----------
  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue[0]
#Kuyruğun boş olup olmadığını kontrol eder.Eğer eleman yoksa 'True', varsa 'False' döndürür.------------
  def isEmpty(self):
    return len(self.queue) == 0
#Kuyruktaki toplam eleman sayısını döndürür.------------------------------------------------------------
  def size(self):
    return len(self.queue)