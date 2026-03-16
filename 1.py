# Experiment-1
class StackADT:
    def __init__(self):
        self.data = []  # list end will be the "top" of the stack

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.is_empty():
            return None  # safe underflow
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def display(self):
        # show stack from bottom to top
        return self.data


def reverse_string_using_stack(s):
    st = StackADT()
    for ch in s:
        st.push(ch)

    rev = ""
    while not st.is_empty():
        rev += st.pop()
    return rev


def main():
    st = StackADT()

    while True:
        print("\n--- STACK ADT MENU ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. isEmpty")
        print("5. Size")
        print("6. Display Stack")
        print("7. Reverse a String (Meaningful Use)")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            val = input("Enter value to push: ")
            st.push(val)
            print("Pushed:", val)

        elif choice == "2":
            removed = st.pop()
            if removed is None:
                print("Underflow! Stack is empty, cannot pop.")
            else:
                print("Popped:", removed)

        elif choice == "3":
            top = st.peek()
            if top is None:
                print("Stack is empty, nothing to peek.")
            else:
                print("Top element:", top)

        elif choice == "4":
            print("isEmpty:", st.is_empty())

        elif choice == "5":
            print("Size:", st.size())

        elif choice == "6":
            print("Stack (bottom -> top):", st.display())

        elif choice == "7":
            s = input("Enter a string to reverse: ")
            print("Reversed string:", reverse_string_using_stack(s))

        elif choice == "0":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

# Experiment-2

#Single loop: O(n)
def single_loop(n):
    count = 0
    for i in range(n):
        count += 1
    print("Ops:", count, "Complexity: O(n)")

# Nested loop: O(n^2)
def nested_loop(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    print("Ops:", count, "Complexity: O(n^2)")

# Triangular loop: O(n^2) but ~n(n-1)/2
def triangular_loop(n):
    count = 0
    for i in range(n):
        for j in range(i):
            count += 1
    print("Ops:", count, "Complexity: O(n^2)")

# Halving loop: O(log n)
def halving_loop(n):
    count = 0
    while n > 1:
        n //= 2
        count += 1
    print("Ops:", count, "Complexity: O(log n)")


# Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i  # Best case: O(1)
    return -1        # Worst case: O(n)

# Binary Search
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if arr[mid] == key:
            print("Found in", steps, "steps. Complexity: O(log n)")
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    print("Not found after", steps, "steps. Complexity: O(log n)")
    return -1


# Experiment-3
def factorial(n):
    if n < 0:
        raise ValueError("Invalid input: n must be ≥ 0")
    if n == 0 or n == 1:  # Base case
        return 1
    else:                 # Recursive case
        return n * factorial(n - 1)

#Test
print("Factorial(4):", factorial(4))

# factorial(4)
# → 4 * factorial(3)-->24
#     → 3 * factorial(2)-->6
#             → 2 * factorial(1)-->2
#                 → 1 (base case)


#Experiment-4
#Naive recursive Fibonacci with call counter
naive_calls = 0
def fib_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)
print("fib_naive(4):", fib_naive(4))



#Memoized Fibonacci with call counter
memo_calls = 0
memo = {}
def fib_memo(n):
    global memo_calls
    memo_calls += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]


# Compare call counts
for n in [5, 2, 3]:
    naive_calls = 0
    result_naive = fib_naive(n)
    print(f"fib_naive({n}) = {result_naive}, calls = {naive_calls}")

    memo_calls = 0
    memo = {}
    result_memo = fib_memo(n)
    print(f"fib_memo({n}) = {result_memo}, calls = {memo_calls}")
    print("---")

# Experiment-5
def hanoi(n, src, aux, dst):
    if n == 1:
        print(f"Move disk 1 from {src} → {dst}")
        return 1
    moves = hanoi(n-1, src, dst, aux)
    print(f"Move disk {n} from {src} → {dst}")
    moves += 1
    moves += hanoi(n-1, aux, src, dst)
    return moves

# For n = 3
print("Hanoi(3):")
total_moves_3 = hanoi(3, "A", "B", "C")
print("Total moves:", total_moves_3)

# For n = 4
print("\nHanoi(4):")
total_moves_4 = hanoi(4, "A", "B", "C")
print("Total moves:", total_moves_4)


# Experiment-6
def binarySearch(arr, key, low, high):
    if low > high:
        return -1  # Not found
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binarySearch(arr, key, low, mid - 1)
    else:
        return binarySearch(arr, key, mid + 1, high)


# Test
arr = [1, 3, 5, 7, 9, 11, 13]
print("Search 7:", binarySearch(arr, 7, 0, len(arr)-1))   # Expected index 3
print("Search 11:", binarySearch(arr, 11, 0, len(arr)-1))   # Expected -1

