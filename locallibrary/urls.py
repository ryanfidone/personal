

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('catalog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
