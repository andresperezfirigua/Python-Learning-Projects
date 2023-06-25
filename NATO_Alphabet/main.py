import pandas
# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

alphabet_dataframe = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet_dictionary = {row.letter: row.code for (index, row) in alphabet_dataframe.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic_translation():
    word = input('Enter a word: ').upper()
    try:
        nato_translation = [alphabet_dictionary[letter] for letter in word]
        if len(nato_translation) == 0:
            raise ValueError('Empty field')
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic_translation()
    except ValueError:
        print("Field can't be empty, please enter a word")
        generate_phonetic_translation()
    else:
        print(nato_translation)


generate_phonetic_translation()
