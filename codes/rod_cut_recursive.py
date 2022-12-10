
import sys

class RodCutRecursive:
    def cutRod(price, n):
        memo = [-1 for x in range(n + 1)]
        memo[0] = 0
        sizes = [0 for x in range(n + 1)]
        sizes[1] = 1

        max = RodCutRecursive.cutRodRecursive(price, memo, sizes, n)

        print("Tamanhos das barras: ", end="")
        RodCutRecursive.showCut(sizes, n)

        return max

    def cutRodRecursive(price, memo, sizes, n):
        i = 0
        max_val = -1

        if (memo[n] != -1):
            max_val = memo[n]
        else:
            while (i < n):
                value = price[i] + RodCutRecursive.cutRodRecursive(price, memo, sizes, n - i - 1)
                if(max_val < value):
                    max_val = value
                    sizes[n] = i+1
                i = i + 1

        memo[n] = max_val
        return max_val

    def showCut(sizes, n):
        if(n == sizes[n]):
            print(sizes[n])
            return
        print(str(sizes[n]) + " ", end="")
        next = n - sizes[n]
        RodCutRecursive.showCut(sizes, next)
