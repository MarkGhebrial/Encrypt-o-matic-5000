from alphabet import alphabet, tebahpla

class EncryptOMatic:
  def __init__ (self, key: str):
    self.key = key.lower()

    if self.key != "space":
      self.spaceSequence = EncryptOMatic("space").encryptString(key)[:3]
    else:
      self.spaceSequence = ""

  def encryptChar (self, char: str, position: str):
    try:
      # Magic
      return tebahpla[(alphabet[char.lower()] + alphabet[self.key[position % len(self.key)]]) % len(alphabet)]
    except KeyError:
      if char == " ":
        return self.spaceSequence
      return char

  def encryptString (self, data: str):
    temp = ""
    for i in range(len(data)):
      temp += self.encryptChar(data[i], i)
    return temp

if __name__ == "__main__":
  e = EncryptOMatic('helllo')
  print(e.encryptString("CP Cybersecurity"))
