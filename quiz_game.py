print("Welcome to 'Guess the footballer!' ")

playing = input("Do you want to play?  ")

if playing.upper() != "YES":
    quit()

print ("OKAY!")

answer = input("Who is kown as the G.O.A.T in football ?  ")

if answer.upper() == "MESSI":
    print("Amazing!")
else :
    print("You need to see the Doctor ASAP!  ")
