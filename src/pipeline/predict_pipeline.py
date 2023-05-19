import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path = os.path.join("artifacts","model.pkl")
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
            # print(preprocessor_path)
            print("Before Loading")
            model = load_object(file_path = model_path)
            # print(model)
            preprocessor = load_object(file_path = preprocessor_path)
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return round(preds[0], 2)
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(self,
                airline: str, 
                source: str, 
                destination: str,
                total_stops: int,
                journey_day: int, 
                journey_month: int, 
                dep_hour: int, 
                dep_minute: int, 
                arrival_hour: int, 
                arrival_minute: int, 
                duration_hours: int, 
                duration_minute: int, 
                ):

        self.airline = airline
        self.source = source
        self.destination = destination
        self.total_stops = total_stops
        self.journey_day = journey_day
        self.journey_month = journey_month
        self.dep_hour = dep_hour
        self.dep_minute = dep_minute
        self.arrival_hour = arrival_hour
        self.arrival_minute = arrival_minute
        self.duration_hours = duration_hours
        self.duration_minute = duration_minute

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Airline": [self.airline],
                "Source": [self.source],
                "Destination": [self.destination],
                "Total_Stops": [self.total_stops],
                "Journey_Day": [self.journey_day],
                "Journey_Month": [self.journey_month],
                "Dep_Hour": [self.dep_hour],
                "Dep_Minute": [self.dep_minute],
                "Arrival_Hour": [self.arrival_hour],
                "Arrival_Minute": [self.arrival_minute],
                "Duration_Hours": [self.duration_hours],
                "Duration_Minute": [self.duration_minute],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

