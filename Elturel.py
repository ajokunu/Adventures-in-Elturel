#Tree Node for story
class TreeNode:

  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, node):
    self.choices.append(node)
#opening moves
story_root = TreeNode("""
You find yourself in the cook cellar belonging to the guild of The Seven, having just finished a salty pork shank and a glass of ale you when hear shouts erupt from the streets outside and feel the ground shake beneath your feet.
Do you: 
1 ) Race Outside!
2 ) Finish your boiled cabbage.
""")

#input variables
user_choice = input("What is your name? ")
print(user_choice)


#prints for testing
print("Once upon a time in the city of Elturel, home to vagrants, priests and vivacious villains alike a pair of chains and a floating sun ruined a perfectly good breakfast.")
print(story_root.story_piece)
