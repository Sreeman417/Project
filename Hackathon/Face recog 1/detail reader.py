import pickle
with open("D:\Python files\Hackathon\Face recog 1\markedroll.dat","rb") as f:
    while True:
        try:
            print(pickle.load(f))
        except EOFError:
            break