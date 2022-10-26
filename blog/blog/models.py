from django.db import models

# Create your models here.

#database models: title, author, body


#subclass of models.Model called POst
class Post(models.Model):
    #limiting the length to 200 characters
    title = models.CharField(max_length = 200)
    #ForeignKey allows many-to-one relationship
    #this means that the user can be the author of many
    #different blog post but not the other way around
    author = models.ForeignKey(
        'auth.User',
        #specify on_delete option
        on_delete = models.CASCADE,
    )
    #TextField which will expand as needed
    body = models.TextField()

    def __str__(self):
        return self.title

#when model is done, create a new migration record for it and migrate the
#change into our database. After this our database is configured

