from src.repository.post import PostRepository
from src.response.post import allPostsJsonForAdmin


class AdminCore:

    @staticmethod
    async def getAllPost():
        posts = await PostRepository().getAllNotApproved()
        postJson = await allPostsJsonForAdmin(posts)
        return postJson

    @staticmethod
    async def changeApproved(idPost: int):
        post = await PostRepository().getOne(idPost)
        post.isApproved = True
        await PostRepository().post(post)