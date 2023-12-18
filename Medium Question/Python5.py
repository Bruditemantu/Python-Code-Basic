##You are developing a program that analyzes weather data. Write a Python function
#that takes a list of temperature readings for a specific location and determines the
#average temperature, highest temperature, and lowest temperature.
def weatherprogram(nums):
    sum=0
    for i in nums:
        sum+=i

    average_temp=sum/len(nums)
    highest_temp=max(nums)
    lowest_temp=min(nums)
    print("Average Temperature:",average_temp)
    print("highest Temperature:",highest_temp)
    print("Lowest Temperature:",lowest_temp)


##input
list1=[25, 28, 21, 24, 27]
weatherprogram(list1)    
