from logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
def ceaser(text, shift, direction):
  if direction == "decode":
    shift = -shift
  elif direction != "encode":
    print("Invalid Option selected!")
    return

  newWord = ""
  for letter in text:
    if letter in alphabet:
      index = (alphabet.index(letter) + shift) % 26
      if(index >= 0):
          newWord +=  alphabet[index]
      else:
        newWord += alphabet[26+index]
    else:
      newWord += letter

  print(f"Your {direction} message is: {newWord}")

repeat = True

while repeat:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  ceaser(text, shift, direction)
  repeat = input("Do you want to repeat? yes/no: ").lower() == "yes"