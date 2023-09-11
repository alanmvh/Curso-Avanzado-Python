# Diseña una clase llamada Contador con los siguientes atributos y métodos:

# conteo - El valor actual del contador inicializado a 0
# incrementar() - El método que incrementa en 1 el conteo
# decrementar() - El método que decrementa en 1 el conteo
# Verifica que funcione el siguiente código:

class Contador():
    def __init__(self, valor_inicial):
        self.conteo = valor_inicial
        
    def incrementar(self):
        self.conteo += 1
    
    def decrementar(self):
        self.conteo -= 1
    
    def __str__(self):
        return "CONTADOR: {}".format(self.conteo)
        
contador1 = Contador(100)

contador1.incrementar()
contador1.incrementar()
contador1.decrementar()

print(contador1)
        
    


    