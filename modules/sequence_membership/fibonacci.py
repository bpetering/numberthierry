# TODO should these be instantiable objects for easier reuse?

# TODO interface for sequence generation
# - start at N?
# - pregen and store results

class Fibonacci(object):
    @classmethod
    def seq(cls, start_at=None):
        return (1,2,3)  # TODO

    @classmethod
    def is_member(cls, n):
        # TODO start sequence at N - may not be possible, but often can save
        # computation of other results

        # -> if we can start a sequence at an arbitrary point, is it faster
        # in general to calculate or load pregen'd? (probably former)
        return n in cls.seq(start_at=n)
