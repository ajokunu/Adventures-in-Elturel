#Tree Node for story
class TreeNode:

  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, node):
    self.choices.append(node)

  def traverse_story(self):
     story_node = self
     print(story_node.story_piece)
#opening moves
story_root = TreeNode("""
You find yourself in the cook cellar belonging to the guild of The Seven, having just finished a salty pork shank and a glass of ale you when hear shouts erupt from the streets outside and feel the ground shake beneath your feet.
Do you: 
1 ) Race Outside!
2 ) Finish your boiled cabbage.
""")

#input variables
user_choice = input("How long should a man toil at the plow before he makes it a spear?")

choice_a = TreeNode("""
You jump up and race to the door, as you grasp the knob and tear the door open you see a hulking demon right outside the door strangling a poor village wench.

Do you:
1 ) Shout 'Oi, eat this ya red bellied beastie!' and kick the beast in the back of its leg'
2 ) slam the door and look around for a weapon 
""")
choice_b = TreeNode("""
As you gulp down the last of your boiled cabbage gurgling can be heard from right outside the door and you spot a nice guilded spear above the dirty hearth holding this mornings boiling grool.
Do you:
1 ) Look around for a more suitable weapon
2 ) Grasp the Spear and yank the door open
""")
story_root.add_child(choice_a)
story_root.add_child(choice_b)
story_root.traverse_story()
#prints for testing
print("Once upon a time in the city of Elturel, home to vagrants, priests and vivacious villains alike a pair of chains and a floating sun ruined a perfectly good breakfast.")
print(story_root.story_piece)
