def deal_into(deck):
    return [i for i in reversed(deck)]

def cut(deck, n):
    return deck[n:] + deck[:n]

def deal_with(deck, n):
    new_deck = [None]*len(deck)
    for i, card in enumerate(deck):
        new_deck[(i*n)%len(deck)] = card
    return new_deck

def shuffle(deck, process):
    for instr in process:
        if instr[:3] == "cut":
            deck = cut(deck, int(instr[4:]))
        elif instr == "deal into new stack":
            deck = deal_into(deck)
        elif instr[:19] == "deal with increment":
            deck = deal_with(deck, int(instr[20:]))
        else:
            print("Invalid instruction:", instr)
            exit(1)
    return deck

with open("day22/process.txt", "r") as f:
    process = f.read().split("\n")

test1 = """\
deal with increment 7
deal into new stack
deal into new stack""".split("\n")

test2 = """\
deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1""".split("\n")

deck1 = [i for i in range(10007)]
print("Position of card 2019:", shuffle(deck1, process).index(2019))