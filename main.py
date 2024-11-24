import json
import datetime
import random
import string


# class for loading and saving Json files
class Json:
    @staticmethod
    def json_load(path):  # load json file
        with open(path) as infile:
            db = json.load(infile)
        return db

    @staticmethod # save json file
    def json_save(db,path):
        with open(path,"w") as outfile:
            json.dump(db, outfile, indent=4)  #  #

# class for user to sign up
class SignUp:

    @staticmethod
    def sign_up(): # complete sign up for user, this function includes multiple functions for signing up
        username = SignUp.get_username()
        email = SignUp.get_email()
        password = SignUp.get_password()
        birthyear = SignUp.get_birthyear()
        if birthyear is not None:
            question_1,answer_1,question_2,answer_2 = SignUp.get_security_question()
            db = Json.json_load("user_db.json")
            info = {
                "id" : random.randint(1000000,9999999),
                "username" : username,
                "email" : email,
                "password" : password,
                "birthyear" : birthyear,
                "question_1" : question_1,
                "answer_1" : answer_1,
                "question_2" : question_2,
                "answer_2": answer_2,
                "courses" :{}
            }

            db.append(info)
            Json.json_save(db,"user_db.json")

    @staticmethod
    def get_username(): # get a unique username
        while True:
            user_input = input("Enter your username => ").lower()
            db = Json.json_load("user_db.json")
            user_found = False
            try:
                for i in db :
                    if i["username"] == user_input:
                        user_found = True
                if user_found:
                    print("⚠ this user already exist ⚠")
                else:
                    return user_input
            except:
                return user_input

    @staticmethod
    def get_email(): # get a unique email
        while True:
            user_input = input("Enter your email address => ").lower()
            db = Json.json_load("user_db.json")
            email_format_list = ["@gmail.com","@email.com","@outlook.com"]
            email_found = False
            email_format = False
            try:
                for i in db:
                    if i["email"] == user_input:
                        email_found = True
            except:
                email_found = False

            if not email_found:
                for j in email_format_list:
                    if user_input.endswith(j):
                        email_format = True
                        break
                if email_format:
                    return user_input
                else:
                    print("⚠ wrong email format ⚠")
            else:
                print("⚠ this email already exist ⚠")

    @staticmethod
    def get_password(): #get a password that must have a letter and number with len >= 6
        while True:
            user_input = input("Enter your password => ")
            letters = string.ascii_letters
            digit = string.digits
            punctuation = string.punctuation
            letters_number = 0
            digit_number = 0
            punctuation_number = 0
            for i in user_input:
                if i in letters:
                    letters_number += 1
                elif i in digit:
                    digit_number += 1
                elif i in punctuation:
                    punctuation_number += 1
            if len(user_input) >= 6 :
                if letters_number > 0 and digit_number > 0 and punctuation_number == 0:
                    return user_input
                else:
                    print("⚠ wrong format of password ( password have to include letters and numbers ❗)")
            else:
                print("⚠ your password is too short ⚠")

    @staticmethod
    def get_birthyear(): # get correct age. if age was not correct, it will end the sign up process
        while True :
            user_input = input("Enter your birth year => ")
            user_input_int = int(user_input)
            correct = 18 < datetime.datetime.now().year - user_input_int < 50
            if correct :
                return user_input
            else:
                print("⚠ you are too old or young for this app, call (123) 213-3414 ⚠")
                return None

    @staticmethod
    def get_security_question(): # asks security question for forget password
        security_db = Json.json_load("security_question.json")
        for i,j in enumerate(security_db,start=1):
            print(f"{i}. {j}")
        while True:
            user_q1 = input("enter your question => ")
            try:
                user_q1 = int(user_q1) - 1
                user_a1 = input(security_db[user_q1])
                security_db.remove(security_db[user_q1])
                user_q1 = security_db[int(user_q1) - 1]
                break
            except ValueError:
                print("❗ please enter a number ❗")
            except IndexError:
                print("❗ wrong number ❗")
        print("\n📍 next question\n")

        for i,j in enumerate(security_db,start=1):
            print(f"{i}. {j}")
        while True:
            user_q2 = input("enter your question => ")
            try:
                user_q2 = int(user_q2) - 1
                user_a2 = input(security_db[user_q2])
                user_q2 = security_db[int(user_q2) - 1]
                break
            except ValueError:
                print("⚠ please enter a number ⚠")
            except IndexError:
                print("⚠ wrong number ⚠")
        return user_q1,user_a1,user_q2,user_a2

# class for login and forgot password
class Login:

    @staticmethod
    def login(): # login function
        while True:
            db = Json.json_load("user_db.json")
            username_input = input("Enter your username or Email => ")
            found = False
            for user in db:
                if user["username"] == username_input or user["email"] == username_input:
                    found = True
                    password_input = input("Enter your password => ")
                    if user["password"] == password_input:
                        return True,user
                    else:
                        print("wrong password")
                        forget_password = input("do you forget your password ? => ")
                        if forget_password.lower() == "yes" or forget_password.lower() == "y":
                            Login.forget_password()
            if not found:
                print("⚠ did not found your account ⚠")

    @staticmethod
    def forget_password(): # forgot password function
        db = Json.json_load("user_db.json")
        user_input = input("Enter your username or email => ")
        found = False
        for user in db:
            if user["username"] == user_input or user["email"] == user_input:
                found = True
                user_answer_1 = input(user["question_1"])
                user_answer_2 = input(user["question_2"])
                while user_answer_1 == user["answer_1"] or user_answer_2 == user["answer_2"]:
                    new_password = input("Enter your new password => ")
                    password_confirmation = input("Enter your new password again =>  ")
                    if new_password == password_confirmation:
                        user["password"] = new_password
                        Json.json_save(db,"user_db.json")
                        print("your password has successfully changed ✅")
                        break
            if not found:
                print("❗ we did not find your user ❗")


# class for Taking course and quiz
class Taking_course:

    @staticmethod
    def take_course(user): # taking course function it loads all db's for signing up course for each person once only
        while True:
            db = Json.json_load("user_db.json")
            Advanced_db = Json.json_load("Advanced_python.json")
            Basic_db = Json.json_load("python_basic.json")
            lesson_db = ["python basic", "Advanced python"]
            user_input = input("select your lesson : \n1) 🔹python basic\n2) 🔹Advanced python\n3) 🔹back\n")
            try:
                user_input = int(user_input) - 1
                break
            except ValueError:
                print("❗ not a number ❗")
        if len(lesson_db) > user_input >= 0:
            if lesson_db[user_input] == "Advanced python":
                if user["username"] in Advanced_db["students"]:
                    print("🚫 you already in this course 🚫")

                else:
                    Advanced_db["students"].append(user["username"])
                    Json.json_save(Advanced_db, "Advanced_python.json")
                    for i in db:
                        if i["username"] == user["username"]:
                            i["courses"]["Advanced python"] = "NA"
                            Json.json_save(db,"user_db.json")
                            print(f"done\nthis course will start at {Advanced_db["start time"]}")

            elif lesson_db[user_input] == "python basic":
                if user["username"] in Basic_db["students"]:
                    print("🚫 you already in this course 🚫")
                else:
                    Basic_db["students"].append(user["username"])
                    Json.json_save(Basic_db, "python_basic.json")
                    for i in db:
                        if i["username"] == user["username"]:
                            i["courses"]["python basic"] = "NA"
                            Json.json_save(db, "user_db.json")
                            print(f"done\nthis course will start at {Basic_db["start time"]}")
        elif user_input == 2:
            pass
        else:
            print("❗ enter a valid number ❗")
            Taking_course.take_course(user)




    @staticmethod
    def take_python_quiz(user): # first quiz function
        quiz = Json.json_load("quiz.json")["Python Basics"]
        score = 0
        user_answers = []
        for questions in quiz:
            print(questions["question"])
            for i in questions["options"]:
                print(i)
            while True:
                user_answer = input("Enter your answer => ")
                try:
                    user_answer = int(user_answer) - 1
                    user_answer = questions["options"][user_answer]
                    break
                except ValueError:
                    print("⚠ please enter a number ⚠")
                except IndexError:
                    print("enter a valid number ❗")
            if user_answer == questions["answer"]:
                user_answers.append({user_answer : "✅"})
                score += 4
            else:
                user_answers.append({user_answer : "❌"})
        print(user_answers, f"\nyour score is {score}")
        db = Json.json_load("user_db.json")
        for users in db :
            if users["username"] == user["username"]:
                users["courses"]["python basic"] = score
        Json.json_save(db, "user_db.json")
        lesson_db = Json.json_load("python_basic.json")
        quiz_info = {user["username"]:user_answers,"score":score}
        lesson_db["quiz_answer"].append(quiz_info)
        Json.json_save(lesson_db, "python_basic.json")

    @staticmethod
    def take_advanced_python_quiz(user): # second quiz function
        quiz = Json.json_load("quiz.json")["Advanced Python"]
        score = 0
        user_answers = []
        for questions in quiz:
            print(questions["question"])
            for i in questions["options"]:
                print(i)
            while True:
                user_answer = input("Enter your answer => ")
                try:
                    user_answer = int(user_answer) - 1
                    user_answer = questions["options"][user_answer]
                    break
                except ValueError:
                    print("please enter a number ❗")
                except IndexError:
                    print("⚠ enter a valid number ⚠")
            if user_answer == questions["answer"]:
                user_answers.append({user_answer: "✅"})
                score += 4
            else:
                user_answers.append({user_answer: "❌"})
        print(user_answers, f"\nyour score is {score}")
        db = Json.json_load("user_db.json")
        for users in db:
            if users["username"] == user["username"]:
                users["courses"]["Advanced python"] = score
        Json.json_save(db, "user_db.json")
        lesson_db = Json.json_load("Advanced_python.json")
        quiz_info = {user["username"]:user_answers,"score":score}
        lesson_db["quiz_answer"].append(quiz_info)
        Json.json_save(lesson_db, "Advanced_python.json")

# class for main menu
class Main:

    @staticmethod
    def main_menu(): # main menu
        while True:
            user_input = input("What do you want to do ?\n1) 🔰sign up\n2) 🔰login\n3) 🔰forget password\n4) 🔰exit\n")
            print("")
            print("*" * 40)
            print("")
            if user_input == "1":
                SignUp.sign_up()
            elif user_input == "2":
                user_logged_in, user = Login.login()
                print("")
                print("*" * 40)
                print("")
                Main.login_menu(user_logged_in,user)
            elif user_input == "3":
                Login.forget_password()
            elif user_input == "4":
                print("bye 👋")
                break
            else:
                print("❗ please enter a valid number ❗")
            print("")
            print("*" * 40)
            print("")

    @staticmethod
    def login_menu(user_logged_in, user):
        if user_logged_in:
            print(f"you have successfully logged in '{user["username"]}'")
        while user_logged_in:
            db = Json.json_load("user_db.json")
            for users in db:
                if users["username"] == user["username"]:
                    user = users
            user_input2 = input("what do you want to do ?\n1) 🔸taking course\n2) 🔸starting exam\n"
                                "3) 🔸logout\n")
            print("")
            print("*" * 40)
            print("")
            if user_input2 == "1":
                Taking_course.take_course(user)
            elif user_input2 == "2":
                while True:
                    user_take = input("which quiz do you want to take?\n1) 💠python\n2) 💠Advanced python\n3) 💠back\n")
                    if user_take == "1":
                        in_course = Json.json_load("python_basic.json")
                        if user["username"] in in_course["students"]:
                            if user["courses"]["python basic"] == "NA":
                                Taking_course.take_python_quiz(user)
                                break
                                print("")
                                print("*" * 40)
                                print("")
                            else:
                                print("‼ you have already entered this quiz ‼")
                        else:
                            print("❌ you did not signed for this exam ❌")
                    elif user_take == "2":
                        in_course = Json.json_load("Advanced_python.json")
                        if user["username"] in in_course["students"]:
                            if user["courses"]["Advanced python"] == "NA":
                                Taking_course.take_advanced_python_quiz(user)
                            else:
                                print("‼ you have already entered this quiz ‼")
                        else:
                            print("❌ you did not signed for this exam ❌")
                    elif user_take == "3":
                        break
                    else:
                        print("❗ wrong input ❗")

            elif user_input2 == "3":
                user_logged_in = False
            else:
                print("❗ please enter a valid number ❗")
Main.main_menu()