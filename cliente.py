import json

class Cliente:
    def __init__(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
    
    def editar_cliente(self, nombre_buscar, nuevo_nombre=None, nuevo_email=None, nueva_direccion=None, nuevo_telefono=None):
        # se busca por nombre, hay que establecer nuevo_NOMBRE para indicar que hay que editar
        # editar el archivo con el cliente
        archivo_json = "clientes.json"
        try:
            clientes = []
            try:
                with open(archivo_json, 'r') as file:
                    clientes = json.load(file)
                    if not isinstance(clientes, list):
                        clientes = []
            except FileNotFoundError:
                pass

            cliente_encontrado = None
            for cliente in clientes:
                if cliente.get('nombre') == nombre_buscar:
                    cliente_encontrado = cliente
                    break
            
            if cliente_encontrado:
                if nuevo_nombre:
                    cliente_encontrado['nombre'] = nuevo_nombre
                if nuevo_email:
                    cliente_encontrado['email'] = nuevo_email
                if nueva_direccion:
                    cliente_encontrado['direccion'] = nueva_direccion
                if nuevo_telefono:
                    cliente_encontrado['telefono'] = nuevo_telefono

                with open(archivo_json, 'w') as file:
                    json.dump(clientes, file, indent=2)
                
                return f"Cliente {nombre_buscar} modificado correctamente en {archivo_json}"
            else:
                return f"No se encontró un cliente con el nombre {nombre_buscar}"

        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")
            return "Error al modificar el cliente"
    
    def __str__(self):
        archivo_json = "clientes.json"
        try:
            clientes = []
            try:
                with open(archivo_json, 'r') as file:
                    clientes = json.load(file)
                    if not isinstance(clientes, list):
                            clientes = []
            except FileNotFoundError:
                pass
            clientes.append(self.__dict__)

            with open(archivo_json, 'w') as file:
                json.dump(clientes, file, indent=2)
        
            return super().__str__()  # Devolver la representación en cadena del objeto
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")
            return "Error al guardar el cliente"

# crear un cliente