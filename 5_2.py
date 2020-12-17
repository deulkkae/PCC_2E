car = 'subaru'
if car == 'subaru':
    print("I predict True.")
if car != 'subaru':
    print("I predict False.")

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()} is allowed to write a post")
    