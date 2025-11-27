def initialize_network(num_nodes):
    print("\nEnter the cost matrix for the network (use 999 for no direct connection):")
    distance_matrix = []
    for i in range(num_nodes):
        row = list(map(int, input(f"Enter costs for node {i} to all nodes: ").split()))
        distance_matrix.append(row)
    return distance_matrix

def distance_vector_routing(num_nodes, distance_matrix):
    routing_tables = [[float("inf")] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                routing_tables[i][j] = 0
            else:
                routing_tables[i][j] = distance_matrix[i][j]
    converged = False
    iteration = 0
    while not converged:
        converged = True
        iteration += 1
        print(f"\nIteration {iteration}:")
        for i in range(num_nodes):
            for j in range(num_nodes):
                for k in range(num_nodes):
                    if routing_tables[i][j] > routing_tables[i][k] + routing_tables[k][j]:
                        routing_tables[i][j] = routing_tables[i][k] + routing_tables[k][j]
                        converged = False
        for i in range(num_nodes):
            print(f"Routing table for node {i}: {routing_tables[i]}")
    return routing_tables

def main():
    print("Distance Vector Routing Algorithm")
    num_nodes = int(input("\nEnter the number of nodes in the network: "))
    distance_matrix = initialize_network(num_nodes)
    routing_tables = distance_vector_routing(num_nodes, distance_matrix)
    print("\nFinal Routing Tables:")
    for i in range(num_nodes):
        print(f"Node {i}: {routing_tables[i]}")

if __name__ == "__main__":
    main()
