h = int(input("height of the tree: "))
for i in range(1,h*2,2):
    print(f'{" "*round((h - (i-1)/2))}{"":*^{i}}')
for i in range(round(h/3)):
    print(f'{" "*(h-1)}| |',end="\n")