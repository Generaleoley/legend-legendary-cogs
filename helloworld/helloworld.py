from redbot.core import commands

class HWCog(commands.Cog):
  """Hello World test cog"""

  @commands.command()
  async dec helloworld(self, ctx):
    """Prints hello world"""
    await ctx.send("Hello World")
