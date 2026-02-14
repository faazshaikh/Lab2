import importlib.util
import random, statistics
import matplotlib.pyplot as plt


# ---------- Load Graph code from graph.py ----------
graph_path = "graph.py"
spec = importlib.util.spec_from_file_location("graph_module", graph_path)
graph_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(graph_module)

create_random_graph = graph_module.create_random_graph
has_cycle = graph_module.has_cycle


# ---------- Experiment helper ----------
def probCYCLE(countofNODE, n, trials=21, seed=0):

    rng = random.Random(seed)
    tempResults = []

    for t in range(trials):

        # create_random_graph uses the global random module, so seed it each trial
        random.seed(rng.randrange(10**9))

        objGRAPH = create_random_graph(countofNODE, n)

        if has_cycle(objGRAPH):
            tempResults.append(1)
        else:
            tempResults.append(0)

    return statistics.mean(tempResults)


def main():

    countofNODE = 100
    trials = 21
    seed = 42

    sizes = list(range(0, 501, 10))  # number of edges

    # ---------- Warm-up (helps with caches / Python one-time effects) ----------
    _ = probCYCLE(countofNODE, 50, trials=3, seed=123)

    # ---------- Collect results ----------
    results = []
    for n in sizes:
        t = probCYCLE(countofNODE, n, trials=trials, seed=seed + n)
        results.append(t)
        print(f"n={n:4d}  prob={t:.4f}")

    # ---------- Plot 1: edges vs probability ----------
    plt.figure()
    plt.plot(sizes, results, marker="o")  # <-- plt.plot used as requested
    plt.xlabel("Number of edges")
    plt.ylabel("Cycle probability")
    plt.title("Cycle probability vs number of edges")
    plt.tight_layout()
    plt.show()  # <-- show plot

    # ---------- Plot 2: proportion of edges vs probability ----------
    edgesMAX = countofNODE * (countofNODE - 1) // 2
    propSizes = [n / edgesMAX for n in sizes]

    plt.figure()
    plt.plot(propSizes, results, marker="o")  # <-- plt.plot used as requested
    plt.xlabel("Proportion of edges (n / edgesMAX)")
    plt.ylabel("Cycle probability")
    plt.title("Cycle probability vs proportion of edges")
    plt.tight_layout()
    plt.show()  # <-- show plot


if __name__ == "__main__":
    main()