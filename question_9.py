# 9. Given two 2D grids of digits, a large grid G and a smaller pattern grid P, determine if the
# pattern P exists within G. [Mark 4]

# Expected Output:
# The string 'YES' if the pattern is found, otherwise 'NO'.
# For the example above, the pattern is found starting at G[4][4], so the output is 'YES'.


def grid_search(G, P):
    rows = len(G)
    cols = len(G[0])

    pattern_rows = len(P)
    pattern_cols = len(P[0])

    for i in range(rows-pattern_rows + 1):
        for j in range(cols - pattern_cols + 1):
            match = True

            for x in  range(pattern_rows):
                for y in range(pattern_cols):
                    if G[i +x][j+y] != P[x][y]:
                        match = False
                        break
                
                if not match:
                    break
            
            if match:
                return "YES"

    return "NO"


G = [
'7283455864',
'6731158619',
'8988242643',
'3830589324',
'2229505813',
'5633845374',
'6473530293',
'7053106601'
]
P = [
'9505',
'3845',
'3530'
]

print(grid_search(G, P))