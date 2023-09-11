from e101 import Contador

def test1():
    contador1 = Contador(1)
    for _ in range(1000):
        contador1.incrementar()
    
    assert contador1.conteo == 1001


def test2():
    contador2 = Contador(1)
    for _ in range(2000):
        contador2.decrementar()
    
    assert contador2.conteo == -1999

# Medir rendimiento de una funcion

def incrementar_1m():
    contador1 = Contador(0)
    for i in range(1_000_000):
        contador1.incrementar()
    
    assert contador1.conteo == 1000000
    
def test3(benchmark):
    benchmark(incrementar_1m)

#