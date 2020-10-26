#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
from Tree import Tree
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

capacity=0
items = []
def read(input_data):
    global capacity
    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    print(firstLine)
    item_count = int(firstLine[0])
    capacity += int(firstLine[1])

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
    return items

def estimate(list):
    ratios=[]
    weight=0
    value=0
    index=0
    for item in list:
        ratios.append((item.index,item.value/item.weight))
    ratios.sort(reverse=True,key = lambda x: x[1])
    for i in ratios:
        if weight+items[i[0]].weight<=capacity:
            weight+=items[i[0]].weight
            value+=items[i[0]].value
        elif weight+items[i[0]].weight>capacity and weight<capacity:
            value+=((capacity-weight)/items[i[0]].weight)*items[i[0]].value
            break;
    return value



def makeTree(items,node,taken):
    duplicate=copy.deepcopy(items)
    if len(items)==0:
        return
    if node.getSpace()<=0:
        return
    else:
        item=duplicate[0]
        index=item.index
        take=None;
        if node.getSpace()-item.weight>=0:
            value=node.getValue()+item.value
            space=node.getSpace()-item.weight
            est=estimate(duplicate+taken)
            label=(item.index,1)
            take=Tree(value,space,est,label)
            node.addChild(take)
            duplicate.pop(0)
            taken.append(item)
            makeTree(duplicate,take,taken)
            taken.pop()
        else:
            duplicate.pop(0)
        add=Tree(node.getValue(),node.getSpace(),estimate(duplicate+taken),(index,0))
        node.addChild(add)
        makeTree(duplicate,add,taken)

options=[]
options.append(0)
def traverse(node):
    best=options[-1]
    if node.getEstimate()<best:
        return
    if not node.getChildren():
        options.append(node.getValue())
        return
    if node.getEstimate()>best:
        for child in node.getChildren():
            traverse(child)
ancestor=[]
def ancestors(node,value):
    if node == None:
        return False
    if node.getValue()==value and node.getLabel():
        ancestor.append(node.getLabel())
        return True
    for child in node.getChildren():
        if ancestors(child,value) and node.getLabel():
            ancestor.append(node.getLabel())
            return True
    return False


def solution():
    solution=0
    for value in options:
        if value>solution:
            solution=value
    return solution

def output():
    output=[0]*len(items)
    for tuple in ancestor:
        output[tuple[0]]=tuple[1]
    return output

def solve_it(input_data):
    read(input_data)
    root=Tree(0,int(capacity),estimate(items),None)
    makeTree(items,root,[])
    #root.printPreorder(root,'')
    traverse(root)
    ancestors(root,solution())
    print(output())
    return


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
