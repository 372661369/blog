from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return Post.published.all()
    def lastmod(self,obj):  #接受items返回对象和修改时间
        return obj.publish