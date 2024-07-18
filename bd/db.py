import sqlite3 as bd;

conn = bd.connect('./bd/base.db');

cursor = conn.cursor();

nqme = '';

def insertar_usuarios(nombre, edad):

    global cursor, conn

    datos = (nombre, edad)

    # sql = 'INSERT INTO usuarios (nombre, edad) VALUES (?, ? );'

    cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ? )', datos);


    print ('Datos insertados correctamente');

    conn.commit();

    cursor.close();
    conn.close();



# cursor.close();
# conn.close();