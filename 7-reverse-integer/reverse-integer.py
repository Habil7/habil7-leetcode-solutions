class Solution:
    def reverse(self, x: int) -> int:
        is_negative_number = x < 0
        remaining_number = abs(x)

        reversed_number = 0

        while remaining_number:
            last_digit = remaining_number % 10
            remaining_number //= 10

            reversed_number = reversed_number * 10 + last_digit

            if reversed_number > 2**31 - 1:
                return 0

        return -reversed_number if is_negative_number else reversed_number