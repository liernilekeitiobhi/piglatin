# ========================== #
#   ITZULPENERAKO FUNTZIOA   #
# ========================== #
'''
Kode hau erabili nahi badugu utils inportatu beharko dugu gauden dokumentura.
'''

def translate_to_piglatin(phrase):
    def word_to_piglatin(word):
        if word[0] in "aeiou":
            return word + "way"
        else:
            for i, letter in enumerate(word):
                if letter in "aeiou":
                    return word[i:] + word[:i] + "ay"
            return word + "ay"

    words = phrase.split()
    return " ".join(word_to_piglatin(word.lower()) for word in words)
