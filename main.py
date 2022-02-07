print('''
*******************************************************************************
       ________   ________    _________  ____________;_
      - ______ \ - ______ \ / _____   //.  .  ._______/
     / /     / // /     / //_/     / // ___   /
    / /     / // /     / /       .-'//_/|_/,-'
   / /     / // /     / /     .-'.-'
  / /     / // /     / /     / /
 / /     / // /     / /     / /
/ /_____/ // /_____/ /     / /
\________- \________-     /_/
*******************************************************************************
''')
print("Welcome 007!")
print("Your mission is to find the villian.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input("You are at a crossroad. Where do you want to go? Type 'up' or 'down' ").lower()
if direction == "up":
  survive = input("You have come to a dungeon. There's a tiger inside! Would you like to sing to it or leave the dugeon? ").lower()
  if survive == "sing":
    door = input("The tiger likes you and you can now leave the dungeon and find the villian! Which door leads to his office? ").lower()
    if door == "brown":
      print("The guards have killed you.")
    if door == "green":
      print("You found the the villian, well done. Mission accomplised!")
    if door == "white":
      print("Plants have attacked you and your oxygen has been snatched from you.")
  else:
    print("Attacked by tiger. No frosted flakes for you.")
else:
  print("Chased by monkeys, run for your life.")