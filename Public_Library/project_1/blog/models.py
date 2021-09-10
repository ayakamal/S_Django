from django.db import models

# Create your models here.
"""
id: identification number of the blog
name
description
CREATE TABLE blog (
    id INT PRIMARY KEY,
    name CHAR 255 NOT NULL,
    description text,
)
"""

class Blog(models.Model):
    # id = primaryKey (django makes the pk column by default)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()