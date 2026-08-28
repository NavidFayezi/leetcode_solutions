class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        string_length = len(s)
        res = []
        words_dict = dict()
        substring_length = 0
        no_words = len(words)

        for word in words:
            substring_length += len(word)
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

        for i in range(string_length - substring_length + 1):
            seen = words_dict.copy()
            j = i
            counter = 0
            while j <= string_length - word_length:

                temp_word = s[j: j + word_length]
                if temp_word in words_dict and seen[temp_word] > 0:
                    seen[temp_word] -= 1
                    j += word_length
                    counter += 1
                else:
                    break

            if counter == no_words:
                res.append(i)
        
        return res
