# PROBLEM: Lexicographic Permutations


def get_permutations():
    permutations = []
    for i in range(3):
        for j in range(3):
            if j == i:
                continue
            for k in range(3):
                if k == j or k == i:
                    continue
                permutations.append(f"{i}{j}{k}")

    print(permutations)


if __name__ == "__main__":
    get_permutations()
