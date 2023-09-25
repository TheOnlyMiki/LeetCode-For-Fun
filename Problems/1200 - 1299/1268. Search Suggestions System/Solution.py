class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        # Option 2
        products = sorted(products)
        left, right = 0, len(products)-1
        output = []
        for i, c in enumerate(searchWord):
            while left <= right and (len(products[left]) <= i or products[left][i] != c):
                left += 1

            while left <= right and (len(products[right]) <= i or products[right][i] != c):
                right -= 1

            if left > right:
                output.append([])
            else:
                output.append(products[left : min(left+3, right+1)])

        return output

        # Option 1
        """
        head = {}
        for product in sorted(products):
            record = head
            for c in product:
                if c not in record:
                    record[c] = {'#':[]}
                record = record[c]
                record['#'].append(product)

        output = []
        for c in searchWord:
            if c in head:
                head = head[c]
                output.append(head['#'][:3])
            else:
                output.append([])
                head = []

        return output
        """
