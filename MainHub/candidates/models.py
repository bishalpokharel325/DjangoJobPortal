from django.db import models

# Create your models here.
# a) Name
# b) Age
# c) gender
# d) mobile
# e) city
# f) salary
# Expectation
# g) willing
# to
# Relocate
GENDER_MALE = "Male"
GENDER_FEMALE = "Female"
GENDER_CHOICE = (
    (GENDER_MALE, "M"),
    (GENDER_FEMALE, "F"),
)


class Candidate(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=15, choices=GENDER_CHOICE, default=GENDER_MALE)
    mobile = models.CharField(max_length=15)
    city = models.CharField(max_length=150)
    salary_expectation = models.IntegerField()
    relocate = models.BooleanField(default=0)

    def __str__(self):
        return self.name


STATUS_ACCEPTED = "ACCEPTED"
STATUS_REJECTED = "REJECTED"
STATUS_PENDING = "PENDING"
STATUS_CHOICES = (
    (STATUS_ACCEPTED, "ACCEPTED"),
    (STATUS_REJECTED, 'REJECTED'),
    (STATUS_PENDING, "PENDING")
)


class CandidateJobMap(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    feedback = models.CharField(max_length=150)

    def __str__(self):
        return "{} mapping for {}".format(self.candidate.name, self.job.position_name)
