princess = ["Snow White", "Cinderella", "Aurora",\
            "Ariel", "Belle", "Rapunzel", "Merida"]

princess.append("Anna")
print(princess)

princess.pop()
print(princess)

princess.remove("Rapunzel")
print(princess)

princess.insert(5, "Elsa")
print(princess)

list = len(princess)
print("length:", list)

princess.sort()
print("sort:", princess)

for p in princess:
    print(f"Princess {p}")

title = 'Hello, Master'

print(title[::1])