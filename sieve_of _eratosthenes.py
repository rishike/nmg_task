def sieve_eratosthenes(limit):
    
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False # excluding 0 and 1
    
    cur_prime = 2 # starting with 2
    
    # squaring the current prime number
    while cur_prime * cur_prime <= limit:
        if is_prime[cur_prime]:
            
            for idx in range(cur_prime * cur_prime, limit + 1, cur_prime):
                is_prime[idx] = False
        cur_prime += 1
    
    # Collecting all prime numbers in a list
    primes = [i for i in range(2, limit + 1) if is_prime[i]]
    
    return primes

if __name__ == "__main__":
    limit = 100
    prime_numbers = sieve_eratosthenes(limit)
    print("Prime numbers up to", limit, "are:", prime_numbers)

