from game import Game
newline = "\n"

# Determine whether to render early start text


def render_early_start(games_list):
    for game in games_list:
        if game.early_start:
            return "--- EARLY START ---"
    return ""

# Add games to lists


# Two max players
two_max = []

two_max.append(
    Game('Battleship', 2, False),
    Game('Chess', 2, False),
    Game('Fog of Love', 2, False)
)

# Four max players
four_max = []

four_max.append(
    Game("Blockus", 4, False),
    Game("Clank!", 4, False),
    Game("Crawl", 4, False),
    Game("Gloomhaven", 4, False),
    Game("Hero Realms", 4, False),
    Game("Jumanji", 4, False),
    Game("Pandemic", 4, True),
    Game("Suburbia", 4, True)
)

# Five max players
five_max = []

five_max.append(
    Game("Carcassonne", 5, False),
    Game("Forbidden Desert", 5, False),
    Game("Intrigue", 5, False),
    Game("Marvel's Villains", 5, False),
    Game("Sherriff of Nottingham", 5, False),
    Game("Ticket to Ride", 5, False),
    Game("Wingspan", 5, True),
)

# Six max players
six_max = []

six_max.append(
    Game("Anomia", 6, False),
    Game("Ascension", 6, False),
    Game("Bargain Quest", 6, False),
    Game("Betrayal of House on the Hill", 6, False),
    Game("Clue", 6, False),
    Game("Dixit", 6, False),
    Game("Flashpoint", 6, False),
    Game("Game of Life", 6, False),
    Game("Here to Slay", 6, False),
    Game("King of Tokyo", 6, False),
    Game("Scythe", 6, False),
    Game("Settlers of Catan", 6, False),
    Game("Everdell", 6, True),
    Game("Risk", 6, True),
)

# 7+ max players
seven_plus_max = []

seven_plus_max.append(
    Game("7 Wonders", 7, False),
    Game("Articulate!", 7, False),
    Game("BANG! The Dice Game", 7, False),
    Game("Between Two Cities", 7, False),
    Game("Cards Against Humanity", 7, False),
    Game("Careers", 7, False),
    Game("Codenames", 7, False),
    Game("Herd Mentality", 7, False),
    Game("Joking Hazard", 7, False),
    Game("Mutiny!", 7, False),
    Game("Red Dragon Inn", 7, False),
    Game("Skribble.io", 7, False),
    Game("Sounds Fishy", 7, False),
    Game("Star Realms", 7, False),
    Game("Tabletop Minigolf", 7, False),
    Game("Taboo", 7, False),
    Game("Texas Hold 'Em", 7, False),
    Game("Tiny Towns", 7, False),
    Game("Not Alone", 7, False),
    Game("UNO", 7, False),
    Game("Eldritch Horror", 7, True),
    Game("Games of Thrones: The Board Game", 7, True),
    Game("Monopoly", 7, True),
)

master_games_list = f"""
:regional_indicator_m: :regional_indicator_a: :regional_indicator_s: :regional_indicator_t: :regional_indicator_e: :regional_indicator_r:     :regional_indicator_g: :regional_indicator_a: :regional_indicator_m: :regional_indicator_e: :regional_indicator_s:     :regional_indicator_l: :regional_indicator_i: :regional_indicator_s: :regional_indicator_t: 

**7+ Max Players**
```
{newline.join([f"{game.name}" for game in seven_plus_max])}

{render_early_start(seven_plus_max)}

{newline.join([f"{game.name}" for game in seven_plus_max if game.early_start == True])}
```

**6 Max Players**
```
{newline.join([f"{game.name}" for game in six_max])}

{render_early_start(six_max)}

{newline.join([f"{game.name}" for game in six_max if game.early_start == True])}
```

**5 Max Players**
```
{newline.join([f"{game.name}" for game in five_max])}

{render_early_start(five_max)}

{newline.join([f"{game.name}" for game in five_max if game.early_start == True])}
```

**4 Max Players**
```
{newline.join([f"{game.name}" for game in four_max])}

{render_early_start(four_max)}

{newline.join([f"{game.name}" for game in four_max if game.early_start == True])}
```

**2 Max Players**
```
{newline.join([f"{game.name}" for game in two_max])}

{render_early_start(two_max)}

{newline.join([f"{game.name}" for game in two_max if game.early_start == True])}
```


🇧 🇦 🇳 🇳 🇪 🇩     🇬 🇦 🇲 🇪 🇸 
THESE GAMES CAN BE CHOSEN. ALL players wanting to participate in game night must agree though.
Boggle
Trivial Pursuit
Game of the Internet
Muffin Time
Scattergories
Scrabble
SORRY!
"""
