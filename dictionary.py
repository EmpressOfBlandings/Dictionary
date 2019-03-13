import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word,data)) > 0:
        yn = input("Did you mean %s instead? Enter Y is yes, N if no: " % get_close_matches(word, data)[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data)[0]]
        elif yn == "N" or yn == "n":
            return "This word doesn't exist. Please double check it."
        else:
            return "We did not understand your entry."
    else:
        return "This word doesn't exist. Please double check it."

word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
