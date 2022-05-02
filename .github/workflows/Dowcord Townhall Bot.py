import discord
import datetime
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    
    if message.content.startswith('#schedule'):                                     #Enables War Automate Schedule
        await message.channel.send('War Schedule is Enabled')
        status = "Enabled"
        
        while(True):                                                                #Infinite Loop
            while(True):                                                            #WoE time schedule
                time = datetime.datetime.now().strftime("%H:%M")                    #Get time of the day
                day = datetime.datetime.now().strftime("%A")                        #Get day of the week
                if time == "18:30" and day == "Thursday":                           #Enter Time for the Announcement
                    await message.channel.send('@everyone WoE in 30 minutes')
                    break
            
            
            while(True):                                                            #WoC time schedule
                time = datetime.datetime.now().strftime("%H:%M")                    #Get time of the day
                day = datetime.datetime.now().strftime("%A")                        #Get day of the week
                if time == "18:30" and day == "Sunday":                             #Enter Time for the Announcement
                    await message.channel.send('@everyone WoC in 30 minutes')
                    break
    
    
    if message.content.startswith('#status'):
        status = "Disabled"
        if status == "Enabled":
            await message.channel.send('Enabled')
        
        else:
            await message.channel.send('Disabled')  
    
    return
  client.run(TOKEN)
