"""
Class: CS230--Section 3
Name: Vrishab Bharti
Description: Homework 3--Wikipedia Assignment
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

#Imports. Added textwrap to wrap the text to the same line and random for the extra credit
from string import punctuation
import textwrap
import random

punc_list = list(punctuation)

#Creating the section header, more specifically the "=" signs around the title and setting the middle of the title
def section_header(title, border_width=40):
    string = ('\n' + ('=' * border_width) + '\n' + title.center(border_width) + '\n' + ('=' * border_width) + '\n')
    print(string)

#Looks into the word and digit count as well as splits the text. Also looks into the count of each deliverable
def word_and_digit_count(text, search):
    words = text.split(' ')
    separators = ['\n\n']
    for separator in separators:
        for i, word in enumerate(words):
            if word.find(separator) > 0:
                i = words.index(word)
                words = words[:i] + word.split(separator) + words[i + 1:]
    lines = 1
    number_of_words = len(words)
    number_of_characters = 3
    total_digits = 0
    years = 0
    search_word_count = 0
    for word in words:
        if word[-1] == '.' or word[-1] == ']':
            lines += 1
        number_of_characters += (len(word) + 1)

        digits = 0
        for i in range(len(word)):
            if word[i].isdigit():
                digits += 1
        total_digits += digits

        if word.isnumeric() and len(word) == 4:
            years += 1

        if search in word:
            search_word_count += 1

    characters_per_line = round(number_of_characters / lines, ndigits=2)
    search_word_print = 'The search string ' + search + ' appears ' + str(search_word_count) + ' times in the file.'
    space = round(len(search_word_print) / 2)

    section_header('File Analysis')
    print('Sentences: '.rjust(space) + str(lines).ljust(space))
    print('Words: '.rjust(space) + str(number_of_words).ljust(space))
    print('Characters: '.rjust(space) + str(number_of_characters).ljust(space))
    print('Average Sentence Length: '.rjust(space) + str(characters_per_line).ljust(space))
    print('Digits: '.rjust(space) + str(total_digits).ljust(space))
    print('Years: '.rjust(space) + str(years).ljust(space))
    print(search_word_print)

    return words

#looks into replacing the words in the original text, which will then get printed in the updated text.
def process_words(words, searchWord):
    processed_words = []
    for word in words:
        if word.isnumeric() and len(word) == 4:
            processed_words.append(word)
            continue

        word_temp = word.replace("'", "").replace(",", "")

        if word_temp.lower() == searchWord.lower():
            processed_word = f"**{word_temp}**"
        else:
            processed_word = word
            for p in punc_list:
                processed_word = processed_word.replace(p, random.choice(punc_list))

            if len(processed_word) == 1:
                if processed_word.isalpha():
                    processed_word = processed_word.upper()
            elif 2 <= len(processed_word) <= 4:
                processed_word = '_'.join(list(processed_word))
            elif len([c for c in processed_word if c.lower() in 'aeiou']) >= 2:
                processed_word = ''.join(c.swapcase() if c.lower() in 'aeiou' else c for c in processed_word)
            if '[' in processed_word and ']' in processed_word:
                processed_word = processed_word[:processed_word.find('[')] + processed_word[processed_word.find(']') + 1:]

        processed_words.append(processed_word)
    return processed_words

#Looks into creating the new updated text and joining the words together
def print_words(words, justify, max_len):
    text = ' '.join(words)

    wrapped_lines = textwrap.wrap(text, width=max_len)

    for line_number, line in enumerate(wrapped_lines):
        if justify == 'l':
            print(f"{line_number + 1:2} {line.ljust(max_len)}")
        elif justify == 'r':
            print(f"{line_number + 1:2} {line.rjust(max_len)}")
        elif justify == 'c':
            print(f"{line_number + 1:2} {line.center(max_len)}")

#This line of code imports the parameter, starts looking into the 'spec = ['Bentley', 45, 'r']' and controls the width and and length of the text output
def main():
    import parameters
    text = parameters.text
    spec = parameters.spec
    search_word, width, justification = spec

    max_line_length = max(len(line) for line in text.split('\n'))
    new_width = min(max_line_length, width + 2)

    words = word_and_digit_count(text, search_word)

    section_header('Original Text', 60)
    print_words(words, 'l', new_width)

    updated_words = process_words(words, search_word)
    section_header('Updated Text', width)
    print_words(updated_words, justification, width + 2)

main()