class User:
    def __init__(self,name,id,friends):
        self.name = name
        self.id = id
        self.friends = friends

class Network:
    def __init__(self, users):
        self.users=users

not_quit = True
users = []
friends = []
while not_quit == True:
    user_input=input('''What do you want to do?
        (a) add a user
        (d) delete a user
        (pu) print all users
        (c) create a connection
        (pc) print all connections
        (q) quit program '''
        )

    #add a user!!!
    if user_input=="a":
        name = input("What is your name bro?")
        users.append(name)
        print ("hello "+ name)

    #delete a user!!!
    elif user_input== "d":
        name = input("Who do you want to remove??")
        users.remove(name)
        print(users)

    #print all users!!!
    elif user_input == "pu":
        print (users)

    #create a connection!!!
    elif user_input == "c":
        make_friend = input("Who do you want to add to your friend list?")
        if make_friend in users:
            friends.append (make_friend)
            print(make_friend + " is now your friend :>")
        else:
            print("stop trying to make a fake friend :<")

    #print all connections
    elif user_input=="pc":
        print (friends)

    #quit program
    elif user_input == "q":
        not_quit == False
        break
