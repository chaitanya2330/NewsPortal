from ..models import *

def run():
    restaurant = NewsDetailModel.objects.create(
        author = "chaitanya",
        title = "Hello",
        title_tags = "Hello",
        paragraph1 = "Hello paragraph1",
        paragraph2 = "Hello paragraph2",
    )
    print(restaurant)

