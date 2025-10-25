class Solution:
    mapping = [
        ("M", 1000),
        ("D", 500),
        ("C", 100),
        ("L", 50),
        ("X", 10),
        ("V", 5),
        ("I", 1),
    ]
    subtractive_mapping = [
        ("CM", 900),
        ("CD", 400),
        ("XC", 90),
        ("XL", 40),
        ("IX", 9),
        ("IV", 4),
    ]

    def intToRoman(self, num: int) -> str:
        assert num > 0
        assert num < 4000

        # First, break the number into its decimal places
        divider = 10
        decimal_places = []
        multiplier = 1
        while num > 0:
            decimal_places.append((num % divider) * multiplier)
            multiplier *= 10
            num = num // 10

        # Then, convert each decimal place to roman numeral, using the helper
        # function, and concatenate the results
        roman_numeral = ""
        for i in decimal_places:
            roman_numeral = self.helper(i) + roman_numeral

        return roman_numeral

    def helper(self, num: int) -> str:
        if num == 0:
            return ""

        for map in self.subtractive_mapping:
            if num == map[1]:
                return map[0]

        num_letter = len(self.mapping)
        current_letter = -1
        for i in range(num_letter):
            if self.mapping[i][1] <= num:
                current_letter = self.mapping[i]
                break

        assert current_letter != -1
        return current_letter[0] + self.helper(num - current_letter[1])


if __name__ == "__main__":
    test_input = 10
    solution = Solution()
    print(solution.intToRoman(test_input))  # output MMMDCCXLIX
