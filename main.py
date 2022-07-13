FACES = ['white', 'yellow', 'red', 'blue', 'green', 'orange']
OPPOSITES = {'white': 'yellow', 'green': 'blue', 'red': 'orange'}
startface = input(f'What is the colour of the face you want to start with? \n {FACES}: ')


if startface in OPPOSITES.keys():
  oppface = OPPOSITES[startface]
elif startface in OPPOSITES.values():
  oppface = list(OPPOSITES.keys())[list(OPPOSITES.values()).index(startface)]
print(oppface)
algo1 = "(R' F R' F2) (R U' R') (F2 R2)"
algo2 = "(R U R') U (R U2 R')"

#STEP 1: Solve first face. 

print(f'Solve the {startface} face. ')

#STEP 2: Solve the layer. 
print(f'If none of the colours on the layer adjacent to the {startface} face are the same, you need to swap the corners. Hold the {startface} face at the bottom, and do the algorithm R2, F2, R2. ')

print(f'If there is a bar, where the squares are adjacent like [1,1], then use {algo1}, when positioning the bar to the back. ')
print('\n')
#STEP 3: Solve the opposite face.
oppinput = int(input(f'How many of the {oppface} squares are opposite the solved {startface}?: '))

if oppinput == 0:
  print(f'If there are no squares of {oppface} in the right place, hold the cube such that a {oppface} is facing the left hand. Then use the algorithm {algo2}.')
elif oppinput == 1:
  print(f'If one of the {oppface} squares is in the right position, orient the cube in your hands such that the right square is above the top left square on the face that is facing you, then do the algorithm {algo2}.')
elif oppinput == 2: 
  print(f'If there are two squares in the right position, then orient the cube such that there is one {oppface} in the top left, then do the algorithm {algo2}.')


print('\n')



#STEP 4: Solve the second layer.
print(f'If the cube is not already solved, then use {algo1}, with the {oppface} on top. ')

print('\n')

print(f'If the cube is then not already solved, position any colours that are adjacent to each other, like [1,1] to the face completely away from you, then use {algo1}')


print('\n')
#STEP 5: Finished. 
print(f'After switching the cube around a little, it should be solved.')
