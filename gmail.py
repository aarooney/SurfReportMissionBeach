from email.message import EmailMessage
import ssl
import smtplib
import wget 
from noaa_coops import Station
"""
App passwords? Gmail API?  Just for my computer?

Next step get the buoy data for today 

What is wget?

How can I get tide data?

How can I get wind data?

Whats a python wrapper?  What is this library I'm using?
"""

def sendEmail(emailSender, emailReceiver, emailAppPassword, body, subject):
    """
    Sends email utilizing an app password generated from the gmail.
    """
    em = EmailMessage()
    em['From'] = emailSender
    em['To'] = emailReceiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailSender, emailAppPassword)
        smtp.sendmail(emailSender, emailReceiver, em.as_string())


def getTide():
    laJollaStation = Station(id="9410230")  # Create Station object for Seattle (ID = 9447130)
    df_water_levels = laJollaStation.get_data(
    begin_date="20150101",
    end_date="20150131",
    product="water_level",
    datum="MLLW",
    units="metric",
    time_zone="gmt")
    df_water_levels.head()
    return "yes"



def getData():
    url = 'https://www.ndbc.noaa.gov/data/realtime2/46258.txt'
    filename = wget.download(url)
    with open(filename, "r") as file:
        file.readline()
        file.readline()
        mostRecentBuoyUpload = file.readline().split(" ")
        filtered_list = list(filter(lambda x: x.strip(), mostRecentBuoyUpload))
        
        waveHeight = filtered_list[8] #In feet
        swellDirection = filtered_list[11] #In degrees
        waterTemperature = filtered_list[14] #In Celsius
        # tide = 
        # wind
        #"Hello, {0}! You are {1} years old.".format(name, age)
        return "wave height is {0} ft.  swell direction is coming in from {1} degrees.  waterTemperature is {2} Fahreinheit".format(waveHeight, swellDirection, waterTemperature)
        # body = f"Wave Height is {waveHeight}m/n swellDirection is coming from the 
        # {swellDirection} degree direction/n waterTemperature is {waterTemperature} celsius"
        
        #return body    
if __name__ == "__main__":
    #WVHT Wave Height
    #SwD Swell Direction
    body = getData()
    #WTMP Water Temperature 
    print(getTide())
    sendEmail("proudcatowner1400@gmail.com", "proudcatowner1400@gmail.com", "safk agpm oyge avec", body, "Mission Beach Surf Report")
    print("Email Sent!")
    # sendEmail("proudcatowner1400@gmail.com", "safk agpm oyge avec", 
    #           "proudcatowner1400@gmail.com", "This is my surfline test", "Surfline Test")

