from fastapi import FastAPI

from digest_app.database import engine
from digest_app.digests import models
from digest_app.digests.operations import get_content, get_user, create_digest

models.Model.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/app/v1/digests/{user_id}')
def digest_create(user_id: int):
    user = get_user(user_id)
    content = get_content(user.subscriptions)

    digest = create_digest(user_id, content)

    return digest
