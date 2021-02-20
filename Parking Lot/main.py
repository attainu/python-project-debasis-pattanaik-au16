import argparse
from parking_lot import parking

def main():

    parkinglot = parking()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", required=False,
                        dest='src_file', help="Input File")
    args = parser.parse_args()

    if args.src_file:
        with open(args.src_file) as f:
            for line in f:
                line = line.rstrip('\n')
                parkinglot.show(line)
    else:
        while True:
            line = input("$ ")
            parkinglot.show(line)


if __name__ == '__main__':
    main()