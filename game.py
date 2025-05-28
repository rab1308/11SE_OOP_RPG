import random
from typing import Optional
from constants import (
    WELCOME_MESSAGE, GAME_OVER_MESSAGE, VICTORY_MESSAGE,
    SEPARATOR_LENGTH, BORDER_LENGTH,
    CRITICAL_HIT_CHANCE, CRITICAL_DAMAGE_MULTIPLIER,
    DODGE_MESSAGE, CRITICAL_HIT_MESSAGE, SPECIAL_ABILITY_MESSAGE,
    PLAYER_BASE_HEALTH, PLAYER_BASE_DAMAGE
)
from character import Character, Boss
from weapon import Rock, Paper, Scissors

class Game:
    """Main game class that manages game flow and state."""
    def __init__(self):
        """Initialize the game."""
        self.player: Optional[Character] = None
        self.boss: Optional[Boss] = None
        self.is_running = False

    def setup_game(self) -> None:
        """Initialize the game with player and boss characters."""
        # Create player with base attributes
        self.player = Character("Hero", PLAYER_BASE_HEALTH, PLAYER_BASE_DAMAGE)
        
        # Randomly select a weapon for the player
        weapon_type = random.choice(list(WEAPON_TYPES.keys()))
        self.player.weapon = WEAPON_TYPES[weapon_type]()
        
        # Randomly select a boss type
        boss_type = random.choice(list(BOSS_TYPES.keys()))
        self.boss = BOSS_TYPES[boss_type]()
        
        # Give the boss a weapon
        boss_weapon_type = random.choice(list(WEAPON_TYPES.keys()))
        self.boss.weapon = WEAPON_TYPES[boss_weapon_type]()

    def print_separator(self) -> None:
        """Print a separator line."""
        print("=" * SEPARATOR_LENGTH)

    def print_border(self) -> None:
        """Print a border line."""
        print("=" * BORDER_LENGTH)

    def display_status(self) -> None:
        """Display current game status."""
        self.print_separator()
        print(f"Player: {self.player.name} (HP: {self.player.health})")
        print(f"Weapon: {self.player.weapon.get_description()}")
        print(f"Strength: {self.player.get_attribute('strength')}")
        print(f"Agility: {self.player.get_attribute('agility')}")
        print(f"Intelligence: {self.player.get_attribute('intelligence')}")
        print(f"Boss: {self.boss.name} (HP: {self.boss.health})")
        self.print_separator()

    def get_player_action(self) -> str:
        """Get player's action choice."""
        while True:
            action = input("\n[1] Attack\n[2] Run\n[3] Use Special Ability\nChoose an action: ").strip()
            if action in ['1', '2', '3']:
                return action
            print("Invalid choice. Please try again.")

    def run(self) -> None:
        """Main game loop."""
        self.is_running = True
        self.setup_game()
        
        print("\n" + "=" * BORDER_LENGTH)
        print(WELCOME_MESSAGE.center(BORDER_LENGTH))
        print("=" * BORDER_LENGTH + "\n")
        
        while self.is_running:
            self.display_status()
            
            if not self.player.is_alive():
                print(GAME_OVER_MESSAGE)
                self.is_running = False
                break
            
            if not self.boss.is_alive():
                print(VICTORY_MESSAGE)
                self.is_running = False
                break
            
            # Player's turn
            action = self.get_player_action()
            
            if action == '1':
                # Check for critical hit
                if random.random() < CRITICAL_HIT_CHANCE:
                    print(f"\n{CRITICAL_HIT_MESSAGE}")
                    self.player.attack(self.boss)
                    self.player.attack(self.boss)  # Double damage
                else:
                    self.player.attack(self.boss)
                print(f"\n{self.player.name} attacks {self.boss.name} with {self.player.weapon.get_description()}!")
            elif action == '3':
                if self.player.use_special_ability():
                    print(f"\n{SPECIAL_ABILITY_MESSAGE}")
                else:
                    print("\nNot enough intelligence to use special ability!")
            else:
                print("\nYou try to run away!")
                self.is_running = False
                break
            
            # Boss's turn if player didn't run
            if self.is_running:
                self.boss.attack(self.player)
                print(f"\n{self.boss.name} attacks {self.player.name} with {self.boss.weapon.get_description()}!")
                
                # Update boss state
                self.boss.update()
