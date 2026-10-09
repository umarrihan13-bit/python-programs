import os

print("=== Science notes ===")
with open("science_notes.txt", "r") as f:
 for line in f:
    print(line.strip())
print()

print("=== word count ===")
with open("math_notes.txt", "r") as f:
    for line in f:
        words = line.split()
        print(len(words), "words ->", line.strip())
print()

print("=== Merging notes ===")
if os.path.exists("all-notes.txt"):
  print("all-notes.txt already exists. overwriting...")
else:
 print("all-notes.txt does not exist. creating...")  

content = ""
with open("science_notes.txt", "r") as f:
   content += "=== Science-notes.txt ===\n"
   content += f.read() + "\n"
with open("math_notes.txt", "r") as f:
   content += "=== Math-notes.txt ===\n"
   content += f.read() + "\n"
   
with open("all-notes.txt", "w") as out:
   out.write(content)
print("saved all-notes.txt")
print()

if os.path.exists("all-notes.txt"):
   os.remove("all-notes.txt")
   print("all-notes.txt deleted")
else:
   print("all-notes.txt does not exist.")    