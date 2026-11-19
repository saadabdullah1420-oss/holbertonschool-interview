# Making Change

`makeChange(coins, total)` returns the fewest coins needed to reach
the exact total. Each denomination can be used any number of times.

A non-positive total returns 0. An unreachable positive total returns -1.

The function uses dynamic programming. For each coin, it visits amounts
in ascending order so that the same denomination can be used again.
