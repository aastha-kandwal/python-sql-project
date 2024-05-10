import mysql.connector


def addchar():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    cid=int(input("Enter character id"))
    cname=input("Enter character name")
    cactor=input("Enter character actor")
    cbldst=input("Enter character's blood status")
    chouse=input("Enter character's hogwarts house")
    cnick=input("Enter character's nick name/popular name")
    cdob=input("Enter characters date of birth YY-MM-DD")
    cwand=input("Enter character's wand descripton")
    cpatronus=input("Enter character's patronus")
    cphyapp=input("Enter character's physical appearance")
    t=(cid,cname,cactor,cbldst,chouse,cnick,cdob,cwand,cpatronus,cphyapp)
    query="insert into hpcharacter values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query,t)
    mydb.commit()


    
def showchar():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    query="select * from hpcharacter"
    mycursor.execute(query)
    res=mycursor.fetchall()
    t=("Character_ID","Character_Name","Character_Actor","Character_Blood Status","Character_Hogwarts-house","Character_Nickname","Character_DOB","Character_Wand","Character_Patronus","Character_Phyical Appearance")
    for i in t:
        print(i,end="\t")
    print()
    print()
    for rec in res:
        for col in rec:
            print(col,end="\t")
        print()
        print()


        
def showhouse():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    query="select * from hphouse"
    mycursor.execute(query)
    res=mycursor.fetchall()
    t=("House_ID","House_Name","House_Founder","House_Animal","House_Colours","House_Element","House_Ghost","House_Member traits","House_Heads","House_Members")
    for i in t:
        print(i,end="\t")
    print()
    print()
    for rec in res:
        for col in rec:
            print(col,end="\t")
        print()
        print()


        
def bssearch():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    print()
    ch=input(" * Enter P to see Pure-bloods \n * Enter H to see Half-Bloods \n * Enter M to see Muggle-Borns")
    print()
    if ch=="P" or ch=="p":
        query="select chname,chbloodst from hpcharacter where chbloodst='Pure-Blood'"
        mycursor.execute(query)
        res=mycursor.fetchall()
        t=("Character_Name","Character_Blood Status")
        for i in t:
            print(i,end="\t")
        print()
        print()
        for rec in res:
            for col in rec:
                print(col,end="\t")
            print()
            print()
    elif ch=="H" or ch=="h":
        query="select chname,chbloodst from hpcharacter where chbloodst='Half-Blood'"
        mycursor.execute(query)
        res=mycursor.fetchall()
        t=("Character_Name","Character_Blood Status")
        for i in t:
            print(i,end="\t")
        print()
        print()
        for rec in res:
            for col in rec:
                print(col,end="\t")
            print()
            print()
    elif ch=="M" or ch=="m":
        query="select chname,chbloodst from hpcharacter where chbloodst='Muggle-Born'"
        mycursor.execute(query)
        res=mycursor.fetchall()
        t=("Character_Name","Character_Blood Status")
        for i in t:
            print(i,end="\t")
        print()
        print()
        for rec in res:
            for col in rec:
                print(col,end="\t")
            print()
            print()
    else:
        print()
        print("$$ *************************** $$")
        print("$$ Please enter a valid choice $$")
        print("$$ *************************** $$")
        print()



        
def housesearch():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    print()
    ch=input(" *Enter G to see Gryffindor Members \n *Enter S to see Slytherin Members \n *Enter R to see Ravenclaw Members \n *Enter H to see Hufflepuff Members")
    print()
    if ch=="G" or ch=="g":
        query="select chname,chhouse from hpcharacter where chhouse='Gryffindor'"
        mycursor.execute(query)
        res=mycursor.fetchall()
        t=("Character_Name","Character_Hogwarts-house")
        for i in t:
            print(i,end="\t")
        print()
        print()
        for rec in res:
            for col in rec:
                print(col,end="\t")
            print()
            print()
    elif ch=="S" or ch=="s":
        query="select chname,chhouse from hpcharacter where chhouse='Slytherin'"
        mycursor.execute(query)
        res=mycursor.fetchall()
        t=("Character_Name","Character_Hogwarts-house")
        for i in t:
            print(i,end="\t")
        print()
        print()
        for rec in res:
            for col in rec:
                print(col,end="\t")
            print()
            print()
    elif ch=="R" or ch=="r":
        query="select chname,chhouse from hpcharacter where chhouse='Ravenclaw'"
        mycursor.execute(query)
        res=mycursor.fetchall()
        t=("Character_Name","Character_Hogwarts-house")
        for i in t:
            print(i,end="\t")
        print()
        print()
        for rec in res:
            for col in rec:
                print(col,end="\t")
            print()
            print()
    elif ch=="H" or ch=="h":
        query="select chname,chhouse from hpcharacter where chhouse='Hufflepuff'"
        mycursor.execute(query)
        res=mycursor.fetchall()
        t=("Character_Name","Character_Hogwarts-house")
        for i in t:
            print(i,end="\t")
        print()
        print()
        for rec in res:
            for col in rec:
                print(col,end="\t")
            print()
            print()
    else:
        print()
        print("$$ *************************** $$")
        print("$$ Please enter a valid choice $$")
        print("$$ *************************** $$")
        print()


def showstudent():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    query="select * from hpmember"
    mycursor.execute(query)
    res=mycursor.fetchall()
    t=("Student_ID","Student_Name","Student_House","Student_Blood Status")
    for i in t:
        print(i,end="\t")
    print()
    print()
    for rec in res:
        for col in rec:
            print(col,end="\t")
        print()
        print()


        
def addhousemem():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    mid=int(input("Enter a 3-Digit Student's ID"))
    mname=input("Enter the Student's Name")
    mhouse=input("Enter the Student's House")
    mbldst=input("Enter the Student's Blood Status")
    t=(mid,mname,mhouse,mbldst)
    query="insert into hpmember values(%s,%s,%s,%s)"
    mycursor.execute(query,t)
    mydb.commit()


def showbook():   
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    query="select * from hpbook"
    mycursor.execute(query)
    res=mycursor.fetchall()
    t=("Book_ID","Book_Name","Book_Movie","Book_Year of Publication","Book_Movie Release Year","                  Book_Summary")
    for i in t:
        print(i,end="\t")
    print()
    print()
    for rec in res:
        for col in rec:
            print(col,end="\t")
        print()
        print()

def review():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    query="select * from hpreview"
    mycursor.execute(query)
    res=mycursor.fetchall()
    t=("Individual_ID","Individual_Name","Individual_Email ID","Individual_Feedback")
    for i in t:
        print(i,end="\t")
    print()
    print()
    for rec in res:
        for col in rec:
            print(col,end="\t")
        print()
        print()


def feedback():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    mid=int(input("Enter a 3-Digit ID"))
    mname=input("Enter your Name")
    mhouse=input("Enter your Email Id")
    mbldst=input("Enter your Feedback")
    t=(mid,mname,mhouse,mbldst)
    query="insert into hpreview values(%s,%s,%s,%s)"
    mycursor.execute(query,t)
    mydb.commit()


def fbshow():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    query="select * from fbbook"
    mycursor.execute(query)
    res=mycursor.fetchall()
    t=("Book_ID","Book_Name","Book_Movie","Book_Year of Publication","Book_Movie Release Year")
    for i in t:
        print(i,end="\t")
    print()
    print()
    for rec in res:
        for col in rec:
            print(col,end="\t")
        print()
        print()



def fbreview():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    query="select * from fbreview"
    mycursor.execute(query)
    res=mycursor.fetchall()
    t=("Individual_ID","Individual_Name","Individual_Email ID","Individual_Feedback")
    for i in t:
        print(i,end="\t")
    print()
    print()
    for rec in res:
        for col in rec:
            print(col,end="\t")
        print()
        print()


def fbfeedback():
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="hp_world")
    mycursor=mydb.cursor()
    mid=int(input("Enter a 3-Digit ID"))
    mname=input("Enter your Name")
    mhouse=input("Enter your Email Id")
    mbldst=input("Enter your Feedback")
    t=(mid,mname,mhouse,mbldst)
    query="insert into fbreview values(%s,%s,%s,%s)"
    mycursor.execute(query,t)
    mydb.commit()



ch=1



while ch!=0:
    print()
    print("*************************************************")
    print("<< Welcome To 'The Wizarding World Library' !! >>")
    print("*************************************************")
    print()
    ch=int(input(" *Enter 1 to visit Harry Potter's Characters' Menu \n *Enter 2 to visit Hogwarts Houses' Menu \n *Enter 3 to visit Fantastic Beasts Books & Movies Feedback Menu \n *Enter 4 to visit Harry Potter Books & Movies Feedback Menu \n *Enter 0 to exit"))
    if ch==1:
        print()
        print("******************************************************")
        print("......Entering into Harry Potter Characters Menu......")
        print("******************************************************")
        print()
        ch=input(" *Enter A to view the List of Harry Potter Characters \n *Enter B to Add a New Character \n *Enter C to Go to the Search Menu \n")
        if ch=="A" or ch=="a":
            print()
            print("******************************************************")
            print("......The Characters of Harry Potter Universe !!......")
            print("******************************************************")
            print()
            showchar()
        elif ch=="B" or ch=="b":
            print()
            print("**********************************************************")
            print(".......Add a New Character to our List. Input Data!.......")
            print("**********************************************************")
            print()
            addchar()
        elif ch=="C" or ch=="c":
            print()
            print("*******************************")
            print("<< Entering into Search Menu >>")
            print("*******************************")
            print()
            ch=int(input(" *Enter 101 to search on the basis of Blood Statuses \n *Enter 102 to search on the basis of Hogwarts Houses"))
            if ch==101:
                print()
                print("*********************************************")
                print("......Opening Blood Status Search Menu.......")
                print("*********************************************")
                print()
                bssearch()
            elif ch==102:
                print()
                print("**********************************************")
                print("......Opening Hogwarts House Search Menu......")
                print("**********************************************")
                print()
                housesearch()
            else:
                print()
                print("$$ *************************** $$")
                print("$$ Please enter a valid choice $$")
                print("$$ *************************** $$")
                print()
        else:
            print()
            print("$$ *************************** $$")
            print("$$ Please enter a valid choice $$")
            print("$$ *************************** $$")
            print()
    elif ch==2:
        print()
        print("***********************************************")
        print("......Entering into Hogwarts Houses' Menu......")
        print("***********************************************")
        print()
        ch=input(" *Enter A to view the List of Hogwarts Houses \n *Enter B to view the List of Hogwarts Students \n *Enter C to Add a New Student to a House")
        if ch=="A" or ch=="a":
            print()
            print("*************************************************************")
            print("<< The House Of Hogwarts School of Witchcraft and Wizardry >>")
            print("*************************************************************")
            print()
            showhouse()
        elif ch=="B" or ch=="b":
            print()
            print("*************************************************************")
            print(".......The Students of Hogwarts School and their Houses......")
            print("*************************************************************")
            print()
            showstudent()
        elif ch=="C" or ch=="c":
            print()
            print("***********************************************************")
            print("......Add a New Student to Hogwarts Houses. Input Data.....")
            print("***********************************************************")
            print()
            addhousemem()
        else:
            print()
            print("$$ *************************** $$")
            print("$$ Please enter a valid choice $$")
            print("$$ *************************** $$")
            print()
    elif ch==3:
        print()
        print("***************************************************************")
        print("......Entering into Fantastic Beasts Book & Movie Catalog......")
        print("***************************************************************")
        print()
        ch=input(" *Enter X to view Books and Movies List \n *Enter Y to go to the Feedback-Review System \n")
        if ch=="X" or ch=="x":
            print()
            print("*******************************************")
            print("......Fantastic Beasts Books & Movies......")
            print("*******************************************")
            print()
            fbshow()
        elif ch=="Y" or ch=="y":
            print()
            print("************************************************")
            print("......Entering into Feedback-Review system......")
            print("************************************************")
            print()
            ch=input(" *Enter R to read Reviews \n *Enter I to input Feedback")
            if ch=="R" or ch=="r":
                print()
                print("***********************************************")
                print("......Reviews List of Harry Potter Series......")
                print("***********************************************")
                print()
                fbreview()
            elif ch=="I" or ch=="i":
                print()
                print("************************************************************")
                print("......Add a New Feedback to HP-Reviews List. Input Data.....")
                print("************************************************************")
                print()
                fbfeedback()
            else:
                print()
                print("$$ *************************** $$")
                print("$$ Please enter a valid choice $$")
                print("$$ *************************** $$")
                print()                
    elif ch==4:
        print()
        print("**************************************************************")
        print(".......Entering into Harry Potter Books & Movie Catalog.......")
        print("**************************************************************")
        print()
        ch=input(" *Enter X to view Books and Movies List \n *Enter Y to go to the Feedback-Review System \n")
        if ch=="X" or ch=="x":
            print()
            print("***************************************")
            print("......Harry Potter Books & Movies......")
            print("***************************************")
            print()
            showbook()
        elif ch=="Y" or ch=="y":
            print()
            print("************************************************")
            print("......Entering into Feedback-Review system......")
            print("************************************************")
            print()
            ch=input(" *Enter R to read Reviews \n *Enter I to input Feedback")
            if ch=="R" or ch=="r":
                print()
                print("***********************************************")
                print("......Reviews List of Harry Potter Series......")
                print("***********************************************")
                print()
                review()
            elif ch=="I" or ch=="i":
                print()
                print("************************************************************")
                print("......Add a New Feedback to HP-Reviews List. Input Data.....")
                print("************************************************************")
                print()
                feedback()
            else:
                print()
                print("$$ *************************** $$")
                print("$$ Please enter a valid choice $$")
                print("$$ *************************** $$")
                print()                
    elif ch not in (0,1,2,3,4):
        print()
        print()
        print("$$ *************************** $$")
        print("$$ Please enter a valid choice $$")
        print("$$ *************************** $$")
        print()
        print()
               

