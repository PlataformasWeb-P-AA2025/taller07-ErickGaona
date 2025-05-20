from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Cargar datos de Club
with open('datos_clubs.txt', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        club = Club(
            nombre=row['nombre'],
            deporte=row['deporte'],
            fundacion=int(row['fundacion'])
        )
        session.add(club)

session.commit()

#print(f"📦 Datos cargados desde el TXT: {len(lista_datos)} registros")


# Cargar datos de Jugador
with open('datos_jugadores.txt', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        club =  session.query(Club).filter_by(nombre="LDU").one()
        jugador = Jugador(
            nombre=row['nombre'],
            dorsal=int(row['dorsal']),
            posicion=row['posicion'],
            club=club
        )
        session.add(jugador)

session.commit()

#print(f"📦 Datos cargados desde el TXT: {len(lista_datos)} registros")
