import asyncio
import discord
import bla

d = discord.Client()
bananenbrot = "277083383425794058"
vollkornbrot = "360859154249678858"
admins = ["277083383425794058", "360859154249678858"]


async def ex(args, message, d):
    try:
        ammount = int(args[0]) + 1 if len(args) > 0 else 2
    except:
        await d.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), descrition="Please enter a valid value for message ammount!"))
        return

    cleared = 0
    failed = 0

    async for m in d.logs_from(message.channel, limit=ammount):
        try:
            await d.delete_message(m)
            cleared += 1
        except:
            failed += 1
            pass
    return ammount
ammount = 50

messages = []

@d.event
async def on_ready():
    print('Logged in as')
    print(d.user.name)
    print(d.user.id)
    print('------')
    await d.change_presence(game=discord.Game(name='Bester Discord der Welt'))


@d.event
async def on_message(message):
    if message.content.startswith('.test'):
        counter = 0
        tmp = await d.send_message(message.channel, 'Calculating messages...')
        async for log in d.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await d.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('.sleep'):
        await asyncio.sleep(5)
        await d.send_message(message.channel, 'Done sleeping')
    if message.content.startswith('.text'):
        await d.send_message(message.channel, 'hallo halloi ')
        d.change_nickname()
    if message.content.startswith('.game'):
        print('geht 1')
        if message.author.id == bananenbrot:
            game = message.content[6:]
            await d.change_presence(game=discord.Game(name=game))
            await  d.send_message(message.channel, 'Ich habe mein Spiel zu ' + game + ' geändert')
        else:
            d.send_message(message.channel, '----------nicht genug rechte----------')

        if message.author.id == vollkornbrot:
            game = message.content[6:]
            await d.change_presence(game=discord.Game(name=game))
            await  d.send_message(message.channel, 'Ich habe mein Spiel zu ' + game + ' geändert')
        else:
            d.send_message(message.channel, '----------nicht genug rechte----------')
    if message.content.startswith('!restart'):
        await d.change_presence(game=discord.Game(name='--restart--'))
        d.close()
        print('restart')
    if message.content.startswith('.help'):
       await d.send_message(message.channel, 'Es gibt die Befehle:' )
       await d.send_message(message.channel, '. test' + bla.descriptionTest)
       await d.send_message(message.channel, '. sleep' + bla.descriptionSleep)
       await d.send_message(message.channel, '. text' + bla.descriptionText)
       await d.send_message(message.channel, '. game' + bla.descriptionGame)
       await d.send_message(message.channel, '. restart' + bla.descriptionRestart)
       await d.send_message(message.channel, '. help' + bla.descriptionHelp)
       await d.send_message(message.channel, '. bjoern' + bla.descriptionBjoern)
    if message.content.startswith('.bjoern'):
        if message.author.id == bananenbrot:
            d.send_message(message.channel, 'Hallo Björn')
        if message.author.id == vollkornbrot:

                d.delete_messages(messages=all())
    if message.content.startswith('.delete'):
        async for m in d.logs_from(message.channel, limit=ammount):
         messages.append(m)
         await d.delete_messages(messages)
         return_msg = await d.send_message(message.channel, "Deleted %s messages." % ammount)
         await asyncio.sleep(4)
         await d.delete_message(return_msg)
d.run(bla.token)