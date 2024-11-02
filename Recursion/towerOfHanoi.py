def towerOfHanoi(n, source, temporary, target):
    if(n==1):
        print(f"move disk 1 from {source} to {target}")
        return
    towerOfHanoi(n-1, source, target, temporary)
    print(f"move disk {n} from {source} to {target}")
    towerOfHanoi(n-1, temporary, source, target)

number=int(input("enter the disk number: "))
towerOfHanoi(number, "A", "B", "C")