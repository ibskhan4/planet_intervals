# Efficiently Identifying Gaps in a Planetary System

This function tackles the intriguing challenge of finding gaps between planets within a defined range. We leverage two key strategies: interval representation and iterative merging.

## Step 1: Building Intervals:

We first construct intervals for each planet by using their center and add the "orbit buffer" on both sides. This captures the space occupied by each planet.

Step 2: Sorting and Merging Intervals:

We sort the intervals based on their starting points. This will be extremely helpful in both merging intervals as well as analyzing the gaps in between. We then iterate through and merge these sorted intervals, resulting in a list of non-overlapping intervals.
For each interval:

If it starts after the end of the last interval in the final list, we add it directly. This signifies a clear gap between planets.
If it overlaps with the last interval, we merge them by taking the minimum starting point and maximum ending point, which represents the combined occupied space.

## Step 3: Extracting Gaps from Merged Intervals:

Finally, we analyze the list of merged intervals to identify the remaining gaps between planets. We consider the potential gaps on either end of the defined range (0-1000) and add them if necessary.
