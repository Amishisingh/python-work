print("Welcome to the Quiz!!")
playerName = input("Enter your name: ")
score = 0
print("Q1 who is the president of India?")
print("options: \nA.Draupadi Murmur  \nB.Narendra Modi \nC.Nelson Mandela ")
answer = input("A\B\C:").upper()
if answer == "A":
  print("correct")
  score = score + 10
else:
    print("Incorrect")
    score = score - 5
print("Q2 who is the Prime Minister of India?")
print("options: \nA.Draupadi Murmur \nB.Narendra Modi \nC.Nelson Mandela")
answer = input("A\B\C:").upper()
if answer == 'B':
  print("correct")
  score = score + 10
else:
    print("Incorrect")
    score = score - 5
print("Entomology is the study of ...?")
print("options: \nA.The origin and history of technical and scientific terms \nB.Behavior of human \nC.Insects")    
answer = input("A\B\C:").upper()
if answer == 'C':
  print("correct")
  score = score + 10
else:
    print("Incorrect")
    score = score - 5
print("------conclusion--------")
print("hey",playerName,"Your score is ",score,"/30")
   