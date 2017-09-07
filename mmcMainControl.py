# Multi-Media Console, Main Controller

# Imports
import os

# Globals
VERSION = "1.0"
G_MEDIA = None

# Main Thread
def main():
    # Show Welcome Text
    showWelcomeMessage()

    # Get Attached Media
    G_MEDIA, nameList = getAttachedMedia()

    # Print Main Menu
    showMainMenu(G_MEDIA,nameList)

# Get included media files
# Types:
# Links = NAME.txt w/ Contents: Link to Web Address
# Movie = NAME.*
# Picture = NAME.*
def getAttachedMedia():
    # Intialize
    links = []
    movies = []
    #photos = []

    # Populate Containers
    try:
        links = os.listdir("Media/Links")
    except:
        links.append("No Directory")

    try:
        movies = os.listdir("Media/Movies")
    except:
        movies.append("No Directory")

    # try:
    #     photos = os.listdir("Media/Pictures")
    # except:
    #     photos.append("No Directory")

    # Compile
    mediaContainer = [links,movies]
    nameList = ["Media Links", "Movies"]

    # Return List
    return mediaContainer, nameList

# Print Welcome Message
def showWelcomeMessage():
    message = "[ Welcome to T-Papi Multi-Media Controller v"+VERSION+" ]" 
    print(message)
    print("-"*len(message))

# Print Title Message
def showHeaderMessage(message):
    header = "[ "+message+" ]"
    print(header)
    print("-"*len(header))

# Print Main Menu Message
def showMainMenu(media,names):
    # Variables
    choiceLabel = 0
    longestSpace = 0

    # Get Spacing
    tick = 0
    for item in media:
        if(longestSpace < len(names[tick]+" ")):
            longestSpace = len(names[tick]+" ")
        tick += 1

    # Print Items
    for item in media:
        print("[ "+str(choiceLabel)+" ] "+names[choiceLabel], end='')
        print(" "*(longestSpace-len(names[choiceLabel])), end='')
        print("("+str(len(item))+" items)")
        choiceLabel += 1

    # Print Exit
    print("[ "+str(choiceLabel)+" ] Exit Program")

    # Get Valid Input
    # Print Instructions
    selection = input("Choose your option: ")

    # Check Input
    # TODO: Make recursive if invalid input
    if selection == str(choiceLabel):
        # Quit (it's always last)
        quit()
    else:
        # Try to use input
        try:
            # Check if valid
            test = media[int(selection)]

            # If it gets here, it's valid
            # Run Method Call
            showContentMenu(names[int(selection)],media[int(selection)])
        except:
            print("Invalid input.")

# Shows a new content menu
def showContentMenu(message,items):
    # Print Spacer
    print("")

    # Print Header
    showHeaderMessage(message)

    # Variables
    choiceLabel = 0

    # Print Back Option
    print("[ "+str(choiceLabel)+" ] Go Back")
    choiceLabel += 1

    # Print Items
    for item in items:
        print("[ "+str(choiceLabel)+" ] "+item.rsplit(".", 1 )[0])
        choiceLabel += 1

    # Get Input
    input("KILL")

# Execute Main Thread
main()
