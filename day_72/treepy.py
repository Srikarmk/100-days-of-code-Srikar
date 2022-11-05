from rich.tree import Tree
from rich import print

tree=Tree("[cyan]My Project")
tree.add("[green]data")
tree.add("[blue]model")
src=tree.add("[red]src")
src.add("[red]processData.py")
print(tree)