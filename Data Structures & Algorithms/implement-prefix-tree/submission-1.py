class TrieNode:
    def __init__(self):
        # Dictionary mapping character -> next TrieNode
        self.children = {}
        
        # True if a word ends at this node
        self.end_of_word = False


class PrefixTree:

    def __init__(self):
        # Root node represents empty prefix
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start from root
        curr = self.root
        
        # Traverse each character in the word
        for w in word:
            # If the path does not exist, create a new node
            if w not in curr.children:
                curr.children[w] = TrieNode()
            
            # Move to the next node
            curr = curr.children[w]
        
        # Mark the end of the word
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        # Start from root
        curr = self.root
        
        # Traverse the word
        for w in word:
            # If any character path does not exist → word not found
            if w not in curr.children:
                return False
            
            # Move to next node
            curr = curr.children[w]
        
        # Only return True if this node marks end of a word
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        # Start from root
        curr = self.root
        
        # Traverse the prefix
        for w in prefix:
            # If path does not exist → no word with this prefix
            if w not in curr.children:
                return False
            
            # Move to next node
            curr = curr.children[w]
        
        # If we successfully traverse the prefix, it exists
        return True