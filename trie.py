class TrieNode:

    def __init__(self, character: str, end_of_word: bool = False):
        self.character = character
        self.end_of_word = end_of_word
        self.next_letters = {}
        for _char in "abcdefghijklmnopqrstuvwxyz":
            self.next_letters[_char] = None

    def insert_letter(self, letter: str, end_of_word: bool = False):
        if self.next_letters[letter] == None:
            self.next_letters[letter] = TrieNode(letter, end_of_word)


class Trie:

    def __init__(self):
        self.root = TrieNode(".")

    def insert(self, word: str) -> None:
        temp = self.root
        for character in word:
            temp.insert_letter(character)
            temp = temp.next_letters[character]

        temp.end_of_word = True

    def search(self, word: str) -> bool:
        temp = self.root
        rc = True
        for character in word:
            if temp.next_letters[character] is None:
                rc = False
                break
            else:
                temp = temp.next_letters[character]

        return rc and temp.end_of_word

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        rc = True
        for character in prefix:
            if temp.next_letters[character] is None:
                rc = False
                break
            else:
                temp = temp.next_letters[character]
        return rc


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
