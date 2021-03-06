import csv
from datetime import datetime
from xmlrpc.client import DateTime


DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"
#print (format_temperature(32))

def convert_date(iso_string):
    x=datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z") # datetime.strptime() to convert the iso string to the date  object then the datetime.strftime() to format it to the required output
    date=x.strftime("%A %d %B %Y")
    #date=datetime.strftime(x,"%A %d %B %Y") # this step works too
    return date   
"""Converts and ISO formatted date into a human readable format.
    
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    


def convert_f_to_c(temp_in_farenheit):
    tem_in_celsius =(float(temp_in_farenheit)-32)*5/9
    tem_in_celsius = "{:.1f}".format(tem_in_celsius) #rounded to 1dp
    celcius=float(tem_in_celsius)
    return celcius
"""Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """

    


def calculate_mean(weather_data):
    sum=0
    for i in  weather_data:
        sum=sum+float(i)
        mean=sum/len(weather_data)
    return mean

    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    


def load_data_from_csv(csv_file):
    new_list=[]
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(reader) # skipping over the header
        for line in reader: 
            if line: # ignore the blank lines between the data rows. checks line if line is True or False. It's True when the row is not empty. 
                line[1]= int(line[1]) # Type cast to int
                line[2]= int(line[2])
                new_list.append(line)

    #print(new_list)
    return new_list
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    


def find_min(weather_data):
    if weather_data ==[]:
        return ()
    get_min=float(weather_data[0])# Save 0th value of weather_data list in get_min variable
    min_location=0
    index=0
    for num in weather_data:
        if float(num) <= get_min:
            get_min=float(num)
            min_location=index            
        index+=1
    return (get_min,min_location)
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    


def find_max(weather_data):
    if weather_data ==[]:
        return ()
    get_max=float(weather_data[0])
    max_location=0
    index=0
    for num in weather_data:
        if float(num) >= get_max:
            get_max=float(num)
            max_location=index
        index+=1
    return (get_max,max_location)
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    


def generate_summary(weather_data):
    # new_list1=[]
    length=(len(weather_data))
    min_value=[]
    max_value=[]
    result=""
    for i in (weather_data):
        if i !=[]: 
            min_value.append(int(i[1])) # create list for min value [49, 57, 56, 55, 53]
            max_value.append(int(i[2])) # create list for max value

    find_min(min_value)
    find_max(max_value)
    a,b=find_min(min_value)# returns 2 param (min, location)which is touple. Save it in 2 variables.
    c,d=find_max(max_value)
    date_for_lowtemp=(convert_date (weather_data[b][0])) #(b) is index that you are capturing in variable
    date_for_hightemp=(convert_date (weather_data[d][0]))
    
    average_min= format_temperature(convert_f_to_c(calculate_mean(min_value)))
    average_max=format_temperature(convert_f_to_c(calculate_mean(max_value)))
    min_temprature= (format_temperature(convert_f_to_c(a)))
    max_temprature= format_temperature(convert_f_to_c(c))
    
    result += f"{length} Day Overview\n"
    result += f"  The lowest temperature will be {min_temprature}, and will occur on {date_for_lowtemp}.\n"
    result += f"  The highest temperature will be {max_temprature}, and will occur on {date_for_hightemp}.\n"
    result += f"  The average low this week is {average_min}.\n"
    result += f"  The average high this week is {average_max}.\n"
    return result   


"""Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    


def generate_daily_summary(weather_data):
    
    output = ""
    for row in weather_data:
        output+= f"---- {convert_date(row[0])} ----\n"
        output+= f"  Minimum Temperature: {format_temperature(convert_f_to_c(int(row[1])))}\n"
        output+= f"  Maximum Temperature: {format_temperature(convert_f_to_c(int(row[2])))}\n"
        output+="\n"
    
    return output
"""Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
