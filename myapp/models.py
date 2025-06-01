from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse


class IndexSlider(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    url = models.CharField(null=False, blank=False)
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class AboutUs(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    h1 = models.CharField(max_length=100, blank=False, null=False)
    description= models.TextField(max_length=2000, blank=False, null=False)
    url = models.CharField(null=False, blank=False)
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class ExploreTopSubjects(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=500, blank=False, null=False)
    url = models.CharField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Courses(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    h1 = models.CharField(max_length=100, blank=False, null=False)
    course_description = models.TextField(blank=False, null=False, max_length=1000, default="Açıqlama")
    courese_requirements = models.TextField(blank=False, null=False, max_length=1000, default="Tələblər")
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    course_hour = models.CharField(max_length=10, blank=False, null=False)
    student_count = models.CharField(max_length=10, blank=False, null=False)
    course_star = models.CharField(max_length=10, blank=False, null=False)
    course_comment_count = models.CharField(max_length=10, blank=False, null=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    course_price = models.CharField(max_length=10, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('course_blog', kwargs={'slug': self.slug})

class Teachers(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    image = models.ImageField(upload_to='images/', null=False, blank=False,default='')
    profession = models.CharField(max_length=100,null=False,blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    READ_ME = models.TextField(editable=False,default=
    'Burada Social Media iconlarının sadəcə adını yazaraq iconlarını çağırısan:')

    social_media_url_1 = models.URLField(max_length=100, null=True, blank=True)
    social_media_icon_1 = models.CharField(max_length=20, null=True, blank=True)

    social_media_url_2 = models.URLField(max_length=100, null=True, blank=True)
    social_media_icon_2 = models.CharField(max_length=20, null=True, blank=True)

    social_media_url_3 = models.URLField(max_length=100, null=True, blank=True)
    social_media_icon_3 = models.CharField(max_length=20, null=True, blank=True)

class TestimonialSlider(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    professions = models.CharField(max_length=20,blank=False,null=False)
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    comment = models.TextField(max_length=500,blank=False,null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class GetInTouch(models.Model):

    location = models.CharField(max_length=50, null=False, blank=False)
    location_url = models.URLField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    social_media_url_1 = models.URLField(max_length=100, null=False, blank=False)
    social_media_icon_1 = models.CharField(max_length=20, null=False, blank=False)

    social_media_url_2 = models.URLField(max_length=100, null=False, blank=False)
    social_media_icon_2 = models.CharField(max_length=20, null=False, blank=False)

    social_media_url_3 = models.URLField(max_length=100, null=False, blank=False)
    social_media_icon_3 = models.CharField(max_length=20, null=False, blank=False)

    social_media_url_4 = models.URLField(max_length=100, null=False, blank=False)
    social_media_icon_4 = models.CharField(max_length=20, null=False, blank=False)

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    subject = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(max_length=500, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class EmailSubscription(models.Model):
    email = models.EmailField(max_length=100,unique=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

EXPERIENCE_CHOICES = [
    ("təcrübəsiz", "Təcrübəsiz"),
    ("tələbə", "Tələbə"),
    ("peşəkar", "Peşəkar"),
]
class CourseRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default="təcrübəsiz")
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        null=True, blank=True,
        default='profile_pictures/default_profile.png'
    )
    bio = models.CharField(max_length=15, blank=True, null=True)
    last_applied = models.DateTimeField(null=True, blank=True)

    def can_apply_again(self):
        from datetime import timedelta

        if not self.last_applied:
            return True
        return timezone.now() - self.last_applied > timedelta(days=30)

    def __str__(self):
        return f"{self.user}"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True,)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1
            while Category.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

class Blog(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    title2 = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    author = models.ForeignKey('CourseRegistration', on_delete=models.CASCADE, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    main_content = models.TextField(max_length=5000, null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, db_index=True, blank=True)
    is_active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            original_slug = self.slug
            counter = 1
            while Blog.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('single', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=500, blank=True, null=True)
    active = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('CourseRegistration', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.author} - {self.body[:20]}"

class UpdateFontAwesome(models.Model):
    READ_ME = models.TextField(editable=False,default=(

        "Buradan saytdakı ikonların çağırıldığı plugini sadəcə aşağıdakı URL-i dəyişərək update edə bilərsiniz.\n\n"
        "Bəs necə update edək? Mən sizə sadəcə linkdəki rəqəmləri dəyişməyinizi tövsiyə edirəm:\n"
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/<VERSIYA>/css/all.min.css"))

    update_url = models.TextField(max_length=300,null=False,blank=False,default=
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css')
    updated_at = models.DateTimeField(auto_now=True)
