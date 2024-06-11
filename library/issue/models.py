from django.db import models
from datetime import date
from books.models import Book
from main.models import CustomUser

class Issue(models.Model):
    STATUS_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    user = models.ForeignKey(CustomUser, related_name='iuser', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='ibook', on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)
    due = models.CharField(max_length=10, choices=STATUS_CHOICES, default='yes')

    def save(self, *args, **kwargs):
        super(Issue, self).save(*args, **kwargs)
        
        if not self.return_date:
            self.return_date = self.calculate_return_date(self.issue_date)
        super(Issue, self).save(*args, **kwargs)

    def calculate_return_date(self, issue_date):
        if issue_date is None:
            issue_date = date.today()

        year = issue_date.year
        month = issue_date.month
        day = issue_date.day

        if month == 12:
            return date(year + 1, 1, day)
        else:
            month += 1
            while True:
                try:
                    return date(year, month, day)
                except ValueError:
                    day -= 1
