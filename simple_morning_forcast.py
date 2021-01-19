import email_class
import weather_gov

weather_report = weather_gov.Weather_Gov(zipcode= '60060')
current_weather = weather_report.forcaster()
email = email_class.Email_Class()
to_email = 'stvnchnsn@gmail.com'
subject = "Near Term Forcast"
message = current_weather
email.send_email(to_email,subject,message)