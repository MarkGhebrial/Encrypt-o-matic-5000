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
        return self.spaceSequence#[position % len(self.spaceSequence)]
      return char

  def encryptString (self, data: str):
    temp = ""
    for i in range(len(data)):
      temp += self.encryptChar(char=data[i], position=i)
    return temp

  def removeSpaceSequences (self, data: str):
    temp = data[:]

    for i in range(len(data) - 2):
      if data[i:(i+3)] == self.spaceSequence:
        temp = data[:i] + " " + data[(i+3):]
        return self.removeSpaceSequences(temp)
    
    return temp

  def decryptChar (self, char: str, position: str):
    try:
      return tebahpla[(alphabet[char.lower()] - alphabet[self.key[position % len(self.key)]]) % len(alphabet)]
    except KeyError:
      return char

  def decryptString (self, data: str):
    data = self.removeSpaceSequences(data)

    temp = ""
    for i in range(len(data)):
      temp += self.decryptChar(char=data[i], position=i)
    return temp

    

if __name__ == "__main__":
  e = EncryptOMatic('helllo')
  s = e.encryptString("CP Cyber security")
  print(s)
  print(e.decryptString(s))
