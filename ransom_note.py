class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        character_set = "abcdefghijklmnopqrstuvwxyz"
        ransom_hash_table = {}
        magazine_hash_table = {}

        for character in character_set:
            ransom_hash_table[character] = 0
            magazine_hash_table[character] = 0
        
        for character in ransomNote:
            ransom_hash_table[character] += 1
        
        for character in magazine:
            magazine_hash_table[character] += 1

        rc = True
        for character in character_set:
            if ransom_hash_table[character] > magazine_hash_table[character]:
                rc = False
                break

        return rc
