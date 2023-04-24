#take list -> return set  and remove duplicates


from functools import reduce


def sum(x, y):
    return x + y

sum(4,5)

list = [1,2,3,3,3,4,4]

s: set[int] = set(list)


def remove_duplicates(xs: any) -> set[int]:
    return set(xs)

k = remove_duplicates(list)
print(s, k)

xs = [1,2,3,4]
seed = 2
def reduce_debug(acc, x):
    print('acc',acc, 'x',x)
    return acc + x

s_reduce = reduce(lambda acc, x: reduce_debug(acc, x), xs, seed)

print(s_reduce,'s_reduce')
xs = [1,2,3,4]

nums = [1, 2, 3, 4, 10, 55]
odd_even_t = tuple[any, any]
seed_nums: odd_even_t = ([], [])
def split_even(acc: odd_even_t, x: int) -> odd_even_t:
    if x % 2 == 0:
        return (acc[0], acc[1] + [x])
    else:
        return (acc[0] + [x], acc[1])

odd, even = reduce(lambda acc, x: split_even(acc, x), nums, seed_nums)
print(f'Odd = {odd} , Even = {even}')




