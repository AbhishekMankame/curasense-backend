## 🌲What is Random Forest?
A Random Forest is basically a collection (ensemble) of Decision Trees.</br>
Imagine a forest with many trees - each one making its own predictions - and then the forest votes on the final prediction.

## 🪵Building the Forest (Bootstrapping)
1️⃣ Bootstrapping:<br>
- Randomly pick subsets of data (with replacement) from the training data to build each tree.
- This creates multiple "mini-datasets" -> some samples repeated, some left out (out-of-bag samples).

1️⃣ Growing Trees:
- For each mini-dataset, build a Decision Tree.
- Trees don't see the entire dataset -> diversity!
- Trees grown deep (fully grown) -> better memorization of patterns in their mini-dataset.

## 🍃 Making Trees Diverse (Feature Bagging)
- At each split in the tree, instead of considering all features (symptoms), consider only a random subset.
- Example: If you have 100 symptoms, maybe consider only 10 at each split.
- This ensures each tree is unique, reducing overfitting.