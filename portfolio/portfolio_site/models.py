from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


class Project(models.Model):
    '''Model representing the projects on the website'''
    project_name = models.CharField(max_length=50, unique=True, help_text='Enter a project name')
    description  = models.TextField(max_length=500, help_text='Describe the project')
    picture = models.ImageField(default='project_images/loading.jpg', upload_to='project_images/')
    
    def ___str___(self):
        return self.project_name
    
    def get_absolute_url(self):
        return reverse('project', args=self.id)
    
    class Meta:
        constraints = [UniqueConstraint(
            Lower('project_name'),
            name='project_unique_name_constraint',
            violation_error_message=('project already exists')
        )]
