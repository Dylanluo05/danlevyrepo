tree_height = input("Enter the height: ")
tree_height = int(tree_height)
spaces = tree_height-1
hashes = 1
stump_spaces = tree_height-1

while tree_height != 0 :
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print('*', end="")
    print()
    tree_height -= 1
    spaces -= 1
    hashes += 2
for i in range(stump_spaces):
    print(' ', end="")
print('*',end="")