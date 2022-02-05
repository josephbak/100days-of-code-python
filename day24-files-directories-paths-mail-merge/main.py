with open("my_file.txt") as file:
    contents = file.read()
    print(contents)


# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")


f = open("data.txt")
number = f.read()
f.close()
print(number)
print(type(number))
