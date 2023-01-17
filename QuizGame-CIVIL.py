print("Welcome To Our CIVIL Quiz")

playing = input("Do You Want To Play?\n")

if playing.lower() !="yes":
    quit()

print("Okay! Let's Play:)")
score=0
answer=input("Who is the father of civil engineering?\nOptions\n(a)Othmar Ammann\n(b)Braden Allenby\n(c)John Smeaton\n(d)John Wolfe Ambrose\nEnter Your Option: ")
if answer.lower()=="c":
    print('Exactly! Keep Going....')
    score+=1
else:
    print("Actually,I don't Think....")
answer=input("What is the full form of TMT bars?\nOptions\n(a)Thermo Modified Treated\n(b)Thermo Mechanically Treated\n(c)Thermal Mechanic Twisted\n(d)Thermo Mechanically Twisted\nEnter Your Option: ")
if answer.lower()=="b":
    print('Absolutely!!!!')
    score+=1
else:
    print("Oops! That's Not Quite Right....")
answer=input("Corrugated sheets are also reffered to as?\nOptions\n(a)CS Sheets\n(b)CI Sheets\n(c)GC Sheets\n(d)GI Sheets\nEnter Your Option: ")
if answer.lower()=="d":
    print('You are Quite Right!!!!')
    score+=1
else:
    print("Oh! No,You're Mistaken....")
answer=input("Flat Iron Bars are used generally for:\nOptions\n(a)R.C.C\n(b)Grill work\n(c)Roofing\n(d)Truss\nEnter Your Option: ")
if answer.lower()=="b":
    print('Wow!You Got it....')
    score+=1
else:
    print("No,You've Got it Wrong....")
answer=input("Who is the first Civil Engineer in India?\noptions\n(a)T.G.Sitharam\n(b)Munirathna Anandakrishnan\n(c)G.V.Loganathan\n(d)Mokshagundam Visvesvaraya\nEnter Your Option: ")
if answer.lower()=="d":
    print("That's Spot On!!!!")
    score+=1
else:
    print("I don't Think So....")
if score<3:
    print("Good Try!!")
if score==3:
    print("You're on the right track,Keep Going....")
if score==4:
    print("You're one step closer to Victory....")
if score==5:
    print("Excellent!!!! You did that very well....")


print("You Got " +str(score)+ " Scores")
