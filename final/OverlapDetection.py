import sys

# Node in the suffix tree
class SuffixTreeNode:
    node_id = 0
    def __init__(self, start=0, end=sys.maxint):
        self.identifier = SuffixTreeNode.node_id
        SuffixTreeNode.node_id += 1
        self.suffix_link = None
        self.edges = {}
        self.parent = None
        # the node label labels which string does this node representing. this is a binary representation.
        # In this case there are 4 cases, 00,01,10,11.
        # When searching for lcs, we look for nodes that labelled 11.
        self.node_label = 0
        self.start = start
        self.end = end

    def add_child(self, id , start, end):
        child = SuffixTreeNode(start=start, end=end)
        child.parent = self
        self.edges[id] = child
        return child

    def add_childnode(self, key, node):
        node.parent = self
        self.edges[key] = node

    def get_depth(self, current_index):
        return min(self.end, current_index + 1) - self.start


class SuffixTree:
    def __init__(self):
        self.root = SuffixTreeNode()
        self.string_stored = ''
        self.num_of_strings = 0
        self.leaves = []

    def add_string(self, s1):
        pos1 = len(self.string_stored)
        string_id = self.num_of_strings
        s1 += '$' + str(string_id)
        self.string_stored += s1
        self.num_of_strings += 1
        # active node start from root
        current_node = self.root
        current_edge = 0
        depth = 0
        remainder = 0

        leaf_nodes = []
        for index in range(pos1, len(self.string_stored)):
            previous_node = None
            remainder += 1
            while remainder > 0:
                if depth == 0:
                    current_edge = index
                if self.string_stored[current_edge] not in current_node.edges:
                    leaf_node = current_node.add_child(self.string_stored[current_edge], index, sys.maxint)
                    leaf_node.node_label = 1 << string_id
                    leaf_nodes.append(leaf_node)
                    if previous_node is not None:
                        previous_node.suffix_link = current_node
                    previous_node = current_node
                else:
                    next_node = current_node.edges[self.string_stored[current_edge]]
                    next_edge_length = next_node.get_depth(index)
                    if depth >= next_node.get_depth(index):
                        current_edge += next_edge_length
                        depth -= next_edge_length
                        current_node = next_node
                        continue
                    if self.string_stored[next_node.start + depth] == self.string_stored[index]:
                        depth += 1
                        if previous_node is not None:
                            previous_node.suffix_link = current_node
                        previous_node = current_node
                        break
                    split = current_node.add_child(
                        self.string_stored[current_edge],
                        next_node.start,
                        next_node.start + depth
                    )
                    next_node.start += depth
                    split.add_childnode(self.string_stored[next_node.start], next_node)
                    leaf_node = split.add_child(self.string_stored[index], index, sys.maxint)
                    leaf_node.node_label = 1 << string_id
                    leaf_nodes.append(leaf_node)

                    if previous_node is not None:
                        previous_node.suffix_link = split
                    previous_node = split
                remainder -= 1

                if current_node == self.root and depth > 0:
                    depth -= 1
                    current_edge = index - remainder + 1
                else:
                    if current_node.suffix_link is not None:
                        current_node = current_node.suffix_link
                    else:
                        self.root
        for leaf in leaf_nodes:
            leaf.end = len(self.string_stored)
        self.leaves.extend(leaf_nodes)

    def find_lcs(self):
        label_ST = 2 ** self.num_of_strings - 1
        ST_nodes = []
        for leaf in self.leaves:
            node = leaf
            while node.parent is not None:
                if node.node_label != label_ST:
                    node.parent.node_label |= node.node_label
                    node = node.parent
                else:
                    ST_nodes.append(node)
                    break
        lcs = ['']
        lcs_length = 0
        for ST_node in ST_nodes:
            cs = ''
            while ST_node.parent is not None:
                label = self.string_stored[ST_node.start:ST_node.end]
                cs = label + cs
                ST_node = ST_node.parent
            if len(cs) > lcs_length:
                lcs_length = len(cs)
                lcs = [cs]
            elif len(cs) == lcs_length and cs not in lcs:
                lcs.append(cs)
        return lcs_length

def lcs(s1,s2):
    suffix_tree = SuffixTree()
    suffix_tree.add_string(s1)
    suffix_tree.add_string(s2)
    lcs = suffix_tree.find_lcs()
    return lcs

# a = lcs('actgds','tgdsa')
# print a

def column(matrix, i):
    return [row[i] for row in matrix]

def maxOverlap( string1 , string2 , k):
    n = len(string1)
    lcs1 = lcs(string1,string2)
    # k is the threshhold
    if lcs1 < k:
        return -(sys.maxint)
    # Initialization.
    else :
        scoring_matrix = [[0 for x in range(n)] for y in range(n)]
        # DP Iteration.
        for i in range(1,n):
            for j in range(1,n):
                adjacentCell = [scoring_matrix[i-1][j]-1,scoring_matrix[i][j-1]-1,scoring_matrix[i-1][j-1]+2*((string1[i]==string2[j])-0.5)]
                scoring_matrix[i][j] = max(adjacentCell)
        # Return the final overlapping score.
        overlaps_col = max(scoring_matrix[n-1])
        overlaps_row = max(column(scoring_matrix,n-1))
        overlaps = max([overlaps_col,overlaps_row])
        return overlaps

# a = maxOverlap('acgtcaaaa','cgtcaaaagc', 10)
# print a
# b = maxOverlap('acgtcaaaa','cgtcaaaagc', 5)
# print b
