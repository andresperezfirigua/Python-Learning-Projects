import pandas
# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

alphabet_dataframe = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet_dictionary = {row.letter: row.code for (index, row) in alphabet_dataframe.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter a word: ').upper()
nato_translation = [alphabet_dictionary[letter] for letter in word if letter in alphabet_dictionary]
print(nato_translation)
