file = open("bucket_list.txt", "w")
file.write("1. Skydiving\n")
file.write("2. Visit Dagestan ,Russia\n")
file.write("3. code my own game\n")
file.close()
print("bucket list saved to bucket-list.txt!")

file = open("bucket_list.txt", "r")
content = file.read()
print("\n=== My Bucket List ===")
print(content)
file.close()


file = open("bucket_list.txt", "r")
lines = file.readlines()
print(f"you have {len(lines)} items in your bucket list.")
file.close()

file = open("bucket_list.txt", "a")
file.write("4. travel to france\n")
file.write("5.run 5k marathon\n") 
file.close()
print("\n2 more items added ")

file = open("bucket_list.txt", "r")
print("\n=== My Updated Bucket List ===")
print(file.read())
file.close()