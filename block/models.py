from django.db import models

class Block(models.Model):
    name=models.CharField(u"板块名称",max_length=100)
    desc=models.CharField(u"板块描述",max_length=100)
    manager_name=models.CharField(u"管理员ID",max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name="板块"
        verbose_name_plural="板块"
