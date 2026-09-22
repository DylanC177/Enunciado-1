class Empleado:
    def __init__(self, nombre, pago_base):
        self.nombre = nombre
        self.pago_base = pago_base

    def obtener_sueldo(self):
        return float(self.pago_base)

class Gerente(Empleado):
    def obtener_sueldo(self):
        return self.pago_base * 1.30 

class Vendedor(Empleado):
    def __init__(self, nombre, pago_base, total_ventas):
        Empleado.__init__(self, nombre, pago_base) 
        self.total_ventas = total_ventas

    def obtener_sueldo(self):
        return self.pago_base + (self.total_ventas * 0.10)

emp = Empleado("Oriana", 10000)
ger = Gerente("Franklin", 20000)
ven = Vendedor("Christhofer", 1200, 5000)

nomina = (emp, ger, ven)

for persona in nomina:
    
    rol = persona.__class__.__name__ 
    sueldo_final = persona.obtener_sueldo()
    
    print("El trabajador {} ({}) gana: ${:.2f} de sueldo".format(
        persona.nombre, 
        rol, 
        sueldo_final
    ))
