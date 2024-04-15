import requests
import random

def get_random_posts():
    posts_response = requests.get('https://jsonplaceholder.typicode.com/posts')
    photos_response = requests.get('https://jsonplaceholder.typicode.com/photos')
    comments_response = requests.get('https://jsonplaceholder.typicode.com/comments')

    if posts_response.status_code == 200 and photos_response.status_code == 200 and comments_response.status_code == 200:
        posts = posts_response.json()
        photos = photos_response.json()
        comments = comments_response.json()

        for post in posts:
            post['image'] = random.choice(photos)['url']
            post['comment'] = random.choice(comments)['body']
            comment = random.choice(comments)
            post['comment_email'] = comment['email']
            post['comment_body'] = comment['body']
            print(post)
        return posts
    else:
        return None