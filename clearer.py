import discord
import asyncio


async def ex(args, message, client, invoke):

    try:
        ammount = int(args[0]) + 1 if len(args) > 0 else 2
    except:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), descrition="Please enter a valid value for message ammount!"))
        return


     messages = []
            async for m in client.logs_from(message.channel, limit=ammount):
               messages.append(m)
                await client.delete_messages(messages)
                return_msg = await client.send_message(message.channel, "Deleted %s messages." % ammount)
     await asyncio.sleep(4)
     await client.delete_message(return_msg)
