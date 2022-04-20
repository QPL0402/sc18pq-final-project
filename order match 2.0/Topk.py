def partition(seq):
    pi, seq = seq[0], seq[1:]                 # 选取并移除主元
    lo = [x for x in seq if x <= pi]#选出小于第一个数的所有元素
    hi = [x for x in seq if x > pi]##选出大于第一个数的所有元素
    return lo, pi, hi

def select(seq, k):
    lo, pi, hi = partition(seq)
    m = len(lo)#小于第一个数的元素有几个
    if m == k: return pi
    if m < k: return select(hi, k-m-1)
    return select(lo, k)

if __name__ == '__main__':
    seq=(1,2,3,4,5)
    print(partition(seq))
    print(select(seq,0))