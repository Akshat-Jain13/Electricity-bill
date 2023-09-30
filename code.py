CODING	
	def menu():
       c='y'
       while(c=='y' or c=='Y'):
      print("===============================================================")
        print("\t\t\t\t MENU")
  print("===============================================================")
        print("1.Add Record")
        print("2.Update Status")
        print("3.Delete Record")
        print("4.Display Table")
        print("5.Generate Bill")
        print("6.Exit")
        print("===============================================================")
        choice=int(input("Enter your choice:"))
        if choice==1:
              adddata()
        elif choice==2:
              updatedata()
        elif choice==3:
              deldata()
        elif choice==4:
              fetchdata()
        elif choice==5:
               bill()
        elif choice==6:
                print("THANK YOU")
                break
        else:
              print("Wrong input")
        print("------------------------------------------------------------------------------------------------")      
        c= input("Do you want to continue or not(Y/N):")
def bill():
     import mysql.connector
     db=mysql.connector.connect(host="localhost",user ="root", password="root",
                                         database="jns")
     cursor =db.cursor()
     try:
                   no=int(input("Enter IVRS number:"))
                   print("----------------------------------------------------------------------------------------")
                   Q1="select IVRS from EB where IVRS={}".format(no)
                   cursor=db.cursor()
                   cursor.execute(Q1)
                   results=cursor.fetchall()
                   for x in results:
                     print("IVRS Number:",x)
                   Q2="select CNAME from EB where IVRS={}".format(no)
                   cursor=db.cursor()
                   cursor.execute(Q2)
                   results=cursor.fetchall()
                   for x in results:
                     print("Customer Name:",x)
                   Q3="select PINCODE from EB where IVRS={}".format(no)
                   cursor=db.cursor()
                   cursor.execute(Q3)
                   results=cursor.fetchall()
                   for x in results:
                     print("Pincode:",x)
                   Q4="select LATESTREADING from EB where IVRS={}".format(no)
                   cursor=db.cursor()
                   cursor.execute(Q4)
                   results=cursor.fetchall()
                   for x in results:
                     print("Reading:",x)
                   Q5="select AMOUNT from EB where IVRS={}".format(no)
                   cursor=db.cursor()
                   cursor.execute(Q5)
                   results=cursor.fetchall()
                   for x in results:
                     print("Bill Amount:",x)
                   Q6="select STATUS from EB where IVRS={}".format(no)
                   cursor=db.cursor()
                   cursor.execute(Q6)
                   results=cursor.fetchall()
                   for x in results:
                     print("Status:",x)  
                   print("----------------------------------------------------------------------------------------")                                  
     except:
                  print("Error: Not in database")
def fetchdata():
     import mysql.connector
     db=mysql.connector.connect(host="localhost",user ="root", password="root",
                                         database="jns")
     cursor =db.cursor()
     try:     
                   cursor=db.cursor()
                   cursor.execute("select * from EB")
                   results=cursor.fetchall()
                   for x in results:
                     print(x)
     except:
                  print("Error:Unable to fetch data")                     
def adddata():       
        import mysql.connector
        db=mysql.connector.connect(host="localhost",user ="root", password="root",
                                         database="jns")
        cursor =db.cursor()
        no=int(input("Enter IVRS number:"))
        n=input("Enter Customer Name:")
        p=float(input("Enter Pincode:"))
        m=float(input("Enter Latest reading:"))
        o=int(input("Enter Amount:"))
        q=input("Status:")
        query1="Insert into EB values({},'{}',{},{},{},'{}')".format(no,n,p,m,o,q)
        cursor.execute(query1)
        db.commit()
        print("Record added!!!")
def updatedata():
    import mysql.connector
    try:
           db=mysql.connector.connect(host="localhost",user ="root", password="root",
                                         database="jns")
           cursor =db.cursor()
           no=int(input("Enter IVRS number:"))
           query2= "update EB set STATUS='PAID' where IVRS={}".format(no)
           cursor.execute(query2)
           print("Record updated!!!")
           db.commit()
    except Exception as e:
              print(e)
def deldata():
    import mysql.connector
    db=mysql.connector.connect(host="localhost",user ="root", password="root",
                                         database="jns")
    cursor =db.cursor()
    no=int(input("Enter IVRS number which is to be deleted:"))
    query3= "delete from EB where IVRS={}".format(no)
    cursor.execute(query3)
    print("Record deleted!!!")
    db.commit()
menu()
