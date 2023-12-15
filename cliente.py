class Cliente:
    def __init__(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
    def registrar_cliente(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}, Dirección: {self.direccion}, Teléfono: {self.telefono}"