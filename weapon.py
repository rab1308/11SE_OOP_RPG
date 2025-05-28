from typing import Optional
from constants import (
    WEAPON_ROCK_DAMAGE, WEAPON_PAPER_DAMAGE, WEAPON_SCISSORS_DAMAGE,
    WEAPON_SWORD_DAMAGE, WEAPON_BOW_DAMAGE, WEAPON_STAFF_DAMAGE
)

class Weapon:
    """Base class for all weapons in the game."""
    def __init__(self, name: str, damage: int, special_effect: str = None):
        """
        Initialize a weapon with a name, damage value, and optional special effect.
        
        Args:
            name (str): Name of the weapon
            damage (int): Base damage value of the weapon
            special_effect (str, optional): Special effect description
        """
        self.name = name
        self.damage = damage
        self.special_effect = special_effect

    def attack(self) -> int:
        """
        Return the weapon's damage value.
        
        Returns:
            int: The damage value of the weapon
        """
        return self.damage

    def get_description(self) -> str:
        """
        Return a description of the weapon including its special effect if present.
        
        Returns:
            str: Weapon description
        """
        description = f"{self.name} - Damage: {self.damage}"
        if self.special_effect:
            description += f" ({self.special_effect})"
        return description

class Rock(Weapon):
    """Basic melee weapon."""
    def __init__(self):
        super().__init__("Rock", WEAPON_ROCK_DAMAGE, "Basic blunt force")

class Paper(Weapon):
    """Light projectile weapon."""
    def __init__(self):
        super().__init__("Paper", WEAPON_PAPER_DAMAGE, "Light and quick")

class Scissors(Weapon):
    """Sharp melee weapon."""
    def __init__(self):
        super().__init__("Scissors", WEAPON_SCISSORS_DAMAGE, "Sharp and precise")

class Sword(Weapon):
    """Powerful melee weapon."""
    def __init__(self):
        super().__init__("Sword", WEAPON_SWORD_DAMAGE, "Heavy slashing damage")

class Bow(Weapon):
    """Ranged weapon."""
    def __init__(self):
        super().__init__("Bow", WEAPON_BOW_DAMAGE, "Long-range precision")

class Staff(Weapon):
    """Magical weapon."""
    def __init__(self):
        super().__init__("Staff", WEAPON_STAFF_DAMAGE, "Channel magical energy")

# Weapon registry for easy access
WEAPON_TYPES = {
    "rock": Rock,
    "paper": Paper,
    "scissors": Scissors,
    "sword": Sword,
    "bow": Bow,
    "staff": Staff
}
