# RPG Lesson: Roadmap for Multi-File Version

This roadmap outlines a plan for evolving the single-file `rpg_oop_concepts.py` into a properly structured multi-file Python package. This progression serves as an educational tool to demonstrate proper code organization and modularity in object-oriented programming.

## Educational Goals

1. Demonstrate proper Python package structure
2. Show how classes and their relationships are maintained across files
3. Teach import management and dependency handling
4. Illustrate how larger projects are organized
5. Reinforce OOP concepts in a more realistic development context

## Proposed File Structure

```
rpg_lesson/
├── README.md                  # Project documentation
├── ROADMAP.md                 # This roadmap file
├── rpg_oop_concepts.py        # Original single-file version
├── rpg_oop_modular/           # Multi-file version
│   ├── __init__.py            # Makes the directory a package
│   ├── main.py                # Entry point with if __name__ == "__main__"
│   ├── game.py                # Game class definition
│   ├── models/                # Game entities
│   │   ├── __init__.py        # Makes models a subpackage
│   │   ├── character.py       # Character class
│   │   ├── boss.py            # Boss class (inherits from Character)
│   │   └── weapon.py          # Weapon class
│   └── utils/                 # Utility functions and classes
│       ├── __init__.py        # Makes utils a subpackage
│       ├── console.py         # Console utility functions
│       └── logger.py          # GameLogger class
```

## Implementation Steps

### 1. Create Package Structure

- Create the directory structure as outlined above
- Add empty `__init__.py` files to make directories into packages

### 2. Extract Utility Functions (utils/)

- Move `clear_screen()`, `press_enter()`, and `print_border()` to `utils/console.py`
- Move `GameLogger` class to `utils/logger.py`
- Ensure proper imports in the `__init__.py` files for easy access

### 3. Extract Game Entities (models/)

- Move `Weapon` class to `models/weapon.py`
- Move `Character` class to `models/character.py`
  - Add import for `Weapon` and `GameLogger`
- Move `Boss` class to `models/boss.py`
  - Add import for `Character` and `GameLogger`
- Update `__init__.py` to expose these classes

### 4. Extract Game Logic (game.py)

- Move `Game` class to `game.py`
- Add imports for all required classes and utilities

### 5. Create Entry Point (main.py)

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
  - Create specialized sidekick subclasses (e.g., `DefenderSidekick`, `HealerSidekick`) that override methods like `defend()` or add unique abilities, making some sidekicks better at defending against villains and bosses. This demonstrates inheritance and polymorphism.
  
  **Example:**
  ```python
  class Sidekick(Character):
      def defend(self, enemy):
          # Default defense behavior
          pass

  class DefenderSidekick(Sidekick):
      def defend(self, enemy):
          # Enhanced defense logic
          pass
  
  player = Player("Hero", 100, 10)
  sidekick = DefenderSidekick("Robin", 60, 5)
  sidekick.weapon = Weapon("Shield", 3)
  player.sidekick = sidekick
  ```
  - Update documentation and UML diagrams to show the new Sidekick class, its relationship with Player, and its specialized subclasses.

  - Create subclasses of `Weapon` (e.g., `Rock`, `Paper`, `Scissors`) and override a method (such as `use()` or `attack()`) in each subclass to implement unique behavior. This will explicitly show method overriding and polymorphism in action.
  
  **Example:**
  ```python
  class Weapon:
      def use(self, target):
          # Default weapon behavior
          pass

  class Rock(Weapon):
      def use(self, target):
          # Rock-specific behavior
          pass

  class Paper(Weapon):
      def use(self, target):
          # Paper-specific behavior
          pass

  class Scissors(Weapon):
      def use(self, target):
          # Scissors-specific behavior
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

1. Start with the single-file version (`lesson1.py`)
2. Introduce the concept of code organization and modularity
3. Walk through the refactoring process step by step
4. Discuss the benefits and challenges of multi-file organization
5. Use this as an opportunity to reinforce OOP concepts in a more realistic context
