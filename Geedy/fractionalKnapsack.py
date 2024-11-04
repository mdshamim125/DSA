class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value/weight
    
def fractionalKnapsack(capacity, items):
    items.sort(key=lambda x: x.ratio, reverse=True)

    totalValue = 0
    for item in items:
        if(capacity > 0):
            if(capacity>=item.weight):
                totalValue+=item.value
                capacity-=item.weight
            else:
                totalValue+=item.ratio * capacity
                break
    return totalValue

items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50
maxValue = fractionalKnapsack(capacity, items)
print("maximum value: ", maxValue)