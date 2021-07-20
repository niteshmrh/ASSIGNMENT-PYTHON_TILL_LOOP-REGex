"""
Q.1 WAP to input number of seconds and print it in form HH:MM:SS. Like for 4000
seconds it will be 01:06:40.
"""
def convert(seconds):
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%02d:%02d:%02d" % (hour, minutes, seconds)
      
n = 4000
print(convert(n))
