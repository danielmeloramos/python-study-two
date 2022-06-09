#1- kwargs

from tabnanny import verbose


def main(**kwargs):
    if kwargs.get("verbose"):
        print("verbose activated")
    return 0

print(main(verbose=True))


