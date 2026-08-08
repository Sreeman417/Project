import pickle
with open("D:\Python files\Hackathon\Face recog 2\details.dat","rb") as f:
    while True:
        try:
            l = pickle.load(f)
            print(l)
        except EOFError:
            break
with open("D:\Python files\Hackathon\Face recog 2\markedroll.dat","rb") as f:
    while True:
        try:
            print(pickle.load(f))
        except EOFError:
            break