from django.db import models

# Create your models here.
class Tasks(models.Model):
    task = models.CharField(max_length=255)

    class Meta:
        """Assign custom table name."""

        db_table = "Tasks"