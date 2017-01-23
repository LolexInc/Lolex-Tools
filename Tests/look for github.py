import os
class search:
    search = 0
    done = 0
while search.done != 1:
    try:
        users = os.listdir("C:\\Users")
        look = search.search
        while users[look] == "Public" or users[look] == "Default" or users[look] == "defaultuser()" or users[look] == "desktop.ini" or users[look] == "defaultuser0":
             look = look + 1
             search.search = look
        githubpath = "C:/Users/" + users[look] + "/AppData/Local/"
        print("Checking for Github...")
        arraylen = len(os.listdir(githubpath)) - 1
        githubis = os.listdir(githubpath)
        while arraylen != 0:
            if githubis[arraylen] != "GitHub":
                arraylen = arraylen - 1
            else:
                print("Github found...")
                githubpath = githubpath + "Github/"
                gitpath = os.listdir(githubpath)
                arraylen = len(gitpath) - 1
                while "PortableGit" in gitpath[arraylen] == False and len(gitpath[arraylen]) < 52:
                    arraylen = arraylen - 1
                print("Found Git...")
                search.done = 1
                break;
    except(IOError):
        print("Search for Git in", githubpath, "failed.")
        search.search = search.search + 1

