from typing import List

from src.database.models import PostModel, EducationInstitutionModel


async def allPostsJson(posts):
    posts_dict = [
        {
            'title': post[0].title,
            'content': post[0].content,
            'linkToPhoto': post[0].linkToPhoto,
            'address': post[0].address,
            'x': post[0].x,
            'y': post[0].y,
            'user': {
                'name': post[1],
                'surname': post[2],
                'fatherName': post[3],
                'educationInstitution': post[4]
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