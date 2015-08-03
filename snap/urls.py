from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'snap.views.display_article', name='home'),
    url(r'^home/$', 'snap.views.profile', name='profile'),
    url(r'^contacts/$', 'snap.views.contacts', name='contacts'),
    
    url(r'^add-article/$','snap.views.add_article',name='add-article'),
    url(r'^edit_article/(?P<pk>\d+)/$', 'snap.views.edit_article', name='update_article'),
    url(r'^delete_article/(?P<pk>\d+)/$', 'snap.views.delete_article', name='delete_article'),
    url(r'^register/$','snap.views.register',name='register'),
    url(r'^login$', 'django.contrib.auth.views.login',{'template_name': 'accounts/login.html'}, name='user_signin'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'accounts/login.html'}, name='user_signin'),
    url(r'^logout/$','snap.views.logout_page',name='logout_page'),
    url(r'^display-article/$','snap.views.display_article',name='display_article'),
    url(r'^article-detail/(?P<pk>\d+)$','snap.views.article_detail',name='article_detail'),
    url(r'^post-comment/$','snap.views.post_comment',name='post_comment'),
    
    url(r'^signin/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name='user_signin'),
    
    url(r'^signout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'account/signin.html','next_page':'/'},
        name='signout'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
