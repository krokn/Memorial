from src.database.models import PostModel, UserModel
from src.repository.post import PostRepository
from src.repository.user import UserRepository
from src.schemas.post import postSchemaToAdd


class PostCore:

    @staticmethod
    async def addPost(post: postSchemaToAdd, emailUser: str):
        user = await UserRepository().get(emailUser)
        postModel = await PostCore().createPostModel(post, user)
        await PostRepository().post(postModel)

    @staticmethod
    async def createPostModel(post: postSchemaToAdd, user: UserModel) -> PostModel:
        postModel = PostModel(
            title=post.title,
            content=post.content,
            linkToPhoto=post.linkToPhoto,
            x=post.x,
            y=post.y,
            idUser=user.id,
            isApproved='in_progress'
        )
        return postModel




