# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import random
from colorama import Fore

#function to retrieve random word from dictionary. List of available word is being sent as argument
def retrieve_word(data):
    all_words = list(data.keys())
    while True:
        word = random.choice(all_words)
        return word

#function to shuffle word. Use random and list functions to shuffle word in string
def shuffle_word(word):
     return (''.join(random.sample(word, len(word))))


def main():
    filename = 'level_dictionary.json'
    file = open(filename)
    data = json.load(file)
    level = 1
    inter_level=1
    retry_count=0
    temp_list=[]
    word=""
    hint=""


    while level < 4:
        list_words =data[str(level)] # load json data of respective level
        word = retrieve_word(list_words)  # retrieve random word from json data
        hint = list_words[word] # retrieve hint frm json file

        while True :
            if word not in temp_list:
                break;
            else:
                word = retrieve_word(list_words)  # retrieve random word from json data
                hint = list_words[word]  # retrieve hint frm json file
        temp_list.append(word)
        shuffle = shuffle_word(word)

        print(Fore.RESET +'*'*100)
        print(Fore.LIGHTMAGENTA_EX +f"Level {level}")
        print(Fore.RESET +'*' * 100)
        print(Fore.RESET+f"Challange => {shuffle}  \t\t Hint => {hint}")
        #print (word)
        while retry_count < 3:
            user_input = input(Fore.RESET+"Enter response : ")
            if user_input.lower() == word:
                print(Fore.GREEN  + f"**************CORRECT********")
                break;
            else:
                retry_count = retry_count + 1
                print(Fore.RED +  f"**************TRY AGAIN*******. Retries left {3-retry_count}")
        if retry_count > 2 :
            print(Fore.LIGHTGREEN_EX + f"Correct answer is  {word}")
            break;
        else:
            flag_continue = input(Fore.RESET +"Do you want to continue (y/n) :")
            if (flag_continue.strip().lower() == 'y'):
                retry_count=0
                inter_level = inter_level+1
                if (inter_level > 3):
                    print(Fore.LIGHTMAGENTA_EX + f"-------------Next Level-------------")
                    level = level + 1
                    inter_level=1
                    temp_list=[]
            else:
                break;

    if level == 4:
        print(Fore.RESET+'*'*100)
        print(Fore.LIGHTMAGENTA_EX + "Congratulations !! You have completed all levels.")

main()

