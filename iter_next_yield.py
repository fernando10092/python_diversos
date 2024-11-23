############ CODIGOS DE SALVAR O ESTADO DA APLICACAO ############
#Semelhante ao FOR
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#YIELD NEXT
def myFunc():
    print('Começo')
    yield
    print("FIM")

try:
    x = myFunc()
    next(x)
    next(x)
except StopIteration as e:
    print(e)


#YIELD NEXT
def ydNext():
    a = 1
    yield a
    print(a)

    a += a
    yield a
    print(a)

    a += a
    yield a
    print(a)


x = idNext()
next(x)
next(x)
next(x)


#SEND
def envio():
    x = yield
    print(x)

    a = yield
    print(a)

try:
    x = envio()
    next(x)
    x.send(20)
 
except StopIteration as e:
    print(e)