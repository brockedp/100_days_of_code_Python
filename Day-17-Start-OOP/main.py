def help():
    pass #allows there to not a an error when you want to leave a function or class blank

class User:
    #Python implicitly injects a default constructor during complitation but if a constructor is created there is no default
    def __init__(self, user_id, username): # constructor
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    #pass
    def report_info(self):
        print(f"Username:{self.username}")
        print(f"Id:{self.id}")
        print(f"Follower:{self.followers}")
        print(f"Following:{self.following}")

    def follow(self, user):
        user.followers += 1
        self.followers += 1

user_1 = User("001","Deno")
#user_1.id = "001"
#user_1.username = 'Deno'
user_2 = User("002","Kenneth")

#print(user_1.username)
user_1.follow(user_2)
user_1.report_info()

