#The Ski Trip
#this game is a fun choose your own adventure type game with many possible outcomes. 
#The decisions are either decided through user input or a randomized dice roll that happens automatically
import random
import time
dice = [1,2,3,4,5,6]
diceimage = ["_________\n|       |\n|   o   |\n|       |\n--------- \n","_________\n|  o    |\n|       |\n|     o |\n---------\n" , "_________\n|  o    |\n|   o   |\n|     o |\n---------\n","_________\n| o   o |\n|       |\n| o   o |\n---------\n","_________\n| o   o |\n|   o   |\n| o   o |\n---------\n","_________\n| o   o |\n| o   o |\n| o   o |\n---------\n"]
def story():
  print("After a long week of work, you and your friend Jordan decide to reward yourselves with a beautiful ski vacation at Mount Tremblant.")
  time.sleep(2)
  print("After a full day of having fun, you and Jordan are just relaxing in front of the fire, when suddenly they ask you to go on a late night ski trip")
  time.sleep(5)
  trip = input("Do you want to go on a late-night ski trip (Y/N)?")
  if trip == "Y":
    print (" You guys go on a couple runs when the wind starts to pick up and a snowstorm starts. You ask Jordan if you guys should head home. This will be decided through a dice roll.")
    time.sleep(5)
    home = random.choice(dice)
    if home <= 4:
      print ( "You rolled a " , home, "\n", diceimage[home-1] , "Since you rolled between a 1 and a 4 Jordan has decided that you guys will stay on the ski hill")
      time.sleep(3)
      print("The storm suddenly gets really bad and its impossible to see anything on the ski slopes. Eventually you find your way into the forest and you realize that Jordan is nowhere to be seen")
      time.sleep(4)
      fork = input("You come across a fork in the path, do you go right or left?")
      if fork == "right":
        print("After walking through the snow for about 2 minutes, you eventually see the light of your cabin and make your way back inside")
        time.sleep(2)
        print ("You go and sit in front of the fireplace to warm up. After about an hour, the snow outside gets really heavy and the winds continue to become stronger.")
        time.sleep(2)
        print ("Eventually, the light flickers and the power goes out. You go to check the fuse box")
        time.sleep(5)
        see = input("Do you see the large armchair in your path (Y/N)?")
        if see == "Y":
          print("You reach the fuse box with no issues.")
        if see == "N":
          print("You stub your toe really hard and the bone looks out of place. You hobble over to the fuse box.")
          time.sleep(2)
          print ("You see that the fuse box is completely fried. You faintly remember your parents teaching you what to do when the power goes out.")
        elec = input("Do you go and try to fix the fuse box (Y/N)?")
        if elec == "Y":
          print ("It seems that there are some loose wires and you get electrocuted. You are unable to continue. You lost the game :(")
        if elec == "N":
          print ("You decide to make the smart decision and try and look around for something useful. As you’re on the ground searching, you come across a tuft of hair.")
          time.sleep(3)
          print ("As you lean down to further inspect, you hear a huge crash from upstairs. Looking around for anything you could use to protect yourself, you see 2 items.")
          time.sleep(5)
          weapon = input("Do you take the rake or do you take the baseball bat (R/B)?")
          print("You quietly climb up the stairs with your chosen weapon in hand. You look in disbelief as you see Jordan standing there with wild eyes, they don’t look like their usual selves.")
          time.sleep(3)
          print("You hide your weapon behind your back as they grab you by the hand and take you upstairs.")
          time.sleep(2)
          fight = input("Do you try and fight Jordan on your way upstairs (Y/N)?")
          if fight == "Y":
            print ("Smart weapon choice! You hit them on the head with it which gives you enough time to escape. You won the game :)")
          if fight == "N":
            print ("You are led into a room with 3 sections. Jordan forces you to pick which way you would like to be hurt.")
            time.sleep(2)
            torture = input("Do you choose a) listening to Justin Bieber so loud your ears bleed, b) the electric chair, c) getting stung by 1000 bees (a/b/c)?")
            if torture == "a":
              print ("The noise is so loud it permanently ruptures your eardrums and you are in immense pain. You are unable to continue. You lost the game :(")
            if torture == "b":
              print ("You hesitantly sit on the chair but as Jordan goes to turn it on, you remember the power is out and that it is unable to harm you.")
              time.sleep(2)
              print ("You reach over, grab your weapon that you brought and hit them on the head which gives you enough time to escape. You won the game :)")
            if torture == "c":
              print ("The pain of all the bee stings is too much for you to handle. You are unable to continue. You lost the game :(")
      elif fork == "left":
        print("After walking for about two minutes you hear a large crash near you")
        time.sleep(2)
        snow = input("Do you continue along this path (Y/N)?")
        if snow == "Y":
          print ("After a short period of time, the route becomes more familiar and you eventually see the light of your cabin and make your way back inside")
          time.sleep(2)
          print ("You go and sit in front of the fireplace to warm up. After about an hour, the snow outside gets really heavy and the winds continue to become stronger.")
          time.sleep(2)
          print ("Eventually, the light flickers and the power goes out. You go to check the fuse box")
          time.sleep(5)
          see = input("Do you see the large armchair in your path (Y/N)?")
          if see == "Y":
            print("You reach the fuse box with no issues.")
          if see == "N":
            print("You stub your toe really hard and the bone looks out of place. You hobble over to the fuse box.")
            time.sleep(2)
            print ("You see that the fuse box is completely fried. You faintly remember your parents teaching you what to do when the power goes out.")
          elec = input("Do you go and try to fix the fuse box (Y/N)?")
          if elec == "Y":
            print ("It seems that there are some loose wires and you get electrocuted. You are unable to continue. You lost the game :(")
          if elec == "N":
            print ("You decide to make the smart decision and try and look around for something useful. As you’re on the ground searching, you come across a tuft of hair.")
            time.sleep(3)
            print ("As you lean down to further inspect, you hear a huge crash from upstairs. Looking around for anything you could use to protect yourself, you see 2 items.")
            time.sleep(5)
            weapon = input("Do you take the rake or do you take the baseball bat (R/B)?")
            print("You quietly climb up the stairs with your chosen weapon in hand. You look in disbelief as you see Jordan standing there with wild eyes, they don’t look like their usual selves.")
            time.sleep(3)
            print("You hide your weapon behind your back as they grab you by the hand and take you upstairs.")
            time.sleep(2)
            fight = input("Do you try and fight Jordan on your way upstairs (Y/N)?")
            if fight == "Y":
              print ("Smart weapon choice! You hit them on the head with it which gives you enough time to escape. You won the game :)")
            if fight == "N":
              print ("You are led into a room with 3 sections. Jordan forces you to pick which way you would like to be hurt.")
              time.sleep(2)
              torture = input("Do you choose a) listening to Justin Bieber so loud your ears bleed, b) the electric chair, c) getting stung by 1000 bees (a/b/c)?")
              if torture == "a":
                print ("The noise is so loud it permanently ruptures your eardrums and you are in immense pain. You are unable to continue. You lost the game :(")
              if torture == "b":
                print ("You hesitantly sit on the chair but as Jordan goes to turn it on, you remember the power is out and that it is unable to harm you.")
                time.sleep(2)
                print ("You reach over, grab your weapon that you brought and hit them on the head which gives you enough time to escape. You won the game :)")
              if torture == "c":
                print ("The pain of all the bee stings is too much for you to handle. You are unable to continue. You lost the game :(")
        if snow == "N":
          print("After you turned around, you realize that the large bang was a huge block of ice dropped on the path you came from.")
          time.sleep(3)
          print("Another block of ice falls on you and you are severely injured.")
          time.sleep(2)
          print("You are unable to continue")
          time.sleep(2)
          print("You have lost the game :(")
    elif home >= 5:
      print ("You rolled a " , home , "\n", diceimage[home-1], "Since you rolled between a 5 and a 6, Jordan has decided that you guys will go home")
      time.sleep(3)
      print ("Jordan suddenly becomes crazed, you are unsure why.")
      time.sleep(3)
      print("They start screaming and foaming at the mouth. It looks like they have bitten by a creature with rabies! Jordan suddenly lunges at you!")
      time.sleep(3)
      print ("Your next dice roll will determine if you are able to dodge the attack.")
      time.sleep(5)
      dodge = random.choice(dice)
      if dodge <=2:
          print ("You rolled a ", dodge ,"\n", diceimage[dodge-1], "Jordan bit you and now you are also infected with rabies and you are unable to continue, you have lost the game :(")
          time.sleep(10)
      elif dodge >=3:
          print ("You rolled a ", dodge ,"\n", diceimage[dodge-1], "You were able to dodge Jordan's attack and you run as fast as you can and eventually see the light of the cabin and slam the door shut.")
          time.sleep(2)
          print ("After about an hour hiding inside the cabin, the snow outside starts to get really heavy and the winds become stronger. Eventually the light flickers and the power goes out.")
          time.sleep(2)
          print ("You go check the fuse box in the dark. There's a flashlight nearby, your dice roll will determine if you are able to remember where it is.")
          light = random.choice(dice)
          if light <= 3:
            print ("You rolled a ", light ,"\n", diceimage[light-1], "You found the flashlight and reach the fuse box without any issues")
            time.sleep(2)
            print ("You see that the fuse box is completely fried. You faintly remember your parents teaching you what to do when the power goes out.")
            time.sleep(2)
            fix = input("Do you try to fix the fuse box? (Y/N)")
            if fix == "Y":
              print ("It seems that there are some loose wires and you get electrocuted. You are unable to continue. You lost the game :(")
            if fix == "N":
              print ("You decide to make the smart decision and try and look around for something useful. As you’re on the ground searching, you come across a tuft of hair.")
              time.sleep(2)
              print ("As you lean down to further inspect, you hear a huge crash from upstairs. Looking around for anything you could use to protect yourself, you see 2 items.")
              time.sleep(5)
              item = input("Do you take the rake or do you take the baseball bat? (R/B)")
              if item == "R":
                print ("You quietly climb up the stairs with the rake in hand. You look in disbelief as you see Jordan standing there with wild eyes, they don’t look like their usual selves.")
                time.sleep(2)
                print ("You hide the rake behind your back as they grab you by the hand and take you upstairs.")
                time.sleep(2)
              fight = input("Do you try and fight Jordan on your way upstairs (Y/N)?")
            if fight == "Y":
                print("Smart weapon choice! You hit them on the head with it which gives you enough time to escape. You won the game :)")
            elif fight == "N":
                  print ("You are led into a room with 3 sections. Jordan forces you to pick which way you would like to be hurt.")
                  time.sleep(2)
                  torture = input("Do you choose a) listening to Justin Bieber so loud your ears bleed, b) the electric chair, c) getting stung by 1000 bees (a/b/c)?")
                  if torture == "a":
                    print ("The noise is so loud it permanently ruptures your eardrums and you are in immense pain. You are unable to continue. You lost the game :(")
                  if torture == "b":
                    print ("You hesitantly sit on the chair but as Jordan goes to turn it on, you remember the power is out and that it is unable to harm you.")
                    time.sleep(2)
                    print ("You reach over, grab your weapon that you brought and hit them on the head which gives you enough time to escape. You won the game :)")
                  if torture == "c":
                    print ("The pain of all the bee stings is too much for you to handle. You are unable to continue. You lost the game :(")
            elif item == "B":
                print ("You quietly climb up the stairs with the baseball bat in hand. You look in disbelief as you see Jordan standing there with wild eyes, they don’t look like their usual selves.")
                time.sleep(2)
                print ("You hide the bat behind your back as they grab you by the hand and take you upstairs.")
                time.sleep(2)
                fight = input("Do you try and fight Jordan on your way upstairs (Y/N)?")
                if fight == "Y":
                  print ("Smart weapon choice! You hit them on the head with it which gives you enough time to escape. You won the game :)")
                elif fight == "N":
                  print ("You are led into a room with 3 sections. Jordan forces you to pick which way you would like to be hurt")
                  time.sleep(2)
                  torture = input("Do you choose a) listening to Justin Bieber so loud your ears bleed, b) the electric chair, c) getting stung by 1000 bees (a/b/c)?")
                  if torture == "a":
                    print ("The noise is so loud it permanently ruptures your eardrums and you are in immense pain. You are unable to continue. You lost the game :(")
                  if torture == "b":
                    print ("You hesitantly sit on the chair but as Jordan goes to turn it on, you remember the power is out and that it is unable to harm you.")
                    time.sleep(3)
                    print ("You reach over, grab your weapon that you brought and hit them on the head which gives you enough time to escape. You won the game :)")
                  if torture == "c":
                    print ("The pain of all the bee stings is too much for you to handle. You are unable to continue. You lost the game :(")
          elif light >-4:
            print ("You rolled a ", light ,"\n", diceimage[light-1], "Unable to find the flashlight you feel you way towards the fusebox when suddenly you trip over a chair and hit your head.")
            time.sleep(4)
            print ("You try to get up but are too dizzy to continue")
            time.sleep(2)
            print ("You lost the game :(")
  elif trip == "N":
    print ("You grab your favourite blanket, make some hot cocoa, and turn on the TV to watch some 'Grey's Anatomy'")
    time.sleep(2)
    print ("After about an hour, the snow outside gets really heavy and the winds continue to become stronger. Eventually, the light flickers and the power goes out. You go to check the fuse box")
    time.sleep(5)
    see = input("Do you see the large armchair in your path (Y/N)?")
    if see == "Y":
      print("You reach the fuse box with no issues.")
    if see == "N":
      print("You stub your toe really hard and the bone looks out of place. You hobble over to the fuse box.")
    time.sleep(3)
    print ("You see that the fuse box is completely fried. You faintly remember your parents teaching you what to do when the power goes out.")
    time.sleep(2)
    elec = input("Do you go and try to fix the fuse box (Y/N)?")
    if elec == "Y":
      print ("It seems that there are some loose wires and you get electrocuted. You are unable to continue. You lost the game :(")
    if elec == "N":
      print ("You decide to make the smart decision and try and look around for something useful. As you’re on the ground searching, you come across a tuft of hair.")
      time.sleep(3)
      print ("As you lean down to further inspect, you hear a huge crash from upstairs. Looking around for anything you could use to protect yourself, you see 2 items.")
      time.sleep(5)
      weapon = input("Do you take the rake or do you take the baseball bat (R/B)?")
      print ("You quietly climb up the stairs with your chosen weapon in hand. You look in disbelief as you see Jordan standing there with wild eyes, they don’t look like their usual selves.")
      time.sleep(3)
      print ("You hide your weapon behind your back as they grab you by the hand and take you upstairs.")
      time.sleep(2)
      fight = input("Do you try and fight Jordan on your way upstairs (Y/N)?")
      if fight == "Y":
        print ("Smart weapon choice! You hit them on the head with it which gives you enough time to escape. You won the game :)")
      if fight == "N":
        print ("You are led into a room with 3 sections. Jordan forces you to pick which way you would like to be hurt.")
        time.sleep(2)
        torture = input("Do you choose a) listening to Justin Bieber so loud your ears bleed, b) the electric chair, c) getting stung by 1000 bees (a/b/c)?")
        if torture == "a":
          print ("The noise is so loud it permanently ruptures your eardrums and you are in immense pain. You are unable to continue. You lost the game :(")
        if torture == "b":
          print ("You hesitantly sit on the chair but as Jordan goes to turn it on, you remember the power is out and that it is unable to harm you.")
          time.sleep(3)
          print ("You reach over, grab your weapon that you brought and hit them on the head which gives you enough time to escape. You won the game :)")
        if torture == "c":
          print ("The pain of all the bee stings is too much for you to handle. You are unable to continue. You lost the game :(")
story()
