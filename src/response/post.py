from typing import List

from src.database.models import PostModel, EducationInstitutionModel


async def allPostsJson(posts: List[PostModel]):
    posts_dict = [
        {
            'title': post.title,
            'content': post.content,
            'linkToPhoto': post.linkToPhoto,
            'address': post.address,
            'x': post.x,
            'y': post.y
        }
        for post in posts
    ]
    return posts_dict


async def get_all_institution_response(institutions: List[EducationInstitutionModel]):
    institutions_dict = [
        {
            'name': institution.name
        }
        for institution in institutions
    ]
    return institutions_dict


async def allPostsJsonForAdmin(posts: List[PostModel]):
    posts_dict = [
        {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'linkToPhoto': post.linkToPhoto,
            'name': post.user.name,
            'surname': post.user.surname,
            'fatherName': post.user.fatherName,
            'email': post.user.email
        }
        for post in posts
    ]
    return posts_dict
