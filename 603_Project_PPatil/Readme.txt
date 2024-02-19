Name: Anagram
“A type of word game in which the letters are taken from one word, or group of words and rearranged in the other words”.
In other words, Anagram of a word is another word obtained by shuffling its letter.

Purpose: The basic idea of the project is to read a file that contains words pick a random word from the dictionary, shuffle it and ask the user to guess the correct word from its anagram.

Goal: Building an interactive game for user to play.

Description:

In the project there are two files 1) anagram.py which has all the program code and 2) .json file which has all the words and hint of the word saved.
We have imported modules in PyCharm – Json, random, colorama and Fore.
The program consists of three functions – retrieve_word, shuffle word and main ().
There are three levels in the game – first, second and third level. Every level has different set of dictionaries. All levels of dictionary have been defined in level_dictionary. Json. This is nothing nested Json of key value pair. Key denotes the word and value is the hint for the word.
Retrieve_word function: the retrieve_word function will retrieve random word from the dictionary with the hint.
Shuffle_word function: shuffle word function will get the word; it will shuffle the words in a string.
Program start with main (). It loads the entire dictionary in the “data”. Now program enters into while loop for the levels. The loop continues till level 3 or breaks if user max out the retry counts or voluntary decides to end the game.
For every level program goes through below steps. Program starts with level 1. It will load all the words for level 1 from the Json file. Then retrieve_word function will get a random word from those words. And hint will get its value. Now this word will be shuffled using shuffle_word function and presented to the player with the hint. User will have three chances to guess the correct word, if player is not able to give correct answer in 3 tries the game ends for the player. The player will receive correct answer and game will end. Or if the user is able to guess the word before the three chances it will move to the next word of the same level.
We are using temp_list to keep track of the words those have been already presented to player so word will not be repeated.
If player successfully cracks three words in the same level player will move to next level. After every correct guess the user has option to either continue the game or exit the game by answering (y/n).
The same steps will be continued for two more levels. If player was able to guess all the words for three levels. The program will display Congratulations you have completed all levels.
The game ends.

Use Case Scenario: 1. If Player gives correct answer

1.	Program runs – players enter in to Level 1
2.	Program present Challenge (as shuffled word) and Hint to player
3.	Player is asked to Enter response: Ans. If entered correct answer. It will display that it is correct. And it will ask if you want to continue the game.
4.	Player answer y. It goes to step 2.
5.	If Player gives three correct answers, player enter level 2. Go to step 2
6.	If Player gives three correct answers in level 2. Player enters in level 3 and execute step 2 to 4.
7.	If Player gives three correct answer in level 3 program ends.

Use Case Scenario: 2. If Player gives incorrect answer
1.	Program runs – players enter in to Level 1
2.	Program present Challenge (as shuffled word) and Hint to player
3.	Player is asked to Enter response: Ans. If entered wrong answer. It will display Try again and retries left 2. And asked to enter the response again.
4.	Player enters wrong answer. It will display Try again and retries left 1. And asked to enter the response again.
5.	Player enters wrong answer. It will display Try again and retries left 0. It will also display correct answer, program ends.





