print("LYRICAL ESCAPADES: FILL IN THE BLANK LYRICS 🎶🎶")
print()
counter = 0

while True:
  print("Even when I don't see it, _______")
  missingLyrics = input("What is the missing part?: ")
  if missingLyrics == "you're working":
    counter += 1
    print()
    break
  else:
    counter += 1
    print("Sorry buddy but you're wrong ❌❌")
    print()

print("Congratulations 🥳🥳 on getting the lyrics, the song is way maker by leeland. It took you", counter, "attempt(s) to get the correct answer")