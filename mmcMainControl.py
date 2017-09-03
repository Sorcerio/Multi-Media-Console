# Multi-Media Console, Main Controller

# Imports
import os

# Globals
VERSION = "1.0"

# Main Thread
def main():
    # Show Welcome Text
    showWelcomeMessage()

    # Get Attached Media
    media = getAttachedMedia()

    # Print Main Menu


# Get included media files
# Types:
# Links = NAME.txt w/ Contents: Link to Web Address
# Movie = NAME.*
# Picture = NAME.*
def getAttachedMedia():
    # Initialize
    links = []
    movies = []
    photos = []

    # Compile
    mediaContainer = [links,movies,photos]

    # Return List
    return mediaContainer

# Print Welcome Message
def showWelcomeMessage():
    message = "[ Welcome to T-Papi Multi-Media Controller v"+VERSION+" ]" 
    print("-"*len(message))
    print(message)
    print("-"*len(message))

# Print Main Menu Message
def showMainMenu(media):
    if len(media) != 0:
        print("Place holder for media.")
    else:
        print("No media to show.")

# Execute Main Thread
main()
