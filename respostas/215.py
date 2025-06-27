class Solution(object):
    def findKthLargest(self, nums, k):
        def partition(arr, pivo):
            
            lows = [num for num in arr if num < pivo]
            highs = [num for num in arr if num > pivo]
            pivot = [num for num in arr if num == pivo]

            return lows, pivot, highs

        def select(arr, k):
            if len(arr) <= 5:
                return sorted(arr)[-k]

            chunks = [arr[i:i+5] for i in range(0, len(arr), 5)]

            medians = [sorted(chunk)[len(chunk)//2] for chunk in chunks]

            median_of_medians = select(medians, len(medians)//2 + 1)

            lows, pivo, highs = partition(arr, median_of_medians)

            if k <= len(highs):  # Esta no grupo dos maiores
                return select(highs, k)
            elif k <= len(highs) + len(pivo): # É o pivo
                return median_of_medians
            else:
                return select(lows, k - len(highs) - len(pivo)) # Esta nos menores que o pivo

        return select(nums, k)