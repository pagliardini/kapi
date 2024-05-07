from flask import Flask, jsonify, request
from flask_cors import CORS
import pymssql

app = Flask(__name__)
CORS(app)

# Configuración de la conexión
server = ''
database = ''
username = ''
password = ''

# Obtener todos los productos o buscar por codigo
@app.route('/productos', methods=['GET', 'POST'])
def get_productos():
    conn = pymssql.connect(server=server, user=username, password=password, database=database)
    cursor = conn.cursor(as_dict=True)

    # Verificación de si se proporciona un codigo para buscar
    codigo = request.args.get('codigo')
    if codigo:
        cursor.execute('SELECT * FROM Productos WHERE Id_Producto = %s OR Id_Producto1 = %s OR Id_Producto2 = %s OR Id_Producto3 = %s', (codigo, codigo, codigo, codigo))
    else:
        cursor.execute('SELECT * FROM Productos')

    productos = []
    for row in cursor:
        producto = {
            'id': row['Id_Producto'],
            'id2': row['Id_Producto1'],
            'id3': row['Id_Producto2'],
            'id4': row['Id_Producto3'],
            'nombre': row['Descripcion'],
            'precio': row['Precio_Venta'],
            # Se pueden agregar mas columnas
        }
        productos.append(producto)
    conn.close()
    return jsonify(productos)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
