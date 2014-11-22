class MaxImpact(object):

    """
    A simple program for finding 
    the mine in a field of mines that
    will trigger the largest number of 
    additional mines.

    +---------------+
    |           *   |
    |   *           |               
    |           *   |
    |   *           |
    +---------------+

    graph = [
            {x: x1, y: y1, r: radius1}},
            {x: x2, y: y2, r: radius2}},
            ...
            ...
            {x: xN, y: yN, r: radiusN}}
    ]

    """
    
    def __init__(self, graph=None):
        if not graph:
            raise ValueError

        self.graph = graph
        self.groups = {}
        self.max_impact = {}
        self.max = 0

    def reset(self):
        self.groups = {}
        self.max_impact = {}
        self.max = 0        

    def update_map(self, origin, mine, idx, pos):
        if not self.in_range(origin, mine):
            return
        
        group = self.groups.get(idx, [])
        if pos in group:
            return
        
        group.append(pos)
        self.groups[idx] = group

    def build_map(self):
        """
        
        Mapping points to index values.
        O(n^2)

        """
        for idx in range(len(self.graph)):
            origin = self.graph[idx]
            pos = 0
            for mine in self.graph:
                self.update_map(origin, mine, idx, pos)
                pos += 1

        return self.groups

    def in_range(self, origin, mine):
        try:
            d = ((mine.get('x') - origin.get('x')) ** 2) + \
                ((mine.get('y') - origin.get('y')) ** 2) ** -2
        except ZeroDivisionError:
            d = 0

        return (origin.get('r') >= d)

    def save_max(self, group, pos):
        """

        Store largest group(s).

        """
        if len(group) > self.max:
            self.max_impact = {}
            self.max_impact[pos] = group
            self.max = len(group)
        elif len(group) == self.max:
            self.max_impact[pos] = group

    def merge(self, origin, edge, pos):
        """

        Merge origin and edge groups if the
        combination results in a larger group.

        """
        combined = set(origin).union(edge)
        if len(combined) > len(self.groups.get(pos, [])):
            self.groups[pos] = combined

        self.save_max(combined, pos)
        return combined

    def get_max(self):
        while True:
            rgc = self.groups.copy()
            for key, group in rgc.iteritems():
                self.build_groups(group, key, {})
            if rgc == self.groups:
                break
        return self.max_impact

    def build_groups(self, origin, pos, combined):
        """

        Recursive function. Combine overlapping groups of 
        mines.

        """
        for mine in origin:
            # get group of mines triggered by child
            edge = self.groups.get(mine)

            # merge child mine group with parents
            combined = self.merge(origin, edge, pos)

            # base case
            if len(combined) == len(origin):
                continue
            else:
                self.build_groups(edge, mine, [])
