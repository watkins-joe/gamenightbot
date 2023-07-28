# Functionality needed

The bot should be able to:

- [ ] Display bot commands
  1. User command: `!gn help`
- [ ] Update the game night leaderboard with the new winner(s)
  1. User command: `!gn winner <username1> <username2> ... <usernameN>`
     1. May want to make it so that only the host of game nite that night can run this command, not sure yet
  2. Can handle multiple winners, each separated by a space
     1. Need to verify spelling of users to properly assign wins to them.
        1. Keep users in a `dict` and do a look-up?
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
     1. Universal time/date format to use, `19:00 EST 07/25`
        1. Military time format/two digit month and day
- [ ] Accept user input for choosing their date and time for hosting game night
  1. User command: `!gn host 07/27 4PM`
     1. Use `EST` as the default time zone, could try to get the time zone of the host
- [ ] Add Game Night events to the server automatically after
  1. Events need to have the following info:
     1. Location:
        1. Voice Channel
        2. `Game Night!!!`
     2. Topic = `Game Nite!!!`
     3. Start Date = `Jul 9, 2023`
     4. Time = `8:00 PM`
     5. Description
        1. Host = `@<username>`
        2. ```
           Host @<username>
           <time in host time zone>
           <time in your time zone>
           ```
     6. Cover Image = `https://static.kinguin.net/cdn-cgi/image/w=750,q=80,fit=scale-down,f=auto/media/category/1/-/1-1024_1382.jpg`
- [x] Implement the game night rotation without hard-coding it as a string
  1. Example rotation: `4mMan > Grindclock > Joe > Almirius > Askarathol`
  - _Completed 7/28/23_
-
- [ ] Add/remove/skip people from the game night rotation
  1. Commands
  - [x] Add: `!gn rotation add <username>`
    1. Example: `!gn rotation add <username>`
    2. This would transform rotation to be `4mMan > Grindclock > Joe > Almirius > Askarathol > <username>`
    3. Could use linked list and modify the pointers to change order around instead of just using an array to preserve order
       1. _Completed 7/28/23_
  - [x] Remove: `!gn rotation rm <username>`
    1.  Example: `!gn rotation rm Grindclock`
    2.  This would transform rotation to be `4mMan > Joe > Almirius > Askarathol`
        1.  _Completed 7/28/23_
  - [ ] Skip: `!gn rotation skip <username>`
    1.  Would allow you to skip someone in rotation if they want to stay, but cannot host.
    2.  Would move on to next person in the list and prompt them and keep going until someone says they can host.
  1. Implement a linked list to keep track of who is hosting for the next game night session
     1. Each user points to the next user and the last user points to the first user (head)
- [ ] Add/remove games from Master Game List
  1. Commands
     1. Add game:
        1. User command: `!gn game add <gameName> <maxPlayers>`
     2. Remove game:
        1. User command: `!gn game rm <gameName> <maxPlayers>`

Lower priority:

- [ ] Adding/removing people from Prize Pool
