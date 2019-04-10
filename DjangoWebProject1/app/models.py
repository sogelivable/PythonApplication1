"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """具体知识"""
    topic = models.ForeignKey(Topic)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."