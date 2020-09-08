class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None
    def insert(self,val):
        if(self.root==None):
            self.root=node(val)
        else:
            self.insert_a(self.root,val)
    def insert_a(self,root,val):
        if(val>root.val):
            if(root.right==None):
                root.right=node(val)
            else:
                self.insert_a(root.right,val)
        else:
            if(root.left==None):
                root.left=node(val)
            else:
                self.insert_a(root.left,val)
    def inorder(self):
        self.inorder_a(self.root)
    def inorder_a(self,root):
        if(root):
            self.inorder_a(root.left)
            print(root.val,end=" ")
            self.inorder_a(root.right)
        
t=Tree()
t.insert(5)
t.insert(3)
t.insert(1)
t.insert(4)
t.insert(7)
t.insert(6)
t.insert(9)

t.inorder()