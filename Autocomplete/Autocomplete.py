from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    pass

    def suffixes(self, suffix=''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        suffix_collection = []

        if self.is_word:
            suffix_collection.append(suffix)
        else:
            for key, value in self.children.items():
                suffix_collection.append(self.children[key].suffixes(suffix + key))
        return suffix_collection

## Add a child node in this Trie

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                # current_node.children[char] = TrieNode()
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root

        for char in prefix:
            if char not in node.children:
                print(char + " is not in the node ", node.children)
                return
            node = node.children[char]
        print("returning node : ", node)
        return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

#Testing:
# prefixNode = MyTrie.find('an')
# if prefixNode:
#     print("found", prefixNode.suffixes())
# else:
#     print( " not found")


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f, prefix='');
