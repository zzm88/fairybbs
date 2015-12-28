from django.contrib import admin
from forum.models import topic, mention, notification, post, node ,comment
# Register your models here.


class post_inline(admin.StackedInline):
    model = post
    exclude = ['user', 'content_rendered']
    extra = 0

class comment_inline(admin.StackedInline):
    model = comment
    exclude = ['user', 'content_rendered']
    extra = 0
    
class topic_admin(admin.ModelAdmin):
    list_display = ('title', 'time_created', 'user', 'click', 'last_replied')
    list_filter = ('time_created',)
    search_fields = ['title', 'user__username']
    inlines = [post_inline,comment_inline]

class post_admin(admin.ModelAdmin):
    list_display = ('id','content','user_id')
    list_filter = ('time_created',) 
    
admin.site.register(topic, topic_admin)
admin.site.register(post, post_admin)
admin.site.register(node)
