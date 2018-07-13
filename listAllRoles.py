@bot.command()
async def listAllRoles(ctx):
    guild = ctx.guild
    output="```Roles available:\n"
    for role in guild.roles:
        if (role.name != "@everyone"):
            output+="\t\""+role.name+"\"\n"
    output+="```"
    await ctx.send(output)
