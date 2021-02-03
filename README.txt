# ascii_animator
a super simple ascii animation script for the terminal

# COMMAND LINE FORMAT: python3 ascii_animator.py {file} {frame_delay=0.5(default)} {iterations=10(default)}

# EX: python3 ascii_animator.py anim01.txt 0.1 30
      -> This will run anim01.txt with a 0.1 second delay between frames for 30 cycles(from beginning to end)

There are three sample animations in the repository

# Creating a animation file is simple.
1: make a new .txt file
2: create an animation frame
3: on the line after the frame write simply "next" and NOTHING else.
4: repeat steps 2-3  until finished
5: when finished write "end"
