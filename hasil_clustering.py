from metaflow import Flow

run = Flow('ManyKMeansFlow').latest_run

try:

    print("3 Clusters:")
    for i, cluster_terms in enumerate(run.data.top_terms[0], 1):
        print(f"Cluster {i}: {cluster_terms[:3]}")

    print("\n4 Clusters:")
    for i, cluster_terms in enumerate(run.data.top_terms[1], 1):
        print(f"Cluster {i}: {cluster_terms[:4]}")

    print("\n5 Clusters:")
    for i, cluster_terms in enumerate(run.data.top_terms[2], 1):
        print(f"Cluster {i}: {cluster_terms[:5]}")

    print("\nData Distribution:")
    print("3 Clusters:", 
        {i: list(run.data.labels[0:len(run.data.labels):3]).count(i) 
         for i in range(3)})
    print("4 Clusters:", 
        {i: list(run.data.labels[0:len(run.data.labels):4]).count(i) 
         for i in range(4)})
    print("5 Clusters:", 
        {i: list(run.data.labels[0:len(run.data.labels):5]).count(i) 
         for i in range(5)})

except AttributeError as e:
    print("Error accessing top terms:", e)
except IndexError as e:
    print("Error with top terms indexing:", e)