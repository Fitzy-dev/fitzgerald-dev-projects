# Jordan Fitzgerald
# 3/26/2026
# Text Analyzer
# This module implements a simple text analyzer with functions to calculate character frequency, check for anagrams, find the most common character, identify unique characters, and remove punctuation from a given text. The main function demonstrates the functionality of the text analyzer by performing various operations on a sample text and printing the results.

# The char_frequency function calculates the frequency of each character in the input text, ignoring case and non-alphabetic characters. The is_anagram function checks if two texts are anagrams by comparing their character frequencies. The most_common_char function finds the most common character in the text based on the frequency count. The unique_chars function identifies characters that appear only once in the text. The remove_punctuation function removes all punctuation from the text, leaving only alphanumeric characters and spaces.
def char_frequency(text):
    text = text.lower()
    frequency = {}

    for char in text:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1

    return frequency

# The is_anagram function checks if two texts are anagrams by comparing their character frequencies. It returns True if the frequencies are the same, indicating that the texts are anagrams, and False otherwise.
def is_anagram(text1, text2):
    return char_frequency(text1) == char_frequency(text2)

# The most_common_char function finds the most common character in the text based on the frequency count. It returns the character with the highest frequency. If the text is empty or contains no alphabetic characters, it returns None.
def most_common_char(text):
    frequency = char_frequency(text)

    if not frequency:
        return None

    return max(frequency, key=frequency.get)

# The unique_chars function identifies characters that appear only once in the text. It returns a list of characters that have a frequency of 1 in the text.
def unique_chars(text):
    frequency = char_frequency(text)
    return [char for char in frequency if frequency[char] == 1]

# The remove_punctuation function removes all punctuation from the text, leaving only alphanumeric characters and spaces. It uses a generator expression to filter out characters that are not alphanumeric or whitespace and joins the remaining characters into a new string.
def remove_punctuation(text):
    return ''.join(char for char in text if char.isalnum() or char.isspace())

# The main function demonstrates the functionality of the text analyzer by performing various operations on a sample text and printing the results. It calculates the character frequency, checks for anagrams, finds the most common character, identifies unique characters, and removes punctuation from the sample text.
def main():
    sample_text = "Hello, World! Hello..."
    print("Character Frequency:", char_frequency(sample_text))
    print("Is Anagram (listen vs silent):", is_anagram("listen", "silent"))
    print("Most Common Character:", most_common_char(sample_text))
    print("Unique Characters:", unique_chars(sample_text))
    print("Text without Punctuation:", remove_punctuation(sample_text))


if __name__ == "__main__":
    main()
