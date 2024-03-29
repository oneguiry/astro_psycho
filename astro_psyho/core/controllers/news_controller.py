from datetime import datetime

from core.models import News
from permissions.models import AccountManager


class NewsController:
    def __init__(self, news_id: int = None):
        self.news = news_id
        if news_id:
            self.news = News.objects.get(id=news_id)

    def edit_news(self, title: str, body: str, author, pub_date: datetime = None):
        self.news.title = title
        self.news.body = body
        self.news.author = AccountManager.objects.get(user=author)
        self.news.pub_date = pub_date
        self.news.save()

    def get_news(self):
        return self.news
