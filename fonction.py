def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end='')
        a, b = b, a + b
    print ()

def print1_to_10():
    i = 0
    while i != 10:
        print(i + 1)
        i = i + 1

"""void  print_1_to_10(void) {
    int i = 0;
    while (i != 10) {
        printf("%dn", (i + 1);
        i = i + 1;
        }
    }"""