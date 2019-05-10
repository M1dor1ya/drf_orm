from django.db import models

# Create your models here.

class Graph(models.Model):
    id = models.AutoField(primary_key=True)
    graph_name = models.CharField(max_length=255)
    graph_content = models.TextField()
    graph_status = models.BooleanField(default=False)
    graph_conf = models.CharField(max_length=255)
    graph_position = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'graph'

