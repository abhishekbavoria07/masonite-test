from masonite.controllers import Controller
from masonite.views import View


class BlogController(Controller):
    def show(self, view: View):
        return view.render("blog")
