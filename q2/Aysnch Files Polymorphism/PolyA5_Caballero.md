1. What do all the methods (move(), special_move(), use()) have in common?
All of these methods share the exact same name and conceptual purpose within their respective groups, acting as a unified interface across different classes. They allow a single, generalized function call to interact seamlessly with entirely different underlying objects and logic.

2. How does this activity show polymorphism in a gaming context?
This activity demonstrates polymorphism by allowing functions like perform_move or apply_item to process various classes—such as different heroes or potions—without needing to check their specific type beforehand. The game engine can simply loop through a collection of diverse objects and call the same method name, letting each object automatically execute its own unique behavior.

3. Other examples where the same action behaves differently depending on the character or item:
An attack() method behaves entirely differently depending on who is performing it, with a warrior executing a heavy sword slash, a mage casting a long-range fireball, and a rogue performing a stealth backstab. Similarly, an equip() method will increase magical intelligence when applied to a staff, but will boost physical defense and block rate when applied to a shield.