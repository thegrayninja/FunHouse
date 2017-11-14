##github.com/thegrayninja

#English Treasure Map
#To help find letters in words easily


#You'll need to provide an external word list. I got mine from
#https://github.com/dwyl/english-words/blob/master/words_dictionary.json
#this listing is saved as json, saved to a variable english_words, in the
#file words_dictionary.py


#version 1.0

import sys
from words_dictionary import english_words

##the following two callouts are for the definition portion.
##remove if you cannot install BeautifulSoup
from urllib.request import urlopen #as uReq
from bs4 import BeautifulSoup #as soup



#TODO Cleanup code!



def Header():
    print("""
    :::::::::::''  ''::'      '::::::  `:::::::::::::'.:::::::::::::::
    :::::::::' :. :  :         ::::::  :::::::::::.:::':::::::::::::::
    ::::::::::  :   :::.       :::::::::::::..::::'     :::: : :::::::
    ::::::::    :':  "::'     '"::::::::::::: :'           '' ':::::::
    :'        : '   :  ::    .::::::::'    '                        .:
    :               :  .:: .::. ::::'                              :::
    :. .,.        :::  ':::::::::::.: '                      .:...::::
    :::::::.      '     .::::::: '''                         :: :::::.
    ::::::::            ':::::::::  '',            '    '   .:::::::::
    ::::::::.        :::::::::::: '':,:   '    :         ''' :::::::::
    ::::::::::      ::::::::::::'                        :::::::::::::
    : .::::::::.   .:''::::::::    '         ::   :   '::.::::::::::::
    :::::::::::::::. '  '::::::.  '  '     :::::.:.:.:.:.:::::::::::::
    :::::::::::::::: :     ':::::::::   ' ,:::::::::: : :.:'::::::::::
    ::::::::::::::::: '     :::::::::   . :'::::::::::::::' ':::::::::
    ::::::::::::::::::''   :::::::::: :' : ,:::::::::::'      ':::::::
    :::::::::::::::::'   .::::::::::::  ::::::::::::::::       :::::::
    :::::::::::::::::. .::::::::::::::::::::::::::::::::::::.'::::::::
    :::::::::::::::::' :::::::::::::::::::::::::::::::::::::::::::::::
    ::::::::::::::::::.:::::::::::::::::::::::::::::::::::::::::::::::
    """)


def HelpMenu():
    print("\n\n\tEnglish Treasure Map - HELP MENU\n")
    print("Example:")
    print("\t.\\EnglishTreasureMap.py people")
    print("\t.\\EnglishTreasureMap.py -l people")
    print("\t.\\EnglishTreasureMap.py -d uranus")
    print("\t.\\EnglishTreasureMap.py -s paste -e s -c t -i p")
    print("\t.\\EnglishTreasureMap.py <option> {search_term}\tnote: option not required\n\n")
    print("Options:\n")
    print("     -a     Return Words that match all letters provided.")
    print("     -c     Must return a specified letter")
    print("     -d     Lookup up the definition of a word (ugly formatting, sorry)")
    print("     -e     Matches words that end with this letter. Only one letter allowed.")
    print("     -h     This help menu.")
    print("     -i     Ignore this letter. Do not return words that contain this letter.\n              Must be used with another switch/option")
    print("     -l     Match words equal size or larger. Letter count may not be exact.")
    print("     -s     Match words smaller or equal size. Letter count may not be exact.")
    print("     -x     Return words that can be used with the provided letters. (Think Scrabble)")
    print("\n\n")
    return(0)



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


def SearchDictionaryExact(UserLetters):
    WordList = []
    x = {}

    for i in UserLetters:
        if i not in x:
            x[i] = 1
        else:
            x[i] += 1

    for DictionaryWord in english_words:
        LettersExist = []
        if len(UserLetters) >= len(DictionaryWord):
            for Letter in DictionaryWord:
                if Letter in UserLetters:
                    LettersExist.append(Letter)
                else:
                    LettersExist.append(99)

            if 99 not in LettersExist:
                y = {}
                for Letter in DictionaryWord:
                    if Letter not in y:
                        y[Letter] = 1
                    else:
                        y[Letter] += 1

                ValidWord = "Yes"
                for Letter in DictionaryWord:
                    if y.get(Letter) > x.get(Letter):
                        ValidWord = "No"

                if ValidWord == "Yes":
                        WordList.append(DictionaryWord)

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





def DefineWord(UserWord):
    #TODO lookup word
    URL = "http://www.dictionary.com/browse/%s" % UserWord
    print("\nWe shall define %s.\n" % (UserWord))
    uClient = urlopen(URL)
    pageContent = uClient.read()
    uClient.close()

    #html parsing
    Soup = BeautifulSoup(pageContent, "html.parser")


    for i in Soup.find_all("div", {"class": "def-content"}):
        #print(Soup.find("div", {"class": "def-content"}))
        if "None" not in i:
            print((i.text).strip())




    return(UserWord)


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


def MustContain(UserLetter, WordList):
    FinalWordList = []
    for Word in WordList:
        UserLetterCount = 0
        for i in Word:
            #print(i)
            if i == UserLetter:
                UserLetterCount += 1
        if UserLetterCount > 0:
            FinalWordList.append(Word)
    return(FinalWordList)


def TreasureMap():
    WordList = []
    try:
        if '-a' in sys.argv[1]:
            WordList = SearchDictionaryAll(sys.argv[2])
        elif '-d' in sys.argv[1]:
            DefineWord(sys.argv[2])
        elif '-e' in sys.argv[1]:
            TempWordList = SearchDictionaryLarger(sys.argv[2])
            WordList = (WordEndsWith(sys.argv[2], TempWordList))
        elif '-h' in sys.argv[1]:
            HelpMenu()
        elif sys.argv[1] == '-l':
            WordList = SearchDictionaryLarger(sys.argv[2])
        elif '-s' in sys.argv[1]:
            WordList = SearchDictionarySmaller(sys.argv[2])
        elif '-x' in sys.argv[1]:
            WordList = SearchDictionaryExact(sys.argv[2])
        else:
            HelpMenu()
    except:
        HelpMenu()

    try:
        SecondArgument = sys.argv[3]
        if SecondArgument == '-i':
            WordList = (IgnoreLetter(sys.argv[4], WordList))
        elif SecondArgument == '-e':
            WordList = (WordEndsWith(sys.argv[4], WordList))
        elif SecondArgument == '-c':
            #print("fuck")
            WordList = (MustContain(sys.argv[4], WordList))
    except:
        SecondArgument = "None"

    try:
        ThirdArgument = sys.argv[5]
        if ThirdArgument == '-i':
            WordList = (IgnoreLetter(sys.argv[6], WordList))
        elif ThirdArgument == '-e':
            WordList = (WordEndsWith(sys.argv[6], WordList))
        elif ThirdArgument == '-c':
            WordList = (MustContain(sys.argv[6], WordList))
    except:
        ThirdArgument = "None"

    try:
        FourthArgument = sys.argv[7]
        if FourthArgument == '-i':
            WordList = (IgnoreLetter(sys.argv[8], WordList))
        elif FourthArgument == '-e':
            WordList = (WordEndsWith(sys.argv[8], WordList))
        elif FourthArgument == '-c':
            WordList = (MustContain(sys.argv[8], WordList))
    except:
        ThirdArgument = "None"



    for Word in WordList:
        print(Word)
    return 0


def main():
    print("from the desk of grayninja\n\n")
    #Header()
    print("Welcome to the English Treasure Map")
    TreasureMap()




if __name__ == main():
    main()
