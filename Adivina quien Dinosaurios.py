import sqlite3

conn=sqlite3.connect('ARK.db')
c=conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS ARK (
    Nombre TEXT PRIMARY KEY,
    Carnivoro REAL NOT NULL,
    Hervivoro REAL NOT NULL,
    Oviparo REAL NOT NULL,
    Viviparo REAL NOT NULL,
    Volador REAL NOT NULL,
    Terrestre REAL NOT NULL,
    Acuatico REAL NOT NULL,
    Farmeo REAL NOT NULL,
    Tanqueo REAL NOT NULL,
    Ofensivo REAL NOT NULL,
    Defensivo REAL NOT NULL,
    Soporte REAL NOT NULL) """)

#c.execute("INSERT INTO ARK VALUES ('Rex',1,0,1,0,0,1,0,0,0,1,1,0)")
#c.execute("INSERT INTO ARK VALUES ('Manamagrm',1,0,0,1,1,1,1,0,0,1,1,0)")
#c.execute("INSERT INTO ARK VALUES ('Estego',0,1,1,0,0,1,0,1,1,0,1,0)")
#c.execute("INSERT INTO ARK VALUES ('Velonasaurio',1,0,1,0,0,1,0,0,0,1,1,0)")
#c.execute("INSERT INTO ARK VALUES ('Wyvern',1,0,1,0,1,0,0,0,0,1,0,0)")
#c.execute("INSERT INTO ARK VALUES ('Giganotosaurio',1,0,1,0,0,1,0,0,0,1,1,0)")
#c.execute("INSERT INTO ARK VALUES ('Trike',0,1,1,0,0,1,0,1,1,0,1,0)")
#c.execute("INSERT INTO ARK VALUES ('Argentavis',1,0,1,0,1,0,0,1,0,0,0,1)")
#c.execute("INSERT INTO ARK VALUES ('Ankilosaurio',0,1,1,0,0,1,0,1,0,0,0,0)")
#c.execute("INSERT INTO ARK VALUES ('Buho',1,0,1,0,1,0,0,0,0,1,1,1)")
#conn.commit()

c.execute("SELECT * FROM ARK")
Lolsito=c.fetchall()

database=[]

for row in Lolsito:        
    database.append({'nombre':row[0],'carnivoro':bool(row[1]),'hervivoro':bool(row[2]),'oviparo':bool(row[3]),'viviparo':bool(row[4]),'volador':bool(row[5]),'terrestre':bool(row[6]),'acuatico':bool(row[7]),'farmeo':bool(row[8]),'tanqueo':bool(row[9]),'ofensivo':bool(row[10]),'defensivo':bool(row[11]),'soporte':bool(row[12])},)

def take_chance(answer,property):
    if answer == "s":
        ans=True
    else:
        ans=False

    to_remove=[]
    for d in database:
        if d[property]!=ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)

ans=input("tu dinosaurio es carnivoro?(S/N)")
take_chance(ans,"carnivoro")
if ans=='s':
    ans1=1
else:
    ans1=0

ans=input("tu dinosaurio hervivoro(S/N)")
take_chance(ans,"hervivoro")
if ans=='s':
    ans2=1
else:
    ans2=0

ans=input("tu dinosaurio es oviparo?(S/N)")
take_chance(ans,"oviparo")
if ans=='s':
    ans3=1
else:
    ans3=0

ans=input("tu dinosaurio es viviparo?(S/N)")
take_chance(ans,"viviparo")
if ans=='s':
    ans4=1
else:
    ans4=0

ans=input("tu dinosaurio es volador?(S/N)")
take_chance(ans,"volador")
if ans=='s':
    ans5=1
else:
    ans5=0

ans=input("tu dinosaurio es terrestre?(S/N)")
take_chance(ans,"terrestre")
if ans=='s':
    ans6=1
else:
    ans6=0

ans=input("tu dinosaurio es acuatico?(S/N)")
take_chance(ans,"acuatico")
if ans=='s':
    ans7=1
else:
    ans7=0

ans=input("tu dinosaurio sirve para farmear?(S/N)")
take_chance(ans,"farmeo")
if ans=='s':
    ans8=1
else:
    ans8=0

ans=input("tu dinosaurio es un tanquesote?(S/N)")
take_chance(ans,"tanqueo")
if ans=='s':
    ans9=1
else:
    ans9=0

ans=input("tu dinosaurio sirve pa pegar madrazos?(S/N)")
take_chance(ans,"ofensivo")
if ans=='s':
    ans10=1
else:
    ans10=0

ans=input("tu dinosaurio sirve para defender tu base?(S/N)")
take_chance(ans,"defensivo")
if ans=='s':
    ans11=1
else:
    ans11=0

ans=input("tu dinosaurio sirve para curar y soportear?(S/N)")
take_chance(ans,"soporte")
if ans=='s':
    ans12=1
else:
    ans12=0



if len(database)==1:
    print("tu dinosaurio es "+database[0]["nombre"])
else:
    print("No tengo los datos sobre el dino")
    print('que dinosaurio era el que pensabas?')
    ans13=input()
    c.execute("INSERT INTO ARK VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(ans13,ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans9,ans9,ans10,ans11,ans12))
    conn.commit()

conn.close()
