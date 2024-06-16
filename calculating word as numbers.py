def letterposition(letter):
  letter = letter.upper()
  return ord(letter) - ord('A') + 1

def calculatesum(letters):
  total = 0
  length = len(letters)
  for i, letter in enumerate(letters):
      position = letterposition(letter)
      if i == length - 1:
          total += position  # Add the last letter's position directly
      else:
          total += position * (26 ** (length - i - 1))
      print(f"Letter:{letter},Position:{position}")

  return total

def main():
  examples = ["A", "B", "Z", "AA", "AB", "ZZ"]
  for example in examples:
      result = calculatesum(example)
      print(f"The sum of the letter positions in '{example}' is {result}")

if __name__ == "__main__":
  main()
