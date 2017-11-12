#github.com/thegrayninja

import sys
from words_dictionary_small import english_words




#TODO Print all letters that end in 'letter'



#TODO Print all words that contain all or some of the provided letters, with except 'letter' option

#TODO Add option to return definition (either google search, or save python with definitions)


def HelpMenu():
    print("\n\n\tEnglish Treasure Map - HELP MENU\n")
    print("Example:")
    print("\t.\\scrabble_help.py people")
    print("\t.\\scrabble_help.py -l people")
    print("\t.\\scrabble_help.py <option> {search_term}\tnote: option not required\n\n")
    print("Options:\n")
    print("     -a     Return Words that match exact letters provided")
    print("     -h     This help menu")
    print("     -l     Match words equal size or larger. Letter count may not be exact.")
    print("     -m     Match words small or equal size. Letter count may not be exact.")
    print("\n\n")
    return 0




def SearchDictionaryExact(UserLetters):
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




def SearchDictionaryAtMost(UserLetters):
    WordList = []
    for DictionaryWord in english_words:
        LettersExist = []
        LetterCount = []
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



def SearchDictionaryAtLeast(UserLetters):
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


def ExcludeLetter(UserLetter, WordList):
    FinalWordList = []
    for Word in WordList:
        if UserLetter not in Word:
            FinalWordList.append(Word)
        else:
            continue
    return(FinalWordList)


def main():
    print("Welcome to the English Treasure Map")
    NumberOfEnglishWords = (len(english_words))
    #print("\n\nThere are currently {} words in the English Dictionary!".format(NumberOfEnglishWords))

    # TODO Make player add values by using ARGS
    #WordList = ["nothing", "queen", "sleep", "people", "apple"]
    try:

        if '-a' in sys.argv[1]:
            WordList = SearchDictionaryExact(sys.argv[2])
        elif '-m' in sys.argv[1]:
            WordList = SearchDictionaryAtMost(sys.argv[2])
        elif '-l' in sys.argv[1]:
            WordList = SearchDictionaryAtLeast(sys.argv[2])
        elif '-h' or '?' in sys.argv[1]:
            HelpMenu()



        else:
            HelpMenu()
    except:
        HelpMenu()

    try:
        if '-e' in sys.argv[3]:
            FinalWordList = (ExcludeLetter(sys.argv[4], WordList))
            for Word in FinalWordList:
                print(Word)
    except:
        for Word in WordList:
            print(Word)
    return 0







if __name__ == main():
    main()
