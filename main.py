#student record
#details of the record: student number, name, contact number, section, email address
from os import system
from time import sleep
import sys
import re

#welcome page of the system
def WelcomePage():
    system('cls')

    print("===============Python Student record===============\n\n\n")
    print("(a) Add Record\t\t\t(d) View Record\n")
    print("(b) Edit Record\t\t\t(e) Load Record\n")
    print("(c) Delete Record\t\t(f) View Log\n\n")

    choice = input("Enter your choice: (Press q to quit):\t ")

    if choice == 'a' or choice =='A':
        AddRecord()

    elif choice == 'b' or choice == 'B':
        EditRecord()

    elif choice == 'c' or choice =='C':
        DeleteRecord()

    elif choice == 'd' or choice == 'D':
        ViewRecord()

    elif choice == 'e' or choice == 'E':
        LoadRecord()

    elif choice == 'f' or choice == 'F':
        Logs()

    elif choice == 'q' or choice =='Q':
        system('cls')
        quit()
    else:
        system('cls')
        print("\n\n\n\n\t\t!!!   Invalid input, try again.")
        sleep(1)
        WelcomePage()


#===================================================
#===============options from the menu===============
def AddRecord():
    system('cls')
    while True:
        stud_num=input("\n\t\tEnter student number: ")
#print length of the input
        print(len(stud_num))

#data type of input
        print(type(stud_num))

#initialize
        list_comparator=[]

        count=0
        for i in stud_num:
            count=count+1

        sample=re.findall('[^a-zA-Z]',stud_num)
        print(sample)
        print(list_comparator)

        if list_comparator == re.findall('[^a-zA-Z][0-9]\S',stud_num):
            if count != 10:
                print("\t\t Invalid input, try again.")
                sleep(1)
                system('cls')
                continue
        else:
            break


    while True:
        system('cls')
        surname=input("\n\t\tEnter your Surname: ")
        break

    while True:
        system('cls')
        given_name=input("\n\t\tEnter your Given Name: ")
        break

    while True:
        system('cls')
        middle_name=input("\n\t\tEnter your Middle Name: ")
        break

    while True:
        system('cls')
        suffix=input("\n\t\tIf any, enter your suffix name (X if none): ")
        break

    while True:
        system('cls')
        mobile=input("\n\t\tEnter your mobile number: (X if none): ")
        break

    while True:
        system('cls')
        section=input("\n\t\tEnter your Section: ")
        break

    while True:
        system('cls')
        email=input("\n\t\tEnter your primary email address: ")
        break

    sleep(1)

#===============confirmation of details before adding a new user===============
    while True:
        system('cls')
        print("\t\tNew student entry:")
        print("\n\nStudent Number: ",stud_num)
        print("\nSurname: ",surname)
        print("\nGiven Name: ",given_name)
        print("\nMiddle name: ",middle_name)
        print("\nSuffix: ",suffix)
        print("\nMobile number: ",mobile)
        print("\nSection: ",section)
        print("\nPrimary email address: ",email)

        sure=input("\n\nAre you sure you want to save changes? (Y/N): ")
        if sure == 'N' or sure =='n':
            AddRecord()
        elif sure == 'Y' or sure =='y':
            system('cls')
            print("\n\n\n\n\t\tInformation was saved successfully!")
            sleep(1.5)
            WelcomePage()
        else:
            system('cls')
            print("\n\n\n\n\t\t!!!   Invalid input, try again.")
            sleep(1)
            continue

#===============edit record===============
def EditRecord():
    system('cls')
    print('edit')
    sleep(1)
    WelcomePage()

#===============delete record===============
def DeleteRecord():
    system('cls')
    print('delete')
    sleep(1)
    WelcomePage()

#===============with sort and search functionality, searh by student number or by name===============
def ViewRecord():
    system('cls')
    print('view')
    sleep(1)
    WelcomePage()

#===============format of the batch file - student number===============
def LoadRecord():
    system('cls')
    print('load')
    sleep(1)
    WelcomePage()

#===============logs===============
def Logs():
    system('cls')
    print('logs')
    sleep(1)
    WelcomePage()

#==========================MAIN SCRIPT starts here====================================
WelcomePage()
