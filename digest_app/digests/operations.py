from starlette import status
from starlette.exceptions import HTTPException

from digest_app.database import db
from digest_app.digests import models


def get_user(user_id):
    """Getting and checking the presence of a user."""

    user = db.query(models.User).get(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'user {user_id} not found'
        )

    return user


def get_content(subscriptions):
    """
    Getting the most popular posts from each user's subscription.
    Returns a list of the content of posts.
    """

    posts = []
    for subscription in subscriptions:
        posts.extend(
            subscription.posts.order_by(models.Post.popularity.desc())[:3]
        )

    return [post.content for post in posts]


def create_digest(user_id, content):
    """
    Creating or updating a digest of the user's content,
    based on his subscriptions.
    """

    digest = db.query(models.Digest).get(user_id)
    if digest:
        digest.posts = content
    else:
        digest = models.Digest(user_id=user_id, posts=content)
        db.add(digest)

    db.commit()
    db.refresh(digest)

    return digest
