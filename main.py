# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Element:
    def __init__(self, val : int):
        self.val = val
        self.parent = self #元素在创建时自己形成一个单独集合，因此父节点指向自己
        self.rank = 1 #表示树的高度
    def value(self):
        return self.val
    def parent(self):
        return self.parent
    def set_parent(self, parent):
        assert parent is not None
        self.parent = parent
    def get_rank(self):
        return self.rank
    def set_rank(self, rank):
        assert rank > 1
        self.rank = rank

class DisjontSet:
    def __init__(self):
        self.hash_map = {}
    def add(self, elem : Element):
        assert elem is not None
        if elem.value() in self.hash_map:
            return False
        self.hash_map[elem.value()] = elem
        return True
    def find_partition(self, elem : Element):
        #返回元素所在集合的根节点
        assert elem is not None or elem.value() in self.hash_map
        parent = elem.parent()
        if parent is elem: #已经是根节点
            return elem
        parent = self.find_partition(elem) #获得集合的根节点
        elem.set_parent(parent) #路径压缩直接指向根节点
        return parent #返回根节点

    def are_disjoint(self, elem1 : Element, elem2 : Element):
        #判断两个元素是否属于同一集合只要判断他们再哈希表中映射的根节点是否同一个
        root1 = self.find_partition(elem1)
        root2 = self.find_partition(elem2)
        return root1 is not root2

    def merge(self, elem1 : Element, elem2 : Element):
        root1 = self.find_partition(elem1)
        root2 = self.find_partition(elem2)
        if root1 is root2:  # 两个元素属于同一个集合
            return False
        new_rank = root1.get_rank() + root2.get_rank()
        if root1.get_rank() >= root2.get_rank():  # 根据树的高度来决定合并方向
            root2.set_parent(root1)
            root1.set_rank(new_rank)
        else:
            root1.set_parent(root2)
            root2.set_rank(new_rank)
        return True



# Press the green button in the gutter to run the script.
if __name__ == '__main__':


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
