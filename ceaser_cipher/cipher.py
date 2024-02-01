# gpt assisted
import nltk
from nltk.corpus import words
import string
nltk.download('words')


def encrypt(text, shift):
    """
    Encrypts the text using a Caesar cipher.
    
    """
    result = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            if char.isupper():
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    return result

def decrypt(text, shift):
    """
    Decrypts the text encrypted by the Caesar cipher.
    
    """
    return encrypt(text, -shift)

def crack(text):
    """
    Attempts to crack a Caesar cipher using the nltk corpus.
   
    """
    english_words = set(words.words())
    max_words = 0
    decryption = ""

    for shift in range(26):
        decrypted_text = decrypt(text, shift)

        processed_text = decrypted_text.translate(str.maketrans('', '', string.punctuation)).lower()

        word_count = sum(word in english_words for word in processed_text.split())
        if word_count > max_words:
            max_words = word_count
            decryption = decrypted_text

    return decryption
