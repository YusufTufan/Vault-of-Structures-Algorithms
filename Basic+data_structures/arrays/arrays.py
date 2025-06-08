from array import *
a = array('i',[1,2,3])
print(a)
#append---------------------------
a.append(4)
print(a)
#insert---------------------------
a.insert(0, 12)
print(a)
#extend---------------------------
my_extnd_array = array('i', [7,8,9,10])
a.extend(my_extnd_array)
print(a)
#remove---------------------------
a.remove(3)
print(a)
#pop------------------------------
a.pop()
print(a)
#index----------------------------
b = a.index(4)
print(b)
#reverse---------------------------
a.reverse()
print(a)
a.reverse()
print(a)
#buffer_info()----------------------
print(a.buffer_info())
#count------------------------------
d = a.count(9)
print(d)
#tounicode--------------------------
char_array = array('u', ['g','e','e','k'])
print(char_array.tounicode())
#tolist--------------------------
e = a.tolist()
print(e)
#fromunicode---------------------
char_array.fromunicode('yusuf')
print(char_array)
