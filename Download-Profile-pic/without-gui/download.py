import instaloader

instaloader1=instaloader.Instaloader()

username = input('Username : ')

instaloader1.download_profile(username,profile_pic_only=True)