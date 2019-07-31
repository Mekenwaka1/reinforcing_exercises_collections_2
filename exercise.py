digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']

dictionary = {}

for item, en_item, fr_item in zip(digits, en, fr):
    value_dict = {}
    value_dict["french"] = en_item
    value_dict["english"] = fr_item
    dictionary[item] = value_dict

print(dictionary)