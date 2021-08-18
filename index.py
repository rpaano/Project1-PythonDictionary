import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))


def definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s? Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0]).upper()
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "Word does not exists."
        else:
            return "We did not understand your word."
    else:
        return "The word does not exist."


word = input("Enter word: ")

print(definition(word))
