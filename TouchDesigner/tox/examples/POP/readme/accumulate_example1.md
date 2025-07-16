# Accumulate

Scan sum

## Algorithm

A scan sum (or prefix sum) is a concept in computing where you create a sequence of cumulative sums from an input array or list. Each element in the scan sum array is the sum of all previous elements, including itself, up to that point in the original array.

For example given an array:

    [1, 2, 3, 4]

The scan sum array would be:

    [1, 3, 6, 10]

Here's how it works:

- 1
- 3 (1 + 2)
- 6 (1 + 2 + 3)
- 10 (1 + 2 + 3 + 4)

Scan sums are commonly used in parallel computing and are helpful in algorithms where cumulative information is needed.
