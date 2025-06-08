#Creating a stack using an Linked-List.
class Node:
  def __init__(self, value): 
    self.value = value       # Düğümün değeri
    self.next = None         # Bir sonraki düğümü gösterir

class Stack:
  def __init__(self):        #constructor
    self.head = None         #Stack'in en üstündeki (top) düğümü
    self.size = 0            # Stack'teki eleman sayısını takip eder

  def push(self, value):     #Stack'e yeni eleman ekler.
    new_node = Node(value)
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self.size += 1

  def pop(self):             #Stack’in En Üst Elemanını Çıkarır
    if self.isEmpty():
      return "Stack is empty"
    popped_node = self.head
    self.head = self.head.next
    self.size -= 1
    return popped_node.value

  def peek(self):           #Stack’in En Üst Elemanını Gösterir (Silmeden)
    if self.isEmpty():
      return "Stack is empty"
    return self.head.value

  def isEmpty(self):        #Stack’in Boş Olup Olmadığını Kontrol Eder
    return self.size == 0

  def stackSize(self):      #Stack’teki Eleman Sayısını Döndürür
    return self.size

  def traverseAndPrint(self): #Stack’i Baştan Sona Yazdırır
    currentNode = self.head
    while currentNode:
      print(currentNode.value, end=" -> ")
      currentNode = currentNode.next
    print()