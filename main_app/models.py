from django.db import models
from django.contrib.auth.models import User

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

class Dev(models.Model):
    id = models.AutoField(primary_key=True)
    cpu = models.IntegerField()
    memory = models.IntegerField()
    disk = models.IntegerField()
    ip = models.CharField(max_length=15)
    dev_user = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    class Meta:
        db_table = 'dev'

    @property
    def dev_user_name(self):
        data_dict = {
            'username': self.dev_user.username,  # self.dev_user相当于获取到一个User实例
            'password': self.dev_user.password
        }
        return data_dict


