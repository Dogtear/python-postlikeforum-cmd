class User:
    islogin = False
    def __init__ (self,username,password):
        self.username = username
        self.password = password
    
    def login(self,username,password):
        if username == self.username and password == self.password:
            self.islogin = True
            return "you are logged in"
        return 'try again'

class Post():
    def __init__(self,post_id, post, desc, createby):
        self.post_id = post_id
        self.post = post
        self.desc = desc
        self.createdby = createby

class Postcomment(Post):
    pass


user_list = []
post_list = []
cur_session = User('', '')

while True:
    print("1. Please Create an account")
    print('2. Show all user ')
    print('3. Log in')
    print('4. Post')
    print('5. Show all Post')
    print('9. Log Out')
    print("0. Quit")
    try:
        choice = int(input("choice:"))
        if choice == 1:
            print('Input your username and Password Below ')
            input_username = input('Username :')
            input_password = input('Password :')
            user_created = User(input_username, input_password)
            user_list.append(user_created)
            print(f'user {user_created.username} is created')


        elif choice == 2:
            if len(user_list) == 0:
                print('no user created yet')
                continue
            else:
                for i in user_list:
                    print(i.username)


        elif choice == 3:
            exist = False
            matching = False
            if len(user_list) != 0:
                if cur_session.islogin == False:
                    print('input your login information Username and Password')
                    login_username = input('Input your Username :')
                    for i in user_list:
                        if login_username == i.username:
                            exist = True
                            print('user exist')
                            if exist:
                                while not matching :
                                    login_password = input('input your password:')
                                    if login_password == i.password:
                                        matching = True
                                        i.login(login_username, login_password)
                                        i.islogin = True
                                        cur_session = i
                                        print(cur_session.islogin)
                                        break
                                    else:
                                        print("password doesnt match")
                else:
                    print('you already log in')
            else:
                print('no user data yet')

        elif choice == 4:
            if cur_session.islogin == True:
                post_title = input('input the post Title :')
                post_description = input('input post Description :')
                user_post = Post(str(len(post_list)+1),post_title, post_description, cur_session.username)
                post_list.append({'Post Id' : user_post.post_id, 'Post Title' : user_post.post, 'Description': user_post.desc, 'Creted By': user_post.createdby})
            else:
                print('please login first')
        
        elif choice == 5:
            print('all post here')
            for ps in post_list:
                print(ps)

        elif choice == 9:
            if cur_session.islogin == True:
                cur_session.islogin = False
                cur_session = User('', '')
                print(cur_session.islogin)
                print('Logging out')
            else:
                print('not logged in yet')

        elif choice == 0:
            print("Terminated")
            break
        else:
            print('input correctly please')
    except ValueError as err :
        print(f'do not input alphabet or symbol only accept number e.g.(0 - 9) your input:{err}')
    
# ===================================================================

# note please complete the class to post firsh 
# then add comment on post
