#!/usr/bin/env python3

import random

while True:
    Total_Speed = 0
    Mean_Speed = 0
    Fast_Warnings_Parking = 0
    Slow_Warnings_Parking = 0
    Fast_Warnings_Street = 0
    Slow_Warnings_Street = 0
    Fast_Warnings_Freeway = 0
    Slow_Warnings_Freeway = 0
    Fast_Warnings_School = 0
    Slow_Warnings_School = 0
    Total_tickets = 0
    In_Limits = 0
    ticket = 0
    Money = 150
    Day = 1
    print('Welcome to Speeding Tickets Version 3')
    print('In this game we will have you drive in numerous zones')
    print('it is up to you to drive in these areas in an appropriate safe manner')
    print('Everytime you give a speed it is considered a turn or "day"')
    print('if you make it through all 25 "Days" you will beat the game')
    print('you have $', Money)
    while Day <= 25:
        ticket = 0
        zone = random.randint(1,4)
        if zone == 1:
            zonename = 'Parking Lot'  
        if zone == 2:
            zonename = 'Street'
        if zone == 3:
            zonename = 'Freeway'
        if zone == 4:
            zonename = 'School Zone'
        print('you are in a ',zonename) 
        speed = input('What speed do you go at? (mph): ')    
        while speed.isalpha() == True:
            speed = input('You did not give a number, please retry: ')
            if speed.isdigit == True:
                print('Thank you')
                break
        speed = int(speed)
        Total_Speed = Total_Speed + speed
        if zone == 1:
            if speed > 10:
                print('too fast, get ticketed')
                ticket = (speed - 7) * 5
                print('your ticket is $',ticket)
                Money  = Money - ticket
                Total_tickets = Total_tickets + 1
            if speed <= 10 and speed > 7 and Fast_Warnings_Parking > 3:
                print('I told you to slow down in the parking lots!')
                print('This is Warnng #', Fast_Warnings_Parking)
                print('I am sorry but I must ticket you')
                ticket = ((speed - 7) * (Fast_Warnings_Parking - 3)) * 5
                Total_tickets = Total_tickets + 1
                print('Your Ticket is $', ticket)
                Money = Money - ticket
            if speed <= 10 and speed > 7 and Fast_Warnings_Parking <= 3:
                print('you are going too fast, slow down, If I have too warn you again I may ticket you')
                Fast_Warnings_Parking = Fast_Warnings_Parking + 1 
            if speed <= 7 and speed > 5:
                print('good job staying in the unwritten speed limit')
                In_Limits = In_Limits + 1
            if speed <= 5 and speed > 4 and Slow_Warnings_Parking > 3:
                print('I warned you to pick up the pace in the Parking lots')
                print('This is Warnng #', Slow_Warnings_Parking)
                print('I am sorry but I must ticket you')
                Total_tickets = Total_tickets + 1
                ticket = ((7 - speed) * (Slow_Warnings_Parking - 3)) * 5
                print('Your Ticket is $', ticket)
                Money = Money - ticket
            if speed <= 5 and speed > 4:
                print('pick up the pace, not enough to ticket, but if I have to again I may ticket you')
                Slow_Warnings_Parking = Slow_Warnings_Parking + 1
            if speed <= 4:
                print('too slow, get ticketed')
                ticket = (4 - speed) * 5
                Money = Money - ticket
                print('Your ticket is $', ticket)
                Total_tickets = Total_tickets + 1
        if zone == 2:
            if speed > 60:
                print('too fast, get ticketed')
                ticket = (speed - 40) * 5
                print('your ticket is $',ticket)
                Money  = Money - ticket
                Total_tickets = Total_tickets + 1
            if speed <= 60 and speed > 50 and Fast_Warnings_Street > 3:
                print('I warned you to slow down in the streets')
                print('This is warning #',Fast_Warnings_Street,', I am sorry but I must ticket you')
                ticket = ((speed - 40) * (Fast_Warnings_Street - 3)) * 5
                print('Your ticket is $', ticket)
                Money = Money - ticket
                Total_tickets = Total_tickets + 1
            if speed <= 60 and speed > 50 and Fast_Warnings_Street <= 3:
                 print('you are going too fast, slow down, anymore and you would get ticketed, but if I have to warn you again I will')
                 Fast_Warnings_Street = Fast_Warnings_Street + 1
            if speed <= 50 and speed > 30:
                print('good job staying in the unwritten speed limit')
                In_Limits = In_Limits + 1
            if speed <= 30 and speed >20 and Slow_Warnings_Street > 3:
                print('I warned you to pick up the pace in the streets')
                print('This is warning #', Slow_Warnings_Street, ', I am sorry but I must ticket you.')
                ticket = ((40 - speed) * (Slow_Warnings_Street - 3)) * 5
                print('Your ticket is $',ticket)
                Money = Money - ticket
                Total_tickets = Total_tickets + 1
            if speed <= 30 and speed > 20 and Slow_Warnings_Street <= 3:
                print('pick up the pace, any slower and I ticket you, but if I have to keep warning you I will also ticket you')
                Slow_Warnings_Street = Slow_Warnings_Street + 1
            if speed <= 20:
                print('too slow, get ticketed')
                ticket = (30 - speed) * 5
                print('Your Ticket is $', ticket)
                Money = Money - ticket
                Total_tickets = Total_tickets + 1
        if zone == 3:
            if speed > 90:
                print('too fast, get ticketed')
                ticket = (speed - 90) * 5
                print('your ticket is $',ticket)
                Money  = Money - ticket
                Total_tickets = Total_tickets + 1
            if speed <= 90 and speed > 80 and Fast_Warnings_Freeway > 3:
                print('I warned you to slow down in the Freeway')
                print('This is warning #', Fast_Warnings_Freeway)
                print('I am sorry but I must ticket you')
                ticket = ((speed - 70) * (Fast_Warnings_Freeway - 3)) * 5
                print('Your ticket is $', ticket)
                Money = Money - ticket
                Total_tickets = Total_tickets + 1
            if speed <= 90 and speed > 80 and Fast_Warnings_Freeway <= 3:
                print('you are going too fast, slow down, anymore and you would get ticketed, but if I have to keep warning you I will ticket you')
                Fast_Warnings_Freeway = Fast_Warnings_Freeway + 1
            if speed <= 80 and speed > 60:
                print('good job staying in the unwritten speed limit')
                In_Limits = In_Limits + 1
            if speed <= 60 and speed > 45 and Slow_Warnings_Freeway > 3:
                print('I warned you to pick up the pace in the freeways')
                print('This is warning #', Slow_Warnings_Freeway)
                print('I am sorry but I must ticket you')
                ticket = ((70 - speed) * (Slow_Warnings_Freeway - 3)) * 5
                print('Your ticket is $',ticket)
                Money = Money - ticket
                Total_tickets = Total_tickets + 1
            if speed <= 60 and speed > 45 and Slow_Warnings_Freeway <= 3:
                print('pick up the pace, any slower, or if I must keep warning you, I ticket you,')
                Slow_Warnings_Freeway = Slow_Warnings_Freeway + 1
            if speed <= 45:
                print('too slow, get ticketed')
                ticket = (45 - speed) * 5
                print('your ticket is $', ticket)
                Money = Money - ticket
                Total_tickets = Total_tickets + 1
        if zone == 4:
            if speed > 45:
                print('too fast, get ticketed')
                ticket = (speed - 45) * 5
                print('your ticket is $',ticket)
                Money  = Money - ticket
                Total_tickets = Total_tickets + 1
            if speed <= 45 and speed > 30 and Fast_Warnings_School > 3:
                print('I warned you to slow down in the school zones')
                print('This is warning #', Fast_Warnings_School)
                print('I am sorry but I must ticket you')
                ticket = ((speed - 25) * (Fast_Warnings_School - 3)) * 5
                Total_tickets = Total_tickets + 1
            if speed <= 45 and speed > 30 and Fast_Warnings_School <= 3:
                print('you are going too fast, any faster, or if I have too keep warning you, you will get ticketed.')
                Fast_Warnings_School = Fast_Warnings_School + 1
            if speed <= 30 and speed >= 20:
                print('good job staying in the unwritten speed limit')
                In_Limits = In_Limits + 1
            if speed < 20 and speed >= 15 and Slow_Warnings_School > 3:
                print('I warned you to speed up in the School Zones')
                print('This is warning #',Slow_Warnings_School)
                print('I am sorry but I must ticket you')
                ticket = ((25 - speed) * (Slow_Warnings_School - 3))
                Total_tickets = Total_tickets + 1
                print('Your ticket is $', ticket)
            if speed < 20 and speed >= 15 and Slow_Warnings_School <= 3:
                print('pick up the pace, any slower, or if I have to keep warning you, you will gat ticketed')
                Slow_Warnings_School = Slow_Warnings_School + 1
            if speed <= 15:
                print('too slow, get ticketed')
                ticket = (15 - speed) * 5
                print('your ticket is $', ticket)
                Money = Money - ticket
                Total_tickets = Total_tickets + 1
        if Money > 0:
            print('Congratulations on Making it through Day ', Day, ' With $',Money, ' Remaining')
            print('Only ',25 - Day,' Days to go!')
            Day = Day + 1
        if Money <= 0:
            print('You Lose')
            Total_Warnings = Fast_Warnings_Freeway + Fast_Warnings_Parking + Fast_Warnings_School + Fast_Warnings_Street + Slow_Warnings_Freeway + Slow_Warnings_Parking + Slow_Warnings_School + Slow_Warnings_Street
            Mean_Speed = Total_Speed/Day
            print(Total_tickets,' Tickets')
            print(In_Limits, ' times in the speed limit')
            print(Total_Warnings, ' total warnings')
            print(Mean_Speed, 'mph average speed')
            Score = ((Day * In_Limits)/(Total_Warnings + Total_tickets)) - Mean_Speed
            if Score < 0:
                Score = 0
            print('Your Score is ', Score)
            Play_Again = input('Play Again? (y/n) ')
            if Play_Again == 'n' or Play_Again == 'N':
                print('Ok')
                quit()
            if Play_Again == 'y' or Play_Again == 'Y':
                break
    if Money > 0:
        Total_Warnings = Fast_Warnings_Freeway + Fast_Warnings_Parking + Fast_Warnings_School + Fast_Warnings_Street + Slow_Warnings_Freeway + Slow_Warnings_Parking + Slow_Warnings_School + Slow_Warnings_Street
        Mean_Speed = Total_Speed/Day
        print('Congratulations! You Win!')
        print('Remember that this is still an early version of the game so always be on the lookout for new updates')
        print('Thanks for Playing!')
        print(Money, '$ left')
        print(In_Limits, ' times in the speed limit')
        print(Total_tickets,' Tickets')
        print(Total_Warnings, ' total warnings')
        print(Mean_Speed, 'mph average speed')
        if Total_Warnings + Total_tickets == 0:
            Score = Score = ((Money + 25) * In_Limits) - Mean_Speed
        if Total_Warnings + Total_tickets != 0:
            Score = (((Money + 25) * In_Limits)/(Total_Warnings + Total_tickets)) - Mean_Speed
        if Score < 0:
            Score = 0
        print('Your Score is ', Score)
        print('Credits:')
        print('Speeding Tickets')
        print('An A.E.M. Media Game by Me')
        print('Original Concept: Me')
        print('Lead Programer: Me')
        print('All Other Programers: Me')
        print('Version 1 Prerelease Testers: Friends')
        print('Version 3 Prerelease Testers: Friend') 
        print('Written in Python through Visual Code Studio')
        print('Run in ZShell')
        print('A.E.M. Media')
        print('Are You Ready?')
        Play_Again = input('Play Again? (y/n) ')
        if Play_Again == 'n' or Play_Again == 'N':
            print('Ok')
            quit()