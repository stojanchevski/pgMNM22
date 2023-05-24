import requests

# Set up your access token and group ID
access_token = 'EAAt2NiiLK0EBAMiIsURKfNxcPA6SskbIz9OZB8uZA5mBm763XHMc3aHgQAZCFGLzSQLQZCu5gknAEMZCY0AZANasWatlttAUfCXBZAVSeUvrSIU2o7sbOfyQAZBfeMbFYZBd5ZAZAEl3jPiasFoheh6BosZCoFn2ThvvdBSspenBVzfAV5YYZBuwpwqfOPWBB2nvtWNStZBPwEHXNsRNpGZBuKsBh7iglGwZBsNF8XxxgCBKzyf7qUF3Eh5fG3pjmZCOjMyni66ma34zgNAay7QZDZD'
group_id = '551742292437956'

# Make a GET request to the Graph API to retrieve group posts
url = 'https://graph.facebook.com/551742292437956/feed?access_token=EAAt2NiiLK0EBAMiIsURKfNxcPA6SskbIz9OZB8uZA5mBm763XHMc3aHgQAZCFGLzSQLQZCu5gknAEMZCY0AZANasWatlttAUfCXBZAVSeUvrSIU2o7sbOfyQAZBfeMbFYZBd5ZAZAEl3jPiasFoheh6BosZCoFn2ThvvdBSspenBVzfAV5YYZBuwpwqfOPWBB2nvtWNStZBPwEHXNsRNpGZBuKsBh7iglGwZBsNF8XxxgCBKzyf7qUF3Eh5fG3pjmZCOjMyni66ma34zgNAay7QZDZD'
response = requests.get(url)
data = response.json()

# Process the response to extract post information
if 'data' in data:
    posts = data['data']
    for post in posts:
        # Extract relevant information from each post
        post_id = post['id']
        message = post.get('message', '')
        created_time = post['created_time']

        # Process the information as needed
        print(f'Post ID: {post_id}')
        print(f'Message: {message}')
        print(f'Created Time: {created_time}')
        print('---')
else:
    print('No posts found.')
