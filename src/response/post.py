from typing import List

from src.database.models import PostModel, EducationInstitutionModel


async def allPostsJson(posts):
    posts_dict = [
        {
            'title': post.title,  # Доступ к post.title из PostModel
            'content': post.content,
            'linkToPhoto': post.linkToPhoto,
            'address': post.address,
            'x': post.x,
            'y': post.y,
            'user': {
                'name': post.user.name,  # Доступ к user.name из UserModel
                'surname': post.user.surname,
                'fatherName': post.user.fatherName,
                'educationInstitution': post.user.EducationInstitution.name  # Алиас из запроса
            }
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


async def allPostsJsonForAdmin(posts):
    posts_dict = [
        {
            'id': post[0].id,
            'title': post[0].title,
            'content': post[0].content,
            'linkToPhoto': post[0].linkToPhoto,
            'name': post[1],
            'surname': post[2],
            'fatherName': post[3],
            'email': post[4],
            'institutionName': post[5]
        }
        for post in posts
    ]
    return posts_dict