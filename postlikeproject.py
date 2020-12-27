import pprint


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

class Postcomment():
    def __init__(self, comment_id, user_comment, comment_val):
        self.comment_id = comment_id
        self.user_comment = user_comment
        self.comment_val = comment_val


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
        # Create Account
        if choice == 1:
            print('Input your username and Password Below ')
            input_username = input('Username :')
            input_password = input('Password :')
            user_created = User(input_username, input_password)
            user_list.append(user_created)
            print(f'user {user_created.username} is created')

        # Show all user
        elif choice == 2:
            if len(user_list) == 0:
                print('no user created yet')
                continue
            else:
                for i in user_list:
                    print(i.username)

        # log in
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

        # Create a Post
        elif choice == 4:
            if cur_session.islogin == True:
                post_title = input('input the post Title :')
                post_description = input('input post Description :')
                user_post = Post(len(post_list)+1, post_title, post_description, cur_session.username)
                post_list.append({'Post Id' : user_post.post_id, 'Post Title' : user_post.post, 'Description': user_post.desc, 'Created By': user_post.createdby,'Comment' : []})
            else:
                print('please login first')
        
        # Display all Post and comment on post
        elif choice == 5: 
            if len(post_list) > 0:
                print('all post here')
                for ps in post_list:
                    pprint.pprint(f'{ps["Post Id"]}. {ps["Post Title"]} {ps["Description"]} Createdy By {ps["Created By"]} Comments:{ps["Comment"]}')
                while True:
                    print("Please choose Post by it's Number to comment on post")
                    print('or press 0 to quit')
                    post_choice = int(input('input your choice :'))
                    try:
                        if post_choice != 0:
                            for serc in post_list:
                                if serc["Post Id"] == post_choice:
                                    post_comment = input('Input your comment:')
                                    input_comment = Postcomment(len(serc["Comment"])+1, post_comment, cur_session.username)
                                    serc["Comment"].append({'Comment_id' :input_comment.comment_id, 'Comment By' : input_comment.user_comment, 'Comment value' : input_comment.comment_val})
                        else:
                            break
                    except ValueError as post_error:
                        print(f'do not input alphabet or symbol, only accept number e.g.(0 - 9) your current input:{post_error}')
            else:
                print('No Post Yet')

        # Log out
        elif choice == 9:
            if cur_session.islogin == True:
                cur_session.islogin = False
                cur_session = User('', '')
                print(cur_session.islogin)
                print('Logging out')
            else:
                print('not logged in yet')

        # Terminated / quit the program
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
