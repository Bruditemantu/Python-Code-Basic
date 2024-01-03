# queastion no 5
class Time:
   def __init__(self, hours, minutes):
       self.hours = hours
       self.minutes = minutes

   def addTime(self, t2):
       t = Time(0, 0)
       t.hours = self.hours + t2.hours
       t.minutes = self.minutes + t2.minutes
       if t.minutes >= 60:
           t.hours += 1
           t.minutes -= 60
       return t

   def displayTime(self):
       print(str(self.hours) + ":" + str(self.minutes))

   def displayMinute(self):
       print(self.hours * 60 + self.minutes)

# Create objects
t1 = Time(2, 50)
t2 = Time(1, 20)

# Add time
t = t1.addTime(t2)

# Display time
t.displayTime()

# Display minutes
t1.displayMinute()
