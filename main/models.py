from django.db import models

# Create your models here.
class Citizen(models.Model):
    NATIONAL_ID_LENGTH = 8  # Assuming Kenyan IDs have 8 digits

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=NATIONAL_ID_LENGTH, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.national_id})"


class LostIDReport(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE, related_name="reports")
    description = models.TextField()  # Details about where/when ID was found or lost
    location = models.CharField(max_length=255)  # Place where ID was lost/found
    date_reported = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default="Lost")#Lost or Found

    def __str__(self):
        return f"{self.status} ID: {self.citizen.national_id} on {self.date_reported}"


class RetrievalRequest(models.Model):
    report = models.ForeignKey(LostIDReport, on_delete=models.CASCADE, related_name="retrieval_requests")
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE, related_name="retrieval_requests")
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default="Pending") #Pending or approved

    def __str__(self):
        return f"Request by {self.citizen.national_id} for report {self.report.id}"

