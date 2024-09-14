from typing import List

from src.database.models import PostModel


async def allPostsJson(posts: List[PostModel]):
    posts_dict = [
        {
            'title': post.title,
            'content': post.content,
            'linkToPhoto': post.linkToPhoto,
            'x': post.x,
            'y': post.y
        }
        for post in posts
    ]
    return posts_dict
