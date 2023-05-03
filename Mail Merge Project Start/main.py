#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

for name in names:
    name = name.strip()
    with open("Input/Letters/starting_letter.txt") as letter_to_send:
        content = letter_to_send.read()
        modified_content = content.replace("[name]", name)
        with open(f"Output/ReadyToSend/{name}.txt", mode="w") as file:
            file.write(modified_content)

