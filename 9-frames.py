import random

class Frame:
    def __init__(self, seq_no, info):
        self.seq_no = seq_no
        self.info = info

def sort_frames(frames):
    n = len(frames)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if frames[j].seq_no > frames[j + 1].seq_no:
                frames[j], frames[j + 1] = frames[j + 1], frames[j]
                swapped = True
        if not swapped:
            break

def main():
    n = int(input("Enter the number of frames: "))
    frames = []
    for i in range(n):
        seq_no = random.randint(1, 100)
        info = input(f"Enter the frame contents for sequence number {seq_no}: ")
        frames.append(Frame(seq_no, info))

    sort_frames(frames)

    print("\nThe frames in sequence are:")
    for frame in frames:
        print(f"Sequence Number: {frame.seq_no}, Frame Contents: {frame.info}")

if __name__ == "__main__":
    main()
