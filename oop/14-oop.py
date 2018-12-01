class a():
    pass
class b(a):
    pass
class c():
    pass
#判斷是否為某子類(子類,父類)的繼承關係
print(issubclass(b,a))
print(issubclass(c,b))
print(issubclass(b,object))
