some_text = "The test"

def lang(text):
    english = 0
    french = 0
    for letter in text:
        if letter == "s" or letter =="S":
            french = french +1
        elif letter.lower == "t":
            english = english +1
    if  french >= english:
        print("French")
    else:
        print("English")
