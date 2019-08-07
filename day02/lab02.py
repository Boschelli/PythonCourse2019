## Fill in the following methods for the class 'Clock'

# 12-hour clock with minutes and hours
class Clock:
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour


    ## Print the time
    def __str__(self):
        return ("The time is %d minutes past %d" % (self.minutes,self.hour))


    ## Add time
    ## Don't return anything
    def __add__(self,minutes):
        self.minutes+=minutes
        # Adjusts time to fit 12-hour cycle
        self.adjust()


    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
        self.minutes-=minutes
        # Adjusts time to fit 12-hour cycle
        self.adjust()


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

    # Adjusts time to fit 12-hour cycle
    def adjust(self):
        # Variable to adjust both minutes and clocks
        m=0

        # Checks if minutes underflow
        if self.minutes < 0:
            # Sets number of times minutes underflow (go under 0 in units of 60)
            m=abs(self.minutes)//60
            # Adjusts minutes for underflow
            self.minutes+=60*m
            # Turns negative minutes into positive form
            self.minutes=60+self.minutes
            # Adjusts hours for lost minutes
            self.hour-=1+m
        # Checks if hours turn negative
        if self.hour < 1:
            # Finds number of times hours underflow (go under 0 in units of 60)
            m = abs(self.hour)//12
            # Adjusts hours for underflow
            self.hour+=12*m
            # Turns negative minutes into positive form
            self.hour=12+self.hour

        # Checks if minutes overflow
        if self.minutes > 59:
            # Sets the number of times minutes overflow (go over 60)
            m=self.minutes//60
            # Adjusts minutes
            self.minutes-=60*m
            # Adjusts hours for excess minutes
            self.hour+=m

        # Checks if hours overflow (go over 12)
        if self.hour > 12:
            # Sets number of times hours overflow
            m=self.hour//12
            # Adjusts hours to fit in 12 hour range
            self.hour-=12*m


# Tests class creation
clocky_boi=Clock(1,0)
print(clocky_boi)

# Tests minute addition
clocky_boi+30
print(clocky_boi)

# Tests minute subtraction
clocky_boi-61
print(clocky_boi)

# Tests clock comparison

# Checks if equal
clocky_boi1=Clock(12,0)
clocky_boi2=Clock(12,0)
print(clocky_boi1 == clocky_boi2)

# Checks if not-equal
clocky_boi3= Clock(1,35)
print(clocky_boi1 != clocky_boi3)
