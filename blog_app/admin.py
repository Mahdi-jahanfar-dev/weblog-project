from django.contrib import admin
from .models import Article, Category, Comment, Contactus

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Contactus)

# we can customaise header and title and more of admin django panel with blow codes:
# admin.site.site_header = 'مدیریت وبلاگ'
# admin.site.site_title = 'پنل مدیریت وبلاگ'
# admin.site.index_title = 'پنل مدیریت وبلاگ'

# or using another way to customaise in django admin panel
# 1_ going to venv/lib/django/contrib/admin/templates/admin/something.html and start customasing in something.html
# but its not standard because when upload your project in host we dont transfer venv files and they will gone
#2 and stantard way_ we making a templates directory in main django project file and making admin directory in templates directory
#and then copy that something.html in django venv files in new directory and then start costumasing..
