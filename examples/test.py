import keybasepy
import os

bot = keybasepy.Bot(prefix="!", username=os.environ["KEYBASE_USERNAME"])


@bot.command()
async def hey(ctx, name=None):
	if name:
		await ctx.send(f"Hello, {name}!")
		return
	await ctx.send("Hello!")


@bot.command(command_name="sum")
async def _sum(ctx, *inputs):
	try:
		result = sum(list(map(int, inputs)))
	except ValueError:
		await ctx.send("Error: Invalid numbers!")
		return
	await ctx.send(f"{'+'.join(inputs)}={result}")

bot.run()
