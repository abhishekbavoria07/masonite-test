from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from app.models.Post import Post

class BlogController(Controller):
    def show(self, view: View):
        return view.render("blog")

    # new store method
    def store(self, request: Request):
        Post.create(
            title = request.input('title'),
            body = request.input('body'),
            author_id = request.user().id
        )

        return 'post created'