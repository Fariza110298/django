from django.db import models
from django.contrib.auth.models import User

class Institut(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="engiz")
    
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Student(models.Model):
    """
    Model representing a student (but not a specific copy of a book).
    """
    
    title = models.CharField(max_length=200)
   
    kafedra = models.ForeignKey('Kafedra', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text='engiz')
    isbn = models.CharField('ISBN',max_length=15, help_text='15 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    institut = models.ManyToManyField(Institut, help_text='Select ')
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    
   
    def display_institut(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ institut.name for institut in self.institut.all()[:3] ])
	
    display_institut.short_description = 'Institut'
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.university_name
		
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for .
        """
        return reverse('student-detail', args=[str(self.id)])

import uuid # Required for unique book instances

class StudentInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'IITT'),
        ('o', 'KHTOF'),
        ('a', 'AS'),
        ('r', 'POU'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Student availability')

    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set book as returned"),)
        

    def __str__(self):
        """
        String for representing the Model object
        """
        return '{0} ({1})'.format(self.id,self.student.title)
class Kafedra(models.Model):
    """
    Model representing .
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    

    class Meta:
        ordering = ["last_name","first_name"]
    
    def get_absolute_url(self):
        """
        Returns 
        """
        return reverse('kafedra-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.last_name,self.first_name)
   