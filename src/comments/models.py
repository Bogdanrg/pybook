from django.db import models


class AbstractComment(models.Model):
    """ Abstract comment model
    """
    text = models.TextField("Message", max_length=512)
    created_date = models.DateTimeField("Publish date", auto_now_add=True)
    updated_at = models.DateTimeField("Changing date", auto_now=True)
    published = models.BooleanField("Is published?", default=True)
    deleted = models.BooleanField("Is deleted?", default=False)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        abstract = True
