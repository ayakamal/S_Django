from django.db import models
from django.forms import ImageField

from django_resized import ResizedImageField


# Create your models here.
"""
id: identification number of the book
name
description
price
CREATE TABLE book (
    id INT PRIMARY KEY,
    name CHAR 255 NOT NULL,
    description text,
)

INSERT INTO book VALUE(1,'book1','this is the new book1 description')

CRUD operations
C ==> Create ==> INSERT INTO book
R ==> Read ==> SELECT * FROM book
U ==> Update ==> UPDATE VALUES ('id', 'name')('2', 'new book1) WHERE id=1
D ==> Delete ==> DELETE FROM book WHERE id=1

"""

class Book(models.Model):
    # id = primaryKey (django makes the pk column by default)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    # photo = ResizedImageField(size=[100, 100],upload_to='books', null=True, blank=True)
    photo = models.ImageField(upload_to='books', null=True, blank=True)
    is_home = models.SmallIntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)


    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self) -> str:
        return self.name