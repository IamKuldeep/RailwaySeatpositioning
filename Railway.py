print ("welcome  to Railway enquiry System._/\_")
name = input("What's your name?:-")
x = int(input("Please enter seat number:-"))
if x>72:
   print (name," Invalid Seat Number!! Try Again..")
elif x%8==0:
   print (name," your seat no.",x," is Side Upper Berth. in front of ",(x-1))
elif (x+1)%8==0:
   print (name," your seat no.",x," is Side Lower Berth. in front of ",(x+1))
elif (x+2)%8==0:
   print (name," your seat no.",x," is  Upper Berth facing towards engine. in front of ",(x-3))
elif (x+3)%8==0:
   print (name," your seat no.",x," is Middle Berth facing towards engine. in front of ",(x-3))
elif (x+4)%8==0:
   print (name," your seat no.",x," is Lower Berth facing towards engine. in front of ",(x-3))
elif (x+5)%8==0:
   print (name," your seat no.",x," is Lower Berth facing opposite engine. in front of ",(x+3))
elif (x+6)%8==0:
   print (name," your seat no.",x," is Middle Berth facing opposite engine. in front of ",(x+3))
else:
   print (name," your seat no.",x," is Upper Berth facing opposite engine. in front of ",(x+3))
