def is_pangram(sentence):
    print("This is the sentence: " + sentence)
    letters = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if len(sentence) == 0:
        print("Failed")
        return False

    for c in sentence:
        letter = c.lower()
        if letter in alphabet:
            if not letter in letters:
                letters.append(letter)

    if len(letters) == len(alphabet):
        print("Succeeded!")
        return True
    else:
        print("Failed")
        return False
    pass
