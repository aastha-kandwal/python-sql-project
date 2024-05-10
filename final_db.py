import mysql.connector


def db():
    myconn=mysql.connector.connect(host="localhost",user="root",password="tiger")
    mycursor=myconn.cursor()
    mycursor.execute("create database hp_world")

    
def hpchar():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    query="create table if not exists hpcharacter(chid integer unique, chname varchar(70), chactor varchar(70), chbloodst varchar(15), chhouse varchar(15), chnick varchar(50), chdob date, chwand varchar(200), chpatronus varchar(40), chphyapp varchar(500))"
    mycursor.execute(query)

    
def hphouse():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    query="create table if not exists hphouse(hno integer, hname varchar(50), hfounder varchar(70), hanimal varchar(40), hcolour varchar(90), helement varchar(59), hghost varchar(50), htraits varchar(500), hhead varchar(550), hmember varchar(5000))"
    mycursor.execute(query)

    
def addhouse():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    hid=int(input("Enter house id"))
    hname=input("Enter house name")
    hfnd=input("Enter founder of the house")
    hani=input("Enter animal of the house")
    hclr=input("Enter house colors")
    hele=input("Enter house element")
    hghost=input("Enter name of house ghost")
    htrait=input("Enter traits of house members")
    hhead=input("Enter name of house heads")
    hmember=input("Enter name of members")
    t=( hid,hname,hfnd,hani,hclr,hele,hghost,htrait,hhead,hmember)
    query="insert into hphouse values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query,t)
    mydb.commit()


def hpmember():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    query="create table if not exists hpmember(mid integer unique, mname varchar(100), mhouse varchar(30), mbloodst varchar(30))"
    mycursor.execute(query)


def hpbook():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    query="create table if not exists hpbook(bid integer unique, bname varchar(200), bmovie varchar(200), byear date, myear date, bsummary varchar(2200))"
    mycursor.execute(query)



def addfb():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    bid=int(input("Enter a 3-Digit Book Id"))
    bname=input("Enter the name of the Book")
    bmovie=input("Enter the movie of the Book")
    byear=input("Enter the year of publication of the Book")
    myear=input("Enter the year of release of the Movie")
    bsmry=input("Enter the summary of the Book")
    t=(bid,bname,bmovie,byear,myear,bsmry)
    query="insert into hpbook values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query,t)
    mydb.commit()


def hpreview():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    query="create table if not exists hpreview(rno integer unique, rname varchar(60), remail varchar(150), rreview varchar(2000))"
    mycursor.execute(query)


def fbbook():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    query="create table if not exists fbbook(bid integer unique, bname varchar(200), bmovie varchar(200), byear date, myear date)"
    mycursor.execute(query)

def addfb():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    bid=int(input("Enter a 3-Digit Book Id"))
    bname=input("Enter the name of the Book")
    bmovie=input("Enter the movie of the Book")
    byear=input("Enter the year of publication of the Book")
    myear=input("Enter the year of release of the Movie")
    t=(bid,bname,bmovie,byear,myear)
    query="insert into fbbook values(%s,%s,%s,%s,%s)"
    mycursor.execute(query,t)
    mydb.commit()


def fbreview():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    query="create table if not exists fbreview(rno integer unique, rname varchar(60), remail varchar(150), rreview varchar(2000))"
    mycursor.execute(query)

db()
hpchar()
hphouse()
addhouse()
hpmember()
hpbook()
fbbook()
addfb()
hpreview()
fbreview()
