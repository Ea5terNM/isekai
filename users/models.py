from django.db import models
from django.contrib.auth.models import  AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    favorite_food_set = models.ManyToManyField(
    to="app_general.item",
    through="users.UserFavoriteitem",
    related_name="favorited_user_set",
    )

class Profile(models.Model):
    address = models.CharField(max_length=150,default="")
    phone = models.CharField(max_length=10, default="")
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)



class UserFavoriteitem(models.Model):
    LIKE_CHOICES = [
        (1, "ชอบ"),
    ]

    like = models.SmallIntegerField(choices=LIKE_CHOICES, default=1)
    user = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="favorite_item_pivot_set",
    )
    item = models.ForeignKey(
        "app_general.item",
        on_delete=models.CASCADE,
        related_name="favorited_user_pivot_set",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=("user", "item"), name="unique_user_item")
        ]

    def like_label(self) -> str:
        selected_level = [l for l in self.like if l[0] == self.like][0]
        return selected_level[1]

    


