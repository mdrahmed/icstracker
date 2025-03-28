from core.remove import init_patterns
from core.utils import load_file

F1 = 'step2-extracted_common_part_retrieval\patterns_o.txt'
F2 = 'step2-extracted_common_part_retrieval\patterns.txt'


def init(filename):
    file = load_file(filename)
    patterns = init_patterns(file)
    strp = [''.join(p) for p in patterns]
    return strp


def prints(data):
    res = sorted(list(set(data)))
    print(res)


def dedup_list(a, b):
    res = []
    for i in a:
        if i not in b:
            res.append(i)
    return res


def main():
    p1 = init(F1)
    p2 = init(F2)
    iintersection = []
    iinj = []
    iunique = []
    for idx, i in enumerate(p1):
        idx += 1
        found = False
        for j in p2:
            if i == j:
                iintersection.append(idx)
                found = True
                break
            elif i in j:
                iinj.append(idx)
                found = True
        if not found:
            iunique.append(idx)
            # print(len(i))

    jintersection = []
    jini = []
    junique = []
    for idx, i in enumerate(p2):
        idx += 1
        found = False
        for j in p1:
            if i == j:
                jintersection.append(idx)
                found = True
                break
            elif i in j:
                jini.append(idx)
                found = True
        if not found:
            junique.append(idx)
    print('intersection in f1:')
    prints(iintersection)
    print('f1 patterns partially in f2:')
    prints(dedup_list(iinj, iintersection))
    print('unique patterns in f1:')
    prints(iunique)

    print('intersection in f2:')
    prints(jintersection)
    print('f2 patterns partially in f1:')
    prints(dedup_list(jini, jintersection))
    print('unique patterns in f2:')
    prints(junique)


main()
