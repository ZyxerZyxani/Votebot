import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random

client = Bot(description="VoteBot By Zyxer", command_prefix="!", pm_help = False)

voters1 = []
voters = []
@client.event
async def on_ready():
    msg="Let's get VOTING!\nYou can only vote once and you can't change your vote. Send a message (a pm) to me that says\n!vote x\nwhere x is what you vote. You will get an ID back and that ID will be written next to the vote you cast, so you can check and confirm that your vote has been counted."
    await client.send_message(discord.Object(id='Insert channel id to send info on how to use this bot on'), msg)

@client.command(pass_context=True)
async def vote(ctx, x):
    vote = "{}".format(x) #Saves the vote a person sent
    auth = "{}".format(ctx.message.author.mention) #Saves the name of the one voting
    if auth in voters: #Checks if the one voting has already voted
#        async for msg in client.logs_from(ctx.message.channel):
#            await client.delete_message(msg)
        msg = "Your vote has already been cast"
        await client.send_message(ctx.message.author, msg) #Tells those that try to vote more than once that they have already voted
    else :
        voterid = random.randint(0, 1000000)# generates a random number from 0-1000000 to use as an ID so the voter can check and confirm that his/her vote has been counted
        while voterid in voterID:# Checks if the ID already exists as to not make any duplicate
            voterid = random.randint(0, 1000000)# Generates another ID if there is another identical ID number
        voterID.append(voterid)# Adds the ID to the list so it can later check if there is a duplicate
        voters.append(auth) #Adds the voters name to list, just to prevent someone from voting twice or more
        subject="votes"#      Change 'votes' to whatever you want the votefile to be called, for example {subject="MoreCheetos"}
        F = open(subject, 'a+') #defines 'F', now 'F' opens a textfile called votes, if such a textfile does not exist, it creates one
        F.write("{} {}\n".format(vote, voterid)) #Adds the vote to the bottom of the textfile 'F' opens. Location should be where this script is kept.
        F.close()
        msg = "Your vote has now been cast. Your votes ID is {}".format(voterid)
#        async for msg in client.logs_from(ctx.message.channel):
#            await client.delete_message(msg)
        await client.send_message(ctx.message.author, msg) #PMs the voter that their vote has been cast.

################################################################################################################
#@client.command(pass_context=True)
#async def vote1(ctx, x):#vote1 is what the bot listens for to apply the vote in this part, so '!vote' can be about one thing and '!vote1' can be about another thing
#    vote = "{}".format(x)
#    auth = "{}".format(ctx.message.author.mention)#This code surrounded by the sharps can be copied and pasted to create more simultaneous votes running at the same time. Remember to change what the bot listens for (vote1 in this example) and don't forget to change the name of the textfile (unless you are ok to mix the votes in one file)
#    if auth in voters1:#Don't forget to make a new list at the top and change the name of 'voters1' to the name of the new list if you copy this.
#        msg = "Your vote has already been cast"
#        await client.send_message(ctx.message.author, msg)
#    else :
#        voters1.append(auth)#need to change 'voters1' to the name of the new list, if you did copy and paste this code
#        subject="votes1"#change 'votes1' to something else to get the textfile that stores the votes in called something else
#        F = open(subject, 'a+')
#        F.write("{}\n".format(vote))
#        F.close()
#        msg = "Your vote has now been cast."
#        await client.send_message(ctx.message.author, msg)
##################################################################################################################
#I haven't tested using copy of the code so I cannot guarantee that it will work flawlessly. Add a '#' at the start of every line to comment it out, to disable the line so to speak.
#
#
#
#@client.command(pass_context=True)
#async def sdeck(ctx):
#    
#@client.command(pass_context=True)
#async def ldeck(ctx):
#    
#
#@client.command(pass_context=True)
#async def cdeck(ctx):

client.run('Insert your own token here')
