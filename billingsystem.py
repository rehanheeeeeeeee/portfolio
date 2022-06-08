import mysql.connector
connect=mysql.connector.connect(host='localhost',password='root',user='root',database='project')
cursor=connect.cursor()
def log_signup():
    while True:
        
        answer=input("do you want to login or signup:")
        if answer=="login":
            
            phoneno=float(input("enter your phone number:"))
            username=input("Enter a username:")
            password=input("enter your password:")
            user=(phoneno,username,password)
            cursor.execute("select * from registered")
            info=cursor.fetchall()              
            if user in info:
            
                print("logged in successfully")
                break
            else:
                
                print("incorrect information")
        elif answer=="signup":
           phoneno=float(input("Enter your phone number:"))
           allphoneno=[]
           username=input("Enter a username:")
           password=input("enter your password:")
           while True:
               confirm_password=input("Enter your password again:")
               if confirm_password==password:
                   break
               else:
                   print("incorrect password try again")
            
        
           cursor.execute("select phoneno from registered")
           numbers=cursor.fetchall()
           for tuple in numbers:
               
               for eachnumber in tuple:
                   
                   allphoneno.append(eachnumber)
        
           if phoneno in allphoneno:
            print("invalid number")
        
           else:    
               cursor.execute("insert into registered  values({},'{}','{}')".format(phoneno,username,password))
               connect.commit()
               print("sign in successful")
               print("signed in successfully")
               break
log_signup()

menu_options=["purchase amount","account settings"]
print("___________________________________Options______________________________________")

def menu():
    answer_option=["yes","no"]
    print("1.purchase_amount")
    option=input("Would you like explore this option(yes/no):")
    if option.lower()==answer_option[0]:
             allphone=[]
             phone=float(input("To access this option please enter your phone number:"))
             cursor.execute("select phoneno from purchase_info")
             numbers=cursor.fetchall()
             for tuple in numbers:
                 for eachnumber in tuple:
                     allphone.append(eachnumber)
             if phone in allphone: 
                amount_options=["amount paid","amount due"]
                print("1.Amount paid\n2.Amount due")
                amount=input("which amount would like to know:")
                if amount==amount_options[0]: 
                   cursor.execute("select amount_paid from purchase_info where phoneno='{}'".format(phone))
                   amounts=cursor.fetchall()
                   amount_paid= 0
                   for eachnumber in amounts:
                       for eachno in eachnumber:
                           amount_paid= amount_paid + eachno
                           
                   print("your amount paid till the date is: "+ str(amount_paid))
                   while True:
                        tell=input("do you want to explore other options(yes/no):")
                        if tell.lower() =="no":
                           break
                        elif tell.lower() == "yes":
                           amo=input("which amount would like to know or do you want to exit this menu:")
                           amount_option=["amount paid","amount due","exit"]
                           print("1.Amount paid\n2.Amount due")
                           if amo==amount_option[0]:
                              cursor.execute("select amount_due from purchase_info where phoneno='{}'".format(phone))
                              rupees=cursor.fetchall()
                              amount_due= 0
                              for eachnumber in rupees:
                                  for eachno in eachnumber:
                                      amount_due= amount_due + eachno
                              print("Your amount due till the date is: " + str(amount_due))
                           elif amo==amount_option[1]:
                              cursor.execute("select amount_paid from purchase_info where phoneno='{}'".format(phone))
                              amounts=cursor.fetchall()
                              amount_paid1= 0
                              for eachnumber in amounts:
                                  for eachno in eachnumber:
                                      amount_paid1= amount_paid1 + eachno
                              print("your amount paid till the date is "+ str(amount_paid1))
                           elif amo==amount_options[2]:
                              break
                    
                elif  amount==amount_options[1]:
                     cursor.execute("select amount_due from purchase_info where phoneno='{}'".format(phone))
                     rupees=cursor.fetchall()
                     amount_due= 0
                     for eachnumber in rupees:
                         for eachno in eachnumber:
                             amount_due= amount_due + eachno
                     print("Your amount due till the date is " + str(amount_due))
                     while True:
                         tell=input("do you want to explore other options(yes/no):")
                         if tell.lower() == "no":
                            break
                         
                         elif tell.lower() == "yes":
                            amo=input("which amount would like to know or do you want to exit this menu:")
                            amount_option=["amount paid","amount due","exit"]
                            if amo==amount_option[0]:
                               cursor.execute("select amount_due from purchase_info where phoneno='{}'".format(phone))
                               rupees=cursor.fetchall()
                               amount_due1= 0
                               for eachnumber in rupees:
                                   for eachno in eachnumber:
                                       amount_due1= amount_due1 + eachno
                               
                               print("Your amount due till the date is " + str(amount_due1))
                            elif amo==amount_option[1]:
                               cursor.execute("select amount_paid from purchase_info where phoneno='{}'".format(phone))
                               amounts=cursor.fetchall()
                               amount_paid= 0
                               for eachnumber in amounts:
                                   for eachno in eachnumber:
                                       amount_paid= amount_paid + eachno
                               print("your amount paid till the date is "+ str(amount_paid))
                            elif amo==amount_option[2]:
                               break           
                else:
                    print("invalid option choosen")
             else:
                 print("invalid number")
menu()
          
def menu2():
    answer_options=["yes","no"]
    print("2.Account settihgs")
    option=input("Would you like explore this option(yes/no):")
    if option.lower()==answer_options[0]:
        allphone=[]
        phone=float(input("To access this option please enter your phone number:"))
        cursor.execute("select phoneno from purchase_info")
        numbers=cursor.fetchall()
        for tuple in numbers:
            for eachnumber in tuple:
                allphone.append(eachnumber)
        if phone in allphone:
            account_options=["username","password","phone number","delete user"]
            print("1.change username\n2.change password\n3.change phone number\n4.Delete user")
            change=input("which information would you like to change:")
            if change==account_options[0]:
                phane=float(input("To access this option please enter your phone number:"))
                new_username=input("enter your new username:")
                cursor.execute("update registered set username='{}' where phoneno={}".format(new_username,phane))
                connect.commit()
                print("Username changed successfully")
            elif change==acount_options[1]:
                phane=float(input("To access this option please enter your phone number:"))
                new_password=input("enter your new password")
                cursor.execute("update registered set password='{}' where phoneno={}".format(new_password,phane))
                connect.commit()
                print("Password changed successfully")
            elif change==account_options[2]:
                phane=float(input("To access this option please enter your phone number:"))
                new_phone_number=input("enter your new phone number:")
                cursor.execute("update regsitered set phoneno={} where phoneno={}".format(new_phone_number,phane))
                connect.commit()
                print("Phone number changed successfully")
            elif change==account_options[3]:
                phane=float(input("To access this option please enter your phone number:"))
                delete_user=input("enter your new phone number:")
                cursor.execute("delete from registered where phoneno={}".format(phane))
                connect.commit()
                print("user deleted successfully")
                
            else:
                print("inavlid option choosen")
        else:
            print("invalid phone number choosen")
                
menu2()

def menu3():
    answer_options1=["yes","no"]
    print("2.Bills")
    option1=input("Would you like to review your bills(yes/no):")
    if option1==answer_options1[0]:
        print("Bill as on 31st january 2022:")
        print("Bill as on 28th february 2022:")
        bills=["january 2022","february 2022"]
        date=input("Of which month bill so you want to see:")
        if date.lower()==bills[0]:
            store=[]
            phonenumber=float(input("Please enter your phone number:"))
            cursor.execute("select phoneno from registered")
            phonenumero=cursor.fetchall()
            for eachno in phonenumero:
                for eachnumber in eachno:
                    store.append(eachnumber)
            if phonenumber in store:
                names=""
                cursor.execute("select username from registered where phoneno={}".format(phonenumber))
                name=cursor.fetchall()
                for each in name:
                    for letter in each:
                        names += letter
                
                cursor.execute("select total_amount_january from bill where phoneno={}".format(phonenumber))
                total=cursor.fetchall()
                cursor.execute("select paid_january from bill where phoneno={}".format(phonenumber))
                paid=cursor.fetchall()
                cursor.execute("select due_january from bill where phoneno={}".format(phonenumber))
                due=cursor.fetchall()
                print("\n\n")
                print("\tWater Authority Kingdom of Bahrain\n\n\n")
                print("Date of issue: 31st january 2022\n")
                print("Name: " +names+ "                 phone number: " +str(phonenumber) + "\n")
                print("Total Monthly charges of the month January 2022: " + str(total)+"\n")
                print("Amount paid for the month of january 2022: " +str(paid)+"\n")
                print("Amount due for the month of  " +str(due)+ "\n")
                print("--------------------------------------------------------------")
                while True:
                    
                    ans=input("do you want to review more bills(yes/no):")
                    if ans.lower()=="yes":
                        which=input("Which dates bill do you want to see to see:")
                        dates=["january 2022","february 2022"]
                        if which.lower()=="january 2022":
                            
                            cursor.execute("select total_amount_january from bill where phoneno={}".format(phonenumber))
                            total=cursor.fetchall()
                            cursor.execute("select paid_january from bill where phoneno={}".format(phonenumber))
                            paid=cursor.fetchall()
                            cursor.execute("select due_january from bill where phoneno={}".format(phonenumber))
                            due=cursor.fetchall()
                            print("\n\n")
                            print("\tWater Authority Kingdom of Bahrain\n\n\n")
                            print("Date of issue: 31st january 2022\n")
                            print("Name: " +names+ "                 phone number: " +str(phonenumber) + "\n")
                            print("Total Monthly charges of the month January 2022: " + str(total)+"\n")
                            print("Amount paid for the month of january 2022: " +str(paid)+"\n")
                            print("Amount due for the month of  " +str(due)+ "\n")
                            print("--------------------------------------------------------------")
                            
                        elif which.lower()=="february 2022":
            
                            cursor.execute("select total_amount_february from bill where phoneno={}".format(phonenumber))
                            total=cursor.fetchall()
                            cursor.execute("select paid_february from bill where phoneno={}".format(phonenumber))
                            paid=cursor.fetchall()
                            cursor.execute("select due_february from bill where phoneno={}".format(phonenumber))
                            due=cursor.fetchall()
                            print("\n\n")
                            print("\tWater Authority Kingdom of Bahrain\n\n\n")
                            print("Date of issue: 31st january 2022\n")
                            print("Name: " +names+ "                 phone number: " +str(phonenumber) + "\n")
                            print("Total Monthly charges of the month January 2022: " + str(total)+"\n")
                            print("Amount paid for the month of january 2022: " +str(paid)+"\n")
                            print("Amount due for the month of  " +str(due)+ "\n")
                            print("----------------------------------------------------------------")
                        else:
                            print("invlid date choosen")
                            
                    else:
                        break
                
            else:
                print("invalid phone number")
            
        elif date==bills[1]: 
            store=[]
            phonenumber=float(input("Please enter your phone number:"))
            cursor.execute("select phoneno from registered")
            phonenumero=cursor.fetchall()
            for eachno in phonenumero:
                for eachnumber in eachno:
                    store.append(eachnumber)
            if phonenumber in store:
                names=""
                cursor.execute("select username from registered where phoneno={}".format(phonenumber))
                name=cursor.fetchall()
                for each in name:
                    for letter in each:
                        names += letter
                cursor.execute("select total_amount_february from bill where phoneno={}".format(phonenumber))
                total=cursor.fetchall()
                cursor.execute("select paid_february from bill where phoneno={}".format(phonenumber))
                paid=cursor.fetchall()
                cursor.execute("select due_february from bill where phoneno={}".format(phonenumber))
                due=cursor.fetchall()
                print("\n\n")
                print("\tWater Authority Kingdom of Bahrain\n\n\n")
                print("Date of issue: 31st january 2022\n")
                print("Name: " +names+ "                 phone number: " +str(phonenumber) + "\n")
                print("Total Monthly charges of the month January 2022: " + str(total)+"\n")
                print("Amount paid for the month of january 2022: " +str(paid)+"\n")
                print("Amount due for the month of  " +str(due)+ "\n")
                print("--------------------------------------------------------------")
                while True:
                    
                    ans=input("do you want to review more bills(yes/no):")
                    if ans.lower()=="yes":
                        which=input("Which dates bill do you want to see to see:")
                        dates=["january 2022","february 2022"]
                        if which.lower()=="january 2022":
                            
                            cursor.execute("select total_amount_january from bill where phoneno={}".format(phonenumber))
                            total=cursor.fetchall()
                            cursor.execute("select paid_january from bill where phoneno={}".format(phonenumber))
                            paid=cursor.fetchall()
                            cursor.execute("select due_january from bill where phoneno={}".format(phonenumber))
                            due=cursor.fetchall()
                            print("\n\n")
                            print("\tWater Authority Kingdom of Bahrain\n\n\n")
                            print("Date of issue: 31st january 2022\n")
                            print("Name: " +names+ "                 phone number: " +str(phonenumber) + "\n")
                            print("Total Monthly charges of the month January 2022: " + str(total)+"\n")
                            print("Amount paid for the month of january 2022: " +str(paid)+"\n")
                            print("Amount due for the month of  " +str(due)+ "\n")
                            print("--------------------------------------------------------------")
                            
                        elif which.lower()=="february 2022":
            
                            cursor.execute("select total_amount_february from bill where phoneno={}".format(phonenumber))
                            total=cursor.fetchall()
                            cursor.execute("select paid_february from bill where phoneno={}".format(phonenumber))
                            paid=cursor.fetchall()
                            cursor.execute("select due_february from bill where phoneno={}".format(phonenumber))
                            due=cursor.fetchall()
                            print("\n\n")
                            print("\tWater Authority Kingdom of Bahrain\n\n\n")
                            print("Date of issue: 31st january 2022\n")
                            print("Name: " +names+ "                 phone number: " +str(phonenumber) + "\n")
                            print("Total Monthly charges of the month January 2022: " + str(total)+"\n")
                            print("Amount paid for the month of january 2022: " +str(paid)+"\n")
                            print("Amount due for the month of  " +str(due)+ "\n")
                            print("----------------------------------------------------------------")
                        else:
                            print("invlid date choosen")

                    else:
                       break
            else:
                print("invalid number")
        else:
            print("Invalid date choosen")
        
menu3()

def administrator():
    password=input("Please enter the password to be able to access this part of the system:")
    pas="hehe"
    if password.lower()==pas:
        
        while True:
            
            opt=["delete user","add user","update amounts","update tables","exit"]
            print("\n\n1.Delete user\n2.Add user\n3.update amounts\n4.update tables\n5.exit")
            bol=input("Which function would like to perform or would you like to exit from this area:")
            
            if bol.lower()==opt[0]:
                
                id=float(input("Please mention the phone number of the user you would like to delete:"))
                cursor.execute("delete from registered where phoneno={}".format(id))
                connect.commit()
                print("user deleted successfully")

            
            elif bol.lower()==opt[1]:
                id=input("Please mention the phone number of the user you would like to add:")
                dd=input("Please mention the username of the user you would like to add:")
                ad=input("Please mention the password of the user you would like to add:")
                cursor.execute("insert into registered values({},'{}','{}')".format(id,dd,ad))
                connect.commit()
                print("User added successfully")
                
            elif bol.lower()==opt[2]:
                ph=float(input("Please enter the phone number of the person whose amounts you want to update"))
                due_a=float(input("Please enter the new due amount of the user:"))
                paid_a=float(input("Please enter the new paid amount of the user"))
                tot=due_a+paid_a
                cursor.execute("update purchase_info set total_amount={},amount_due={},amount_paid={} where phoneno={}".format(tot,due_a,paid_a,ph))
                connect.commit()
                print("Amounts updated successfully")
                
                
            elif bol.lower()==opt[3]:
                months=["january","february","march","april","may","june","july","august","septemeber","octuber","november","december"]
                tell=input("Which months table would you like to add")
                if tell.lower()=="january":
                    cursor.execute("alter table bill add paid_january INT")
                    cursor.execute("alter table bill add due_january INT")
                    cursor.execute("alter table bill add total_amount_january INT")
                    print("tables added successfully")               
                    add=float(input("Please add the total amount the month that needs to be paid by the user:"))
                    du=float(input("Please add the due amount the month that needs to be paid by the user:"))
                    pa=float(input("Please add the amount paid by the user for the month:"))
                    cursor.execute("update bill set total_amount_january={},due_january={},paid_january={}".format(add,du,pa))
                    connect.commit()
                    print("Tables and amounts added successfully")
                elif tell.lower()=="february":
                    cursor.execute("alter table bill add paid_february INT")
                    cursor.execute("alter table bill add due_february INT")
                    cursor.execute("alter table bill add total_amount_february INT")
                    print("tables added successfully")               
                    add=float(input("Please add the total amount the month that needs to be paid by the user:"))
                    du=float(input("Please add the due amount the month that needs to be paid by the user:"))
                    pa=float(input("Please add the amount paid by the user for the month:"))
                    cursor.execute("update bill set total_amount_february={},due_february={},paid_february={}".format(add,du,pa))
                    connect.commit()
                    print("Tables and amounts added successfully")
                elif tell.lower()=="march":
                    cursor.execute("alter table bill add paid_march INT")
                    cursor.execute("alter table bill add due_march INT")
                    cursor.execute("alter table bill add total_amount_march INT")
                    print("tables added successfully")
                    add=float(input("Please add the total amount the month that needs to be paid by the user:"))
                    du=float(input("Please add the due amount the month that needs to be paid by the user:"))
                    pa=float(input("Please add the amount paid by the user for the month:"))
                    cursor.execute("update bill set total_amount_march={},due_march={},paid_march={}".format(add,du,pa))
                    connect.commit()
                    print("Tables and amounts added successfully")
                elif tell.lower()=="april":
                    cursor.execute("alter table bill add paid_april INT")
                    cursor.execute("alter table bill add due_april INT")
                    cursor.execute("alter table bill add total_amount_april INT")
                    print("tables added successfully")
                    add=float(input("Please add the total amount the month that needs to be paid by the user:"))
                    du=float(input("Please add the due amount the month that needs to be paid by the user:"))
                    pa=float(input("Please add the amount paid by the user for the month:"))
                    cursor.execute("update bill set total_amount_april={},due_april={},paid_april={}".format(add,du,pa))
                    connect.commit()
                    print("Amounts added successfully")          
                elif tell.lower()=="may":
                    cursor.execute("alter table bill add paid_may INT")
                    cursor.execute("alter table bill add due_may INT")
                    cursor.execute("alter table bill add total_amount_may INT")
                    print("tables added successfully")               
                    add=float(input("Please add the total amount the month that needs to be paid by the user:"))
                    du=float(input("Please add the due amount the month that needs to be paid by the user:"))
                    pa=float(input("Please add the amount paid by the user for the month:"))
                    cursor.execute("update bill set total_amount_may={},due_may={},paid_may={}".format(add,du,pa))
                    connect.commit()
                    print("Amounts added successfully")
                elif tell.lower()=="june":
                    cursor.execute("alter table bill add paid_june INT")
                    cursor.execute("alter table bill add due_june INT")
                    cursor.execute("alter table bill add total_amount_june INT")
                    print("tables added successfully")               
                    add=float(input("Please add the total amount the month that needs to be paid by the user:"))
                    du=float(input("Please add the due amount the month that needs to be paid by the user:"))
                    pa=float(input("Please add the amount paid by the user for the month:"))
                    cursor.execute("update bill set total_amount_june={},due_june={},paid_june={}".format(add,du,pa))
                    connect.commit()
                    print("Amounts added successfully")          
                elif tell.lower()=="july":
                    cursor.execute("alter table bill add paid_july INT")
                    cursor.execute("alter table bill add due_july INT")
                    cursor.execute("alter table bill add total_amount_july INT")
                    print("tables added successfully")
                    add=float(input("Please add the total amount the month that needs to be paid by the user:"))
                    du=float(input("Please add the due amount the month that needs to be paid by the user:"))
                    pa=float(input("Please add the amount paid by the user for the month:"))
                    cursor.execute("update bill set total_amount_july={},due_july={},paid_july={}".format(add,du,pa))
                    connect.commit()
                    print("Amounts added successfully")
                elif tell.lower()=="august":
                    cursor.execute("alter table bill add paid_august INT")
                    cursor.execute("alter table bill add due_august INT")
                    cursor.execute("alter table bill add total_amount_august INT")
                    print("tables added successfully")
                    add=float(input("Please add the total amount the month that needs to be paid by the user:"))
                    du=float(input("Please add the due amount the month that needs to be paid by the user:"))
                    pa=float(input("Please add the amount paid by the user for the month:"))
                    cursor.execute("update bill set total_amount_august={},due_august={},paid_august={}".format(add,du,pa))
                    connect.commit()
                    print("Amounts added successfully")
                elif tell.lower()=="septemeber":
                    cursor.execute("alter table bill add paid_september INT")
                    cursor.execute("alter table bill add due_september INT")
                    cursor.execute("alter table bill add total_amount_september INT")
                    print("tables added successfully")               
                    add=float(input("Please add the total amount the month that needs to be paid by the user:"))
                    du=float(input("Please add the due amount the month that needs to be paid by the user:"))
                    pa=float(input("Please add the amount paid by the user for the month:"))
                    cursor.execute("update bill set total_amount_september={},due_september={},paid_september={}".format(add,du,pa))
                    connect.commit()
                    print("Amounts added successfully")
                elif tell.lower()=="octuber":
                    cursor.execute("alter table bill add paid_octuber INT")
                    cursor.execute("alter table bill add due_octuber INT")
                    cursor.execute("alter table bill add total_amount_octuber INT")
                    print("tables added successfully")               
                    add=float(input("Please add the total amount the month that needs to be paid by the user:"))
                    du=float(input("Please add the due amount the month that needs to be paid by the user:"))
                    pa=float(input("Please add the amount paid by the user for the month:"))
                    cursor.execute("update bill set total_amount_octuber={},due_octuber={},paid_octuber={}".format(add,du,pa))
                    connect.commit()
                    print("Amounts added successfully")          
                elif tell.lower()=="november":
                    cursor.execute("alter table bill add paid_november INT")
                    cursor.execute("alter table bill add due_november INT")
                    cursor.execute("alter table bill add total_amount_november INT")
                    print("tables added successfully")               
                    add=float(input("Please add the total amount the month that needs to be paid by the user:"))
                    du=float(input("Please add the due amount the month that needs to be paid by the user:"))
                    pa=float(input("Please add the amount paid by the user for the month:"))
                    cursor.execute("update bill set total_amount_november={},due_november={},paid_november={}".format(add,du,pa))
                    connect.commit()
                    print("Amounts added successfully")
                elif tell.lower()=="december":
                    cursor.execute("alter table bill add due_december INT")
                    cursor.execute("alter table bill add total_amount_december INT")
                    print("tables added successfully")               
                    add=float(input("Please add the total amount the month that needs to be paid by the user:"))
                    du=float(input("Please add the due amount the month that needs to be paid by the user:"))
                    pa=float(input("Please add the amount paid by the user for the month:"))
                    cursor.execute("update bill set total_amount_december={},due_december={},paid_december={}".format(add,du,pa))
                    connect.commit()
                    print("Amounts added successfully")
                else:
                    print("invalid month")
            
            elif bol.lower()==opt[4]:
                
                break

                 
    else:
        print("incorrect password")

administrator()







