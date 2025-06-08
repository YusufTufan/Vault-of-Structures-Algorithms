#Creating a stack using an array.
class Stack:
#constructor-------------------------------------------------------------------------------------------
    def __init__(self):  
        self.stack = []  
        
#Stack'e yeni bir eleman ekler.------------------------------------------------------------------------
    def push(self, element):  
        self.stack.append(element)  
#Stack'in en üstündeki elemanı çıkarır ve döndürür.Eğer stack boşsa, hata mesajı döndürür.-------------
    def pop(self):  
        if self.isEmpty():  
            return "Stack is empty"  
        return self.stack.pop()  
#Stack'in en üstündeki elemanı döndürür ama çıkartmaz.Eğer stack boşsa, hata mesajı döndürür.----------
    def peek(self):  
        if self.isEmpty():  
            return "Stack is empty"  
        return self.stack[-1]  
#Stack'in boş olup olmadığını kontrol eder.Eğer eleman yoksa 'True', varsa 'False' döndürür.------------
    def isEmpty(self):  
        return len(self.stack) == 0  
#Stack'teki toplam eleman sayısını döndürür.------------------------------------------------------------
    def size(self):  
        return len(self.stack)