"""
      Flip Coin and print percentage of Heads and Tails
        a. I/P -> The number of times to Flip Coin. Ensure it is positive integer.
        b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or heads
        c. O/P -> Percentage of Head vs Tails
"""


import random


def print_ans(head_percentage, tail_percentage):
    print(f"Head Percentage : {head_percentage}")
    print(f"Tail Percentage : {tail_percentage}")

def logic(input_val):
    try:
        if input_val < 0:
            raise ValueError("Non Negative Numbers Not Allowed")
        head_counter = 0
        tail_counter = 0

        for i in range(input_val):
            random_number = random.random()

            if random_number > 0.5:
                head_counter += 1
            else:
                tail_counter += 1

        percentage_of_head = head_counter / input_val * 100
        percentage_of_tail = tail_counter / input_val * 100

        return (percentage_of_head, percentage_of_tail)

    except ValueError as e:
        print("ErrorType ->")

def main():
        input_val = int(input("Please enter how many times to flip a coin : "))
        ans = logic(input_val)

        print_ans(ans[0],ans[1])


if __name__ == "__main__":
    main()