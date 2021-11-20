# ============================================================================ #
# problem 1

def submit_post (ID, blog, **kwargs) :
    pass

blog_posts = [
    {'ID' : 'af853d12', 'Photos': 3, 'Likes': 21, 'Comments': 2},
    {'ID' : 'af853e09', 'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'ID' : 'af853e22', 'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'ID' : 'af853f00', 'Comments': 4, 'Shares': 2},
    {'ID' : 'af853fa3', 'Photos': 8, 'Comments': 1, 'Shares': 1},
    {'ID' : 'af85402b', 'Photos': 3, 'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in blog_posts:
    total_likes = total_likes + post['Likes']

print(f"Total likes: {total_likes}")

submit_post('af85402b', blog_posts, Title = 'Yoda was wrong: There is a try!')
submit_post('af85402c', blog_posts, Title = 'Dr. Pythonlove Or: How I Learned to Stop Worrying and Love the Exception')

print(blog_posts)

# ============================================================================ #
# problem 2

import time

print("Press CTRL + C to prevent waiting very long:")

for x in range(1000) :
    try :
        time.sleep(.01)
    except :
        print("\nNope, I fooled you!")
