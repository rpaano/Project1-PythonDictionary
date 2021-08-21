import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def definition(w):
    w.lower()
    if w in data:
        return data[w]
    elif close := get_close_matches(w, data.keys()):
        yn = input(
            "Did you mean %s? Please enter 'Y' for yes and 'N' for no: " % get_close_matches(w, data.keys())[0]).upper()
        return data[close[0]] if yn == "Y" else (
            "The word does not exists." if yn == "N" else "We did not understand your entry.")
    else:
        return "The word doesn't exists. Please double check it."


print(*output if type(output := definition(input("Enter word: "))) == list else output,
      sep="\n" if type(output) == list else "")
