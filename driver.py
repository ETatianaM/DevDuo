#import our matcher
from user import User

#this is where we will store our pool of workers
pool = []

#in a real application we would have it be empty to start, and users would add to the pool over time
#in this scenario to demonstrate use cases we have filled it with multiple users 

#adding users to our pool
user1 = User("Alice", 1, "MW", "Project A", False)
user2 = User("Bob", 8, "MTuTh", "Project B", False)
user3 = User("Charlie", 2, "MWTh", "Project C", False)
user4 = User("David", 5, "TuTh", "Project D", False)
user5 = User("Eva", 4, "MW", "Project A", False)
user6 = User("Jose", 28, "MTuTh", "Project B", False)
user7 = User("Grace", 7, "MWTh", "Project C", False)
user8 = User("Mia", 3, "TuTh", "Project D", False)
user9 = User("Ivy", 10, "MW", "Project A", False)
user10 = User("Jack", 1, "MTuTh", "Project B", False)
#adding them to list
pool = [user1, user2, user3, user4, user5, user6, user7, user8, user9, user10]

#function to create a profile from user input
def create_profile():
    name = input("Name: ")
    experience = int(input("Years of experience: "))
    availability = input("Enter availability (Days ie 'MW', 'TuThF', etc): ")
    project = input("Enter project: ")
    

    #creating a user profile
    return User(name, experience, availability, project, False)

#main 'runner' of our program, while loop to keep asking for users to input
#this is a prototype, but this would be run with the front end and instead of a while loop it would update when 
#a user create a profile etc. it would just be a function to match and we wouldnt need the while

while True:
    add_user = input("Would you like to create a profile to match? (y/n): ").lower()

    if add_user == "n":
        print("Thank you for using the Pair Programming Matcher Tool!")
        break
    elif add_user == "y":
        new_user = create_profile()
    else:
        print("Invalid response, please enter 'y or 'n")
    
    #after creating profile we want to see what the user wants out of this matcher
    #notice that availibility is important as we cannot match people who are not available on the same days

    #checking if the user wants to be added to pool, or to get a match immediately (if possible)
    check = input("Do you want to immediately find a match? (y/n): ")
    if check == "n":
        print("You have successfully been added to pool!")
        new_user.set_now(False)
        #add use to pool
        pool.append(new_user)
    elif check == "y":
        new_user.set_now(True)
        print("You are looking for a match: Choose one of the number options below to describe your situation")
        print("(1) Match with a more experienced programmer for mentorship")
        print("(2) Match with a programmer with similar levels of experience")
        print("(3) Match with a programmer on a specific project")
        #these prints will display our use cases, and as we are just a prototype we can add more cases at will
        print("(4) Other match")
        found_match = False
        selected_match = None
        choice = input("Select your option: ")
        if choice == "1":
            for u in pool:
                if u.get_experience() > 5 and u.get_availability() == new_user.get_availability():
                    selected_match = u
                    found_match = True
                    break
            if found_match:
                print("We found a match!")
                print(f"We are matching you with {selected_match.get_name()}, who was {selected_match.get_experience()} years of experience.")
                pool.remove(selected_match)
            else:
                print("No match right now... adding to pool")
                #since no match but match now is true they will get priority in "Other match"
                pool.append(new_user)
        #finds people within two years of experience
        elif choice == "2":
            for u in pool:
                if u.get_experience() >= new_user.get_experience() - 2 and u.get_experience() <= new_user.get_experience() + 2 and u.get_availability() == new_user.get_availability():
                    selected_match = u
                    found_match = True
                    break
            if found_match:
                print("We found a match!")
                print(f"We are matching you with {selected_match.get_name()}, who was {selected_match.get_experience()} years of experience.")
                pool.remove(selected_match)
            else:
                print("No match right now... adding to pool")
                #since no match but match now is true they will get priority in "Other match"
                pool.append(new_user)
        elif choice == "3":
            for u in pool:
                if u.get_project() == new_user.get_project() and u.get_availability() == new_user.get_availability():
                    selected_match = u
                    found_match = True
                    break
            if found_match:
                print("We found a match!")
                print(f"We are matching you with {selected_match.get_name()}, who is working on the same project.")
                pool.remove(selected_match)
            else:
                print("No match right now... adding to pool")
                #since no match but match now is true they will get priority in "Other match"
                pool.append(new_user)
        elif choice == "4":
            for u in pool:
                #first check the "priority" matches
                if u.get_now == True and u.get_availability() == new_user.get_availability():
                    selected_match = u
                    found_match = True
                    break
            if found_match:
                print("We found a match!")
                print(f"We are matching you with {selected_match.get_name()}, who is looking for a match.")
                pool.remove(selected_match)
            else:
                if u.get_availability() == new_user.get_availability():
                    selected_match = u
                    found_match = True
                    break
                if found_match:
                    print("We found a match!")
                    print(f"We are matching you with {selected_match.get_name()}.")
                    pool.remove(selected_match)
                else:
                    print("No match right now... adding to pool")
                    pool.append(new_user) #still add to pool
                

            
    #for extra spacing
    print("")
    print("")