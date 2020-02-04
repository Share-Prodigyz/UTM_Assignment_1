##############################################
# Author: Justin Sousa
# Class: CCT 111, Winter 2019
# Programming Assignment #1
# 10/02/19
#
# Description: This programming project will use the input and print functions, if statments, along with some simple mathematics for conversion. It purpose it to take a given percentage of speed and use it in the einstein factor to determine how long it would take to travel to certain things. 
# No sources to cite.
##############################################

import math 

def einstein_factor(velocity):
    '''Calculates the famous einstein factor that takes in the parameter velocity,
       and uses the set value of the speed of light (299,792,458), to determine the value of the 
       einstein factor it is 1 divided by the square root of 1 minus the velocity squared divided
       by the speed of light squared.
    '''
    speed_light = 299792458    
    einstein_factor.factor = 1 / (math.sqrt( 1 - (velocity ** 2 / speed_light ** 2 )))
    

def calculating_ship_weight():
    '''Calculates the weight of the ship by calling the variable - factor - from the function 
       einstein_factor.
    '''
    ship_weight = 70000
    if einstein_factor.factor == 1:
        new_ship_weight = round( ship_weight , 2 )
    elif einstein_factor.factor > 1:
        new_ship_weight = round( ship_weight * einstein_factor.factor , 2 )
    elif einstein_factor.factor < 1:
        print( "This is not possible") 
    print( "At this speed: \n    Weight of the shuttle is" , new_ship_weight )
    

def calculating_travel_times():
    '''Calculates the times for the ship to travel to each respective place, by dividing the base times for each place by the value of factor
       which is being obtained from the function einstein_factor. 
    '''
    alpha_cenauri = 4.3
    alpha_cenauri_new_time = round( alpha_cenauri / einstein_factor.factor, 2 ) 
    print('    Percieved time to travel to Alpha Cenauri is ' , alpha_cenauri_new_time , ' years' )    
    banarads_star = 6.0
    banarads_star_new_time = round(banarads_star / einstein_factor.factor , 2 )
    print('    Percieved time to travel to Banarad Star is ' , banarads_star_new_time , ' years' )      
    betelgeuse = 309
    betelgeuse_new_time = round(betelgeuse / einstein_factor.factor, 2 )
    print('    Percieved time to travel to Betelgeuse is ' , betelgeuse_new_time , ' years' )       
    andromeda_galaxy = 2000000
    andromeda_galaxy_new_time = round(andromeda_galaxy / einstein_factor.factor, 2 )
    print('    Percieved time to travel to Andromeda Galaxy is ' , andromeda_galaxy_new_time , ' years' )   


user_input_str = input("Please enter velocity (percentage of speed of light): " )
user_input_float = float(user_input_str)
speed_light = 299792458
user_velocity_aprox =  speed_light * ( user_input_float / 100 )
print('Ship is travelling at' , ( user_input_float) , '% of the speed of light' )


einstein_factor(user_velocity_aprox)
calculating_ship_weight()
calculating_travel_times()
