check_prime = [26, 39, 51, 53, 57, 79, 85]
for i in check_prime:
    for j in range(2,i):
        if j < i and i % j == 0:
            print ("{} is NOT a prime number".format(i) + "because {} is a factor of {}".format(j,i))
            break
        elif (j + 1) == i:
            print ("{} IS a prime number".format(i))
        else:
            j +=1
