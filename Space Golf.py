from itertools import permutations as p
from math import hypot as t
def golf(h):return round(min([t(*i[0])+sum([t(j[0]-k[0],j[1]-k[1])for j,k in zip(i,i[1:])])for i in [i for i in p(h)]]),2)

print golf({(2, 2), (2, 8), (8, 8), (5, 5), (8, 2)})
