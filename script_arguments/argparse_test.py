import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', required=True,
                        help='translate destination language code')
    args = parser.parse_args()
    print(f'RESULT: {args.action}')
