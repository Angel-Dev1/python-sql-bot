def format_data(data):
    # Implementar la lógica para formatear los datos según sea necesario
    formatted_data = []
    for item in data:
        # Ejemplo de formateo: convertir a string y eliminar espacios
        formatted_data.append(str(item).strip())
    return formatted_data

def log_error(error_message):
    # Implementar la lógica para registrar errores
    with open('error_log.txt', 'a') as log_file:
        log_file.write(f"{error_message}\n")