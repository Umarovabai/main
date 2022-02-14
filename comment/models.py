from django.db import models


class Created(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Comment(Created):
    comment = models.TextField()
    author = models.ForeignKey(
        'account.user', related_name='comments', on_delete=models.DO_NOTHING,
    )
    problem = models.ForeignKey(
        'problem.Problem', related_name='comments', on_delete=models.CASCADE,
        null=True, blank=True,
    )
    reply = models.ForeignKey(
        'problem.Reply', related_name='comments',  on_delete=models.CASCADE,
        null=True, blank=True,
    )

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ('-created', )

