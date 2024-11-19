import random
import math
import matplotlib.pyplot as plt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def separate_primes_and_composites(numbers):
    primes = [num for num in numbers if is_prime(num)]
    composites = [num for num in numbers if not is_prime(num) and num > 1]
    return primes, composites

def main():
 
    while True:
        try:
            K = int(input("Enter the number of random numbers (K, minimum 10): "))
            if K < 10:
                print("K must be at least 10. Try again.")
                continue
            N = int(input("Enter the upper limit for random numbers (N): "))
            break
        except ValueError:
            print("Please enter valid integers for K and N.")

   
    random_numbers = random.sample(range(1, N + 1), K)
    print(f"Generated list: {random_numbers}")

   
    primes, composites = separate_primes_and_composites(random_numbers)

    prime_squares = [p**2 for p in primes]
    composite_roots = [math.sqrt(c) for c in composites]

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].scatter(primes, prime_squares, color="blue", label="Prime Numbers")
    axes[0].set_title("Prime Numbers vs Squares")
    axes[0].set_xlabel("Prime Numbers")
    axes[0].set_ylabel("Squares")
    axes[0].grid(True)
    axes[0].legend()

    axes[1].scatter(composites, composite_roots, color="red", label="Composite Numbers")
    axes[1].set_title("Composite Numbers vs Square Roots")
    axes[1].set_xlabel("Composite Numbers")
    axes[1].set_ylabel("Square Roots")
    axes[1].grid(True)
    axes[1].legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
