import json
from blog.models import Post

def populate_posts(json_file_path='posts.json'):
    # Populate new posts
    with open(json_file_path) as f:
        posts_json = json.load(f)

    for post_data in posts_json:
        post = Post.objects.create(
            title=post_data.get('title', ''),
            content=post_data.get('content', ''),
            author_id=post_data.get('user_id', None)
        )
        print(f"Created Post with title: {post.title} and ID: {post.id}")

if __name__ == "__main__":
    populate_posts()
