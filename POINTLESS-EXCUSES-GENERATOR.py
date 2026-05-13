import random

names = ["My dog", "My cat", "The neighbor's son", "My cousin"]
verbs = ["ate the", "destroyed the", "stole the", "set fire to the"]
things = ["my homework.", "my document.", "my appointment.", "my work."]

print("Pointless Excuses Generator")
print()

running = True

while running:
  print("1 - Generate excuse")
  print("2 - Exit")
  print()
  try:
    choice = int(input("Enter your choice:"))
    print()
    if choice == 1:
     random0 = random.randint(0, 5)
     random1 = random.randint(0, 3)
     random2 = random.randint(0, 3)
     random3 = random.randint(0, 3)
     random4 = random.randint(0, 100)
     if random0 == 1:
      random5 = random.randint(0, 2)
      if random5 == 0:
        print("Special Excuse 1/3: The Death Star destroyed my car, so I couldn't come to work.")
        print()
        print("Credibility: 100%")
        print()
        print("Response: May the Force be with you!")
        print()
      elif random5 == 1:
        print("Special Excuse 2/3: Superman threw the bus I was on at a villain, so I was late.")
        print()
        print("Credibility: 100%")
        print()
        print("Response: For Truth, Justice, and a Better Tomorrow!")
        print()
      else:
        print("Special Excuse 3/3: I was called to fight Lord Voldemort, so I'll have to miss a few days of work.")
        print()
        print("Credibility: 100%")
        print()
        print("Response: It's leviOsa, not levioSA!")
        print()
     else:
      print(names[random1], verbs[random2], things[random3])
      print()
      print(f"Excuse credibility: {random4}%")
      print()
      if random4 < 30:
       print("Response: Stop lying!")
      elif random4 < 70:
       print("Response: Yeah, right...")
      else:
       print("Response: Seriously?! I'm so sorry!")
      print()
    elif choice == 2:
     running = False
     print("Thanks for using the system!")
    else:
      print("Invalid digit.")
  except ValueError:
    print("Invalid digit.")
    print()
