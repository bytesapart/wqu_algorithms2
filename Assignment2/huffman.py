import heapq
from collections import defaultdict
import string


def encode(frequency):
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


if __name__ == '__main__':
    # Generate Fibonacci series
    start_num = 1
    end_num = int(raw_input("Enter the end number for Fibonacci Series:\n"))
    if end_num >= 26:
        print('Can only map 26 Ascii values to numbers. Please use a Fib series of max 26\n')
        exit(1)
    else:
        fib_series = map(fib, range(start_num, end_num + 1))
    print('The fibonacci series is %s\n' % str(fib_series))
    # Create the Fib Dict
    ascii_list = list(string.ascii_lowercase)
    fib_dict = defaultdict(int, dict(zip(ascii_list[:len(fib_series)], fib_series)))

    # Perform Huffman Encoding
    print('The Symbol<->Frequency dictionary for encoding is as follows: %s\n' % str(fib_dict))
    huff = encode(fib_dict)
    print('The Huffman Encoding is as follows:\n')
    print "Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code"
    for p in huff:
        print p[0].ljust(10) + str(fib_dict[p[0]]).ljust(10) + p[1]