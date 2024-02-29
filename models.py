from django.db import models

#c:/Users/DELL/projectformit/env/Scripts/Activate
#py manage.py runserver
class Attritiondata(models.Model):
    GENDER_CHOICES= [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    BUSINESS_TRAVEL_CHOICES= [
        ("Travel_Rarely", "Travel_Rarely"),
        ("Travel_Frequently", "Travel_Frequently"),
        ("Non-Travel", "Non-Travel"),
    ]
    DEPARTMENT_CHOICES= [
        ("Sales", "Sales"),
        ("Research_&_Development", "Research_&_Development"),
        ("Human_Resources","Human_Resources"),
    ]
    EDUCATION_CHOICES= [
        ("Below_College", "Below_College"),
        ("College", "College"),
        ("Bachelor", "Bachelor"),
        ("Master","Master"),
        ("Docter","Docter"),
    ]
    EDUCATION_FIELD_CHOICES= [
        ("Life_Sciences", "Life_Sciences"),
        ("Medical", "Medical"),
        ("other", "other"),
        ("Marketing", "Marketing"),
        ("Technical_Degree", "Technical_Degree"),
        ("Human_Resources", "Human_Resources"),
    ]
    ENVIROMENT_SATISFACTION_CHOICES= [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Very_High","Very_High"),
    ]
    JOB_INVOLVEMENT_CHOICES= [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Very_High","Very_High"),
    ]
    JOB_ROLE_CHOICES= [
        ("Sales_Executive", "Sales_Executive"),
        ("Research_Scientist","Research_Scientist"),
        ("Laboratory_Technician", "Laboratory_Technician"),
        ("Manufacturing_Director","Manufacturing_Director"),
        ("Research_Director","Research_Director"),
        ("Healthcare_Representative","Healthcare_Representative"),
        ("manager", "Manager"),
        ("Sales_Representative", "Sales_Representative"),
        
    ]
    JOB_SATISFACTION_CHOICES= [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Very_High","Very_High"),
    ]
    MARITAL_STATUS_CHOICES= [
        ("Married", "Married"),
        ("single", "Single"),
        ("Divorced", "Divorced"),
    ]
    OVERTIME_CHOICES= [
        ("YES", "YES"),
        ("NO", "NO"),
    ]
    PERFORMANCE_RATING_CHOICES= [
        ("Low", "Low"),
        ("Good", "Good"),
        ("Excellent", "Excellent"),
        ("Outstanding","Outstanding"),
    ]
    RELATIONSHIP_SATISFACTION_CHOICES= [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Very_High","Very_High"),
    ]
    WORK_BALANCE_CHOICES= [
        ("Excellent", "Excellent"),
        ("Good", "Good"),
        ("Average", "Average"),
        ("Poor", "Poor"),
    ]
    Age= models.IntegerField(default=0)
    BusinessTravel= models.CharField(max_length=100,choices=BUSINESS_TRAVEL_CHOICES)
    DailyRate= models.IntegerField(default=0)
    Department= models.CharField(max_length=100,choices=DEPARTMENT_CHOICES)
    DistanceFromHome= models.IntegerField(default=0)
    #Education= models.CharField(max_length=100,choices=EDUCATION_CHOICES)
    Education= models.IntegerField(default=0)
    EducationField= models.CharField(max_length=100,choices=EDUCATION_FIELD_CHOICES)
    EmployeeNumber=models.IntegerField(default=0)
    #EnvironmentSatisfaction= models.CharField(max_length=100,choices=ENVIROMENT_SATISFACTION_CHOICES)
    EnvironmentSatisfaction = models.IntegerField(default=0)
    Gender= models.CharField(max_length=100,choices=GENDER_CHOICES)
    HourlyRate= models.IntegerField(default=0)
    #JobInvolvement= models.CharField(max_length=100,choices=JOB_INVOLVEMENT_CHOICES)
    JobInvolvement= models.IntegerField(default=0)
    #JobLevel= models.IntegerField()
    JobLevel= models.IntegerField(default=0)
    JobRole= models.CharField(max_length=100,choices=JOB_ROLE_CHOICES)
    #JobSatisfaction= models.CharField(max_length=100,choices=JOB_SATISFACTION_CHOICES)
    JobSatisfaction= models.IntegerField(default=0)
    MaritalStatus= models.CharField(max_length=100,choices=MARITAL_STATUS_CHOICES)
    MonthlyIncome= models.IntegerField(default=0)
    MonthlyRate= models.IntegerField(default=0)
    NumCompaniesWorked= models.IntegerField(default=0)
    OverTime= models.CharField(max_length=100,choices=OVERTIME_CHOICES)
    PercentSalaryHike= models.IntegerField(default=0)
    #PerformanceRating= models.CharField(max_length=100,choices=PERFORMANCE_RATING_CHOICES)
    PerformanceRating= models.IntegerField(default=0)
    #RelationshipSatisfaction= models.CharField(max_length=100,choices=RELATIONSHIP_SATISFACTION_CHOICES)
    RelationshipSatisfaction= models.IntegerField(default=0)
    StockOptionLevel= models.IntegerField(default=0)
    TotalWorkingYears= models.IntegerField(default=0)
    TrainingTimesLastYear= models.IntegerField(default=0)
    #WorkLifeBalance= models.CharField(max_length=100,choices=WORK_BALANCE_CHOICES)
    WorkLifeBalance= models.IntegerField(default=0)
    YearsAtCompany= models.IntegerField(default=0)
    YearsInCurrentRole= models.IntegerField(default=0)
    YearsSinceLastPromotion= models.IntegerField(default=0)
    YearsWithCurrManager= models.IntegerField(default=0)
    class Meta:
        db_table ='myapi_attritiondata'
     
     
    def __str__(self):
        return self.EmployeeNumber 