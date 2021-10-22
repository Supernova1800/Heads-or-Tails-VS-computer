import numpy as np
import random

inputs = np.zeros((2,2,2),dtype = int)
last_1 = 0
last_2 = 0
scores = [0,0]
def update_inputs(current):
  global last_1,last_2
  if inputs[last_2][last_1][0] == current:
    inputs[last_2][last_1][1] = 1
    inputs[last_2][last_1][0] = current
  else:
    inputs[last_2][last_1][1] = 0
    inputs[last_2][last_1][0] = current
  last_2 = last_1
  last_1 = current
def predection():
  if inputs[last_2][last_1][1] == 1:
    predict = inputs[last_2][last_1][0]
  else:
    predict = random.randint(0,1)
  return predict
def update_scores(predicted,player_input):
  if predicted == player_input:
    scores[0]+=1
    print("computer score %d  player score is %d"%(scores[0],scores[1]))
  else:
    scores[1]+=1
    print("computer score %d  player score is %d"%(scores[0],scores[1]))
def reset():
  for i in range(2):
    for j in range(2):
      for k in range(2):
        inputs[i][j][k] = 0
  scores[0],scores[1]=0,0
def gameplay():
  reset()
  print(inputs)
  print(scores)
  valid_entries = [0,1]
  while True:
    predicted = predection()
    player_input = int(input("player input will be either 0 or 1  "))
    while player_input not in valid_entries:
      print("\ninvalid input")
      player_input = int(input("player input will be either 0 or 1  "))
    update_inputs(player_input)
    update_scores(predicted,player_input)
    if scores[0] == 10:
      print("\n Bad luck you lost the game")
      break
    elif scores[1]==10:
      print("\ncongrats you won the game")
      break
gameplay()