# Berkley Algorithm
from datetime import timedelta

numClients = int(input("Enter number of clients: "))
clientTimes = input("Enter Client times in HH:MM format separated by space: ").split()
serverTime = input("Enter Server Time: ")

def timeToSeconds(time):
    h,m = time.split(":")
    inSeconds = int(h)*60*60 + int(m)*60
    return inSeconds

def timeToHours(timeInSeconds):
    formattedTime = timedelta(seconds=timeInSeconds) 
    return formattedTime

sum = 0
for time in clientTimes:
    sum += timeToSeconds(time)
sum+=timeToSeconds(serverTime)

averageTime = int(sum/(numClients+1))

print(f"The new time for all the systems is: {timeToHours(averageTime)}")

