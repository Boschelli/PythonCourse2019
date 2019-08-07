## Fill in the following methods for the class 'Clock'

# 12-hour clock with minutes and hours
class Clock:
    def __init__(self, hour, minutes):
        self.minutes = minutes + 60*hour
        self.hour = hour
    ## Print the time
    def __str__(self):
        # Calculates hours and minutes for output string
        hours=self.minutes//60
        minutes=self.minutes-(hours*60)
        return ("The time is %d:%02d"%(hours,minutes))
    ## Add time
    def __add__(self,minutes):
        self.minutes+=minutes
        # Checks for minute overflow
        if self.minutes > 1440:
            self.minutes-=1440*(self.minutes//1440)
    ## Subtract time
    def __sub__(self,minutes):
        self.minutes-=minutes
        # Checks for minute underflow
        if self.minutes < 0:
            self.minutes=1440+(self.minutes+1440*(abs(self.minutes)//1440))
    ## Are two times equal?
    def __eq__(self, other):
        if self.minutes == other.minutes:
            return True
        return False
    ## Are two times not equal?
    def __ne__(self, other):
        if self.minutes != other.minutes:
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
