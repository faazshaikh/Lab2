import importlib.util
import random, statistics
import matplotlib.pyplot as plt


# ---------- Load Graph code from graph.py ----------
graph_path = "graph.py"
spec = importlib.util.spec_from_file_location("graph_module", graph_path)
graph_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(graph_module)

create_random_graph = graph_module.create_random_graph
is_connected = graph_module.is_connected


# ---------- Experiment helper ----------
def probCONNECTED(countofNODE, n, trials=20, seed=0):

    rng = random.Random(seed)
    tempResults = []

    for t in range(trials):

        random.seed(rng.randrange(10**9))

        objGRAPH = create_random_graph(countofNODE, n)

        if is_connected(objGRAPH):
            tempResults.append(1)
        else:
            tempResults.append(0)

    return statistics.mean(tempResults)


def main():

    countofNODE = 100
    trials = 20
    seed = 42

    sizes = list(range(0, 501, 10))

    # ---------- Collect results ----------
    results = []
    for n in sizes:
        t = probCONNECTED(countofNODE, n, trials=trials, seed=seed + n)
        results.append(t)
        print(f"n={n:4d}  prob={t:.4f}")

    # ---------- Graph 1: full range ----------
    plt.figure()
    plt.plot(sizes, results, marker="o")
    plt.xlabel("Number of edges")
    plt.ylabel("Connected probability")
    plt.title("Connected probability vs number of edges")
    plt.tight_layout()
    plt.show()


    # ---------- Graph 2: transition region ----------
    regionSizes = [n for n in sizes if 150 <= n <= 400]
    regionResults = [results[i] for i in range(len(sizes)) if 150 <= sizes[i] <= 400]

    plt.figure()
    plt.plot(regionSizes, regionResults, marker="o")
    plt.xlabel("Number of edges")
    plt.ylabel("Connected probability")
    plt.title("Connected probability vs number of edges")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()