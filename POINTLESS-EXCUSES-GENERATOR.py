import random

subjects = ["My dog", "My cat", "My neighbor's son", "My cousin"]
verbs = ["ate", "destroyed", "stole", "set fire to"]
objects = ["my homework.", "my document.", "my appointment.", "my work."]

print("Pointless Excuses Generator")
print()

running = True

while running:
    print("1 - Generate excuse")
    print("2 - Exit")
    print()
    try:
        choice = int(input("Type your choice: "))
        print()
        if choice == 1:
            random1 = random.randint(0, 3)
            random2 = random.randint(0, 3)
            random3 = random.randint(0, 3)
            random4 = random.randint(0, 100)
            print(subjects[random1], verbs[random2], objects[random3])
            print()
            print(f"Excuse credibility: {random4}%")
            print()
            if random4 < 30:
                print("Response: Stop lying!")
            elif random4 < 70:
                print("Response: Yeah, sure...")
            else:
                print("Response: Really?! I'm so sorry!")
            print()
        elif choice == 2:
            running = False
            print("Thanks for using the system!")
        else:
            print("Invalid input.")
    except ValueError:
        print("Invalid input.")
        print()
