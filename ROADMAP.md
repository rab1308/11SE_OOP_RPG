# RPG Lesson: Simple File Structure

This document outlines a clean, simple file structure for organizing the RPG game code without using Python packages. This approach keeps the project straightforward while maintaining good code organization.

## Goals

1. Keep the code organized in a simple, flat structure
2. Maintain clear separation of concerns
3. Make it easy to understand and modify
4. Focus on demonstrating OOP concepts

## Proposed File Structure

```
rpg_game/
├── README.md           # Project documentation
├── main.py             # Entry point with if __name__ == "__main__"
├── game.py             # Game class definition
├── character.py        # Character class
├── boss.py             # Boss class (inherits from Character)
├── weapon.py           # Weapon class
├── game_logger.py      # GameLogger class
└── console_utils.py    # Console utility functions
```

## Implementation Steps

### 1. Create File Structure

- Create the files as outlined above
- No need for `__init__.py` files or package structure

### 2. Extract Utility Functions

- Move `clear_screen()`, `press_enter()`, and `print_border()` to `console_utils.py`
- Move `GameLogger` class to `game_logger.py`

### 3. Extract Game Entities

- Move `Weapon` class to `weapon.py`
- Move `Character` class to `character.py`
  - Add import for `Weapon` and `GameLogger`
- Move `Boss` class to `boss.py`
  - Add import for `Character`

### 4. Extract Game Logic

- Move `Game` class to `game.py`
- Add imports for all required classes and utilities

### 5. Create Entry Point

- Create `main.py` with the code from the original `if __name__ == "__main__"` block
- Import the `Game` class

### 6. Test and Debug

- Ensure all imports are correct
- Test the application to verify it works as expected
- Fix any issues that arise

## Educational Notes for Each File

### models/weapon.py
- Demonstrates a simple class with minimal dependencies
- Shows how to create a class that will be composed within another class

### models/character.py
- Shows importing a class (`Weapon`) for composition
- Demonstrates dependency on a utility class (`GameLogger`)
- Illustrates a class with both attributes and methods

### models/boss.py
- Demonstrates inheritance by importing the parent class
- Shows how to extend functionality through method overriding
- Illustrates the `super()` function for parent class method calls

### utils/logger.py
- Shows a utility class with static methods
- Demonstrates separation of concerns

### utils/console.py
- Shows grouping related utility functions
- Demonstrates platform-specific code handling

### game.py
- Demonstrates a complex class that orchestrates other classes
- Shows importing multiple dependencies
- Illustrates a class that manages game state and flow

### main.py
- Shows a clean entry point
- Demonstrates minimal code in the main module

## UML Considerations

- Create a UML class diagram showing the relationships between classes
- Use the diagram to illustrate how the relationships are maintained across files
- Highlight how imports represent the relationships in the UML diagram

## Code Organization and Constants

### Recommended Project Structure
```
rpg_game/
│
├── main.py
├── utilities.py
├── weapon.py
├── character.py
├── boss.py
└── game.py
```

### Benefits of This Structure

1. **Modularity**
   - **Ease of Maintenance**: Each file contains a specific part of the functionality, making it easier to locate and fix bugs or make improvements.
   - **Reusability**: Components can be easily reused in other projects or parts of the application.

2. **Separation of Concerns**
   - **Organization**: Code is divided based on responsibilities, adhering to the principle of separation of concerns.
   - **Clarity**: Each file has a clear, single purpose, making the codebase more understandable.

3. **Scalability**
   - **Growth**: The project can grow without becoming unwieldy, with new features added to appropriate modules.
   - **Testing**: Easier to write and maintain unit tests for isolated components.

4. **Collaboration**
   - **Team Work**: Multiple developers can work on different files simultaneously with minimal conflicts.
   - **Version Control**: Changes are more granular and easier to track in version control.

5. **Encapsulation and Abstraction**
   - **Encapsulation**: Related data and methods are kept together, protecting data integrity.
   - **Abstraction**: Implementation details are hidden behind clear interfaces.

### Constants Management

Including a `constants.py` file helps centralize configuration values:

```python
# Weapon constants
WEAPON_ROCK_NAME = "Rock"
WEAPON_ROCK_DAMAGE_BONUS = 2

WEAPON_PAPER_NAME = "Paper"
WEAPON_PAPER_DAMAGE_BONUS = 3

WEAPON_SCISSORS_NAME = "Scissors"
WEAPON_SCISSORS_DAMAGE_BONUS = 4

# Boss constants
BOSS_WEAPON_NAME = "Boss Weapon"
BOSS_WEAPON_DAMAGE_BONUS = 5

# Character stats
GOBLIN_KING_NAME = "Goblin King"
GOBLIN_KING_HEALTH = 50
GOBLIN_KING_DAMAGE = 8

DARK_SORCERER_NAME = "Dark Sorcerer"
DARK_SORCERER_HEALTH = 60
DARK_SORCERER_DAMAGE = 9

# Player constants
PLAYER_INITIAL_HEALTH = 110
PLAYER_INITIAL_DAMAGE = 10

# UI constants
BORDER_LENGTH = 80
INTRO_MESSAGE = """
Welcome to the RPG Adventure!
In a world where darkness looms, you are the chosen hero destined to defeat the evil bosses and restore peace.
"""
```

**Advantages of Using constants.py**
- **Centralised Configuration**: Single source of truth for all constant values
- **Self-documenting**: Clearly shows what values are used throughout the application
- **Easier Maintenance**: Update values in one place rather than searching through code
- **Type Safety**: Constants are named meaningfully, avoiding magic numbers
- **Environment Management**: Easier to support different configurations for different environments

## Future Enhancements

- **Support multiple boss and villain types**: 

- **Demonstrate polymorphism with weapons**:

- **Add a Sidekick for the player**:

- **Implement an Inventory class for characters**:
  - Create an `Inventory` class to manage items (e.g., weapons, potions) with methods like `add_item()`, `remove_item()`, and `list_items()`.
  - Add an `inventory` attribute to the `Character` class so all characters (Player, Sidekick, Boss, Villain, etc.) can have and manage their own inventory.
  - This design uses **composition** (a character "has an" inventory), **encapsulation** (inventory logic is managed in its own class), and **reusability** (any character type can use the inventory).
  
  **Example:**
  ```python
  class Inventory:
      def __init__(self):
          self.items = []
      def add_item(self, item):
          self.items.append(item)
      def remove_item(self, item):
          self.items.remove(item)
      def list_items(self):
          return self.items

  class Character:
      def __init__(self, ...):
          # ... existing attributes ...
          self.inventory = Inventory()

  player.inventory.add_item(Weapon("Sword", 10))
  sidekick.inventory.add_item(Weapon("Shield", 3))
  ```
  - Update documentation and UML diagrams to show the Inventory class and its relationship to Character and subclasses.

  - Implement a `Sidekick` class that inherits from `Character`, allowing the player to have a companion with its own attributes and methods.
  - The `Player` class should have an attribute (e.g., `sidekick`) referencing a `Sidekick` object, demonstrating composition/association.
  - Sidekicks can be assigned weapons from the `Weapon` class or its subclasses, just like players or other characters.
  - Create specialised sidekick subclasses (e.g., `DefenderSidekick`, `HealerSidekick`) that override methods like `defend()` or add unique abilities, making some sidekicks better at defending against villains and bosses. This demonstrates inheritance and polymorphism.
  
  **Example:**
  ```python
  class Sidekick(Character):
      def defend(self, enemy):
          # Default defence behaviour
          pass

  class DefenderSidekick(Sidekick):
      def defend(self, enemy):
          # Enhanced defence logic
          pass
  
  player = Player("Hero", 100, 10)
  sidekick = DefenderSidekick("Robin", 60, 5)
  sidekick.weapon = Weapon("Shield", 3)
  player.sidekick = sidekick
  ```
  - Update documentation and UML diagrams to show the new Sidekick class, its relationship with Player, and its specialised subclasses.

  - Create subclasses of `Weapon` (e.g., `Rock`, `Paper`, `Scissors`) and override a method (such as `use()` or `attack()`) in each subclass to implement unique behavior. This will explicitly show method overriding and polymorphism in action.
  
  **Example:**
  ```python
  class Weapon:
      def use(self, target):
          # Default weapon behaviour
          pass

  class Rock(Weapon):
      def use(self, target):
          # Rock-specific behaviour
          pass

  class Paper(Weapon):
      def use(self, target):
          # Paper-specific behaviour
          pass

  class Scissors(Weapon):
      def use(self, target):
          # Scissors-specific behaviour
          pass
  ```
  - Update documentation and UML diagrams to highlight this use of polymorphism.

  - For different kinds of bosses (e.g., FireBoss, IceBoss), create subclasses that inherit from the `Boss` class. Each boss type can have unique abilities or behaviors.
  - For regular enemies or villains (e.g., Goblin, Orc, Necromancer), create subclasses that inherit from `Character` or from a new `Villain` class (which itself inherits from `Character`).
  - Only special, powerful enemies should inherit from `Boss`. Regular enemies should not inherit from `Boss`.

  **Example class hierarchy:**
  ```python
  class Boss(Character):
      pass

  class FireBoss(Boss):
      pass

  class IceBoss(Boss):
      pass

  class Villain(Character):
      pass

  class Goblin(Villain):
      pass

  class Orc(Villain):
      pass
  ```

- Update UML diagrams and documentation to reflect the new class hierarchy when implemented.

1. **Configuration Files**: Add a `config.py` or JSON configuration
2. **Save/Load System**: Implement game state persistence
3. **Additional Entities**: Add more character types, weapons, etc.
4. **Unit Tests**: Add a `tests/` directory with unit tests for each class

## Teaching Approach

1. Start with the single-file version (`rpg_oop_concepts.py`)
2. Introduce the concept of code organisation and modularity
3. Walk through the refactoring process step by step
4. Discuss the benefits and challenges of multi-file organisation
5. Use this as an opportunity to reinforce OOP concepts in a more realistic context
