##github.com/thegrayninja

#English Treasure Map
#To help find letters in words easily


#You'll need to provide an external word list. I got mine from
#https://github.com/dwyl/english-words/blob/master/words_dictionary.json,
#but it's missing firetruck..but I'm still grateful! :D
#this listing is saved as json, saved to a variable english_words, in the
#file words_dictionary.py


import sys
from words_dictionary import english_words


#TODO Print all letters that end in 'letter'
#TODO Add option to return definition (either google search, or save python with definitions)


def HelpMenu():
    print("\n\n\tEnglish Treasure Map - HELP MENU\n")
    print("Example:")
    print("\t.\\scrabble_help.py people")
    print("\t.\\scrabble_help.py -l people")
    print("\t.\\scrabble_help.py <option> {search_term}\tnote: option not required\n\n")
    print("Options:\n")
    print("     -a     Return Words that match all letters provided.")
    print("     -e     Matches words that end with this letter. Only one letter allowed.")
    print("     -h     This help menu.")
    print("     -i     Ignore this letter. Do not return words that contain this letter.\n              Must be used with another switch/option")
    print("     -l     Match words equal size or larger. Letter count may not be exact.")
    print("     -s     Match words smaller or equal size. Letter count may not be exact.")
    print("\n\n")
    sys.exit(0)



def SearchDictionaryAll(UserLetters):
    WordList = []
    for DictionaryWord in english_words:
        if len(UserLetters) == len(DictionaryWord):
            if sorted(UserLetters) == sorted(DictionaryWord):
               WordList.append(DictionaryWord)
            else:
                continue
        else:
            continue
    return (WordList)


def SearchDictionarySmaller(UserLetters):
    WordList = []
    for DictionaryWord in english_words:
        LettersExist = []
        if len(UserLetters) >= len(DictionaryWord):
            for Letter in DictionaryWord:
                if Letter in UserLetters:
                    LettersExist.append(Letter)
                else:
                    LettersExist.append(99)
            if 99 not in LettersExist:
                #TODO Don't print words that have extra letters than what the user provided. ie, pilot, tool
                WordList.append(DictionaryWord)
                continue
            else:
                continue

        else:
            continue

    return (WordList)



def SearchDictionaryLarger(UserLetters):
    WordList = []
    for DictionaryWord in english_words:
        LettersExist = []

        if len(UserLetters) <= len(DictionaryWord):
            for Letter in UserLetters:
                if Letter in DictionaryWord:
                    LettersExist.append(Letter)
                else:
                    LettersExist.append(99)
            if 99 not in LettersExist:
                #TODO Don't print words that have extra letters than what the user provided. ie, pilot, tool
                WordList.append(DictionaryWord)
                continue
            else:
                continue
        else:
            continue
    return (WordList)


def IgnoreLetter(UserLetter, WordList):
    FinalWordList = []
    for Word in WordList:
        if UserLetter not in Word:
            FinalWordList.append(Word)
        else:
            continue
    return(FinalWordList)


def WordEndsWith(UserLetter, WordList):
    FinalWordList = []
    for Word in WordList:
        LengthofWord = (len(Word) -1)
        if UserLetter == Word[LengthofWord]:
            FinalWordList.append(Word)
        else:
            continue
    return(FinalWordList)


def main():
    print("Welcome to the English Treasure Map")
    #NumberOfEnglishWords = (len(english_words))

    WordList = []
    try:

        if '-a' in sys.argv[1]:
            WordList = SearchDictionaryAll(sys.argv[2])
        elif '-s' in sys.argv[1]:
            WordList = SearchDictionarySmaller(sys.argv[2])
        elif '-l' in sys.argv[1]:
            WordList = SearchDictionaryLarger(sys.argv[2])
        elif '-h' or '?' in sys.argv[1]:
            HelpMenu()

        else:
            HelpMenu()
    except:
        HelpMenu()

    try:
        if '-i' in sys.argv[3]:
            WordList = (IgnoreLetter(sys.argv[4], WordList))
            #for Word in WordList:
            #    print(Word)
    except:
        print("")

    try:
        if '-e' in sys.argv[3]:
            WordList = (WordEndsWith(sys.argv[4], WordList))
    except:
        print("")

    try:
        if '-e' in sys.argv[5]:
            WordList = (WordEndsWith(sys.argv[6], WordList))
    except:
        print("")


    for Word in WordList:
        print(Word)
    return 0


if __name__ == main():
    main()
