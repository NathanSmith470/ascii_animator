from time import sleep
import os, sys

# COMMAND LINE FORMAT: python3 ascii_animator.py {file} {frame_delay=0.5(default)} {iterations=10(default)}

# EX: python3 ascii_animator.py anim01.txt 0.1 30

# VARS
anim_file = None
delay = 0.5
t_cycles = 10

if __name__ == "__main__":
    # GET ARGUMENTS
    try:
        anim_file = sys.argv[1]
        if anim_file == "--help" or anim_file == "-h":
            print("")
            quit()
    except IndexError:
        print("No Animation File!")
        quit()
    try:
        delay = float(sys.argv[2])
    except IndexError:
        delay = 0.5
    try:
        t_cycles = int(sys.argv[3])
    except IndexError:
        t_cycles = 10

    # READ FILE
    afile = open(anim_file,"r")
    frames = []
    tfram = ""

    for l in afile.readlines():
        if l.replace("\n","") == "next":
            frames.append(tfram)
            tfram = ""
        elif l.replace("\n","") == "end":
            frames.append(tfram)
            tfram = ""
        else:
            tfram += l

    # START ANIMATION
    print("Starting Animation...")
    sleep(1)


    for t in range(0,t_cycles):
        for f in frames:
            os.system("clear")
            print(f)
            sleep(delay)
