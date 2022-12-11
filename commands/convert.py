import discord
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from commands import davinci as d, bot_math as bm
from dotenv import load_dotenv
load_dotenv()


def convert(number: int, unit1: str, unit2: str):
    if unit1 == 'm':
        # If the unit is kilometers
        if unit2 == 'km':
            # Convert the number
            result = number / 1000
        # If the unit is centimeters
        elif unit2 == 'cm':
            # Convert the number
            result = number * 100
        # If the unit is millimeters
        elif unit2 == 'mm':
            # Convert the number
            result = number * 1000
        # If the unit is micrometers
        elif unit2 == 'um':
            # Convert the number
            result = number * 1000000
        # If the unit is nanometers
        elif unit2 == 'nm':
            # Convert the number
            result = number * 1000000000
        # If the unit is miles
        elif unit2 == 'mi':
            # Convert the number
            result = number / 1609.344
        # If the unit is feet
        elif unit2 == 'ft':
            # Convert the number
            result = number * 3.28084
        # If the unit is inches
        elif unit2 == 'in':
            # Convert the number
            result = number * 39.3701
        # If the unit is yards
        elif unit2 == 'yd':
            # Convert the number
            result = number * 1.09361
        # If the unit is not one of the above
        else:
            # Return an embed that says the unit is invalid
            embed = discord.Embed(
                title = 'Invalid Unit',
                description = 'The unit you entered is invalid. Please enter one of the following units: km, cm, mm, um, nm, mi, ft, in, yd',
                color = discord.Color.red()
            )
            # Return the embed
            return embed
    # If the unit is kilometers
    elif unit1 == 'km':
        # If the unit is meters
        if unit2 == 'm':
            # Convert the number
            result = number * 1000
        # If the unit is centimeters
        elif unit2 == 'cm':
            # Convert the number
            result = number * 100000
        # If the unit is millimeters
        elif unit2 == 'mm':
            # Convert the number
            result = number * 1000000
        # If the unit is micrometers
        elif unit2 == 'um':
            # Convert the number
            result = number * 1000000000
        # If the unit is nanometers
        elif unit2 == 'nm':
            # Convert the number
            result = number * 1000000000000
        # If the unit is miles
        elif unit2 == 'mi':
            # Convert the number
            result = number / 1.609344
        # If the unit is feet
        elif unit2 == 'ft':
            # Convert the number
            result = number * 3280.84
        # If the unit is inches
        elif unit2 == 'in':
            # Convert the number
            result = number * 39370.1
        # If the unit is yards
        elif unit2 == 'yd':
            # Convert the number
            result = number * 1093.61
        # If the unit is not one of the above
        else:
            # Create an embed that says the unit is invalid
            embed = discord.Embed(
                title = 'Invalid Unit',
                description = 'The unit you entered is invalid. Please enter one of the following units: m, cm, mm, um, nm, mi, ft, in, yd',
                colour = discord.Colour.blue()
            )
            # Return the embed
            return embed
    # If the unit is centimeters
    elif unit1 == 'cm':
        # If the unit is meters
        if unit2 == 'm':
            # Convert the number
            result = number / 100
        # If the unit is kilometers
        elif unit2 == 'km':
            # Convert the number
            result = number / 100000
        # If the unit is millimeters
        elif unit2 == 'mm':
            # Convert the number
            result = number * 10
        # If the unit is micrometers
        elif unit2 == 'um':
            # Convert the number
            result = number * 10000
        # If the unit is nanometers
        elif unit2 == 'nm':
            # Convert the number
            result = number * 10000000
        # If the unit is miles
        elif unit2 == 'mi':
            # Convert the number
            result = number / 160934.4
        # If the unit is feet
        elif unit2 == 'ft':
            # Convert the number
            result = number / 30.48
        # If the unit is inches
        elif unit2 == 'in':
            # Convert the number
            result = number / 2.54
        # If the unit is yards
        elif unit2 == 'yd':
            # Convert the number
            result = number / 91.44
        # If the unit is not one of the above
        else:
            # Create an embed that says the unit is invalid
            embed = discord.Embed(
                title = 'Invalid Unit',
                description = 'The unit you entered is invalid. Please enter one of the following units: m, km, mm, um, nm, mi, ft, in, yd',
                colour = discord.Colour.blue()
            )
            # Return the embed
            return embed
    # If the unit is millimeters
    elif unit1 == 'mm':
        # If the unit is meters
        if unit2 == 'm':
            # Convert the number
            result = number / 1000
        # If the unit is kilometers
        elif unit2 == 'km':
            # Convert the number
            result = number / 1000000
        # If the unit is centimeters
        elif unit2 == 'cm':
            # Convert the number
            result = number / 10
        # If the unit is micrometers
        elif unit2 == 'um':
            # Convert the number
            result = number * 1000
        # If the unit is nanometers
        elif unit2 == 'nm':
            # Convert the number
            result = number * 1000000
        # If the unit is miles
        elif unit2 == 'mi':
            # Convert the number
            result = number / 1609344
        # If the unit is feet
        elif unit2 == 'ft':
            # Convert the number
            result = number / 304.8
        # If the unit is inches
        elif unit2 == 'in':
            # Convert the number
            result = number / 25.4
        # If the unit is yards
        elif unit2 == 'yd':
            # Convert the number
            result = number / 914.4
        # If the unit is not one of the above
        else:
            # Create an embed that says the unit is invalid
            embed = discord.Embed(
                title = 'Invalid Unit',
                description = 'The unit you entered is invalid. Please enter one of the following units: m, km, cm, um, nm, mi, ft, in, yd',
                colour = discord.Colour.blue()
            )
            # Return the embed
            return embed
    # If the unit is micrometers
    elif unit1 == 'um':
        # If the unit is meters
        if unit2 == 'm':
            # Convert the number
            result = number / 1000000
        # If the unit is kilometers
        elif unit2 == 'km':
            # Convert the number
            result = number / 1000000000
        # If the unit is centimeters
        elif unit2 == 'cm':
            # Convert the number
            result = number / 10000
        # If the unit is millimeters
        elif unit2 == 'mm':
            # Convert the number
            result = number / 1000
        # If the unit is nanometers
        elif unit2 == 'nm':
            # Convert the number
            result = number * 1000
        # If the unit is miles
        elif unit2 == 'mi':
            # Convert the number
            result = number / 1609344000
        # If the unit is feet
        elif unit2 == 'ft':
            # Convert the number
            result = number / 304800
        # If the unit is inches
        elif unit2 == 'in':
            # Convert the number
            result = number / 25400
        # If the unit is yards
        elif unit2 == 'yd':
            # Convert the number
            result = number / 914400
        # If the unit is not one of the above
        else:
            # Create an embed that says the unit is invalid
            embed = discord.Embed(
                title = 'Invalid Unit',
                description = 'The unit you entered is invalid. Please enter one of the following units: m, km, cm, mm, nm, mi, ft, in, yd',
                colour = discord.Colour.blue()
            )
            # Return the embed
            return embed
    
    # If the unit is nanometers
    elif unit1 == 'nm':
        # If the unit is meters
        if unit2 == 'm':
            # Convert the number
            result = number / 1000000000
        # If the unit is kilometers
        elif unit2 == 'km':
            # Convert the number
            result = number / 1000000000000
        # If the unit is centimeters
        elif unit2 == 'cm':
            # Convert the number
            result = number / 10000000
        # If the unit is millimeters
        elif unit2 == 'mm':
            # Convert the number
            result = number / 1000000
        # If the unit is micrometers
        elif unit2 == 'um':
            # Convert the number
            result = number / 1000
        # If the unit is miles
        elif unit2 == 'mi':
            # Convert the number
            result = number / 1609344000000
        # If the unit is feet
        elif unit2 == 'ft':
            # Convert the number
            result = number / 304800000
        # If the unit is inches
        elif unit2 == 'in':
            # Convert the number
            result = number / 25400000
        # If the unit is yards
        elif unit2 == 'yd':
            # Convert the number
            result = number / 914400000
        # If the unit is not one of the above
        else:
            # Create an embed that says the unit is invalid
            embed = discord.Embed(
                title = 'Invalid Unit',
                description = 'The unit you entered is invalid. Please enter one of the following units: m, km, cm, mm, um, mi, ft, in, yd',
                colour = discord.Colour.blue()
            )
            # Return the embed
            return embed

    # If the unit is miles
    elif unit1 == 'mi':
        # If the unit is meters
        if unit2 == 'm':
            # Convert the number
            result = number * 1609.344
        # If the unit is kilometers
        elif unit2 == 'km':
            # Convert the number
            result = number * 1.609344
        # If the unit is centimeters
        elif unit2 == 'cm':
            # Convert the number
            result = number * 160934.4
        # If the unit is millimeters
        elif unit2 == 'mm':
            # Convert the number
            result = number * 1609344
        # If the unit is micrometers
        elif unit2 == 'um':
            # Convert the number
            result = number * 1609344000
        # If the unit is nanometers
        elif unit2 == 'nm':
            # Convert the number
            result = number * 1609344000000
        # If the unit is feet
        elif unit2 == 'ft':
            # Convert the number
            result = number * 5280
        # If the unit is inches
        elif unit2 == 'in':
            # Convert the number
            result = number * 63360
        # If the unit is yards
        elif unit2 == 'yd':
            # Convert the number
            result = number * 1760
        # If the unit is not one of the above
        else:
            # Create an embed that says the unit is invalid
            embed = discord.Embed(
                title = 'Invalid Unit',
                description = 'The unit you entered is invalid. Please enter one of the following units: m, km, cm, mm, um, nm, ft, in, yd',
                colour = discord.Colour.blue()
            )
            # Return the embed
            return embed

    # If the unit is feet
    elif unit1 == 'ft':
        # If the unit is meters
        if unit2 == 'm':
            # Convert the number
            result = number / 3.281
        # If the unit is kilometers
        elif unit2 == 'km':
            # Convert the number
            result = number / 3281
        # If the unit is centimeters
        elif unit2 == 'cm':
            # Convert the number
            result = number * 30.48
        # If the unit is millimeters
        elif unit2 == 'mm':
            # Convert the number
            result = number * 304.8
        # If the unit is micrometers
        elif unit2 == 'um':
            # Convert the number
            result = number * 304800
        # If the unit is nanometers
        elif unit2 == 'nm':
            # Convert the number
            result = number * 304800000
        # If the unit is miles
        elif unit2 == 'mi':
            # Convert the number
            result = number / 5280
        # If the unit is inches
        elif unit2 == 'in':
            # Convert the number
            result = number * 12
        # If the unit is yards
        elif unit2 == 'yd':
            # Convert the number
            result = number / 3
        # If the unit is not one of the above
        else:
            # Create an embed that says the unit is invalid
            embed = discord.Embed(
                title = 'Invalid Unit',
                description = 'The unit you entered is invalid. Please enter one of the following units: m, km, cm, mm, um, nm, mi, in, yd',
                colour = discord.Colour.blue()
            )
            # Return the embed
            return embed

    # If the unit is inches
    elif unit1 == 'in':
        # If the unit is meters
        if unit2 == 'm':
            # Convert the number
            result = number / 39.37
        # If the unit is kilometers
        elif unit2 == 'km':
            # Convert the number
            result = number / 39370
        # If the unit is centimeters
        elif unit2 == 'cm':
            # Convert the number
            result = number * 2.54
        # If the unit is millimeters
        elif unit2 == 'mm':
            # Convert the number
            result = number * 25.4
        # If the unit is micrometers
        elif unit2 == 'um':
            # Convert the number
            result = number * 25400
        # If the unit is nanometers
        elif unit2 == 'nm':
            # Convert the number
            result = number * 25400000
        # If the unit is miles
        elif unit2 == 'mi':
            # Convert the number
            result = number / 63360
        # If the unit is feet
        elif unit2 == 'ft':
            # Convert the number
            result = number / 12
        # If the unit is yards
        elif unit2 == 'yd':
            # Convert the number
            result = number / 36
        # If the unit is not one of the above
        else:
            # Create an embed that says the unit is invalid
            embed = discord.Embed(
                title = 'Invalid Unit',
                description = 'The unit you entered is invalid. Please enter one of the following units: m, km, cm, mm, um, nm, mi, ft, yd',
                colour = discord.Colour.blue()
            )
            # Return the embed
            return embed

    # If the unit is yards
    elif unit1 == 'yd':
        # If the unit is meters
        if unit2 == 'm':
            # Convert the number
            result = number / 1.094
        # If the unit is kilometers
        elif unit2 == 'km':
            # Convert the number
            result = number / 1094
        # If the unit is centimeters
        elif unit2 == 'cm':
            # Convert the number
            result = number * 91.44
        # If the unit is millimeters
        elif unit2 == 'mm':
            # Convert the number
            result = number * 914.4
        # If the unit is micrometers
        elif unit2 == 'um':
            # Convert the number
            result = number * 914400
        # If the unit is nanometers
        elif unit2 == 'nm':
            # Convert the number
            result = number * 914400000
        # If the unit is miles
        elif unit2 == 'mi':
            # Convert the number
            result = number / 1760
        # If the unit is feet
        elif unit2 == 'ft':
            # Convert the number
            result = number * 3
        # If the unit is inches
        elif unit2 == 'in':
            # Convert the number
            result = number * 36
        # If the unit is not one of the above
        else:
            # Create an embed that says the unit is invalid
            embed = discord.Embed(
                title = 'Invalid Unit',
                description = 'The unit you entered is invalid. Please enter one of the following units: m, km, cm, mm, um, nm, mi, ft, in',
                colour = discord.Colour.blue()
            )
            # Return the embed
            return embed
        
    # If the unit is not one of the above
    else:
        # Create an embed that says the unit is invalid
        embed = discord.Embed(
            title = 'Invalid Unit',
            description = 'The unit you entered is invalid. Please enter one of the following units: m, km, cm, mm, um, nm, mi, ft, in, yd',
            colour = discord.Colour.blue()
        )
        # Return the embed
        return embed

    # Create an embed that says the result
    embed = discord.Embed(
        title = 'Result',
        description = f'{number} {unit1} is {result} {unit2}',
        colour = discord.Colour.blue()
    )
    # Return the embed
    return embed
