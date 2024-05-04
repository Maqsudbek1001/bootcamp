def find_longest_text(*texts):
    longest = min(texts, key=len)
    print("Eng kalta matn: " + longest)

text1 = input("name ")
text2 = input("name ")
text3 = input("name ")
find_longest_text(text1, text2, text3)
