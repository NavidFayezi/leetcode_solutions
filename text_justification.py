class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        assert maxWidth > 0

        num_words = len(words)
        counter = 0
        temp_list = []
        line_length = 0
        line_length_no_spaces = 0
        res = []
        while counter < num_words:

            # If line has enough space for the next word, add the next word
            if line_length + len(words[counter]) <= maxWidth:
                line_length += len(words[counter]) + 1
                line_length_no_spaces += len(words[counter])
                temp_list.append(words[counter])
                counter += 1

            # Otherwise, justify the current line
            else:
                line_length = 0
                res.append(
                    self.justify_line(
                        temp_list, maxWidth, line_length_no_spaces
                    )
                )
                temp_list = []
                line_length_no_spaces = 0

        # the last line should be handled differently. See an example of
        # correct output
        last_line = ""
        for word in temp_list:
            last_line += " " + word
        last_line = last_line[1:]
        trailing_spaces = maxWidth - len(last_line)
        last_line += trailing_spaces * " "
        res.append(last_line)
        return res

    def justify_line(
        self, line: list[str], max_width: int, length_wo_spaces: int
    ) -> list[str]:
        num_words = len(line)
        space_placeholder = max(num_words - 1, 1)
        total_space = max_width - length_wo_spaces
        min_space_after_word = total_space // space_placeholder
        spaces_array = [
            min_space_after_word * " " for i in range(space_placeholder)
        ]
        spaces_left = total_space % space_placeholder

        # After each word in the line, there should be space(s)
        # spaces_array[i] stores the number of spaces that must be printed
        # after the the word i, i.e., line[i]
        for i in range(spaces_left):
            spaces_array[i] = spaces_array[i] + " "

        # This loop appends spaces to words
        res = ""
        for i in range(num_words):
            res += line[i]
            if i >= space_placeholder:
                pass
            else:
                res += spaces_array[i]

        return res


if __name__ == "__main__":
    test_input = [
        "Science",
        "is",
        "what",
        "we",
        "understand",
        "well",
        "enough",
        "to",
        "explain",
        "to",
        "a",
        "computer.",
        "Art",
        "is",
        "everything",
        "else",
        "we",
        "do",
    ]
    solution = Solution()
    print(solution.fullJustify(test_input, 20))
