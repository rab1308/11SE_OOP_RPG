from typing import Optional, Dict
from weapon import Weapon
from constants import (
    PLAYER_BASE_HEALTH, PLAYER_BASE_DAMAGE,
    BOSS_GOBBLIN_KING_HEALTH, BOSS_GOBBLIN_KING_DAMAGE,
    BOSS_ICE_SORCERER_HEALTH, BOSS_ICE_SORCERER_DAMAGE,
    BOSS_SHADOW_KNIGHT_HEALTH, BOSS_SHADOW_KNIGHT_DAMAGE,
    ATTRIBUTE_STRENGTH, ATTRIBUTE_AGILITY, ATTRIBUTE_INTELLIGENCE
)

class Character:
    """Base class for all characters in the game."""
    def __init__(self, name: str, health: int, damage: int):
        """
        Initialize a character with basic attributes.
        
        Args:
            name (str): Name of the character
            health (int): Initial health points
            damage (int): Base damage value
        """
        self.name = name
        self.health = health
        self.base_damage = damage
        self.weapon: Optional[Weapon] = None
        
        # Initialize attributes
        self.attributes: Dict[str, int] = {
            ATTRIBUTE_STRENGTH: 10,    # Affects damage
            ATTRIBUTE_AGILITY: 10,     # Affects dodge chance
            ATTRIBUTE_INTELLIGENCE: 10 # Affects special abilities
        }
        
    def get_attribute(self, attribute: str) -> int:
        """
        Get the value of a specific attribute.
        
        Args:
            attribute (str): Attribute name
            
        Returns:
            int: Attribute value
        """
        return self.attributes.get(attribute, 0)
    
    def set_attribute(self, attribute: str, value: int) -> None:
        """
        Set the value of a specific attribute.
        
        Args:
            attribute (str): Attribute name
            value (int): New attribute value
        """
        if attribute in self.attributes:
            self.attributes[attribute] = value

    def is_alive(self) -> bool:
        """Return True if character has health remaining."""
        return self.health > 0

    def take_damage(self, damage: int) -> None:
        """
        Reduce character's health by the given damage amount.
        
        Args:
            damage (int): Amount of damage to take
        """
        # Calculate dodge chance based on agility
        dodge_chance = self.get_attribute(ATTRIBUTE_AGILITY) / 100
        if random.random() > dodge_chance:
            self.health = max(0, self.health - damage)
        else:
            print(f"\n{self.name} dodges the attack!")

    def attack(self, target: 'Character') -> None:
        """
        Attack another character with combined weapon and base damage.
        
        Args:
            target (Character): The target character to attack
        """
        # Calculate damage based on strength
        strength_bonus = self.get_attribute(ATTRIBUTE_STRENGTH) / 10
        total_damage = self.base_damage * (1 + strength_bonus)
        
        if self.weapon:
            total_damage += self.weapon.attack()
        
        target.take_damage(total_damage)

    def use_special_ability(self) -> None:
        """
        Use character's special ability based on intelligence.
        
        Returns:
            bool: True if ability was used successfully
        """
        intelligence = self.get_attribute(ATTRIBUTE_INTELLIGENCE)
        if intelligence >= 20:  # Require minimum intelligence
            print(f"\n{self.name} uses a powerful special ability!")
            return True
        return False

class Boss(Character):
    """Special boss character class."""
    def __init__(self, name: str, health: int, damage: int, special_ability: str = None):
        """
        Initialize a boss character with special abilities.
        
        Args:
            name (str): Name of the boss
            health (int): Initial health points
            damage (int): Base damage value
            special_ability (str, optional): Special ability description
        """
        super().__init__(name, health, damage)
        self.special_ability = special_ability
        self.ability_cooldown = 0
        self.ability_ready = True
        
        # Bosses have higher attributes
        self.attributes[ATTRIBUTE_STRENGTH] = 15
        self.attributes[ATTRIBUTE_AGILITY] = 12
        self.attributes[ATTRIBUTE_INTELLIGENCE] = 13

    def attack(self, target: Character) -> None:
        """
        Boss attack with enhanced damage and special abilities.
        
        Args:
            target (Character): The target character to attack
        """
        # Boss attacks with 1.5x damage
        total_damage = self.base_damage * 1.5
        
        # Apply strength bonus
        strength_bonus = self.get_attribute(ATTRIBUTE_STRENGTH) / 10
        total_damage *= (1 + strength_bonus)
        
        if self.weapon:
            total_damage += self.weapon.attack()
        
        # Use special ability if ready
        if self.special_ability and self.ability_ready:
            self.use_special_ability(target)
            self.ability_ready = False
            self.ability_cooldown = 3  # 3 turns cooldown
        
        target.take_damage(total_damage)

    def use_special_ability(self, target: Character) -> None:
        """
        Use the boss's special ability with enhanced effects.
        
        Args:
            target (Character): The target character
        """
        intelligence = self.get_attribute(ATTRIBUTE_INTELLIGENCE)
        bonus = intelligence / 100
        
        if self.special_ability == "Fire Breath":
            print(f"\n{self.name} uses Fire Breath!")
            base_damage = self.base_damage * 0.5
            target.take_damage(base_damage * (1 + bonus))
        elif self.special_ability == "Ice Nova":
            print(f"\n{self.name} uses Ice Nova!")
            base_damage = self.base_damage * 0.3
            target.take_damage(base_damage * (1 + bonus))
        elif self.special_ability == "Shadow Strike":
            print(f"\n{self.name} uses Shadow Strike!")
            base_damage = self.base_damage * 0.4
            target.take_damage(base_damage * (1 + bonus))

    def update(self) -> None:
        """
        Update boss state, including ability cooldown.
        """
        if not self.ability_ready:
            self.ability_cooldown -= 1
            if self.ability_cooldown <= 0:
                self.ability_ready = True

# Boss types
class GoblinKing(Boss):
    """Basic boss with fire-based abilities."""
    def __init__(self):
        super().__init__("Goblin King", BOSS_GOBBLIN_KING_HEALTH, BOSS_GOBBLIN_KING_DAMAGE, "Fire Breath")
        self.attributes[ATTRIBUTE_STRENGTH] = 18  # Fire-based strength bonus

class IceSorcerer(Boss):
    """Boss with ice-based abilities."""
    def __init__(self):
        super().__init__("Ice Sorcerer", BOSS_ICE_SORCERER_HEALTH, BOSS_ICE_SORCERER_DAMAGE, "Ice Nova")
        self.attributes[ATTRIBUTE_INTELLIGENCE] = 18  # Ice-based intelligence bonus

class ShadowKnight(Boss):
    """Boss with shadow-based abilities."""
    def __init__(self):
        super().__init__("Shadow Knight", BOSS_SHADOW_KNIGHT_HEALTH, BOSS_SHADOW_KNIGHT_DAMAGE, "Shadow Strike")
        self.attributes[ATTRIBUTE_AGILITY] = 18  # Shadow-based agility bonus

# Boss registry for easy access
BOSS_TYPES = {
    "goblin_king": GoblinKing,
    "ice_sorcerer": IceSorcerer,
    "shadow_knight": ShadowKnight
}
