from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100) # e.g., Python, Django, OpenCV, YOLOv11
    category = models.CharField(max_length=100, default='Backend') # Backend, AI, Frontend
    proficiency = models.IntegerField(help_text="Enter percentage from 1 to 100")

    def __img__(self):
        return self.name

class Internship(models.Model):
    company_name = models.CharField(max_length=150) # e.g., Millionaire Track
    role = models.CharField(max_length=150) # e.g., Digital Marketing Intern
    start_date = models.CharField(max_length=50) # e.g., March 2025
    end_date = models.CharField(max_length=50) # e.g., April 2025
    achievements = models.TextField(help_text="Separate points with a new line or bullet")

    def __str__(self):
        return f"{self.role} at {self.company_name}"

class Project(models.Model):
    title = models.CharField(max_length=200) # e.g., PaperPilot
    tagline = models.CharField(max_length=250)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200) # e.g., Python, Django, RAG, Deep Learning
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title