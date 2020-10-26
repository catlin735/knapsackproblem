"""
Tree data structure.
Author: Catherine Lin
"""

class Tree:
    def __init__(self,value,space,estimate,label):
        self.value=value
        self.space=space
        self.estimate=estimate
        self.label=label
        self.children=[]

    def addChild(self,child):
        self.children.append(child)
        return child

    def getChildren(self):
        return self.children

    def getValue(self):
        return self.value

    def getSpace(self):
        return self.space

    def getEstimate(self):
        return self.estimate

    def getLabel(self):
        return self.label

    def printPreorder(self,root,whitespace):
        output=whitespace+str(root.getLabel())+":"+str(root.getValue())+", "+str(root.getSpace())+", "
        output=output+str(root.getEstimate())

        if not root.getChildren():
            print(output)
            return
        else:
            print(output)
            for child in root.getChildren():
                self.printPreorder(child,whitespace+"\t")
