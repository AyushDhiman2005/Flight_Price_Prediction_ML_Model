def getCity_Code(city_name):
    city_dict={'Delhi': 1, 'Mumbai': 2, 'Bangalore': 3, 'Kolkata': 4, 'Hyderabad': 5, 'Chennai': 6}
    return city_dict[city_name]

def getTiming_Code(timing):
    time_dict={'Evening': 1, 'Early_Morning': 2, 'Morning': 3, 'Afternoon': 4, 'Night': 5, 'Late_Night': 6}
    return time_dict[timing]

def getStopCode(num):
    if str(num)=='zero':
        return 1
    elif str(num)=='one':
        return 2
    else:
        if num==0:
            return 1
        elif num==1:
            return 2
        else:
            return 3

def getClass_Code(airliner_Class):
    c={'Economy': 1, 'Business': 2}
    return c[airliner_Class]  




def final_y(X):
    to_predict = [0,0,0,0,0,0,0,0]
    to_predict[0] = getCity_Code(X[0])
    to_predict[1] = getTiming_Code(X[1])
    to_predict[2] = getStopCode(X[2])
    to_predict[3] = getTiming_Code(X[3])
    to_predict[4] = getCity_Code(X[4])
    to_predict[5] = getClass_Code(X[5])
    to_predict[6] = X[6]
    to_predict[7] = X[7]

    return to_predict

def Errors(model,xTrain,yTrain):
    from sklearn.metrics import mean_absolute_error, mean_squared_error,root_mean_squared_error
    mae=mean_absolute_error(xTrain,yTrain) 
    mse =mean_squared_error(xTrain,yTrain) 
    rmse =root_mean_squared_error(xTrain,yTrain) 

    print(f'''
Errors:-
1. Mean Absolute Error = {mae}
2. Mean Squared Error = {mse}
3. Root Mean Square Error ={rmse}  
    ''')

def get_Available_City():
    city_list=['Delhi','Mumbai','Bangalore','Kolkata','Hyderabad','Chennai']
    return city_list


def get_Timing():
    timing_list=[ 'Early_Morning', 'Morning', 'Afternoon', 'Evening','Night', 'Late_Night']
    return timing_list
    