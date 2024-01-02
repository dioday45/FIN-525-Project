# FIN-525-Project
Final project for the course Financial Big Data (FIN-525)

## Plan

1. **Preprocess data**
   1. Import more assets ? 500-1000?
   2. All assets should have the same interval/number of data
   3. Select $T, N$
   4. Filter weird assets
   5. Compute returns
2. **Create $C$ and $D$ matrices**
   1. $C$ is correlation matrix (normalized returns)
   2. Remove noise with eigenvalue clipping
   2. $D$ is distance matrix $(D=\sqrt{2(1-C)})$ 
   3. Analyse eigenvalues
3. **Create graph from $D$** (see this [paper](https://www.frontiersin.org/articles/10.3389/fphy.2020.00323/full) and the image below for visualization of the 3 techniques)
   1. Minimum Spanning Tree + RMT (https://arxiv.org/pdf/1703.00485.pdf --> standard method)
   2. Threshold Networks on correlation
   3. Planar Maximally Filtered Graph (pas mal si combined with threshold networks)
   4. Louvain like in class
   5. Maximal likelihood (like in class)

<img src="assets/fphy-08-00323-g001.jpg" alt="img" style="zoom:50%;" />

4. **Community detection**
   1. Louvain
   2. Perform the clusters in rolling windows and have a look at the Adjusted Rand Index (lecture 12) to see the stability of the different methods.
<!--- 
   3. Correlated modules / Hierarchical modular structure (see p.5 of this [paper](https://arxiv.org/pdf/2103.05623.pdf))
-->
<img src="assets/Screenshot 2023-12-31 at 11.53.52.png" alt="Screenshot 2023-12-31 at 11.53.52" style="zoom:50%;" />

5. **Community analysis**
   1. Leading crypto

6. **Strategy optimization**
   1. Markowitz using only leading crypto or top 5 leading crypto by cluster
   2. Compare out sample risk of the different strategies
   
<!---
2. Compare inter vs intra cluster optimization (see this [paper](https://arxiv.org/pdf/2112.13383.pdf))
-->
