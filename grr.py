import multiprocessing

def function(args):
    print(f'{args[0]} {args[1]}')

if __name__ == "__main__":

    pool = multiprocessing.Pool(4)

    array = []
    array.append([1,2])
    array.append([3,4])
    # array[0].append(1)
    # array[0].append(2)
    # array[1].append(3)
    # array[1].append(4)

    pool.map(function, array)