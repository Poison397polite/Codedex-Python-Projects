"""Program the translate morse code to english and vise versa"""

from Clear import clear

english2Morse = {
    "A" : "• —", "B" : "— • • •", "C" : "— • — •", "D" : "— • •", "E" : "•", "F" : "• • — •",
    "G" : "— — •", "H" : "• • • •", "I" : "• •", "J" : "• — — —", "K" : "— • —", "L" : "• — • •",
    "M" : "— —", "N" : "— •", "O" : "— — —", "P" : "• — — •", "Q" : "— — • —", "R" : "• — •",
    "S" : "• • •", "T" : "—", "U" : "• • —", "V" : "• • • —", "W" : "• — —", "X" : "— • • —",
    "Y" : "— • — —", "Z" : "— — • •", "0" : "— — — — —", "1" : "• — — — —", "2" : "• • — — —", "3" : "• • • — —",
    "4" : "• • • • —", "5" : "• • • • •", "6" : "— • • • •", "7" : "— — • • •", "8" : "— — — • •", "9" : "— — — — •"
}

morse2English = {
    ".-" : "A", "-..." : "B", "-.-." : "C", "-.." : "D", "." : "E", "..-." : "F",
    "--." : "G", "...." : "H", ".." : "I", ".---" : "J", "-.-" : "K", ".-.." : "L",
    "--" : "M", "-." : "N", "---" : "O", ".--." : "P", "--.-" : "Q", ".-." : "R",
    "..." : "S", "-" : "T", "..-" : "U", "...-" : "V", ".--" : "W", "-..-" : "X",
    "-.--" : "Y", "--.." : "Z", "-----" : "0", ".----" : "1", "..---" : "2", "...--" : "3",
    "....-" : "4", "....." : "5", "-...." : "6", "--..." : "7", "---.." : "8", "----." : "9", "/" : " "
}

def printTitleAndLetters():
    """Prints title and letters"""
    print("----------------------------------------------------")
    print("               Morse code translator                ")
    print("        Translate from morse code to english        ")
    print("              or english to morse code              ")
    for key, value in english2Morse.items():
        line = f"{key}  =  {value}"
        print(f"{line:^52}")
    print("    To translate from morse code to english use     ")
    print(".(period) for the dots and -(hyphen) for the dashes ")
    print("  with out any spaces between the .'s and the -'s   ")
    print("       Enter 'space/space' between each word        ")
    print("----------------------------------------------------")

printTitleAndLetters()

while True:
    englishOrMorse = input("\nDo you want to translate english to morse code(a) or vise versa(b): ").lower()

    if englishOrMorse == "a":
        englishText = input("\nEnter the english text: ").upper().strip().split()

        for word in englishText:
            for letter in word:
                print(english2Morse[letter], end = "   ")
            print(end = "    ")

    elif englishOrMorse == "b":
        while True:
            try:
                morseText = input("\nEnter the morse code: ").strip().split()
                for morse in morseText:
                    print(morse2English[morse], end = "")
                break
            except KeyError:
                print("\nInvalid morse code entered try again.")

    else:
        print("\nInvalid  input. Enter a or b")
        continue

    if input("\nTranslate again? (y/n): ").lower() == "y":
        clear()
        printTitleAndLetters()
    else:
        break

print("\nThanks for using!")
