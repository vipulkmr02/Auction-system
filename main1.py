from bddrs import *

participant = Participant(
    "vipul", ("localhost", 61000)
)

participant.start()

while True:
    i = input("> ")

    if i == "stop":
        break

    elif i.startswith("+"):
        participant.bid(int(i.split()[1]))
