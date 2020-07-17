with open('data.txt', 'r') as file:
    content = file.readlines()
lst = []
for _ in content:
    lst.append(_[:-2])