"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
MENU = "(H)ello \n(G)oodbye \n(Q)uit"
name = input("Enter name: ")
print(MENU)

# Get user choice with upper case
option = input(">>> ").upper()

# Main loop for choice selection
while option != "Q":
    if option == "H":
        print(f"Hello {name}")
    elif option == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    print(MENU)
    option = input(">>> ").upper()

print("Finished.")
