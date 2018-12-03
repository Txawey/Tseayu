# -*- coding: utf-8 -*-
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from datetime import timedelta
import asyncio
import time

Tseayu = discord.Client()  # Initialise Client
tseayu = commands.Bot(command_prefix="?")  # Initialise client bot

versionnumber="1.5.0"
timezone=timedelta(hours=-5)

@tseayu.event
async def on_ready():
    # This will be called when the bot connects to the server
    print("Tse'ayu alaksi lu. O_O")

## Quit command
@tseayu.command(name='ftangnga')
async def botquit(ctx):
    await ctx.send("-_- oeri nari tstu soli set")
    await tseayu.close()
    await Tseayu.close()
    quit()

## Version
@tseayu.command()
async def version(ctx):
    displayversion=["Version: ", versionnumber]
    await ctx.send(''.join(displayversion))

## Timestamp Test
@tseayu.command()
async def time(ctx):
    shift=ctx.message.created_at+timezone
    await ctx.send("Date is %s EST" % shift.strftime("%Y-%m-%d %H:%M:%S"))

@tseayu.command()
async def rolelist(ctx):
    learningRoleNames = ["Sngä'iyu","Numeyu","Tsulfätunay","Tsulfätu"]
    modRoleNames = ["Kenongyu","Eyktan","Olo'eyktan"]
    teacherRoleNames = ["Srungsiyu","Karyunay","Karyu"]
    learningRoles = []
    modRoles = []
    teacherRoles = []
    extraRoles = []
    allRoles=ctx.guild.roles
    for role in allRoles:
        if role.name in learningRoleNames:
            learningRoles.append(role)
        elif role.name in modRoleNames:
            modRoles.append(role)
        elif role.name in teacherRoleNames:
            teacherRoles.append(role)
        elif role.name == "'Eylan":
            eylanRole = role
        elif role.name != "@everyone":
            extraRoles.append(role)
    await ctx.send("O_O Learning Roles: ")
    for role in learningRoles:
        await ctx.send(role.name)
    await ctx.send("O_O Teaching Roles: ")
    for role in teacherRoles:
        await ctx.send(role.name)
    await ctx.send("O_O Moderation Roles: ")
    for role in modRoles:
        await ctx.send(role.name)
    await ctx.send("O_O Eylan Role: ")
    await ctx.send(eylanRole)
    await ctx.send("O_O Extra Roles: ")
    for role in extraRoles:
        await ctx.send(role.name)

## Member Census
@tseayu.command()
async def census(ctx):
    learningRoleNames = ["Sngä'iyu","Numeyu","Tsulfätunay","Tsulfätu"]
    modRoleNames = ["Kenongyu","Eyktan","Olo'eyktan"]
    teacherRoleNames = ["Srungsiyu","Karyunay","Karyu"]
    learningRoles = []
    countlRoles = []
    modRoles = []
    countmRoles = []
    teacherRoles = []
    counttRoles = []
    extraRoles = []
    counteRoles = []
    allRoles=ctx.guild.roles
    for role in allRoles:
        if role.name in learningRoleNames:
            learningRoles.append(role)
            countlRoles.append(0)
        elif role.name in modRoleNames:
            modRoles.append(role)
            countmRoles.append(0)
        elif role.name in teacherRoleNames:
            teacherRoles.append(role)
            counttRoles.append(0)
        elif role.name == "'Eylan":
            eylanRole = role
        elif role.name != "@everyone":
            extraRoles.append(role)
            counteRoles.append(0)
        else:
            everyone = role
    allMembers=ctx.guild.members
    ## initialize all other counters:
    numLearners = 0
    numTeachers = 0
    numMods = 0
    numEylan = 0
    numExtra = 0
    numElse = 0
    numdiffLearners = 0
    numdiffTeachers = 0
    numdiffMods = 0
    numdiffExtra = 0
    for member in allMembers:
        everyonetest = 0
        numdiffLearnersTest = 0
        numdiffTeachersTest = 0
        numdiffModsTest = 0
        numdiffExtraTest = 0
        for role in member.roles:
            if role in learningRoles:
                numLearners += 1
                if not numdiffLearnersTest:
                    numdiffLearners += 1
                    numdiffLearnersTest = 1000
                everyonetest = 1
                i = 0
                for testrole in learningRoles:
                    if testrole == role:
                        countlRoles[i] += 1
                    i += 1
            elif role in teacherRoles:
                numTeachers += 1
                if not numdiffTeachersTest:
                    numdiffTeachers += 1
                    numdiffTeachersTest = 1000
                everyonetest = 1
                i = 0
                for testrole in teacherRoles:
                    if testrole == role:
                        counttRoles[i] += 1
                    i += 1
            elif role in modRoles:
                numMods += 1
                if not numdiffModsTest:
                    numdiffMods += 1
                    numdiffModsTest = 1000
                everyonetest = 1
                i = 0
                for testrole in modRoles:
                    if testrole == role:
                        countmRoles[i] += 1
                    i += 1
            elif role in extraRoles:
                numExtra += 1
                if not numdiffExtraTest:
                    numdiffExtra += 1
                    numdiffExtraTest = 1000
                everyonetest = 1
                i = 0
                for testrole in extraRoles:
                    if testrole == role:
                        counteRoles[i] += 1
                    i += 1
            elif role == eylanRole:
                numEylan += 1
                everyonetest = 1
        if everyonetest == 0:
            numElse += 1
    await ctx.send("O_O lu hasey")
    with open("census.csv",'w') as cen:
        cen.write("Learner Roles:\nTotal,%i\nTotal Different,%i\n" % (numLearners, numdiffLearners))
        i = 0
        for i in range(len(learningRoles)):
            cen.write("%s,%i\n" % (learningRoles[i].name, countlRoles[i]))
        cen.write("Teacher Roles:\nTotal,%i\nTotal Different,%i\n" % (numTeachers, numdiffTeachers))
        i = 0
        for i in range(len(teacherRoles)):
            cen.write("%s,%i\n" % (teacherRoles[i].name, counttRoles[i]))
        cen.write("Moderation Roles:\nTotal,%i\nTotal Different,%i\n" % (numMods, numdiffMods))
        i = 0
        for i in range(len(modRoles)):
            cen.write("%s,%i\n" % (modRoles[i].name, countmRoles[i]))
        cen.write("Other Roles:\nTotal,%i\nTotal Different,%i\n" % (numExtra, numdiffExtra))
        i = 0
        for i in range(len(extraRoles)):
            cen.write("%s,%i\n" % (extraRoles[i].name, counteRoles[i]))
        cen.write("Eylan Role:\nTotal,%i\n" % numEylan)
        cen.write("Roleless:\nTotal,%i\n" % numElse)
    await ctx.send("O_O Summary:")
    await ctx.send(file=discord.File('census.csv'))
    


## Message Search
@tseayu.command(name='oeltsattsolea')
async def ott(ctx):
    testMembers=[]
    testMembersS=[]
    testMembersN=[]
    await ctx.send("O_O oel frakemit tse'a")
    currentDate = ctx.message.created_at
    previousDate = currentDate - timedelta(days=90)
    allMembers = ctx.guild.members
    learningRoleNames = ["Sngä'iyu","Numeyu","Tsulfätunay","Tsulfätu"]
    modRoleNames = ["Kenongyu","Eyktan","Olo'eyktan"]
    teacherRoleNames = ["Srungsiyu","Karyunay","Karyu"]
    learningRoles = []
    modRoles = []
    teacherRoles = []
    allRoles=ctx.guild.roles
    for role in allRoles:
        if role.name in learningRoleNames:
            learningRoles.append(role)
        elif role.name in modRoleNames:
            modRoles.append(role)
        elif role.name in teacherRoleNames:
            teacherRoles.append(role)
        elif role.name == "'Eylan":
            eylanRole = role
    if any(role in ctx.message.author.roles for role in modRoles):
        await ctx.send("O_O lu fìtseng %ia hapxìtu" % len(allMembers))
        for member in allMembers:
            if any(role in member.roles for role in learningRoles) and not any(role in member.roles for role in modRoles):
                for role in member.roles:
                    if role == learningRoles[0]:
                        testMembersS.append(member)
                    elif role == learningRoles[1]:
                        testMembersN.append(member)
        allChannels = ctx.guild.text_channels
        testMembers.extend(testMembersN)
        for member in testMembersS:
            if member not in testMembers:
                testMembers.append(member)
        await ctx.send("O_O fmeretok %ia hapxìtut" % len(testMembers))
        #Test Name Sorting:
    ##    for role in learningRoles:
    ##        await ctx.send(role.name)
    ##    for role in teacherRoles:
    ##        await ctx.send(role.name)
    ##    for role in modRoles:
    ##        await ctx.send(role.name)
    ##    await ctx.send(eylanRole)
        CatNames=["Lì'fyaolo'","Lì'fya leNa'vi","Aylì'fya Alahe","Mokri","NCI","Lerngruppe"]
        testChannels = []
        for channel in allChannels:
            if channel.category.name in CatNames:
                testChannels.append(channel)
        await ctx.send("O_O fmeretok faysyänel:")
        for channel in testChannels:
            await ctx.send("%s" % channel.name)
            
        
        
        idleMembers = []
        seraMembers = []
        seraTimes = []
        for singleMember in testMembers:
            counter = 0
            for channel in testChannels:
                async for message in channel.history(limit = None, after = previousDate, reverse = False):
                    if message.author==singleMember:
                        counter += 1
                        if counter == 1:
                            timezoneshift=message.created_at+timezone
                            seraMembers.append(singleMember.display_name)
                            seraTimes.append(timezoneshift.strftime("%Y-%m-%d %H:%M:%S"))
            if counter == 0:
                idleMembers.append(singleMember)
            #await ctx.send(counter)
        await ctx.send("O_O lu hasey")
        rolesMoved=[]
        if idleMembers == []:
            await ctx.send("O_O frapo sereia")
        else:
            await ctx.send("O_O faysute ke sola:")
            for member in idleMembers:
                await ctx.send(member.display_name)
                rolesMoved.append(member.roles)
    #            await member.edit(roles=[eylanRole])
            await ctx.send(file=discord.File('youletmedownson.jpg'))
            with open('idlemembers.csv', 'w') as idlemem:
                idleNumber = len(idleMembers)
                for j in range(idleNumber):
                    idlemem.write("%s,Roles Moved:," % idleMembers[j].display_name)
                    jroles=rolesMoved[j]
                    for i in range(len(jroles)):
                        if i != 0:
                            idlemem.write("%s," % jroles[i].name)
                    idlemem.write("\n")
            await ctx.send("O_O puk a fraysute a ke sola:")
            await ctx.send(file=discord.File('idlemembers.csv'))
        with open('report.csv', 'w') as f:
            seraNumber = len(seraMembers)
            for i in range(seraNumber):
                f.write("%s, " % seraMembers[i])
                f.write("%s\n" % seraTimes[i])
        await ctx.send("O_O puk a fraysute a sera:")
        await ctx.send(file=discord.File('report.csv'))
    else:
        await ctx.send("O_O ...slä nga ke tsun tsive'a")
# Replace token with your bots token
tseayu.run("NTEzNzg4MDYyOTI5NTE4NjE1.DuPDLg.NR_pY4UFZzCMmxfTOH4i9zhVHrc")
