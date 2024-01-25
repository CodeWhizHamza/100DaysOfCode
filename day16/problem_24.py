# PROBLEM: Lexicographic Permutations


def get_permutations(max: int):
    # permutations = []
    for i in range(max):
        for j in range(max):
            if j == i:
                continue
            for k in range(max):
                if k in (i, j):
                    continue
                for l in range(max):
                    if l in (i, j, k):
                        continue
                    for m in range(max):
                        if m in (i, j, k, l):
                            continue

                        for n in range(max):
                            if n in (i, j, k, l, m):
                                continue

                            for o in range(max):
                                if o in (i, j, k, l, m, n):
                                    continue

                                for p in range(max):
                                    if p in (i, j, k, l, m, n, o):
                                        continue

                                    for q in range(max):
                                        if q in (i, j, k, l, m, n, o, p):
                                            continue

                                        for r in range(max):
                                            if r in (i, j, k, l, m, n, o, p, q):
                                                continue
                                            yield f"{i}{j}{k}{l}{m}{n}{o}{p}{q}{r}"

    # print(permutations)


if __name__ == "__main__":
    i = 0
    for permutation in get_permutations(10):
        i += 1

        if i == 1_000_000:
            print(permutation)
            break
