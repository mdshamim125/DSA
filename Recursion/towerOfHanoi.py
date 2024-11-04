"""সমস্যা: তিনটি পিলার এবং n সংখ্যক ডিস্ক আছে। ডিস্কগুলোকে প্রথম পিলার থেকে শেষ পিলারে স্থানান্তর করতে হবে, যেখানে প্রতিবার একটি ডিস্ক স্থানান্তর করা যায় এবং বড় ডিস্ক ছোট ডিস্কের উপর থাকতে পারবে না।"""



def towerOfHanoi(n, source, temporary, target):
    if(n==1):
        print(f"move disk 1 from {source} to {target}")
        return
    towerOfHanoi(n-1, source, target, temporary)
    print(f"move disk {n} from {source} to {target}")
    towerOfHanoi(n-1, temporary, source,  target)

number=int(input("enter the disk number: "))
towerOfHanoi(number, "A", "B", "C")