import coinFlip.coinGames as coinGames
import random
initialCapital = 1000

coinSideBetted = 't' if random.randint(0,1) == 0 else 'h'
coinGames.gameA(coinSideBetted, initialCapital, random.randint(1, 100))

coinGames.gameB(coinSideBetted, initialCapital, random.randint(1, 100))

# ! Commented because will be executed 1mi times!!
# print('----------------')
# print('Mixing game A with game B')

# if(coinSideBetted == 't'):
#     coinGames.gameA(coinSideBetted, initialCapital, 1000000)
# else:
#     coinGames.gameB(coinSideBetted, initialCapital, 1000000)