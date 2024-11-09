from src.repository.post import PostRepository
from src.response.post import allPostsJsonForAdmin


class AdminCore:

    @staticmethod
    async def getAllPost():
        posts = await PostRepository().getAllNotApproved()
        postJson = await allPostsJsonForAdmin(posts)
        return postJson

    @staticmethod
    async def changeApproved(idPost: int, status: str):
        post = await PostRepository().getOne(idPost)
        if status == 'True':
            post.isApproved = 'True'
        else:
            post.isApproved = 'False'
        await PostRepository().post(post)