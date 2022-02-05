#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


names = []
with open("./Input/Names/invited_names.txt") as f:
    name_list = f.readlines()
    # print(name_list)
    for ele in name_list:
        names.append(ele.strip("\n"))

print(names)

with open("./Input/Letters/starting_letter.txt") as letter:
    lines_of_letters = letter.readlines()
    # print(lines_of_letters)
    # l = lines_of_letters[0]
    # print(l)
    # l.replace("[name]", "jjj")
    # print(l)
    for name in names:
        #new_line_one = lines_of_letters[0]
        # new_line_one.replace('name', name)
        # print(name)
        new_line_one = f"Dear {name},\n"
        lines_of_letters[0] = new_line_one
        f = open(f"invited_{name}.txt", "w")
        str = ""
        f.write(str.join(lines_of_letters))
        f.close()
        print(lines_of_letters)


