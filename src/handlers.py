from datetime import datetime, timedelta

from sneks.sam.ui_stuff import loader_for, make_404
from sneks.snekjson import blob

from random import randint

class sblob(blob):
    def __init__(self, sval, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sval = sval
    def __str__(self):
        return self.sval
    def __repr__(self):
        return self.sval

def get_post(text, title="The story of the forgotten post title.", url="#", active=False, published_date=None):
    published_date = published_date if published_date else datetime(year=randint(2015,2018), month=randint(1,12), day=randint(1,28), hour=randint(0,23), minute=randint(0,60))
    return blob(
        text="<p>{}</p>".format(text),
        title=sblob(title, html=title),
        url=url,
        active=active,
        published_date=published_date
    )

@loader_for("base.jinja.html")
def index_handler(*args, **kwargs):
    posts = [
        get_post("I can't remember what I was going to write about today.  Sorry.","This is a post title"),
        get_post("Yet again, I can't remember what I was going to write about today.  Sorry.","This is a second post title"),
        get_post("As per usual, I can't remember what I was going to write about today.  Sorry.","This is a third post title"),
        get_post("As per usual, I can't remember what I was going to write about today.  Sorry.","This is a fourth post title"),
        get_post("As per usual, I can't remember what I was going to write about today.  Sorry.","This is a fifth post title"),
        get_post("As per usual, I can't remember what I was going to write about today.  Sorry.","This is a sixth post title"),
        get_post("As per usual, I can't remember what I was going to write about today.  Sorry.","This is a seventh post title"),
    ]
    posts.sort(reverse=True, key=lambda x:x.published_date)
    data = {
        "archive_title":None,
        "archive_text":None,
        "posts":posts,
        "post":posts[0],
        "intended_template":"post",
        "menu":[],
        "rss_feed":None
    }
    return data
