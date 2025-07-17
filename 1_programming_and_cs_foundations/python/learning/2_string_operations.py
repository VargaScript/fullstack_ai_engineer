"""greeting = "hola, me llamo Adair Vargas"
first_name = "Adair"
last_name = "Vargas"
data = {"first_name": "Adair", "last_name": "Vargas"}
full_name = ["Adair", "Isai", "Vargas", "Pastrana"]
spaces = "         Holaaaaa           "

print(greeting.capitalize())                                # Hola, me llamo adair vargas
print(greeting.casefold())                                  # hola, me llamo adair vargas
print(greeting.center(30, "-"))                             # -hola, me llamo Adair Vargas--
print(greeting.count("a"))                                  # 5
print(greeting.encode(encoding="utf-16"))                   # b'\xff\xfeh\x00o\x00l\x00a\x00,\x00 \x00m\x00e\x00 \x00l\x00l\x00a\x00m\x00o\x00 \x00A\x00d\x00a\x00i\x00r\x00 \x00V\x00a\x00r\x00g\x00a\x00s\x00'
print(greeting.endswith("gas"))                             # True
print(greeting.expandtabs())                                # ???
print(greeting.find("Adair"))                               # 15
print("Hola, {} {}".format(first_name, last_name))          # Hola, Adair Vargas
print("Hola, {first_name} {last_name}".format_map(data))    # Hola, Adair Vargas
print(greeting.index("Vargas"))                             # 21
print(greeting.isalnum())                                   # False
print(greeting.isalpha())                                   # False
print(greeting.isascii())                                   # True
print(greeting.isdecimal())                                 # False
print(greeting.isdigit())                                   # False
print(greeting.isidentifier())                              # False 
print(greeting.islower())                                   # False
print(greeting.isnumeric())                                 # False
print(greeting.isprintable())                               # True
print(greeting.isspace())                                   # False
print(greeting.istitle())                                   # False
print(greeting.isupper())                                   # False
print(" ".join(full_name))                                  # Adair Isai Vargas Pastrana
print(greeting.ljust(30, "-"))                              # hola, me llamo Adair Vargas---
print(greeting.lower())                                     # hola, me llamo adair vargas
print(spaces.lstrip())                                      # Holaaaaa________________
print(greeting.maketrans({"D": "Cloud"}))                   # ???
print(greeting.partition(","))                              # ("hola", ",", " me llamo Adair Vargas")
print(greeting.removeprefix("hol"))                         # a, me llamo Adair Vargas
print(greeting.removesuffix("gas"))                         # hola, me llamo Adair Var
print(greeting.replace("hola", "Hola"))                     # Hola, me llamo Adair Vargas
print(greeting.rfind("Vargas"))                             # 21
print(greeting.rindex("Adair"))                             # 15   
print(greeting.rjust(30, "-"))                              # ---hola, me llamo Adair Vargas
print(greeting.rpartition(","))                             # ("hola", ",", "me", "llamo", "Adair", "Vargas")
print(greeting.rsplit())                                    # ['hola,', 'me', 'llamo', 'Adair', 'Vargas']
print(spaces.rstrip())                                      # _________________Holaa
print(greeting.split(" "))                                  # ["hola,", "me", "llamo", "Adair", "Vargas"]
print(greeting.splitlines())                                # ???
print(greeting.startswith("hola"))                          # True
print(spaces.strip())                                       # Holaaaaa
print(greeting.swapcase())                                  # HOLA, ME LLAMO aDAIR, vARGAS
print(greeting.title())                                     # Hola, Me Llamo Adair Vargas
print(greeting.translate({"D": "Cloud"}))                   # ???
print(greeting.upper())                                     # HOLA, ME LLAMO ADAIR VARGAS
print(greeting.zfill(40))                                   # 0000000000000hola, me llamo Adair Vargas

"""






import string

#Exercises
sentence_1 = "  Hello, my name is Adair Vargas.  "
sentence_2 = "Python is a powerful and versatile programming language."
sentence_3 = "Email addresses: adair@example.com, isaiv@example.net"
sentence_4 = "Line1\nLine2\nLine3"
word = "Evil o live"
sentence = "my name is adair isai vargas pastrana"
data_sentence = "Data science is the future, and the future is data."

#1. Count the number of vowels in a string.
def count_vowels(sentence):
    vowels = 'aeiou'
    lower_sentence = sentence.lower()
    vowels_count = 0
    for letter in lower_sentence:
        if letter in vowels:
            vowels_count += 1
    return print(vowels_count)

count_vowels(sentence_2)

#2. Check if a string is a palindrome.
def check_palindrome(sentence):
    lower_sentence = sentence.lower()
    if lower_sentence == lower_sentence[::-1]:
        return print("That sentence is a palindrome")
    return print("That sentence is not a palindrome")

check_palindrome(word)

#3. Convert a string to title case.
def convert_title_case(sentence):
    to_list = sentence.split()
    result = []

    for word in to_list:
        if word:
            capitalized_word = word[0].upper() + word[1:]
            result.append(capitalized_word)
        else:
            result.append('')

    return ' '.join(result)

print(convert_title_case(sentence))

def convert_title_case2(sentence):
   to_title = sentence.title()
   return to_title

print(convert_title_case2(sentence))
 
#4. Replace all spaces in a string with underscores.
def replace_with_underscores(sentence):
    replaced_spaces = sentence.replace(" ", "_")
    return replaced_spaces

print(replace_with_underscores(sentence))

import string

def replace_with_underscores2(sentence):
    underscored_list = []

    for char in sentence:
        if char == ' ':
            underscored_list.append('_')
        else:
            underscored_list.append(char)
        
    return ''.join(underscored_list)

print(replace_with_underscores2(sentence))

#5. Find the most frequent character in a string.
def most_frequent_char(sentence):
    chars_quantity = {}
    lower_sentence = sentence.lower()

    for char in lower_sentence:
        if char in chars_quantity:
            chars_quantity[char] += 1
        else:
            chars_quantity[char] = 1

    most_frequent = ''
    max_count = 0

    for char in chars_quantity:
        if chars_quantity[char] > max_count:
            most_frequent = char
            max_count = chars_quantity[char]

    return most_frequent, max_count

print(most_frequent_char(sentence))

#6. Count how many times each word appears in a sentence.
def count_words(data_sentence):
    lower_sentence = data_sentence.lower()
    cleaned_sentence = lower_sentence.translate(str.maketrans('', '', string.punctuation))
    turn_list = cleaned_sentence.split()
    words = {}
    
    for word in turn_list:
        if word in words: 
            words[word] += 1
        else: 
            words[word] = 1
            
    return print(words)

count_words(data_sentence)

#7. Remove all punctuation from a string.
def remove_punctuation(sentence_3):
    no_punctuation = sentence_3.translate(str.maketrans('', '', string.punctuation))
    return no_punctuation

print(remove_punctuation(sentence_3))

#8. Extract the domain from an email.
def extract_domain(emails):
    emails_list = emails.split()
    domains = []

    for email in emails_list:
        if "@" in email:
            clean_email = email.strip(string.punctuation)
            domain = clean_email.split("@")[1]
            domains.append(domain)

    return domains

print(extract_domain(sentence_3))

#9. Implement a function that mimics str.replace() without using it.
def custom_replace(text, target, replacement):
    result = ""
    i = 0

    while i < len(text):
        if text[i:i+len(target)] == target:
            result += replacement
            i += len(target)
        else:
            result += text[i]
            i += 1

    return result

print(custom_replace(sentence, "at", "oof"))

#10. Write a function that detects if a string is an anagram of another.
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    char_count_1 = {}
    char_count_2 = {}

    for char in str1:
        char_count_1[char] = char_count_1.get(char, 0) + 1

    for char in str2:
        char_count_2[char] = char_count_2.get(char, 0) + 1

    return char_count_1 == char_count_2

print(are_anagrams(sentence))