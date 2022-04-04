from contextlib import contextmanager


@contextmanager
def swallow_exceptions(exception):
    try:
        yield
    except tuple(exception):
        for i in exception:
            print("---", i.__name__, "swallowed ---")


def main():
    with swallow_exceptions([ZeroDivisionError]):
        1 / 0


if __name__ == '__main__':
    main()
