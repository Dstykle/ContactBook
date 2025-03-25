# list to keep all contacts when code is run
list_of_contacts = []

# class to store in contact and make it into a call.
# Functions can be added for more actions
class Contacts:
    def __init__(self, first_name, last_name, number, address, email):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.address = address
        self.email = email
        if self.first_name == "":
            self.name = "None entered"
        if self.number == "":
            self.number = "None entered"
        if self.address == "":
            self.address = "None entered"
        if self.email == "":
            self.email = "None entered"

    def contact(self):
        print("\nAbout:" + self.first_name + "\n" + "Name: " + self.first_name, self.last_name + "\n" +
              "Number: " + self.number + "\n" + "Address: " + self.address +
              "\n" + "Email: " + self.email)


# Asking the user if they want to make a new contact
print("Welcome and thank you for using my Contact Book program\n")
new = input("Would you like to make a new contact? (yes/no): ")
if new.upper() == "YES":
    # record how many contacts they want to make
    while True:
        try:
            times = int(input("How many would you like to make? "))
        except ValueError:
            print("Enter in a positive integer")
            continue
        if times > 0:
            # Num will be used later on in code
            num = times
            break
        elif times < 0:
            print("Enter in a positive integer.")

    for i in range(times):
        # Below will be the code that takes the input of each of the parameters for the
        # class Contact and stores it in a list
        print(f"This will be your contact number {i+1}.\nIf you do not have the information asked leave it blank.")
        first_name = input("What is his/her first name? ")
        last_name = input("What is his/her last name? ")
        number = input("What is his/her number? ")
        address = input("What is his/her address? ")
        email = input("What is his/her email? ")
        # Printing out the information given to make sure the user does not want to make changes.
        print("\nFirst Name: " + first_name + "\nLast name: " + last_name + "\nNumber: " + number + "\nAddress: "
        + address + "\nEmail: " + email + "\n")
        restart = input("Would you like to re-enter/enter anything in? (yes/no) ")
        # If the user wants to fix something
        if restart.capitalize() == "Yes":
            while True:
                restart = input("When finished enter in done.\nWhat would you like to fix? ")
                if restart == "done" or restart == "Done":
                    break
                elif restart.capitalize() == "First name":
                    first_name = input("What is his/her first name? ")
                elif restart.capitalize() == "Last name":
                    last_name = input("What is his/her last name? ")
                elif restart.capitalize() == "Number":
                    number = input("What is his/her number? ")
                elif restart.capitalize() == "Address":
                    address = input("What is his/her address? ")
                elif restart.capitalize() == "Email":
                    email = input("What is his/her email? ")
                else:
                    print("Enter in a valid entry.")
                    continue
        else:
            pass

        # This will grab all of the information given and turn it into a contact
        list_of_contacts.append(Contacts(first_name=first_name,last_name=last_name,number=number,address=address,email=email))
        # We will store it in a text file to save this information
        contacts = open("Contacts.txt", "a+")
        contacts.write(
            "\nFirst Name: " + first_name + "\nLast name: " + last_name + "\nNumber: " + number + "\nAddress: "
            + address + "\nEmail: " + email + "\n")
        contacts.close()

    # Asking user if they want to view any information they just entered
    view = input("Would you like to view anyone's information? (yes/no): ")
    if view.capitalize() == "Yes":
        person = None
        # This code will ask the user which contact they would like to view and finishes when they enter done
        while person != "done":
            print("\nType in 'done' once you are done.")
            try:
                person = input("Who's information would you like to view? (answer in the number you entered "
                               "his/her information in)\nFor example I typed in Kobe's information "
                               "first then Leah's\n"
                               "I will type in 1 for Kobe and 2 for Leah\n"
                               "If you would like to view all then type in all. ")
                if person == "all":
                    # num comes in to get each index in the list of all contacts made in it.
                    num -= 1
                    while num != -1:
                        list_of_contacts[num].contact()
                        num -= 1
                    print("Your contacts have been recorded in the text document.\nThank you for using this contact book, see you later.")
                    break
                else:
                    person = int(person)
                    list_of_contacts[person-1].contact()
            # Catch any errors made when var person is being assigned its value
            except ValueError:
                print("Enter in a number.")
            except IndexError:
                print("Enter in a valid contact number.")
            except TypeError:
                print("Enter in a valid contact number")
    elif view.capitalize() == "No":
        print("Your contacts have been recorded in the text document.\nThank you for using this contact book, see you later.")

        pass
    else:
        print("Enter in a valid response.")
elif new.capitalize() == "No":
    print("Thank you for using this contact book, see you later.")
    exit()
else:
    print("Enter in a valid response.")
