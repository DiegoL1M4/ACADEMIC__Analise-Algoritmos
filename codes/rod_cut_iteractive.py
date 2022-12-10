
from asyncio.windows_events import NULL
import sys

class RodCutIteractive:
    def cutRod(price, n):
        memo = [0 for x in range(n + 1)]
        memo[0] = 0
        sizes = [0 for x in range(n + 1)]
        sizes[1] = 1

        for i in range(1, n + 1):
            max_val = -sys.maxsize-1
            sizes[i] = i+1
            for j in range(i):
                if(max_val < price[j] + memo[i-j-1]):
                    max_val =price[j] + memo[i-j-1]
                    sizes[i] = j+1
            memo[i] = max_val
    
        return memo[n], sizes

    def showCut(sizes, n):
        if(n == sizes[n]):
            print(sizes[n])
            return
        print(str(sizes[n]) + " ", end="")
        next = n - sizes[n]
        RodCutIteractive.showCut(sizes, next)
