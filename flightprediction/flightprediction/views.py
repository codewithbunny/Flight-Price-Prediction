from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
import math
# import string

def index(request):
    if request.method == 'POST':
        dep_time = request.POST.get('Dep_Time')
        arr_time = request.POST.get('Arrival_Time')
        source = request.POST.get('Source')
        destination = request.POST.get('Destination')
        stops = request.POST.get('Stops')
        airline = request.POST.get('Airline')

        Journey_day = int(pd.to_datetime(dep_time, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(dep_time, format ="%Y-%m-%dT%H:%M").month)
        Dep_hour = int(pd.to_datetime(dep_time, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(dep_time, format ="%Y-%m-%dT%H:%M").minute)
        print(arr_time)
        Arrival_hour = int(pd.to_datetime(arr_time, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(arr_time, format ="%Y-%m-%dT%H:%M").minute)
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)

        if stops == 'Non-Stop':
            Total_stops = 0
        else:
            Total_stops = int(stops)

        data =CustomData(
            airline,
            source,
            destination,
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)
        print("After Prediction")
        # result = round(results[0], 2)
        # print(results)

        return render(request, 'index.html', {'param' : f'{results}'})
    
    else:
        return render(request, 'index.html')
    