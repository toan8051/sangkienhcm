import uuid # new
from django.db import models
from django.contrib.auth import get_user_model # new
from django.urls import reverse # new


class Donvivttp(models.Model):
    # id = models.UUIDField( # new
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False
    # )

    name = models.CharField(max_length=255,)
    #last_updated = models.DateTimeField(auto_now_add=True)
    #board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='departments')
    # starter = models.ForeignKey(
    #     get_user_model(),
    #     on_delete=models.CASCADE,
    #     related_name='departments',
    #     )
    nguoidungthuocdonvi = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,null=True, blank=True, related_name='tenusers')

    class Meta: # new
        indexes = [ # new Performance
            models.Index(fields=["id"], name="id_index_topic"),
        ]

    def get_absolute_url(self):
        return reverse("sangkienlist", args=[self.id])

    def __str__(self):
        return self.name      


    # def get_absolute_url(self): # new
    #     return reverse("department", args=[str(self.id)])     

class Sangkien(models.Model):
    RANK_CHOICES = (
        ('I', 'Loại I',),
        ('II', 'Loại II',),
        ('III', 'Loại III',),
        ('KK', 'Khuyến Khích',),
        ('KĐ', 'Không Đạt cấp VTTP',),
    )
    #author = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    author_2 = models.CharField(max_length=255, blank=True)
    author_3 = models.CharField(max_length=255, blank=True)
    cellphone = models.CharField(max_length=255)
    idea_name = models.CharField(max_length=1000)
    content = models.TextField(max_length=4000)
    upload_file = models.FileField(blank=True) # new upload_to="media/", 
    note = models.TextField(max_length=4000, blank=True)
    donvivttp = models.ForeignKey(Donvivttp, on_delete=models.CASCADE, related_name='ideas')


    assign = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,null=True, blank=True, related_name='assign')
    rank = models.CharField(
        max_length=3,
        choices= RANK_CHOICES,
        blank=True,
    )
    status_approved = models.BooleanField(default = False, blank=True)
    sent_VNPT = models.BooleanField(default = False, blank=True)
    sent_sangtao_VNPT = models.BooleanField(default = False, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='ideas_created_by',
        )

    updated_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='+',
    )

    # created_by = models.ForeignKey(User, related_name='posts')
    # updated_by = models.ForeignKey(User, null=True, related_name='+')

    class Meta: # new
        indexes = [ # new Performance
            models.Index(fields=["id"], name="id_index_post"),
        ]
        ordering = ["created_at"]

    def get_absolute_url(self):
        return reverse(
            "sangkien-update", args=[str(self.donvivttp.id), str(self.id)]
        )

    def __str__(self):
        return self.idea_name
