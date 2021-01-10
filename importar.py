import mysql.connector
import datetime


sql_columns = "SHOW columns FROM horarios Where FIELD like 'TxtM%' OR FIELD LIKE 'TxtT%'"
sql_agafa_dia_setmana = (
    "SELECT * FROM `horarios` WHERE {0} LIKE '%{1}%' and NidAnyo>2019")
sql_insertar_dia = (
    "INSERT INTO `cefire` (`user_id`, `data`, `inici`, `fi`, `id`) VALUES ('{0}', '{1}', '{2}', '{3}', NULL) ")
sql_insertar_curs = (
    "INSERT INTO `curs` (`user_id`, `data`, `inici`, `fi`, `curs`, `id`) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', NULL) ")
sql_insertar_guardia = (
    "INSERT INTO `guardia` (`user_id`, `data`, `inici`, `fi`, `id`) VALUES ('{0}', '{1}', '{2}', '{3}', NULL) ")
sql_insertar_permis = (
    "INSERT INTO `permis` (`user_id`, `data`, `inici`, `fi`, `motiu`, `arxiu`,`id`) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', NULL) ")
sql_insertar_compensa = (
    "INSERT INTO `compensa` (`user_id`, `data`, `inici`, `fi`, `motiu`,`id`) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', NULL) ")
sql_insertar_visita = (
    "INSERT INTO `visita` (`user_id`, `data`, `inici`, `fi`, `centre`,`id`) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', NULL) ")


prova_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="prova",
    charset='utf8'
)

cefire_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="cefire_valencia",
    charset='utf8'
)

# #prova_db.set_character_set('utf8')
# cursor = prova_db.cursor()
# cursor.execute("SET NAMES utf8;")
# cursor.execute("SET CHARACTER SET utf8;")
# cursor.execute("SET character_set_connection=utf8;")
# prova_db.commit()

# #cefire_db.set_character_set('utf8')
# cursor2 = cefire_db.cursor()
# cursor2.execute("SET NAMES utf8;")
# cursor2.execute("SET CHARACTER SET utf8;")
# cursor2.execute("SET character_set_connection=utf8;")
# cefire_db.commit()


def data_desde_w_d(y, w, d, h, m):
    return datetime.datetime.strptime(str(y)+'-'+str(w-1)+'-'+str(d)+'-'+str(h)+'-'+str(m), "%Y-%W-%w-%H-%M")

def extraer_cadena_hasta_final(cadena,inici):
    print("----------------------------------------")
    print(cadena)
    cadena = cadena.upper()
    indice_c = cadena.index(inici)
    subcadena = cadena[indice_c:]
    return subcadena

def extraer_visita_hasta_final(cadena,inici):
    print("----------------------------------------")
    print(cadena)
    cadena = cadena.upper()
    print(cadena)
    indice_c = cadena.index(inici)
    print(indice_c)
    subcadena = cadena[indice_c:]
    if "CEFIRE" in subcadena:
        indice_f = cadena.index("CEFIRE")
        subcadena=subcadena[:indice_f]
    return subcadena



def extraer_cadena_hasta_final_perm(cadena,inici):
    print("----------------------------------------")
    print(cadena)
    cadena = cadena.upper()
    indice_c = cadena.index(inici)
    indice_f = cadena.find('(');
    subcadena = cadena[indice_c:indice_f]
    return subcadena

def extraer_archivo_perm(cadena):
    print("----------------------------------------")
    print(cadena)
    indice_c = cadena.find('(');
    indice_f = cadena.find(')');
    subcadena = cadena[(indice_c+1):indice_f]
    if (subcadena[-3:].lower() == "pdf" or subcadena[-4:].lower() == "jpeg" or subcadena[-3:].lower() == "odt" or subcadena[-3:].lower() == "jpg" or subcadena[-3:].lower() == "png" or subcadena[-3:].lower() == "txt"):
        return subcadena
    else:
        return "";



r2 = data_desde_w_d(2020, 10, 1, 14, 00)
print(r2)

mycursor_cefire = cefire_db.cursor(buffered=True)
mycursor_prova = prova_db.cursor(buffered=True)
mycursor_prova.execute(sql_columns)

myresult_prova = mycursor_prova.fetchall()


for x in myresult_prova:
    # print(x[0])
    #print("SELECT * FROM `horarios` WHERE {0} LIKE '\%CEFIRE\%' and NidAnyo>2018".format(x[0]))

    if x[0] == 'TxtManyanaL':
        hora_inici = 9
        hora_fi = 14
        dia = 1
        pos=3
    elif x[0] == 'TxtTardeL':
        hora_inici = 16
        hora_fi = 20
        dia = 1
        pos=4
    elif x[0] == 'TxtManyanaM':
        hora_inici = 9
        hora_fi = 14
        dia = 2
        pos=5
    elif x[0] == 'TxtTardeM':
        hora_inici = 16
        hora_fi = 20
        dia = 2
        pos=6
    elif x[0] == 'TxtManyanaX':
        hora_inici = 9
        hora_fi = 14
        dia = 3
        pos=7
    elif x[0] == 'TxtTardeX':
        hora_inici = 16
        hora_fi = 20
        dia = 3
        pos=8
    elif x[0] == 'TxtManyanaJ':
        hora_inici = 9
        hora_fi = 14
        dia = 4
        pos=9
    elif x[0] == 'TxtTardeJ':
        hora_inici = 16
        hora_fi = 20
        dia = 4
        pos=10
    elif x[0] == 'TxtManyanaV':
        hora_inici = 9
        hora_fi = 14
        dia = 5
        pos=11
    elif x[0] == 'TxtTardeV':
        hora_inici = 16
        hora_fi = 20
        dia = 5
        pos=12
    elif x[0] == 'TxtManyanaS':
        hora_inici = 9
        hora_fi = 14
        dia = 6
        pos=13
    elif x[0] == 'TxtTardeS':
        hora_inici = 16
        hora_fi = 20
        dia = 6
        pos=14
    elif x[0] == 'TxtManyanaD':
        hora_inici = 9
        hora_fi = 14
        dia = 0
        pos=15
    elif x[0] == 'TxtTardeD':
        hora_inici = 16
        hora_fi = 20
        dia = 0
        pos=16
    
    mycursor_prova.execute(sql_agafa_dia_setmana.format(x[0],"CEFI"))
    myresult_prova_cefire = mycursor_prova.fetchall()

    for y in myresult_prova_cefire:
        print(y)
        mycursor_cefire.execute(sql_insertar_dia.format(y[0], data_desde_w_d(y[2], y[1], dia, hora_inici, 0), str(hora_inici)+":00:00", str(hora_fi)+":00:00"))
     
    mycursor_prova.execute(sql_agafa_dia_setmana.format(x[0],"CURS"))
    myresult_prova_curs = mycursor_prova.fetchall()

    for y in myresult_prova_curs:
        print(y)
        mycursor_cefire.execute(sql_insertar_curs.format(y[0], data_desde_w_d(y[2], y[1], dia, hora_inici, 0), str(hora_inici)+":00:00", str(hora_fi)+":00:00", extraer_visita_hasta_final(y[pos],"CURS").replace("\'","\\\'")))
    
    mycursor_prova.execute(sql_agafa_dia_setmana.format(x[0],"GUARDIA"))
    myresult_prova_guardia = mycursor_prova.fetchall()

    for y in myresult_prova_guardia:
        print(y)
        mycursor_cefire.execute(sql_insertar_guardia.format(y[0], data_desde_w_d(y[2], y[1], dia, hora_inici, 0), str(hora_inici)+":00:00", str(hora_fi)+":00:00"))
    
    mycursor_prova.execute(sql_agafa_dia_setmana.format(x[0],"PERM"))
    myresult_prova_permis = mycursor_prova.fetchall()

    for y in myresult_prova_permis:
        print(y)        
        mycursor_cefire.execute(sql_insertar_permis.format(y[0], data_desde_w_d(y[2], y[1], dia, hora_inici, 0), str(hora_inici)+":00:00", str(hora_fi)+":00:00",extraer_cadena_hasta_final_perm(y[pos],"PERM"),extraer_archivo_perm(y[pos])))
        
        
    mycursor_prova.execute(sql_agafa_dia_setmana.format(x[0],"COMPEN"))
    myresult_prova_compensa = mycursor_prova.fetchall()

    for y in myresult_prova_compensa:
        print(y)
        mycursor_cefire.execute(sql_insertar_compensa.format(y[0], data_desde_w_d(y[2], y[1], dia, hora_inici, 0), str(hora_inici)+":00:00", str(hora_fi)+":00:00",extraer_visita_hasta_final(y[pos],"COMPEN").replace("\'","\\\'")))
    

    mycursor_prova.execute(sql_agafa_dia_setmana.format(x[0],"VISIT"))
    myresult_prova_visita = mycursor_prova.fetchall()

    for y in myresult_prova_visita:
        print(y)
        mycursor_cefire.execute(sql_insertar_visita.format(y[0], data_desde_w_d(y[2], y[1], dia, hora_inici, 0), str(hora_inici)+":00:00", str(hora_fi)+":00:00",extraer_visita_hasta_final(y[pos],"VISIT").replace("\'","\\\'")))
    
    mycursor_prova.execute(sql_agafa_dia_setmana.format(x[0],"SALID"))
    myresult_prova_salida = mycursor_prova.fetchall()

    for y in myresult_prova_salida:
        print(y)        
        mycursor_cefire.execute(sql_insertar_visita.format(y[0], data_desde_w_d(y[2], y[1], dia, hora_inici, 0), str(hora_inici)+":00:00", str(hora_fi)+":00:00",extraer_visita_hasta_final(y[pos],"SALID")))
    
    mycursor_prova.execute(sql_agafa_dia_setmana.format(x[0],"EIXID"))
    myresult_prova_eixida = mycursor_prova.fetchall()

    for y in myresult_prova_eixida:
        print(y)        
        mycursor_cefire.execute(sql_insertar_visita.format(y[0], data_desde_w_d(y[2], y[1], dia, hora_inici, 0), str(hora_inici)+":00:00", str(hora_fi)+":00:00",extraer_visita_hasta_final(y[pos],"EIXID")))
    
    cefire_db.commit()
   

