class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        # Option 2 - BFS
        if endGene not in bank or not bank:
            return -1

        gene_map = [startGene]
        record = {startGene}
        transform = 0
        next_gene_map = None

        while gene_map:
            next_gene_map = []
            for gene in gene_map:
                if gene == endGene:
                    return transform

                for temp in bank:
                    if temp not in record and sum(1 for a, b in zip(gene, temp) if a != b) == 1:
                        next_gene_map.append(temp)
                        record.add(temp)
                        
            gene_map = next_gene_map
            transform += 1

        return -1
        
        # Option 1 - traverse the whole maps, too complicated, but they all faster
        """
        if endGene not in bank or not bank:
            return -1

        gene_map = {startGene:set()}
        transform_map = {startGene:0}

        def updateTransform(gene1, gene2):
            for g in gene_map[gene1]:
                transform_map[g] = min(transform_map[g], transform_map[gene1]+1, transform_map[gene2]+2)
            for g in gene_map[gene2]:
                transform_map[g] = min(transform_map[g], transform_map[gene2]+1, transform_map[gene1]+2)

        def connectGene(gene):
            if gene not in gene_map:
                gene_map[gene] = set()
                transform_map[gene] = 11

            for temp in bank:
                if temp not in gene_map:
                    if sum(1 for c1, c2 in zip(gene, temp) if c1 != c2) == 1:
                        transform_map[temp] = transform_map[gene]+1
                        gene_map[gene] = gene_map[temp] = {gene, temp} | gene_map[gene]
                elif temp not in gene_map[gene]:
                    if sum(1 for c1, c2 in zip(gene, temp) if c1 != c2) == 1:
                        transform_map[temp] = min(transform_map[temp], transform_map[gene]+1)
                        transform_map[gene] = min(transform_map[temp]+1, transform_map[gene])
                        updateTransform(gene, temp)
                        gene_map[gene] = gene_map[temp] = gene_map[temp] | gene_map[gene]

        connectGene(startGene)
        for gene in bank:
            connectGene(gene)

        if endGene not in gene_map or startGene not in gene_map[endGene]:
            return -1

        return transform_map[endGene]
        """
