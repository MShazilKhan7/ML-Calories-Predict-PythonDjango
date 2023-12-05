from django.db import models
import joblib
import pandas as pd
# Create your models here.


class CaloriesData(models.Model):
    male = "M"
    female = "F"
    GenderChoices = [
        (male,"Male"),
        (female,"Female")
    ]
    gender = models.CharField(choices=GenderChoices, max_length=1)
    age    = models.IntegerField()
    height = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DecimalField(max_digits=6, decimal_places=2)
    heartRate = models.DecimalField(max_digits=6, decimal_places=2)
    bodyTemp = models.DecimalField(max_digits=6, decimal_places=2)
    
    
    
    @property
    def calories(self):
       ml_model = joblib.load('ml_model/calories_burnt.joblib')
       print(self.gender)
       d  = {'Gender': [self.gender], 'Age': [self.age], 'Height':[self.height],  'Weight':[self.weight],  'Duration': [self.duration],  'Heart_Rate': [self.heartRate],  'Body_Temp': [self.bodyTemp]}
       df  = pd.DataFrame(d)
       df['Gender'] = df['Gender'].astype('category')
       df['Age'] = df['Age'].astype('int')
       df['Height'] = df['Height'].astype('float')
       df['Weight'] = df['Weight'].astype('float')
       df['Duration'] = df['Duration'].astype('float')
       df['Heart_Rate'] = df['Heart_Rate'].astype('float')
       df['Body_Temp'] = df['Body_Temp'].astype('float')

       calories = ml_model.predict(df)
       return calories