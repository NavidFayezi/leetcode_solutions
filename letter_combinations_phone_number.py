class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        no_combo = 1
        for digit in digits:
            no_combo *= len(digit_to_letter[digit])

        res = ["" for i in range(no_combo)]

        divisor = 1
        for digit in digits:
            letters = digit_to_letter[digit]
            divisor *= len(letters)
            res_index = 0
            letters_index = 0

            max_letter_repetition = no_combo // divisor
            repetition_counter = 0
            while res_index < no_combo:
                res[res_index] += letters[letters_index]
                repetition_counter += 1
                if repetition_counter >= max_letter_repetition:
                    letters_index = (letters_index + 1) % len(letters)
                    repetition_counter = 0

                res_index += 1

        return res
