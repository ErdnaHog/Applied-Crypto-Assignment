def is_prime(num):
    if num == 0 or num == 1:
        return False
    sqrt_num = int(num ** 0.5)
    for i in range(2, sqrt_num+1):
        if num % i == 0:
            return False
    return True


def step_one(g, user_num, n):
    compute_num = (g ** user_num) % n
    return compute_num


def step_two(user_compute_num, user_num, n):
    key = (user_compute_num ** user_num) % n
    return key
