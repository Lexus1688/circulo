class circulo:
    PI = 3.1416
    def __init__(self,radio):
        self.radio = radio
    def circunferencia(self):
        return 2 * self.PI * self.radio

    def area(self):
        return self.PI * self.radio ** 2

if __name__ == "__circulo__":
    instancia_circulo = circulo(10)
    print(f"EL perimetro del circulo es: {instancia_circulo.circunferencia()}")
    print(f"El area del circulo es: {instancia_circulo.area()}")
