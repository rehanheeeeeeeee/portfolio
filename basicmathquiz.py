from itertools import combinations
from itertools import permutations
import logging
import mysql.connector
connect=mysql.connector.connect(host="localhost",password="root",user="root",database="quiz")
cursor=connect.cursor()
logging.basicConfig(level=logging.DEBUG,format="%(levelname)s:%(message)s")
print("\n\tTHIS IS A BASIC MATH QUIZ TO TEST YOUR KNOWLEDGE ON SOME BASIC TOPICS\n")
def loginsignup():
    while True:
        option=["login","signin"]
        ans=input("Do you want to login or signin:")
        if ans.lower() in option:
            break
        else:
            logging.critical("Please choose between either log in or signin")
    while True:
        if ans.lower()=="login":
            logging.info("Please enter the required details:")
            phone=int(input("phone number:"))
            while True:
                emailid=input("enter your email:")
                if "@gmail.com" in emailid:
                    break
                else:
                    logging.critical("Please add @gmail.com in a correct way while entering in your email")
            
            password=input("Enter your password:")
            taple=(phone,emailid,password)
            cursor.execute("select phone_number,email,password from id")
            data=cursor.fetchall()
            if taple in data:
                logging.debug("You've logged in successfully Welcome back")
                break
            else:
                logging.error("The information you've entered is incorrect")
        elif ans.lower()=="signin":
            logging.info("Please enter the required information")
            cursor.execute("select phone_number from id")
            allphone=cursor.fetchall()
            listoff=[phane for each in allphone for phane in each ]
            while True:
                phone=int(input("Please enter your phone number:"))
                if phone in listoff:
                    logging.error("This phone number is already in use please enter a different phone number")
                else:
                    break
            name=input("Enter your name:")
            while True:
                
                emailid=input("enter your email:")
                if "@gmail.com" in emailid:
                    break
                else:
                    logging.critical("Please add @gmail.com in a correct way while entering in your email")
            password=input("Enter your password:")
            while True:
                confirm=input("Please enter your password again:")
                if confirm==password:
                    break
                else:
                    logging.error("You've typed different passwords please check the password youve entered earliar")
           
            cursor.execute("insert into id values({},'{}','{}','{}')".format(phone,name,emailid,password))
            connect.commit()
            cursor.execute("insert into leaderboard values({},0)".format(phone))
            connect.commit()
            logging.info("You have successsfully signed in")
            break         
#loginsignup()

def quiz():
    attempt=input("Do you want to attempt the quiz(yes/no):")
    while True:
        number=int(input("Please provide us with your phone number so we can track your score:"))
        cursor.execute("select phone_number from id")
        al=cursor.fetchall()
        lost=[x for each_tuple in al for x in each_tuple]
        if number in lost:
            break
            logging.info("Thank you for your coperation")
        else:
            logging.error("invalid Phone number")
        
    if attempt.lower()=="yes":
        logging.info("\n\tWelcome to the math quiz here some basic questions related to math wlll be asked and each question carries one mark\n")
        print("So lets begin...\n")
        score=0
        mistakes=0
        A={1,2,3,4,5,6}
        B={8,6,10,12}
        data=str(A.isdisjoint(B))
        logging.info("Please the write the answer as a boolean value here")
        answer=input("1. Are the two sets A=[1,2,3,4,5,6] and B=[8,6,10,12] disjoint sets? (True or False):")
        if answer==data:
            score=score+1
        logging.info("\nPlease write down all the combinations in tuples and combine them all in a list for example:[(x,y),(a,b)]")
        answer1=input("1. state all the possible two order combinations of the set [1,2,3]:\n")
        k=[1,2,3]
        ans200=[(1,2),(2,3),(1,3)]
        ans3=[(1,3),(1,2),(2,3)]
        ans100=combinations(k,2)
        possible=[ans200,ans100,ans3]
        if answer1 in possible:
            score = score+1
        logging.info("Sets are written inside of curly brackets")
        answer4=input("3. What will be the union of the thses two sets:\nA={3,6,9}\nB={2,4,6,8}\nAnswer:")
        X={3,6,9}
        Y={2,4,6,8}
        ans4=str(X.union(Y))
        if answer4==ans4:
            score = score+1
        answer5=input("\n4. What will be the intersection of the following sets:\nA={2,4,6,8}\nB={7,8,9}\nAnswer:")
        Z={2,4,6,8}
        Q={7,8,9}
        ans5=str(Z.intersection(Q))
        if answer5==ans5:
            score=score+1
        logging.info("Please write down all the PERMUTATIONS in tuples and combine them all in a list for example:[(x,y),(a,b)]")
        answer6=input("\n5. state all the possible permutations of the set:\nA=[2,3]\nAnswer:")
        P=[2,3]
        ans6=list(permutations(P,2))
        ans7=[(3,2),(2,3)]
        answers=[ans6,ans7]
        if answer6 in answers:
            score=score+1
        print(score)
        cursor.execute("update leaderboard set score={} where phone_number = {}".format(score,number))
        connect.commit()
        cursor.execute("select id.name,leaderboard.score from id join leaderboard on id.phone_number=leaderboard.phone_number")
        cunt=cursor.fetchall()
        print(cunt)
quiz()



        
        






        






            
