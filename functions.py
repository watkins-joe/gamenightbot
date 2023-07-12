# Add command-specific functions here

async def process_winners(ctx, args):
    """
    Processes winner(s) of a game night session.

    Args:
        `ctx`: Context object.

        `args`: The winner(s) of game night, separated by a space.

        Minimum of one winner, no maximum.

        Usage: `!gn winners userOne userTwo ... userN
    """

    # Debugging
    # print("args", args)
    winners = ", ".join(args[1:])
    # print("winners", winners)

    await ctx.send(f'Congratulations {winners}!')
