def validate_data(data):
    if not isinstance(data, list):
        raise ValueError("Los datos deben ser una lista.")
    
    if not data:
        raise ValueError("La lista de datos no puede estar vacía.")
    
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Cada elemento de los datos debe ser un diccionario.")
        
        # Aquí se pueden agregar más validaciones específicas según los requisitos de los datos
        # Ejemplo: verificar que ciertas claves existan en el diccionario
        required_keys = ['id', 'name', 'value']  # Ejemplo de claves requeridas
        for key in required_keys:
            if key not in item:
                raise ValueError(f"Falta la clave requerida: {key} en el elemento {item}.")
    
    return True