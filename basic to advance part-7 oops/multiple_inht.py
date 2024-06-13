class a:
    f = "hello world (from a)"
    

class b:
    ff = "welcome to bangladesh (from b)"
    

class c(a, b): # multiple inheritance (multiple parents)
    fff = "i am ironman (from c)"
    

f1 = c()
print(f1.fff)
print(f1.ff)
print(f1.f)
