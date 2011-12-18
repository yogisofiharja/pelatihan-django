from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('bloging.views',
    url(r'^sekarang/','sekarang', name ='waktu_sekarang' ),
    url(r'^home/', 'home', name = 'home'),
    url(r'^sunting/', 'sunting', name='sunting'),
    url(r'^membaca/(?P<id_artikel>\d+)', 'baca', name='blog_baca'),
)
