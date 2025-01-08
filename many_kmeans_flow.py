from metaflow import FlowSpec, step
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

class ManyKMeansFlow(FlowSpec):

    @step
    def start(self):
        df = pd.read_csv("scaled_data.csv")
        self.data = df.to_numpy()
        self.feature_names = df.columns.tolist()
        self.next(self.cluster_3)

    @step
    def cluster_3(self):
        self.n_clusters = 3
        self.top_term_count = 3  # Jumlah kata untuk klaster 3
        self.perform_clustering()
        self.next(self.cluster_4)

    @step
    def cluster_4(self):
        self.n_clusters = 4
        self.top_term_count = 4  # Jumlah kata untuk klaster 4
        self.perform_clustering()
        self.next(self.cluster_5)

    @step
    def cluster_5(self):
        self.n_clusters = 5
        self.top_term_count = 5  # Jumlah kata untuk klaster 5
        self.perform_clustering()
        self.next(self.end)

    def perform_clustering(self):
        model = KMeans(n_clusters=self.n_clusters, random_state=42)
        self.labels = model.fit_predict(self.data)
        self.cluster_centers = model.cluster_centers_
        self.top_terms = self.get_top_terms()

    def get_top_terms(self):
        top_terms = []
        for i in range(self.n_clusters):
            cluster_data = self.data[self.labels == i]
            cluster_mean = np.mean(cluster_data, axis=0)
            top_indices = cluster_mean.argsort()[::-1]
            
            cluster_top_terms = [
                self.feature_names[j] for j in top_indices[:self.top_term_count]
            ]
            
            top_terms.append(cluster_top_terms)
        
        return top_terms

    @step
    def end(self):
        print("3 Clusters Top Terms:", self.top_terms[0])
        print("4 Clusters Top Terms:", self.top_terms[1])
        print("5 Clusters Top Terms:", self.top_terms[2])

if __name__ == '__main__':
    ManyKMeansFlow()