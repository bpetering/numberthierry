# TODO this seems too cumebrsome - make easier to return multiple results from
# a module - e.g. conversions to bases X, Y, Z

class Binary(object):
    @classmethod
    def convert(cls, n):
        return bin(n)
