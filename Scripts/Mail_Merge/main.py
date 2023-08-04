from letterhandler import LetterHandler

letter = LetterHandler()
for name in letter.names:
    letter.write_to_letter(name)
