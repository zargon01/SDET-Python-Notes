'''Program Requirement
Write a program that takes a sentence as input and performs operations using switch-case 
and method. The program should exit after executing the selected operation.
Operations
Case 1:
Print only the words that have an even number of alphabetic characters (ignore digits and 
special characters).
Case 2:
Replace all digits in the sentence with #.
Case 3:
If the sentence contains two or more words starting with a vowel, reverse only those vowel starting words in the sentence and print the modified sentence.
Case 4:
Exit the program.
Additional Requirements
• Each case must be implemented in a separate method:
o printEvenWords (String as parameter)
o replaceDigits
o reverseVowelWords (String as parameter)
• Use a switch-case statement to select which operation to perform.
• After executing the chosen case, the program should exit.
Sample Input
I work in LTIMindtree BBSR office for 02 Years
Sample Output
case1: -work,in,BBSR,office
case2: -I work in LTIMindtree BBSR office for ## Years
case3: -I work ni LTIMindtree BBSR eciffo for 02 Year'''

#Case 1
def EvenWords(string):
    words = string.split()
    even_words = []
    for word in words:
        alpha_count = 0
        for c in word:
            if c.isalpha():
                alpha_count += 1
        if alpha_count > 0 and alpha_count % 2 == 0:
            even_words.append(word)
    print(f"case1: {even_words}")

#Case 2
def ReplaceDigits(string):
    result = ""
    for c in string:
        if c.isdigit():
            result += "#"
        else:
            result += c
    print(f"case2: {result}")

#Case 3
def ReverseVowel(string):
    words = string.split()
    vowels = "aeiouAEIOU"
    vowel_words = []
    for word in words:
        if len(word) > 0 and word[0] in vowels:
            vowel_words.append(word)
    if len(vowel_words) >= 2:
        for i in range(len(words)):
            if len(words[i]) > 0 and words[i][0] in vowels:
                words[i] = words[i][::-1]
    modified = " ".join(words)
    print(f"case3: {modified}")

    


string = "I work in LTIMindtree BBSR office for 02 Years"

EvenWords(string)
ReplaceDigits(string)
ReverseVowel(string)





