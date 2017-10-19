# Multi-Media Console, Main Controller

# Imports
import os               # For File Management
import urllib.request   # For YouTube Searches
import urllib.parse     # For YouTube Searches
import re               # For Regular Expressions
from lxml import html   # For Reading XML Data
import requests         # For Making Web Requests

# Globals
VERSION = "1.0"
G_MEDIA = None

###########################################################################################
# Main Thread
def main():
    # Show Welcome Text
    showWelcomeMessage()

    # Get Attached Media
    G_MEDIA, nameList = getAttachedMedia()

    # Print Main Menu
    showMainMenu(G_MEDIA,nameList)

###########################################################################################
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

###########################################################################################
# Print Welcome Message
def showWelcomeMessage():
    message = "[ Welcome to T-Papi Multi-Media Controller v"+VERSION+" ]" 
    print(message)
    print("-"*len(message))

###########################################################################################
# Print Title Message
def showHeaderMessage(message):
    header = "[ "+message+" ]"
    print(header)
    print("-"*len(header))

###########################################################################################
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

    # Print YouTube
    print("[ "+str(choiceLabel)+" ] YouTube")

    # Print Exit
    print("[ "+str(choiceLabel+1)+" ] Exit Program")

    # Get Valid Input
    # Print Instructions
    selection = input("Choose your option: ")

    # Check Input
    # TODO: Make recursive if invalid input
    if selection == str(choiceLabel+1):
        # Quit (it's always last)
        quit()
    elif selection == str(choiceLabel):
        # YouTube (it's always second to last)
        showYouTubeMenu()
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

###########################################################################################
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

###########################################################################################
# Shows the YouTube Menu
def showYouTubeMenu():
    # Print Spacer
    print("")

    # Print Header
    showHeaderMessage("YouTube")

    # Variables
    choiceLabel = 0

    # Print Back Option
    print("[ "+str(choiceLabel)+" ] Go Back")
    choiceLabel += 1

    # Print Favorites Option
    print("[ "+str(choiceLabel)+" ] Favorites")
    choiceLabel += 1

    # Print Favorites Option
    print("[ "+str(choiceLabel)+" ] Search")

    # Get User Choice
    modeChoice = input("Choose your option: ")

    # Check choices
    if modeChoice == "0":
        # Go Back
        print("")
        main()
    elif modeChoice == "1":
        # Favorites
        print("")
        main() # TODO: Make Favorites!
    elif modeChoice == "2":
        # Search
        # Print Spacer
        print("")

        # Show Header
        showHeaderMessage("Youtube - Search")

        # Get Search Query
        newQuery = input("Search: ")

        # Search the Query
        results = searchYouTubeQuery(newQuery)

        # Variables
        choiceLabel_S = 0

        # Print Back Option
        print("[ "+str(choiceLabel_S)+" ] Go Back")
        choiceLabel_S += 1

        # Display All Choices
        for item in results:
            # Get Name of Video
            page = requests.get("http://www.youtube.com/watch?v="+str(item))
            tree = html.fromstring(page.content)
            videoTitle = tree.xpath("//*[@id='container']/h1")
            print(videoTitle)

            # # Print Choice
            # print("[ "+str(choiceLabel)+" ] "+videoTitle+", Id: "+str(item))

    else:
        # Go Back, Tell them to try harder
        print("Invalid Input. Returning to Main Menu.\n")
        main()

###########################################################################################
# Searches YouTube for a list of Video Ids that match the Search Query
# In part, by: Grant Curell, Code Project, 2015
def searchYouTubeQuery(inQuery):
    query_string = urllib.parse.urlencode({"search_query" : inQuery})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    # print("http://www.youtube.com/watch?v=" + search_results[0])

    return search_results

###########################################################################################
# Execute Main Thread
main()
