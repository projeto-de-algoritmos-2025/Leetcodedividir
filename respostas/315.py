class Solution:
    def countSmaller(self, nums):
        qnt_elementos = len(nums)
        result = [0] * qnt_elementos
        enum = list(enumerate(nums)) #enumera pra não perder o indice original

        def merge_sort(start, end):
            if end - start == 1:
                return enum[start:end] # condição de parada

            mid = (start + end) // 2 
            left = merge_sort(start, mid)
            right = merge_sort(mid, end)

            merged = [] #lista final
            pointer_left = pointer_right = 0
            inversoes = 0 # contador de inversões

            while pointer_left < len(left) and pointer_right < len(right): # compara os elementos da esquerda com os da direita
                if left[pointer_left][1] > right[pointer_right][1]: # se o elemento da esquerda for maior que o da direita na tupla
                    merged.append(right[pointer_right]) #adiciona o elemento da direita na lista final
                    inversoes += 1 # +1 na inversão já q o da direita < que o da esquerda
                    pointer_right += 1 # avança o ponteiro da direita que é menor
                else: # elemento da esquerda é menor
                    result[left[pointer_left][0]] += inversoes #adiciona o numero de inversões a lista result
                    merged.append(left[pointer_left])
                    pointer_left += 1

            while pointer_left < len(left): # ADICIONA O ELEMENTO FALTANTE DO LOOP PRINCIPAL
                result[left[pointer_left][0]] += inversoes
                merged.append(left[pointer_left])
                pointer_left += 1

            while pointer_right < len(right):
                merged.append(right[pointer_right])
                pointer_right += 1

        
            return merged

        merge_sort(0, qnt_elementos)
        return result