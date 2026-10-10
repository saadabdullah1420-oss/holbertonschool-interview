# Minimum Operations

## Description
Calculate the minimum number of operations needed to obtain exactly n
H characters using Copy All and Paste.

## Algorithm
Factorize n into prime factors and add those factors together.
Each factor represents the number of operations needed for that step.

## Prototype
`def minOperations(n)`

## Return
Returns the minimum number of operations, or 0 if n is impossible.
