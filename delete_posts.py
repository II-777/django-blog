from blog.models import Post

def delete_posts():
    deleted_count, _ = Post.objects.all().delete()
    print(f"{deleted_count} posts deleted successfully.")

if __name__ == "__main__":
    delete_posts()
