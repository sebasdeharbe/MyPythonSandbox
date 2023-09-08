# file_path = 'D:\Programación\Python\20230610\diccionario.txt'

def convert_to_js_array(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    data = [line.strip() for line in lines]
    js_array = f'var lista = {str(data)}'
    
    with open('arreglo.txt', 'w') as archivo_salida:
        archivo_salida.write(js_array)

# Ejemplo de uso
file_path = 'diccionario.txt'
convert_to_js_array(file_path)