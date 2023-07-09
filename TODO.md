# Functionality needed

The bot should be able to:

- [ ] Update the game night leaderboard with the new winner(s)
  1. User command: `!gn winner <username1> <username2> ... <usernameN>`
  2. Can handle multiple winners, each separated by a space
- [ ] Keep track games remaining in each game night season. Seasons follow the actual calendar seasons of spring 🌸, summer ☀️, fall 🍂, and winter ❄️.
  1.  This is usually written at the bottom of the leaderboard, but can be anywhere on the leaderboard
- [ ] Keep track of the previous game night season champions
  1. This is a static list for now, not too hard to keep track of.
     1. Example entry: `👑 Season X - Joe`
- [ ] Add new season champions at the end of each season
  1. Example bot message: `Congratulations to <username> for becoming the Game Night Season X Champion!`
  2. Add random meme celebration video or something dumb too
- [ ] Prompt/ping user when it is their turn to host in rotation
  1. Example bot message: `Hey, @Joe! It's your turn to be host of game night for the week of <upcomingWeek>! On what date and time do you want to host?`
- [ ] Add/remove/skip people from the game night rotation
  1. Example rotation: `4mMan > Grindclock > Joe > Almirius > Askarathol`
  2. Commands
     1. Add: `!gn rotation add <username>`
        1. Example: `!gn rotation add <username>`
        2. This would transform rotation to be `4mMan > Grindclock > Joe > Almirius > Askarathol > <username>`
        3. Could use linked list and modify the pointers to change order around instead of just using an array to preserve order
     2. Remove: `!gn rotation rm <username>`
        1. Example: `!gn rotation rm Grindclock`
        2. This would transform rotation to be `4mMan > Joe > Almirius > Askarathol`
     3. Skip: `!gn rotation skip <username>`
        1. Would allow you to skip someone in rotation if they want to stay, but cannot host.
        2. Would move on to next person in the list and prompt them and keep going until someone says they can host.
