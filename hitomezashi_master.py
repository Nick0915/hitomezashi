#!/bin/python3

import hitomezashi2
from sys import argv
from sys import exit

def print_help():
    text = '''
    Welcome to the Hitomezashi stitch pattern generator!
    What is Hitomezashi?
        Hitomezashi is a form of stitching clothes that appreciates the beauty of
        fixing broken things. It uses a grid of alternating (on-top/underneath
        fabric) stitches going in both axes to generate an interesting pattern.
    Randomization:
        The resulting pattern can vary based on whether a particular row or column
        of stitches stared on-top or underneath the fabric. Randomizing which the
        starting stitch is leads to very interesting, procedurally generated
        patterns. This program also offers the ability to enter phrases as a basis
        for how the stitches start: consonants start the stitch underneath, and
        syllables start it on-top. These must be provided for both the vertical
        and horizontal series of stitches, but don't have any length requirement.
        The shorter they are, though, the more repetition you may see.
    Usage:
        'python3 hitomezashi_master.py'                                                       <- defaults to a screen size of 600 x 600
                                                                                                 and a grid size of 50 x 50, and
                                                                                                 randomizes the start stitch
        'python3 hitomezashi_master.py <screen size: int> <grid size: int>'                   <- uses the provided screen and grid sizes
                                                                                                 (always squares) and randomizes the start
                                                                                                 stitch
        'python3 hitomezashi_master.py <screen size: int> <grid size: int> <x-seed> <y-seed>' <- same as before, but uses the given lines
                                                                                                 instead of randomization for the start
    Examples:
        'python3 hitomezashi_master.py 500 20'
            creates a screen of 500 x 500 and a grid of 20 x 20 with random starts
        'python3 hitomezashi_master.py 400 100 "goodbye world" "my final message"'
            creates a screen of 400 x 400 and a grid of 100 x 100 with the
            vertical starts determined by "goodbye world" and the horizontal ones
            by "my final message"
    Note:
        Please allow up to a minute for large grid sizes to render. If you are
        seeing a white screen for an extended period of time, please end the task
        through task manager or by pressing Ctrl+C (if ran from the command prompt).
        Try seeing what happens with the default invocation of this program. If
        that happens to work, it may be that your provided input sizes were too
        large.
    Image saving:
        This program automatically saves the generated images as a postscript file
        (.ps extension). These can be easily converted to jpg or png images using
        online converters or a tool like Photoshop/GIMP. The creation of a file
        can be turned off by changing "CREATE_FILE" to false in hitomezashi2.py
    Inspiration:
        https://www.youtube.com/watch?v=JbfhzlMk2eY&t=29s&ab_channel=Numberphile'''
    print(text)

def main():
    try:
        count = len(argv)
        if count == 2 and argv[1].lower() == 'help':
            print_help()
            return
        assert not (count != 1 and count != 3 and count != 5)
        if count != 1:
            hitomezashi2.SCREEN_SIZE = int(argv[1])
            hitomezashi2.NUM_CELLS = int(argv[2])
            assert hitomezashi2.SCREEN_SIZE >= 300
            assert hitomezashi2.NUM_CELLS <= hitomezashi2.SCREEN_SIZE / 2
            if count == 5:
                hitomezashi2.SEEDED = True
                hitomezashi2.x_seed = [0 if hitomezashi2.is_vowel(x) else 1 for x in argv[3]]
                hitomezashi2.y_seed = [0 if hitomezashi2.is_vowel(x) else 1 for x in argv[4]]

        hitomezashi2.main()
    except (AssertionError, ValueError):
        print(f"cannot run the program with the given inputs: [{argv[1:]}]")
        print("correct usages:\n"
                "\tpython3 hitomezashi_master.py help\n"
                "\tpython3 hitomezashi_master.py\n"
                "\tpython3 hitomezashi_master.py <screen size: int> <grid size: int>\n"
                "\tpython3 hitomezashi_master.py <screen size: int> <grid size: int> <x-seed: str> <y-seed: str>")
        print("if custom sizes were provided, please make sure that the grid size is at most half the screen size")
        print("\tmake sure also that the screen size is larger than 299")
    finally:
        print("Exiting application...")
        exit()



if __name__ == "__main__":
    main()