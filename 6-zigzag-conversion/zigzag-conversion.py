class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        current_row_index = 0
        step_direction = 1  

        rows_characters = [[] for _ in range(numRows)]

        for character in s:
            rows_characters[current_row_index].append(character)

            if current_row_index == 0:
                step_direction = 1
            elif current_row_index == numRows - 1:
                step_direction = -1

            current_row_index += step_direction

        zigzag_string = ""

        for row in rows_characters:
            for character in row:
                zigzag_string += character
                
        return zigzag_string