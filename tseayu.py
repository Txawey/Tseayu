
# -*- coding: utf-8 -*-

import discord
from discord.ext.commands import Bot
from discord.ext import commands
from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime
import asyncio
import time

Tseayu = discord.Client()  # Initialise Client
tseayu = commands.Bot(command_prefix="?")  # Initialise client bot

versionnumber="2.0.0"
timezone=timedelta(hours=-5)
learningRoleNames = ["Sngä'iyu","Numeyu","Tsulfätunay","Tsulfätu"]
modRoleNames = ["Kenongyu","Eyktan","Olo'eyktan"]
teacherRoleNames = ["Srungsiyu","Karyunay","Karyu"]

@tseayu.event
async def on_ready():
    # This will be called when the bot connects to the server
    print("Tse'ayu alaksi lu. O_O")

## Quit command
@tseayu.command(name='ftangnga')
@commands.is_owner()
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

@tseayu.command(name='sìltsan')
async def praise(ctx):
    await ctx.send("O_O tstunwi")

@tseayu.command()
async def rolelist(ctx):
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
    if any(role in ctx.message.author.roles for role in modRoles):
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
    else:
        await ctx.send("O_O ke omum ngat")

## Member Census
@tseayu.command()
async def census(ctx):
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
    if any(role in ctx.message.author.roles for role in modRoles):
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
        with open("census.csv",'w',encoding="utf-8") as cen:
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
    else:
        await ctx.send("O_O ke smon nga")
    
## Individual Member Message Search
@tseayu.command()
async def search(ctx,searchee: int,RoleType,inputDate: str):
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
    if any(role in ctx.message.author.roles for role in modRoles):
        testMember = 0
        allMembers=ctx.guild.members
        for member in allMembers:
            if searchee == member.id:
                testMember = member
        
        if testMember:
            learnteach=['l','L','t','T']
            mod=['m','M']
            LearningCatNames=["Lì'fyaolo'","Lì'fya leNa'vi","Aylì'fya Alahe","Mokri","NCI","Lerngruppe"]
            allChannels = ctx.guild.text_channels
            if RoleType in learnteach:
                testChannels = []
                for channel in allChannels:
                    if channel.category.name in LearningCatNames:
                        testChannels.append(channel)
                try:
                    year, month, day = map(int, inputDate.split('-'))
                    searchFromDate = date(year,month,day)
                    searchFrom = datetime.combine(searchFromDate,datetime.min.time())
                    with open('membersummary.txt','w',encoding="utf-8") as summary:
                        summary.write('%s Message Summary:\nContent\tDate Sent\tChannel\n' % testMember.name)
                        for channel in testChannels:
                            async for message in channel.history(limit = None, after = searchFrom-timedelta(days=1) ,reverse = True):
                                if message.author == testMember:
                                    summary.write("%s\t%s\t%s\n" % (message.content, message.created_at.strftime("%Y-%m-%d %H:%M:%S"), channel.name))
                except ValueError:
                    with open('membersummary.txt','w',encoding="utf-8") as summary:
                        summary.write('%s Message Summary:\nContent\tDate Sent\tChannel\n' % testMember.name)
                        for channel in testChannels:
                            async for message in channel.history(limit = None, after=testMember.joined_at-timedelta(days=1), reverse = True):
                                if message.author == testMember:
                                    summary.write("%s\t%s\t%s\n" % (message.content, message.created_at.strftime("%Y-%m-%d %H:%M:%S"), channel.name))

                await ctx.send("O_O lu hasey")
                await ctx.send("O_O fì'u vurvi lu")
                await ctx.send(file=discord.File('membersummary.txt'))
            elif RoleType in mod:
                try:
                    year, month, day = map(int, inputDate.split('-'))
                    searchFromDate = date(year,month,day)
                    searchFrom = datetime.combine(searchFromDate,datetime.min.time())
                    with open('membersummary.txt','w',encoding="utf-8") as summary:
                        summary.write('%s Message Summary:\nContent\tDate Sent\tChannel\n' % testMember.name)
                        for channel in testChannels:
                            async for message in channel.history(limit = None, after = searchFrom-timedelta(days=1) ,reverse = True):
                                if message.author == testMember:
                                    summary.write("%s\t%s\t%s\n" % (message.content, message.created_at.strftime("%Y-%m-%d %H:%M:%S"), channel.name))
                except ValueError:
                    with open('membersummary.txt','w',encoding="utf-8") as summary:
                        summary.write('%s Message Summary:\nContent\tDate Sent\tChannel\n' % testMember.name)
                        for channel in testChannels:
                            async for message in channel.history(limit = None, after=testMember.joined_at-timedelta(days=1), reverse = True):
                                if message.author == testMember:
                                    summary.write("%s\t%s\t%s\n" % (message.content, message.created_at.strftime("%Y-%m-%d %H:%M:%S"), channel.name))
                await ctx.send("O_O lu hasey")
                await ctx.send("O_O fì'u vurvi lu")
                await ctx.send(file=discord.File('membersummary.txt'))
            else:
                await ctx.send("O_O ke omum tsapamrelvit")
        else:
            await ctx.send("O_O ke smon tsatute")
    else:
        await ctx.send("O_O ke smon nga")

## Idle Member Search
@tseayu.command(name='oeltsattsolea')
async def ott(ctx):
    testMembers=[]
    testMembersS=[]
    testMembersN=[]
    donttest=[]
    await ctx.send("O_O oel frakemit tse'a")
    currentDate = ctx.message.created_at
    previousDate = currentDate - timedelta(days=90)
    allMembers = ctx.guild.members
    allowedRoleNames = ["Eyktan","Olo'eyktan"]
    learningRoles = []
    modRoles = []
    teacherRoles = []
    allowedRoles = []
    allRoles=ctx.guild.roles
    for role in allRoles:
        if role.name in learningRoleNames:
            learningRoles.append(role)
        elif role.name in modRoleNames:
            modRoles.append(role)
            if role.name in allowedRoleNames:
                allowedRoles.append(role)
        elif role.name in teacherRoleNames:
            teacherRoles.append(role)
        elif role.name == "'Eylan":
            eylanRole = role
    if any(role in ctx.message.author.roles for role in allowedRoles):
        await ctx.send("O_O lu fìtseng %ia hapxìtu" % len(allMembers))
        for member in allMembers:
            if any(role in member.roles for role in learningRoles) and not any(role in member.roles for role in modRoles) and not any(role in member.roles for role in teacherRoles):
                for role in member.roles:
                    if role == learningRoles[0]:
                        testMembersS.append(member)
                    elif role == learningRoles[1]:
                        testMembersN.append(member)
                    elif role == learningRoles[2] or role == learningRoles[3]:
                        donttest.append(member)
        allChannels = ctx.guild.text_channels
        for member in testMembersN:
            if member not in donttest:
                testMembers.append(member)
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
            elif channel.id == 406185289485123594:
                testChannels.append(channel)
        print("O_O fmeretok faytsyänelit:"
        for channel in testChannels:
            print("%s" % channel.name)
            
        
        
        idleMembers = []
        seraMembers = []
        seraTimes = []
        rolesMoved=[]
        for channel in testChannels:
            async for message in channel.history(limit = None, after = previousDate, reverse = False):
                if message.author not in seraMembers and message.author in testMembers:
                    seraMembers.append(message.author)
        for member in testMembers:
            if member not in seraMembers:
                idleMembers.append(member)
                rolesMoved.append(member.roles)
                await member.edit(roles=[eylanRole])
##        for singleMember in testMembers:
##            counter = 0
##            for channel in testChannels:
##                async for message in channel.history(limit = None, after = previousDate, reverse = False):
##                    if message.author==singleMember:
##                        counter += 1
##                        if counter == 1:
##                            timezoneshift=message.created_at+timezone
##                            seraMembers.append(singleMember.display_name)
##                            seraTimes.append(timezoneshift.strftime("%Y-%m-%d %H:%M:%S"))
##                            break
##                if counter != 0:
##                    break
##            if counter == 0:
##                idleMembers.append(singleMember)
            #await ctx.send(counter)
        await ctx.send("O_O lu hasey")
        
        if idleMembers == []:
            await ctx.send("O_O frapo sereia")
        else:
##            await ctx.send("O_O faysute ke sola:")
##            for member in idleMembers:
##                await ctx.send(member.display_name)
##                rolesMoved.append(member.roles)
##    #            await member.edit(roles=[eylanRole])
##            await ctx.send(file=discord.File('youletmedownson.jpg'))
            with open('idlemembers.csv', 'w', encoding="utf-8") as idlemem:
                idleNumber = len(idleMembers)
                for j in range(idleNumber):
                    try:
                        idlemem.write("%s,%i,Roles Moved:," % (idleMembers[j].display_name,idleMembers[j].id))
                    except UnicodeEncodeError:
                        idlemem.write("UNKNOWNUNICODE,%i,Roles Moved:," % idleMembers[j].id)
                    jroles=rolesMoved[j]
                    for i in range(len(jroles)):
                        if i != 0:
                            idlemem.write("%s," % jroles[i].name)
                    idlemem.write("\n")
            await ctx.send("O_O puk a fraysute a ke sola:")
            await ctx.send(file=discord.File('idlemembers.csv'))
            await ctx.send(file=discord.File('youletmedownson.jpg'))
        with open('report.csv', 'w', encoding="utf-8") as f:
            seraNumber = len(seraMembers)
            for i in range(seraNumber):
                try:
                    f.write("%s,%i\n" % (seraMembers[i].display_name,seraMembers[i].id))
                except UnicodeEncodeError:
                    f.write("UNNKNOWNUNICODE,%i\n" % seraMembers[i].id)
                ##f.write("%s, " % seraMembers[i])
                ##f.write("%s\n" % seraTimes[i])
        await ctx.send("O_O puk a fraysute a sera:")
        await ctx.send(file=discord.File('report.csv'))
    else:
        await ctx.send("O_O ...slä nga ke tsun tsive'a")
# Replace token with your bots token
with open('token.txt', 'r') as token:
    tseayuToken=token.read()
tseayu.run(tseayuToken)
