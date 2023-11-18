from django.db import models

class Task(models.Model):
    Name=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    STATUS = [
       ('Progress', 'In Progress'),
       ('Finished', 'Finished')
   ]
    status=models.CharField(
        max_length=32,
       choices=STATUS,
       default='Progress',
    )
    
    def __str__(self):
        return str(self.id)
        
