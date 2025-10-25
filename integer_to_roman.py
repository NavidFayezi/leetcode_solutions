class Solution:
    """Convert integers to Roman numerals.

    This class provides a solution for converting a positive integer
    (1..3999) into its Roman numeral representation. It uses two
    lookup tables: `mapping` for the standard numerals and
    `subtractive_mapping` for subtractive pairs (like IV, IX).

    Methods
    -------
    intToRoman(num: int) -> str
        Convert `num` to its Roman numeral string.

    helper(num: int) -> str
        Internal recursive helper that converts a single decimal place
        (e.g. 900, 40, 3) into Roman numerals.
    """
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
        """Convert an integer to a Roman numeral.

        Parameters
        ----------
        num : int
            The integer to convert. Must satisfy 1 <= num < 4000.

        Returns
        -------
        str
            The Roman numeral representation of `num`.

        Raises
        ------
        AssertionError
            If `num` is not in the valid range (1..3999).
        """

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
        """Recursive helper that converts a number place to Roman.

        The function expects `num` to be a single decimal place value
        (for example 900, 40, 3). It returns the Roman numeral fragment
        corresponding to that value. If `num` is 0 it returns an empty
        string.

        Parameters
        ----------
        num : int
            Decimal-place integer to convert (>= 0).

        Returns
        -------
        str
            Roman numeral fragment for `num`.
        """

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
    test_input = 3749
    solution = Solution()
    print(solution.intToRoman(test_input))  # output MMMDCCXLIX
