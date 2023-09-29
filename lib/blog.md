## Big Lessons
- Putting the cart before the horse -- or focusing on the game loop code before setting a design philosophy and level of abstraction
- Learn to debug -- or code blindly and debug at the end

## Cart Before the Horse
Once again, I find it unhelpful to start coding without having a firm understanding and acceptance of a framework and overall systems hierarchy and flow. 

Questions answered here could be:
- What attributes do we want?
- What ORMs do we need? Should we code the general basics?
- How much commenting do we leave in?
- How much complexity and dynamic features do we anticipate being able to handle?
- What's the MVP? How do we modify this -- because it changes coding dynamics and focus? What's most important?
- How do we conduct PR?
- How do we track sync ups and overall decisions?

Going from this:
|-- lib/
|-- models/
|   |-- __init__.py (contains SQL connection, monster rendering)
|   |-- character.py (contains character init, getters/setters, ORMs, and hardcoded characters list)
|   |-- monster.py (contains monster init, getters/setters, ORMs, hard-coded monsters list)
|   |-- player.py (contains player init, getters/setters, ORMs)
|   |-- scenario.py (list of hard-coded scenarios)
|-- cli.py (SQL connection, CLI menu, game logic code)
|-- debug.py

To this:

|-- lib/
|-- data/
|   |-- default_characters.py
|   |-- default_monsters.py
|   |-- default_scenarios.py
|-- models/
|   |-- __init__.py
|   |-- character.py
|   |-- monster.py
|   |-- player.py
|-- cli.py
|-- debug.py
|-- game.py

In my case, I wanted to focus on experimenting with and understanding the overall structure of what makes a non SQLAlchemy CLI python app work? What file does what? Should I code the scenarios with monsters? How can we do this overall framework while keeping single responsibility, encapsulation, desire for dynamic class and ORM interactions, and future feature development in mind?

Again and again, I found that the challenges are lessened (not gone mind you) when single responsibility and modularization is used. It allows for greater future app development in a targeted way without having to reorganize and separate out responsibility and logic.

I separated CLI display code from the game sequence. I left out game sequence coding until last. I made sure validations for player registration and character creation could take place first. And this was only possible because my code files demonstrate single responsibility and appropriate abstraction. I could comment out the game logic methods without disrupting my other CLI menu options. Furthermore, separating the hard-coded lists of monsters and scenarios and characters meant my models could focus on database operations. Plus, this leaves room to generate more complex logic between them. 


## Learning to Debug
Sure I printed out some rows to help me see what was generated in the console. Overall, though, it was very slow for me to debug until I got far enough along--basically not until I had a CLI that could run. Then and only then, did I come across a lot of small errors in my models and game init logic. Maybe this is how it always is since running CLI means you're now able to see all the app's internal interactions. 