## Fill in the following methods for the class 'Clock'

# 12-hour clock with minutes and hours
class Clock:
    def __init__(self, hour, minutes):
        self.minutes = minutes + 60*hour
        self.hour = hour

    ## Print the time
    def __str__(self):
        # Creates initial time string
        hours=self.minutes//60
        minutes=self.minutes-(hours*60)
        time="%d:%02d"%(hours,minutes)
        # Returns formatted time
        return ("The time is %s"%time)


    ## Add time
    ## Don't return anything
    def __add__(self,minutes):
        self.minutes+=minutes
            # Checks if minutes overflow
        if self.minutes > 1440:
                # Sets the number of times minutes overflow (go over 60)
            m=self.minutes//1440
                # Adjusts minutes
            self.minutes-=1440*m


    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
        self.minutes-=minutes
        if self.minutes < 0:
            # Sets number of times minutes underflow (go under 0 in units of 60)
            m=abs(self.minutes)//1440
            # Adjusts minutes for underflow
            self.minutes+=1440*m
            # Turns negative minutes into positive form
            self.minutes=1440+self.minutes

    ## Are two times equal?
    def __eq__(self, other):
        if self.minutes == other.minutes and self.hour == other.hour:
            return True
        return False

    ## Are two times not equal?
    def __ne__(self, other):
        if self.minutes != other.minutes or self.hour != other.hour:
            return True
        return False

# Tests class creation
clocky_boi=Clock(0,0)
print(clocky_boi)

# Tests minute addition
clocky_boi+30
print(clocky_boi)

# Tests minute subtraction
clocky_boi-350000
print(clocky_boi)

# Tests clock comparison

# Checks if equal
clocky_boi1=Clock(12,0)
clocky_boi2=Clock(12,0)
print(clocky_boi1 == clocky_boi2)

# Checks if not-equal
clocky_boi3= Clock(1,35)
print(clocky_boi1 != clocky_boi3)
