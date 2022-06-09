#1- kwargs

def main(**kwargs):
    if kwargs.get("verbose"):
        print("verbose activated")
    return 0

main(verbose=True)


