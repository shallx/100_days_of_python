import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato = {row["letter"]:row["code"] for (_, row) in df.iterrows()}

print(nato)

name = input("Namaywa:").upper()
print([nato[l] for l in name])

