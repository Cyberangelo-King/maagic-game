import time as t

def w1():
    input("Press Enter to continue...")
    print("\n")

def y2():
    print("""
    ╔════════════════════════════════════════════╗
    ║  Welcome to Angelo's Magical Tricks Show!  ║
    ║       Prepare to be amazed and amused!     ║
    ╚════════════════════════════════════════════╝
    """)
    t.sleep(1)

def u3():
    print("""
    ╔════════════════════════════════════╗
    ║      Choose a Trick from Angelo:   ║
    ║ 1. Think of a Number Trick         ║
    ║ 2. 4-Digit Prediction Trick        ║
    ║ 3. Fortune Teller Trick            ║
    ║ 4. Birthday Trick                  ║
    ║ 5. Exit                            ║
    ╚════════════════════════════════════╝
    """)

def s4():
    try:
        print("Think of a number between 1 and 10. No peeking!")
        w1()
        # *****BUNNY*****
        print("Multiply it by 9. Don't worry, you won't need a calculator for this!")
        w1()
        # *****RABBIT*****
        print("If the result is a two-digit number, add the digits together. Math is fun, right?")
        w1()
        # *****Darlynn*****
        print("Subtract 5 from the result. Almost there, I promise!")
        w1()
        # *****HOPPING*****
        print("Now, find the letter corresponding to the final number (A=1, B=2, ..., Z=26). I hope it's not 'X'!")
        w1()
        # *****C--*****
        print("Think of a country starting with that letter. Remember, it's not 'Xanadu'.")
        w1()
        # *****OYAL*****
        print("Think of an animal starting with the second letter of the country's name. Please, no unicorns!")
        w1()
        # *****My exes*****
        print("You are thinking of Denmark and an Elephant! Or maybe a Dingo in Denmark?")
        w1()
    except Exception as a:
        print(f"An error occurred: {a}. Must be those pesky unicorns again.")
        w1()

def r5():
    try:
        print("Think of any four-digit number. No, 1234 is too obvious!")
        w1()
        # ================
        print("Reverse the digits of this number. Bet you didn't see that one coming!")
        w1()
        # ================
        print("Subtract the smaller number from the larger number. Easy-peasy!")
        w1()
        # ================
        print("Reverse the digits of the result. Time to put your math hat on again!")
        w1()
        # ================
        print("Add this reversed number to the result of the subtraction. Just a little more math magic.")
        w1()
        # ================
        print("The final answer is always 1089! Aren't numbers just magical?")
        w1()
    except Exception as b:
        print(f"An error occurred: {b}. Looks like my magic wand needs new batteries.")
        w1()

def q6():
    try:
        print("Choose a number between 1 and 10. Any number, Don't tell me tho!")
        w1()
        # *****shediva*****
        print("Multiply the number by 2. Double the trouble!")
        w1()
        # *****iyan and Egusi*****
        print("Add 8 to the result. It's getting exciting now!")
        w1()
        # *****CARROT*****
        print("Divide by 2. Halve the fun!")
        w1()
        # *****i prolly need a gf at this moment*****
        print("Subtract the original number from the result. Almost there, magician in the making!")
        w1()
        # *****This is just me being jobless*****
        print("The final result is always 4! Because 4 is the magic number, didn't you know?")
        w1()
    except Exception as c:
        print(f"An error occurred: {c}. Must be those mischievous magic goblins!")
        w1()

def p7():
    try:
        print("Write down the number of the month you were born (e.g., January=1, February=2, etc.). No cheating!")
        w1()
        # ################
        print("Multiply this number by 5. Easy, right?")
        w1()
        # ################
        print("Add 6 to the result. This is going somewhere, trust me.")
        w1()
        # ################
        print("Multiply the result by 4. Feeling like a math wizard yet?")
        w1()
        # ################
        print("Add 9. Hang in there, you're doing great!")
        w1()
        # ################
        print("Multiply the result by 5. Almost done, promise!")
        w1()
        # ################
        print("Add the day of the month you were born. Hope you remembered your birthday!")
        w1()
        # ################
        print("Subtract 205 from the result. Phew, almost there!")
        w1()
        # ################
        print("The final number will be in the format MMDD (month and day). Magic, right?")
        w1()
    except Exception as d:
        print(f"An error occurred: {d}. Did someone say abracadabra?")
        w1()

def o8():
    y2()
    while True:
        u3()
        m = input("Enter the number of your choice: ")
        
        if m == "1":
            s4()
        elif m == "2":
            r5()
        elif m == "3":
            q6()
        elif m == "4":
            p7()
        elif m == "5":
            print("Thank you for playing Angelo's Magical Tricks Game! Goodbye and stay magical!")
            break
        else:
            print("Invalid choice. Please try again. The magic awaits!")
        
        print("\nReturning to main menu...\n")
        w1()

if __name__ == "__main__":
    o8()
