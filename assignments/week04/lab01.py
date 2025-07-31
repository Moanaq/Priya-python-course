def personal_info_manager():
    # Create initial person tuple
    person = ("Pupea", 19, "Bangkok", "Thailand")  # name, age, city, country
    hobbies = []
    

    print("1. Display into, 2. Add hobby, 3. Remove Hobby, 4. Edit age, 5. Exit")
    choice = input("What do you want to do?: ")

    if choice == "1":
        print("Name: ",person[0])
        print("Age: ",person[1])
        print("City: ",person[2])
        print("Country: ",person[3])
        print("Honnies: ",hobbies)

    elif choice == "2":
        hobby = input("insert new hobbies : ")
        hobbies.append(hobby)

    elif choice == "3":
        del hobbies[0]

    elif choice == "4":
        age = input("Insert new age: ")
        person_list = list(person)
        person[1] = age
        person = tuple(person_list)

    elif choice == "5":
        exit(0)

if __name__ == "__main__":
    personal_info_manager()