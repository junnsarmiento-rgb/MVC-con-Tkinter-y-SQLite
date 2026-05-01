"Registro de Productos en Inventario"
import sqlite3


class Producto:
    def __init__(self, db_name='productos.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def agregar_producto(self, nombre, cantidad, precio):
        query = 'INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)'
        self.conn.execute(query, (nombre, cantidad, precio))
        self.conn.commit()

    def listar(self):
        query = 'SELECT * FROM productos'
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def eliminar_producto(self, producto_id):
        query = 'DELETE FROM productos WHERE id = ?'
        self.conn.execute(query, (producto_id,))
        self.conn.commit()


