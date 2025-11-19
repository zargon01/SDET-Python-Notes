# Selection Sort

## What
Selection Sort is a comparison-based sorting algorithm. It sorts an array by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element until the entire array is sorted.

## When
Use Selection Sort when working with small datasets, when memory writes are costly, or when teaching fundamental sorting concepts.

## Where
Selection Sort is suitable for environments where memory writes are expensive, such as embedded systems or hardware with limited write cycles.

## How

1. Find the smallest element and swap it with the first element.
2. Find the next smallest among remaining elements and swap it with the second element.
3. Repeat until all elements are in correct position.

Time Complexity: O(n^2) due to nested loops.

Example Steps:
- Start with [7, 12, 9, 11, 3]
- Move 3 to front: [3, 7, 12, 9, 11]
- Move 9 to correct position: [3, 7, 9, 12, 11]
- Move 11 to correct position: [3, 7, 9, 11, 12]
Final sorted array: [3, 7, 9, 11, 12]

## Why
Selection Sort is easy to understand and implement, requires only O(1) extra memory, and performs fewer swaps compared to many other algorithms. It is ideal for teaching and for cases where memory writes are costly.

## Advantages
- Easy to understand and implement.
- Requires only O(1) extra memory space.
- Fewer memory writes compared to other algorithms.

## Disadvantages
- Time complexity of O(n^2) makes it slower for large datasets.
- Not stable (does not maintain relative order of equal elements).

## Applications
- Teaching fundamental sorting mechanisms.
- Small lists where overhead of complex algorithms isn't justified.
- Heap Sort algorithm is based on Selection Sort.

## References
- https://www.w3schools.com/dsa/dsa_algo_selectionsort.php
- https://www.geeksforgeeks.org/dsa/selection-sort-algorithm-2/
- https://takeuforward.org/sorting/selection-sort-algorithm/
- r/GATEtard
- r/PythonLearning
- r/DSALeetCode
