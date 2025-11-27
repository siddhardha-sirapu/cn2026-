def main():
    n = int(input("Enter the number of nodes: "))
    adjacency_matrix = [[0] * (n + 1) for _ in range(n + 1)]

    print("Enter adjacency matrix:")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            adjacency_matrix[i][j] = int(input(f"Enter connection between node {i} and node {j} (0 or 1): "))

    root = int(input("Enter the root node: "))

    print(f"Adjacent nodes of root node {root}:")
    for j in range(1, n + 1):
        if adjacency_matrix[root][j] == 1:
            print(j, end="\t")

    print() 


if __name__ == "__main__":
    main()
