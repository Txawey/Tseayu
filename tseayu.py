
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
import csv

Tseayu = discord.Client()  # Initialise Client
tseayu = commands.Bot(command_prefix="?")  # Initialise client bot

versionnumber="3.0"
versionname="\"'on atìtstewnga'\""
timezone=timedelta(hours=-5)
learningRoleNames = ["Sngä'iyu","Numeyu","Tsulfätunay","Tsulfätu"]
modRoleNames = ["Kenongyu","Eyktan","Olo'eyktan"]
teacherRoleNames = ["Srungsiyu","Karyunay","Karyu"]

@tseayu.event
async def on_ready():
    # This will be called when the bot connects to the server
    print("Tse'ayu alaksi lu. O_O")

## Join Logs:
@tseayu.event
async def on_member_join(member):
    if member.guild.id == 154318499722952704:
        testline = ["1950-01-01",0,0,0]
        with open('JoinLogs.csv','r',newline='') as joinlog:
            lines = csv.reader(joinlog)
            savedLines=[]
            for row in lines:
                savedLines.append(row)
                testline = row
                print(','.join(testline))
        year, month, day = map(int, testline[0].split('-'))
        testDate = date(year,month,day)
        testJoins = testline[1]
        testLeaves = testline[2]
        testrds = testline[3]
        currentDate = datetime.now().date()
        with open('JoinLogs.csv','w') as joinlogwrite:
            if currentDate == testDate:
                i = 0
                for row in savedLines:
                    i += 1
                    row[0] = str(row[0])
                    row[1] = int(row[1])
                    row[2] = int(row[2])
                    row[3] = int(row[3])
                    if i == len(savedLines):
                        row[1]+=1
                    joinlogwrite.write("%s,%i,%i,%i\n" % (row[0],row[1],row[2],row[3]))
            else:
                for row in savedLines:
                    joinlogwrite.write("%s,%i,%i,%i\n" % (row[0],row[1],row[2],row[3]))
                joinlogwrite.write("%s,%i,%i,%i\n" % (currentDate.strftime("%Y-%m-%d"),1,0,0))

@tseayu.event
async def on_member_remove(member):
    if member.guild.id == 154318499722952704:
        testline = ["1950-01-01",0,0,0]
        with open('JoinLogs.csv','r',newline='') as joinlog:
            lines = csv.reader(joinlog)
            savedLines=[]
            for row in lines:
                savedLines.append(row)
                testline = row
                print(','.join(testline))
        year, month, day = map(int, testline[0].split('-'))
        testDate = date(year,month,day)
        testJoins = testline[1]
        testLeaves = testline[2]
        testrds = testline[3]
        currentDate = datetime.now().date()
        with open('JoinLogs.csv','w') as joinlogwrite:
            if currentDate == testDate:
                i = 0
                for row in savedLines:
                    i += 1
                    row[0] = str(row[0])
                    row[1] = int(row[1])
                    row[2] = int(row[2])
                    row[3] = int(row[3])
                    if i == len(savedLines):
                        row[2]+=1
                        if member.joined_at.date()==currentDate:
                            row[3]+=1
                    joinlogwrite.write("%s,%i,%i,%i\n" % (row[0],row[1],row[2],row[3]))
            else:
                for row in savedLines:
                    joinlogwrite.write("%s,%i,%i,%i\n" % (row[0],row[1],row[2],row[3]))
                joinlogwrite.write("%s,%i,%i,%i\n" % (currentDate.strftime("%Y-%m-%d"),0,1,0))

## Display Join Logs
@tseayu.command()
async def joinlogs(ctx):
    ## Array Initialize
    learningRoles = []
    modRoles = []
    teacherRoles = []
    extraRoles = []
    allRoles=ctx.guild.roles

    ## Sort roles
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
    ## Check if mod.  If so, give join logs.
    if any(role in ctx.message.author.roles for role in modRoles):
        await ctx.send("O_O Join Logs:")
        await ctx.send(file=discord.File('JoinLogs.csv'))
    else:
        await ctx.send("O_O Kehe")

## Instructions Command
@tseayu.command()
async def pefya(ctx):
        ## Array Initialize
    learningRoles = []
    modRoles = []
    teacherRoles = []
    extraRoles = []
    allRoles=ctx.guild.roles

    ## Sort roles
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
    ## Check if mod.  If so, display instructions
    if any(role in ctx.message.author.roles for role in modRoles):
        Instructions = []
        ## List of Instructions
        Instructions.append('O_O Instructions (All Commands Require Kenongyu+ Unless Otherwise Stated):\n\n')
        Instructions.append('?pefya: This Menu.\n')
        Instructions.append('?ftangnga: Quit Bot (Owner Only)\n')
        Instructions.append('?version: Show Version Number\n?time: Display Time in EST.\n')
        Instructions.append('?sìltsan: Praise Me :D\n')
        Instructions.append('?rolelist: List All Roles On This Server\n')
        Instructions.append('?census: List Stats on Members in All Roles\n')
        Instructions.append('?search <UserID> <RoleType(l,m, or t)> <Date (yyyy-mm-dd or anything else for from member join date)>: Compiles and outputs all messages by the searched member into a .txt file\n')
        Instructions.append("?oeltsattsolea: Automated 'Eylan Migration (Eyktan+ Only)\n")
        Instructions.append('?joinlogs: Prints the current version of the join logs\n')

        ## Compile and Send
        PefyaSivar=''.join(Instructions)
        await ctx.send(PefyaSivar)

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
    displayversion=["Version:", versionnumber, versionname]
    await ctx.send(' '.join(displayversion))

## Timestamp Test
@tseayu.command()
async def time(ctx):
    shift=ctx.message.created_at+timezone
    await ctx.send("Date is %s EST" % shift.strftime("%Y-%m-%d %H:%M:%S"))

## Praise the Bot Command :D
@tseayu.command(name='sìltsan')
async def praise(ctx):
    await ctx.send("O_O tstunwi")

## List Roles
@tseayu.command()
async def rolelist(ctx):
    ## Array Initialize
    learningRoles = []
    modRoles = []
    teacherRoles = []
    extraRoles = []
    allRoles=ctx.guild.roles

    ## Sort roles
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
    ## Check if allowed.  If so, list all server roles in categories
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
    ## Initialize role arrays
    learningRoles = []
    countlRoles = []
    modRoles = []
    countmRoles = []
    teacherRoles = []
    counttRoles = []
    extraRoles = []
    counteRoles = []
    allRoles=ctx.guild.roles
    ## Sort Roles
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
    ## Check if allowed
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
        ## Increment all counters that correspond to each individual member's roles
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

        ## List all role data in csv file
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
    ## Role Sorting
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
    ## Mod Staff Check
    if any(role in ctx.message.author.roles for role in modRoles):
        ## Check if Search Member Exists
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
            ## Check for the role being searched for
            if RoleType in learnteach:
                testChannels = []
                for channel in allChannels:
                    if channel.category.name in LearningCatNames:
                        testChannels.append(channel)
                ## Check for date: else search from all time
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
                ## Check for date: else search from all time
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
    ## Initialize everything
    testMembers=[]
    testMembersS=[]
    testMembersN=[]
    donttest=[]
    allMembers = ctx.guild.members
    allowedRoleNames = ["Eyktan","Olo'eyktan"]
    learningRoles = []
    modRoles = []
    teacherRoles = []
    allowedRoles = []
    otherRoles = []
    allRoles=ctx.guild.roles
    await ctx.send("O_O oel frakemit tse'a")

    ## Set Date to Search From
    currentDate = ctx.message.created_at
    previousDate = currentDate - timedelta(days=90)
    ## Sort Roles
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
        else:
            otherRoles.append(role)

    ##Check for the allowed role
    if any(role in ctx.message.author.roles for role in allowedRoles):

        await ctx.send("O_O lu fìtseng %ia hapxìtu" % len(allMembers))
        ## Sort Out Members With Sngä'iyu or Numeyu and Ignore those With Mod/Teaching Roles or Higher Learning Roles
        for member in allMembers:
            if any(role in member.roles for role in learningRoles) and not any(role in member.roles for role in modRoles) and not any(role in member.roles for role in teacherRoles):
                for role in member.roles:
                    if role == learningRoles[0]:
                        testMembersS.append(member)
                    elif role == learningRoles[1]:
                        testMembersN.append(member)
                    elif role == learningRoles[2] or role == learningRoles[3]:
                        donttest.append(member)
        for member in testMembersN:
            if member not in donttest:
                testMembers.append(member)
        for member in testMembersS:
            if member not in testMembers:
                testMembers.append(member)
        await ctx.send("O_O fmeretok %ia hapxìtut" % len(testMembers))

        #Test Name Sorting:
        print("Learning Roles:")
        for role in learningRoles:
            print(role.name)
        print("Teaching Roles:")
        for role in teacherRoles:
            print(role.name)
        print("Mod Roles:")
        for role in modRoles:
            print(role.name)
        print("Eylan Role:")
        print(eylanRole)

        ## Sort out the channels to be tested
        CatNames=["Lì'fyaolo'","Lì'fya leNa'vi","Aylì'fya Alahe","Mokri","NCI","Lerngruppe"]
        allChannels = ctx.guild.text_channels
        testChannels = []
        for channel in allChannels:
            if channel.category.name in CatNames:
                testChannels.append(channel)
            elif channel.id == 406185289485123594:
                testChannels.append(channel)
        print("O_O fmeretok faytsyänelit:")
        for channel in testChannels:
            print("%s" % channel.name)

        ## Search for any messages by every member
        idleMembers = []
        seraMembers = []
        seraTimes = []
        rolesMoved=[]
        for channel in testChannels:
            async for message in channel.history(limit = None, after = previousDate, reverse = False):
                if message.author not in seraMembers and message.author in testMembers:
                    seraMembers.append(message.author)
        ## Edit all idle members to be 'Eylan (in addition to other roles)
        for member in testMembers:
            if member not in seraMembers:
                idleMembers.append(member)
                rolesMoved.append(member.roles)
                newRoles=[]
                for role in member.roles:
                    if role in otherRoles:
                        newRoles.append(role)
                newRoles.append(eylanRole)
                await member.edit(roles=newRoles)
        await ctx.send("O_O lu hasey")

        ## Check if there are no idle members, else output name, id, and moved roles to a csv file.
        if idleMembers == []:
            await ctx.send("O_O frapo sereia")
        else:
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

        ## List all members tested who are active in a csv.
        with open('report.csv', 'w', encoding="utf-8") as f:
            seraNumber = len(seraMembers)
            for i in range(seraNumber):
                try:
                    f.write("%s,%i\n" % (seraMembers[i].display_name,seraMembers[i].id))
                except UnicodeEncodeError:
                    f.write("UNNKNOWNUNICODE,%i\n" % seraMembers[i].id)
        await ctx.send("O_O puk a fraysute a sera:")
        await ctx.send(file=discord.File('report.csv'))
    else:
        await ctx.send("O_O ...slä nga ke tsun tsive'a")

# Replace token with your bots token
with open('token.txt', 'r') as token:
    tseayuToken=token.read()
tseayu.run(tseayuToken)
