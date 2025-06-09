# Boş bir liste oluştur(10 uzunluklu)
my_list = [None] * 10

# Hash fonksiyonu
#onksiyonu, verilen karakterin Unicode (ASCII) değerini döndürür.(Tüm charların toplamı  % 10)
def hash_function(value):
    return sum(ord(char) for char in value) % 10 

# Eleman ekleme fonksiyonu
def add(name):
    index = hash_function(name)
    my_list[index] = name

# Eleman arama fonksiyonu
def contains(name):
    index = hash_function(name)
    return my_list[index] == name

# Örnek kullanım
add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')

print("'Pete' hash tablosunda var mı?", contains('Pete'))