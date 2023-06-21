import sqlite3

def crear_DB():
    with sqlite3.connect("ranking.db") as conexion:
        conexion.commit()

def crear_tabla():
    with sqlite3.connect("ranking.db") as conexion:
        try:
            conexion.execute(
                """ create table score
                ( 
                    id integer primary key autoincrement,
                    nombre text,
                    score int
                )
                """
            )
            print("Se creo la tabla scores")
        
        except sqlite3.OperationalError:
            print("Tabla ya creada")


def insertar_fila(nombre, score):
    with sqlite3.connect("ranking.db") as conexition:
        try:
            conexition.execute(
                "insert into score(nombre,score) values (?,?)", (nombre, score))
            conexition.commit()
        except:
            print("Error insert row")   


def listar_filas():
    with sqlite3.connect("ranking.db") as conexion:
        cursor=conexion.execute("SELECT * FROM score order by score DESC")
        lista_ranking = []
        for fila in cursor:
            lista_ranking.append(fila)
    return lista_ranking