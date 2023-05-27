# TooManyBrews
The Proxy-only Card Game

# My Thesis
Collectible Card Games (CCGs) are predatory, exclusionary, and produce a lot of waste. This is an open-source Proxy-only Card Game (PCG), anyone can print and play or play on a digital client, and those cards will be as legitimate as any other. You can even make your own custom art, custom cards, and if you want, you can add them to the project. 
The current artstyle is inspired by how I used to proxy cards as a child back when I couldn’t afford “real” cards.

# But how’s it played?
Both players bring a 40 card deck, these are shuffled together at the start of the game. Both players use this 80 deck to draw cards from to play. To win, play units and send them on three successful quests.

There are 6 preconstructed decks of which you can print and play at home to get started. I’ve also provided images such that you can play on Tabletop Simulator.  After that its up to you, find cards you love and build a deck with them.

I've built a card generator so you can make your own cards, and look through all 80+ cards I designed during the Jam: https://github.com/FourOrbStudios/TooManyBrews. Should work out of the box with python, it takes from  db.csv to generate cards, and takes card art from the icon directory.

# Meet the decks:
**Bonkers**

Bonkers are big rascals, this deck is full of massive units.

**Tokens**

The token deck is full of ways to make lots and lots of little units. Filled with synergies to pump out tokens, and destroy your opponent's tokens.

**Tricks**

This deck is all about tricks, this is the deck built to have a spell war, there's always a reason to keep mana up.

**Control**

Value is the name of the game with control. Balancing cards and mana usage is the key to out maneuver your opponent on the battlefield with this deck.

**Junk One & Junk Two**

The beauty of sharing a deck with your opponent is you can bring whatever you want to the table, in this case, these junk decks each have 40 unique cards in them. Finding synergies may be a needle in a haystack, but it’s a haystack your opponent is also digging through.



# Setup
* Shuffle two 40 card decks and place the 80 card deck in the center of the table.
* Players Decide who is going first.
* Both players draw 7 cards.
* Start the game. The player who goes first only draws one card and can only play one mana source on their first turn.

# Playing The Game
A turn consists of five phases.

## Start of turn
* Resolve any start of turn effects.
* Untap all units.
* Draw 2 cards.
* Play up to 2 cards from your hand face down as mana sources.


## Actions
Do any of the following actions as many times as you would like.
* Play cards from your hand by paying their mana cost and resolving their effects.
* Activate abilities on cards you control.
* To end this step, declare the start of questing.

## Questing
* Declare the start of questing.
* (Choose attackers step) Choose any number of units you control and target them at either an opponent's units, buildings, or the deck (questing).
* (Declare blockers step) Any unit not being attacked can be placed in front of an attacking unit, these units will fight instead of the targeted unit.
* Each unit will deal damage to each other equal to their power. Any unit that takes more damage than its health dies and is placed in the discard.
* If at least one unit was not blocked from questing, take a card from the top of the deck and place it in your treasure pile. If you have three treasure cards, you win the game.

## Actions
Do any of the following actions as many times as you would like.
* Play cards from your hand by paying their mana cost and resolving their effects.
* Activate abilities on cards you control.
* To end this step, declare the end of turn.

## End of turn
* Resolve any end of turn effects.
* Remove any unspent mana.
* Restore each unit and building to full health.

## Additional rules:
* Once a player has gained 3 treasure cards, the game ends and that player is declared the winner.
* If a player would take a treasure card, but is unable to due to the deck being out of cards, that player wins the game.
* If a player would draw a card but is unable to due to the deck being out of cards, that player loses.
* Any permanent card that takes more damage than its health is destroyed, and placed in the discard.
* Cards and effects labeled Action must be played on your turn.
* Cards and effects labeled Reaction Must be played on your opponents turns.
* Whenever a card or ability is played, the opposing player gets the first opportunity to react, followed by the player who played the card/ability. If an additional card/ability is played, the newer ability is resolved first.
* If an effect says to put a unit (not a card) onto the field,  this unit must be represented by a token. Treat this unit as a card for as long as it is on the field, once it leaves the field it ceases to exist.
# Political Section
This section covers my issues with CCGs in a bit more detail, and discusses the conceptual pillars Too Many Brews is built with.

## Problems With Collectible Card Games
* Pay to play and pay to compete models inherently block out mass populations from being able to experience and play these games.
* Power creep is inherently relied upon as a method to extract value from current fans.
* Modern CCGs rely on whaling for a large portion of income, which usually works by limiting specific features of your game to the ultra wealthy.
* Due to secondary markets, cards are treated as investments and often traded in unregulated markets, allowing for fraud, collusion, and other nasty business.
* They use gachapon-style luck based systems (loot boxes, card packs etc) to get players addicted and obscure the value of items.
* They often target these gambling features to kids who aren’t in a position to identify these predatory tactics.
* Modern CCGs often rely on randomness to create viral moments, often at the detriment of both player experience and the game as a whole.
* Physical CCGs produce a massive amount of waste by producing an excess of junk cards.

## Conceptual Pillars For Too Many Brews
* Players can print and play, or if we make a digital version, it will have full modding so players can add their own cards and art.
* Every card is a proxy. There is no “real” card.
* Every card must be unambiguous regardless of if custom art is used.
* The only secondary market would be for custom proxies, special art etc.
* Every card is a rare if you want it be.
* The system allows for people to create their own cards and formats.

## Tangible Game Design Pillars
* The game will use a copyleft viral license to protect itself from the scourge of capitalism.
* 2 Win conditions.
* Decks are shared together. Sharing is caring.
* No randomness other than card draw. No searching, no shuffling.
* Balanced such that going second is neither an advantage or disadvantage.
* Mana is inbuilt to provide more consistent fun.
* Spells are split into Action and Reaction speed, such that no cards are strictly better.
* Every permanent effect has health to avoid unpleasant mechanics.

## Card Design Philosophy
The philosophy I applied to making cards that I’d recommend people follow when making their own cards for a consistent game feel.
* Card name and art must be visually distinct enough to be determined from a glance.
* Design for fun, flavour, and interaction above all else.
* Cards should be intuitive enough that a card is understood from the first read, providing the player knows the keywords mentioned on the card.
* Try to stick to the approximate power curve guideline. 1 mana = 1.5 Attack and health.
* Use mana reduction effects over mana cheating effects for anything under 5 mana.
* Avoid making a better version of a card that already exists. If you think another card needs a change, leave a comment on that card in the card repository.
* Add flavour text where possible.
* Make sure no part of any designed card (Name, text, art, symbols), infringes upon the copyright or intellectual property of any privately owned assets.
* The current font in use is Maybe Next by Khurasan, found here https://fontesk.com/maybe-next-font/.
* If you need a hand making cards, the code I used for generating these cards is also open source (GPL3) at https://github.com/FourOrbStudios/TooManyBrews.

# Deckbuilding
* For now, a deck is made up of 40 cards, with a maximum of 3 of any one card.

Future plans: Long term plan is to split the cardbase up into factions and make decks out of 20 from one faction (your main faction), and 10 from two other factions (allied factions). You can have up to 3 of the same card from your main faction. You can have up to 2 of the same card from your allied faction. I’m also considering making the second faction be limited to 1 of each card in your third faction.

# Accessibility Considerations
A caveat for this section, feedback has not yet been provided by anyone who requires the following accessibility considerations, this is mostly based of GMTK’s accessibility series and anecdotal experience. But that's part of the joy of a collaborative project, if you have any additional thoughts, or think something needs correction, let me know.

### Deaf and hard of hearing
Currently there are no “name a card” or any other effect that requires communication of anything other than a target, card played, or potentially clarifying what number values for something such as a card cost. As such I think the game should be playable without oral communication.

### Colour blindness
Currently the game is in greyscale, however, when coloured art is implemented this will need to be readdressed. Potentially add a check for this in the integration pipeline.

### Low vision and reading issues
The font was chosen as balance between aesthetics and readability. As such I think we’re covered regarding low vision up to a certain level. Card art being distinct is already a primary design consideration for cards, which should help with this. I think this font will need to be replaced with a more readable font in the future to improve this.
Note: My temporary card art isn’t great at this.

### Motor impairment and fatigue
There are no deck searching and shuffling other than the initial shuffle to start the game, which hopefully reduces the strain for motor impairment and fatigue significantly. I would be curious to hear what other aspects of board game design are generally considered strenuous, but I haven’t had the time to research this yet.

### Issues reading English
The current deck generator takes from a spreadsheet to build cards, this makes it reasonably trivial to extend to other languages, providing we can do sufficient translation. Crowdsourcing this will probably be a future endeavors, as will cultural considerations. This will cause issues in physical games if two players bring decks that are different languages, but this is probably unsolvable in paper.

Terminology 
* Deck: The pile of cards all players draw from.
* Discard: The place cards go once they have been played.
* Out of play: A zone where cards can go where they can no longer be targeted or interacted with in any way other than the ability that placed them in the out of play zone.
* Counter: A card that is countered is placed in the discard without it’s effects being resolved.
* Permanent: Any card with health. This card will stay on the field after it is played.
* Spell: Any non-permanant card. When played, its effect occurs. After the card resolves, the spell is then put into the discard.
* Unit: A permanent that can quest, attack, and block. A unit cannot quest or attack the turn it enters the field.
* Building: A permanent that cannot quest, attack, or block, but has a health and can be attacked.
* The Stack: The list of all currently cast spells that are yet to resolve. Whenever a new spell is cast, it is added to the top of the stack. The topmost card of the stack is the first to resolve.
* Attack: How much damage a unit does.
* Health: How much damage a unit or building can take before it dies.
* Mana cost: How many mana sources must be exhausted to cast a spell from hand.
* Exhaust: An exhausted unit cannot quest, attack, block, or or use any action that would exhaust it.
* Action - Cost: Pay the provided cost to put the ability on the stack, this can only be activated on your turn.
* Reaction - Cost: Pay the provided cost to put the ability on the stack, this can only be activated on your opponent's turn.
* (Upon Entering The field): This effect happens when this card enters the field.
* (Upon Death): This effect happens when this card enters the discard from the field.
* (Upon Cast): This effect happens when this card enters the discard from the field.
* (Upon Discard): This effect happens when this card enters the discard from the field.
* (Surprise): This card can be played on your opponent's turn for its surprise cost.
* (Echo): This card can be played from your discard by paying it’s echo cost and removing it from the game. 

# World Building

### Tribes:

* Joblin. Job Goblins, little sneaky rascals when unemployed.
* Pengin. Noble protectors of all things weak and squishy. Always where you least expect them.
* Mushy. Mushroom people, more hungry than they are tasty.
* Leafborn. Plant people, great dancers, not much for talking.
* Bonker. Big Bonky Bois.
* Spiders. 8 legged friends.

### Classes:
* Wizard
* Sorcerer
* Warrior
* Necromancer
* Temeromancer
* Witchmage

# Game Dev Notes

Questions yet to answer:
* Consistency vs singleton, which is more interesting.
* Explaining how to play in a more concise manner needs work.

Problems I’ve Encountered:
* Currently there is no framework to support Local Game Stores.
* Topdecking randomness is feeling rather strong.
* Very strong one offs are problematic.
* Going wide is fundamentally stronger than going big, as you’ve only gotta get in with one unit.
* Despite every card having no inherent value, sentimental value cards may be a concern for deck sharing?
* Decks running out of momentum, this may be inherent in tempo.
* Currently there is no way to persistently buff a unit, via something like enchantments.

Credits:
* Game design: Fourbius
* Good art (logos & card design): Gloom
* Card art: Fourbius
* Playtesting: Gloom, Pinkarella
