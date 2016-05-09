import argparse
import re


def ParsArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f1', '-F1', nargs='?', help="Path to txt file with list of pcs")
    parser.add_argument('-f2', '-F2', nargs='?', help="path to txt file with list of pcs#2")
    return parser


def ParsFile(path):
    # take info from file
    file = open(path, 'r')
    list_pcs = []
    for line in file:
        # print(line[1:])
        line = re.sub("^\s+|\n|\r|\s+$", '', line)
        if (line != "\n") & (line != ''):
            list_pcs.append(line.upper())

    return list_pcs


def main():
    parser = ParsArgs()
    namespace = parser.parse_args()
    list1 = ParsFile(namespace.f1)
    list2 = ParsFile(namespace.f2)
    a = [a for a in list1 if a in list2]
    for x in a:
        print(x)
    return a


if __name__ == '__main__':
    main()
