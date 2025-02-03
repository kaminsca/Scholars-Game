# The Scholar’s Game

## 1. Setup and Values:
- Each player has two hands.
- At the beginning of the game, each hand has a value of 1.
- There are five possible values: 1, 2, 3, 4, and 5.

## 2. Gameplay:
- Players take turns to perform actions.
- A player's turn is consumed when they take one of four actions:
  1. Adding the value of one of their own hands to the value of one of their opponent's hands.
  2. Switching the functionality of one of their own hands with the value 4 or 5.
  3. Performing one of the functions allowed by the values in the game.
  4. Redistributing the total value of their two hands added together between the two individual hands (redistribution must change the game state and therefore cannot result in the same pair of values).

## 3. Adding Values:
- During a player's turn, they can add the current value of one of their own hands to the value of one of their opponent's hands.
- If the sum of the values exceeds 5, subtract 5 to determine the new value (rolling over).

## 4. Switching Functionality:
- A player can switch the functionality of one of their own hands with the value 4 or 5.
- Switching functionality consumes the player's turn.

## 5. Value Functions:
- **Value 1**: Defeats value 5 when assigned the rock function.
- **Value 2**: Scissors function. Defeats 4 or 5 with paper function. Transforms a 1 into a 5 with rock function. Defeated by value 5 with rock function. Can simultaneously defeat two rocks.
- **Value 3**: Double scissors function. Simultaneously eliminates two hands with paper function or eliminates one hand with paper function while transforming another from 1 to 5 with rock function. Simultaneously defeats two rocks. Defeated by value 5 with rock function.
- **Value 4**: Can be assigned either scissors or paper function. If scissors, lacks the ability to simultaneously defeat two rocks. If at any time the value 4 appears, the player whose hand holds that value must immediately decide which of the two functions to assign to that hand. This initial choice does not constitute a "switch" and therefore does not consume a turn.
- **Value 5**: Can be assigned either rock or paper function. Defeated by value 1 with rock function. Defeated by scissors or double scissors with rock function only when used on two rocks simultaneously. Can also be defeated by paper. If at any time the value 5 appears, the player whose hand holds that value must immediately decide which of the two functions to assign to that hand. This initial choice does not constitute a "switch" and therefore does not consume a turn.

## 6. Using Functions:
- When a player consumes their turn to use one of the functions allowed by the values, they can use these functions on either their opponent's hands or their own hands. In the case of scissors and double scissors, which can act on multiple hands at once, the player may choose either the pair of their opponent's hands or one of their own hands and one of their opponent's hands.

## 7. Redistributing Total Value:
- A player can consume their turn by redistributing the total value of their two hands added together between the two individual hands, provided that the redistribution changes the game state by resulting in a pair of values different from the initial pair of values regardless of hand assignment.

## 8. Winning:
- The game ends when a player eliminates both of their opponent's hands.
