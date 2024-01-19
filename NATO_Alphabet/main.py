import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato = {row["letter"]:row["code"] for (_, row) in df.iterrows()}

print(nato)

def get_name():
    try:
        name = input("Namaywa:").upper()
        print([nato[l] for l in name])
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        get_name()


get_name()