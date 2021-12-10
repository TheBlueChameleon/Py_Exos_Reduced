import numpy as np
import time

# ============================================================================ #
# Below, you'll find two, essentially identical solutions.
# The main difference is that the first solution uses a few explicit for loops
#   which makes it easier to see what's going on here.
# The second, more compact version does everything with numpy functions requires
#   a very good understanding of NumPy's functions.
# Both approaches use the following data as input


givens = {
    # name             : (price, points)
    "dark chocolate"   : ( 1.00,      5),
    "milk chocolate"   : ( 0.90,      4),
    "caramel nuts bar" : ( 2.30,     12),
    "coco cube"        : ( 1.50,      8),
    "mint drops bag"   : ( 0.30,      1)
}

money = 10.0

# ============================================================================ #
# more vanilla python

tic = time.perf_counter()

price_list  = [ sweet[0] for sweet in givens.values() ]
points_list = [ sweet[1] for sweet in givens.values() ]

max_quantities = [ int(money / price) + 1 for price in price_list ]

grid = np.indices( max_quantities )

total_prices = np.zeros( grid[0].shape )
for price, layer in zip(price_list, grid) :
    total_prices += price * layer

total_points = np.zeros( grid[0].shape )
for points, layer in zip(points_list, grid) :
    total_points += points * layer

total_points[ total_prices > money ] = -1

best_index_flat       = np.argmax( total_points )
best_index_unravelled = np.unravel_index( best_index_flat, shape=total_prices.shape )

toc = time.perf_counter()

separator = "-" * 21 + "+" + \
            "-" * 10 + "+" + \
            "-" *  7 + "+" + \
            "-" *  7

items = np.sum(best_index_unravelled)

print("SOME PYTHON APPROACH:")
print(f"{'SWEET':20} | QUANTITY | PRICE | SCORE")
print(separator)
for i, (name, qty) in enumerate(zip(givens, best_index_unravelled)) :
    print(f"{name:20} | {qty:8} | {qty * price_list[i]:5.2f} | {qty * points_list[i]:5}")
print(separator)
print(f"{'TOTAL':20} | {items:8} | {total_prices[best_index_unravelled]:5.2f} | {total_points[best_index_unravelled]:5}")

print(f"Analyzed {total_prices.size} combinations in {(toc - tic) * 1000:5.2f} ms.")
print()

# ============================================================================ #
# very compact version

tic = time.perf_counter()

price_list  = np.array( [sweet[0] for sweet in givens.values()] )
points_list = np.array( [sweet[1] for sweet in givens.values()] )

max_quantities = np.array(money / price_list, dtype=np.int64)

grid = np.indices(max_quantities + 1)

total_prices = np.dot(grid.T,  price_list).T
total_points = np.dot(grid.T, points_list).T

#total_prices = np.tensordot(grid,  price_list, axes=(0,0))
#total_points = np.tensordot(grid, points_list, axes=(0,0))

total_points[ total_prices > money ] = -1

best_index_flat       = np.argmax( total_points )
best_index_unravelled = np.unravel_index( best_index_flat, shape=total_prices.shape )

toc = time.perf_counter()

separator = "-" * 21 + "+" + \
            "-" * 10 + "+" + \
            "-" *  7 + "+" + \
            "-" *  7

items = np.sum(best_index_unravelled)

print("PURE NUMPY APPROACH:")
print(f"{'SWEET':20} | QUANTITY | PRICE | SCORE")
print(separator)
for i, (name, qty) in enumerate(zip(givens, best_index_unravelled)) :
    print(f"{name:20} | {qty:8} | {qty * price_list[i]:5.2f} | {qty * points_list[i]:5}")
print(separator)
print(f"{'TOTAL':20} | {items:8} | {total_prices[best_index_unravelled]:5.2f} | {total_points[best_index_unravelled]:5}")

print(f"Analyzed {total_prices.size} combinations in {(toc - tic) * 1000:5.2f} ms.")
