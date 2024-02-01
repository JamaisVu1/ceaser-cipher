from ceaser_cipher.cipher import encrypt, decrypt, crack


def test_encrypt_shift_1():
    actual = encrypt("apple", 1)
    expected = "bqqmf"
    assert actual == expected


def test_encrypt_shift_10():
    actual = encrypt("apple", 10)
    expected = "kzzvo"
    assert actual == expected


def test_encrypt_shift_20():
    actual = encrypt("apple", 20)
    expected = "ujjfy"
    assert actual == expected


def test_uppercase():
    actual = encrypt("BANANA", 10)
    expected = "LKXKXK"
    assert actual == expected


def test_with_whitespace():
    actual = encrypt("apples and bananas", 1)
    expected = "bqqmft boe cbobobt"
    assert actual == expected


def test_with_non_alpha():
    actual = encrypt("Gimme a 1!", 1)
    expected = "Hjnnf b 1!"
    assert actual == expected


def test_round_trip():
    original = "Gimme a 1!"
    shift = 5
    encrypted = encrypt(original, shift)
    actual = decrypt(encrypted, shift)
    expected = original
    assert actual == expected


def test_crack_phrase():
    phrase = "It was the best of times, it was the worst of times."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    expected = phrase
    assert actual == expected


def test_crack_nonsense():
    phrase = "Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    expected = ""
    assert actual == expected

def test_encrypt_shift():
    assert encrypt("abc", 3) == "def"
    assert encrypt("xyz", 2) == "zab"

def test_decrypt_with_shift():
    original = "Hello, World!"
    shift = 5
    encrypted = encrypt(original, shift)
    assert decrypt(encrypted, shift) == original

def test_case_sensitive():
    assert encrypt("Abc", 1) == "Bcd"
    assert encrypt("XYZ", 2) == "ZAB"

def test_handling_non_alpha():
    assert encrypt("Hello, World! 123", 3) == "Khoor, Zruog! 123"

