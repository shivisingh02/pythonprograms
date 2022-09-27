#parameterized functions 
from email.policy import default
msg = ' this is my house '
def wordcount(msg):
    words = msg.split() 
    return len(words)
print(wordcount("this is time to go"))
print(msg.split())
# parameter style 
# required 
# default
# args/kwargs 
