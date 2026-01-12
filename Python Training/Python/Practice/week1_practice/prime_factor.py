"""
Factors
a. Desc -> Computes the prime factorization of N using brute force.
b. I/P -> Number to find the prime factors
c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
d. O/P -> Print the prime factors of number N.
"""
import math
def cal_prime_factor(n):
    ans_list = []
    if n<0 :
        raise ValueError("Value must greater than 0")
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            ans1 = i
            ans2 = n//i
            if ans1 not in ans_list:
                ans_list.append(ans1)
            if ans2 not in ans_list:
                ans_list.append(ans2)

    return ans_list.sort()

def main():
    try:
        n = int(input("Enter the value of N : "))
        ans = cal_prime_factor(n)
        print(ans)

    except ValueError as e:
        print("Error -> ",e)


if __name__ == "__main__":
    main()