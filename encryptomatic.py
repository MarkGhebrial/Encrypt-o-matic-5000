from alphabet import alphabet, tebahpla

class EncryptOMatic:
  def __init__ (self, key: str):
    self.key = key.lower()

    # Create a sequence of three characters to use instead of spaces
    if self.key != "space":
      self.spaceSequence = EncryptOMatic("space").encryptString(key)[:3]
    else:
      self.spaceSequence = ""

  def encryptChar (self, char: str, position: str):
    try:
      # Get the value of the character, then add the value of the character at key[position] and turn it back into a character
      return tebahpla[(alphabet[char.lower()] + alphabet[self.key[position % len(self.key)]]) % len(alphabet)]
    except KeyError:
      # If the character is not aphanumeric, then don't change it
      if char == " ":
        return self.spaceSequence
      return char

  def encryptString (self, data: str) -> str:
    '''Encrypt each character in data, then retun that value
    '''
    temp = ""
    for i in range(len(data)):
      temp += self.encryptChar(char=data[i], position=i)
    return temp

  def removeSpaceSequences (self, data: str) -> str:
    '''Recursively replace all space sequences with actual spaces
    '''
    temp = data[:]

    for i in range(len(data) - 2):
      if data[i:(i+3)] == self.spaceSequence: # Scan next few chars to see if they are the space sequence
        temp = data[:i] + " " + data[(i+3):] # If so, remove them and put a space instead
        return self.removeSpaceSequences(temp) # Repeat until there are no more space sequences
    
    return temp

  def decryptChar (self, char: str, position: str) -> str:
    try:
      return tebahpla[(alphabet[char.lower()] - alphabet[self.key[position % len(self.key)]]) % len(alphabet)]
    except KeyError:
      return char

  def decryptString (self, data: str) -> str:
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
