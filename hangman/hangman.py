from executioner import put_on_mask, show_instructions, announce, end_game
from rope import put_rope_on_neck
import sys

if __name__ == "__main__":
    while True:
        put_on_mask()
        try:
            menu_pick = int(input())
            if menu_pick == 1:
                put_rope_on_neck()
            elif menu_pick == 2:
                show_instructions()
            else:
                sys.exit()
                break
        except ValueError:
            print("Invalid Input.")
# Win prompt
