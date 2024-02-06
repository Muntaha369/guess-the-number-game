import random
comp_num=random.randint(0,100)
guess=None
attempts=0
while True:
 try:
  guess=int(input("guess a no. between 1 to 100 : "))
  attempts+=1
  if guess<0 or guess>100:
     print("guess between 1 and 100 only")
  elif comp_num==guess:
     print("woo hoo you guessed in" ,attempts,"attempts")
     break
    
  elif comp_num<guess:
     print("guess lower")
    
  elif comp_num>guess:
     print("guess higher")
    
  print(attempts,"attempt")
 except ValueError:
   print("enter number's only")
 

