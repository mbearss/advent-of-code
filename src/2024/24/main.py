import networkx as nx

def and_gate(inputs):
    return all(inputs)

def or_gate(inputs):
    return any(inputs)

def xor_gate(inputs):
    return sum(inputs) % 2 == 1

gate_operations = {
    "AND": and_gate,
    "OR": or_gate,
    "XOR": xor_gate,
}

def simulate(graph):
    topo_order = list(nx.topological_sort(graph))
    node_values = {}
    wrong = set()
    highest_z = None

    for node in graph.nodes:
        if node[0] == "z":
            if highest_z is None or int(node[1:]) > int(highest_z[1:]):
                highest_z = node

    for node in topo_order:
        node_type = graph.nodes[node]["type"]
        if node_type == "input":
            node_values[node] = graph.nodes[node]["value"]
        elif node_type == "gate":
            gate_type = graph.nodes[node]["gate_type"]
            predecessors = list(graph.predecessors(node))
            if len(predecessors) == 2:
                op1, op2 = predecessors
                if op1 in node_values and op2 in node_values:
                    inputs = [node_values[op1], node_values[op2]]
                    node_values[node] = gate_operations[gate_type](inputs)

                    # Detect incorrect connections
                    if node[0] == "z" and gate_type != "XOR" and node != highest_z:
                        wrong.add(node)
                    if (
                        gate_type == "XOR"
                        and node[0] not in ["x", "y", "z"]
                        and op1[0] not in ["x", "y", "z"]
                        and op2[0] not in ["x", "y", "z"]
                    ):
                        wrong.add(node)
                    if gate_type == "AND" and "x00" not in [op1, op2]:
                        for successor in graph.successors(node):
                            if graph.nodes[successor]["gate_type"] != "OR":
                                wrong.add(node)
                    if gate_type == "XOR":
                        for successor in graph.successors(node):
                            if graph.nodes[successor]["gate_type"] == "OR":
                                wrong.add(node)

    return node_values, wrong

if __name__ == "__main__":
    circuit = nx.DiGraph()
    with open("input.txt", "r") as f:
        lines = f.readlines()
        i = 0
        while len(line := lines[i].strip()) > 0:
            w, s = line.split(":")
            circuit.add_node(w, type="input", value=int(s))
            i += 1
        i += 1
        while i < len(lines):
            line = lines[i].strip()
            g1, op, g2, _, g3 = line.split(" ")
            circuit.add_node(g3, type="gate", gate_type=op)
            circuit.add_edge(g1, g3)
            circuit.add_edge(g2, g3)
            i += 1

    node_values, wrong = simulate(circuit)

    bits = ['1' if node_values[wire] else '0' for wire in sorted(node_values, reverse=True) if wire[0] == "z"]
    print(int("".join(bits), 2))
    print(",".join(sorted(wrong)))
