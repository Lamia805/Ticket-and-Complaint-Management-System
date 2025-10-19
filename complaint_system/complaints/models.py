from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):

    CATEGORY_CHOICES = [
        ('Bug', 'Bug Report'),
        ('Feature', 'Feature Request'),
        ('General', 'General Feedback'),
        ('Other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Process', 'In Process'),
        ('Solved', 'Solved'),
        ('Closed', 'Closed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaints')
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    satisfied = models.BooleanField(default=None, null=True, blank=True)
    
   
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, 
        null=True,               
        blank=True,               
        related_name='assigned_complaints',
        limit_choices_to={'is_staff': True} 
    )

    def __str__(self):
        return f'{self.title} by {self.user.username}'

class Comment(models.Model):
  
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.complaint.title}'