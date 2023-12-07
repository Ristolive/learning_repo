text="The quick brown fox jumps over the lazy dog"

a=0
e=0
i=0
o=0
u=0

for x in text:
    if "a" in x:
        a+=1
print(f"a={a}")

for x in text:
    if "e" in x:
        e+=1
print(f"e={e}")

for x in text:
    if "i" in x:
        i+=1
print(f"i={i}")

for x in text:
    if "o" in x:
        o+=1
print(f"o={o}")

for x in text:
    if "u" in x:
        u+=1
print(f"u={u}")