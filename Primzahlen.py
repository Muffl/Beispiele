import matplotlib.pyplot as plt

def SieveOfEratosthenes(n):

    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all prime numbers
    plotter=[]
    for p in range(n + 1):
        if prime[p]:
            print(p),  # Use print(p) for python 3
            plotter.append(p)
    plt.plot(range(len(plotter)))
    plt.show()

# driver program
if __name__ == '__main__':
    n = 10
    print("Following are the prime numbers smaller"),
    # Use print("Following are the prime numbers smaller") for Python 3
    print("than or equal to"), n
    # Use print("than or equal to", n) for Python 3
    SieveOfEratosthenes(n)