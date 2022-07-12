import getopt
import sys


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "l:", ["lang="])
    except getopt.GetoptError:
        print(f"Usage: {sys.argv[0]} -l <lang>")  # will print something like "option -a not recognized"
        sys.exit(2)
    lang = 'en'
    for o, a in opts:
        print(f'o={o} , a={a}')
        if o in ("-l", "--lang"):
            print(f' *** {a}')
            lang = str(a)
        else:
            assert False, "unhandled option"

    print(f'RESULT: {lang}')


if __name__ == "__main__":
    main()
