# encoding: utf-8

import sys
import importlib
import inspect


(MODULES_MINIMUM, MODULES_DEFAULT, MODULES_ALL) = range(3)

class Module(object):
    def __init__(self, abs_name):
        (self.module_type, self.module_name) = abs_name.split('.')
        self.abs_name = abs_name

    def __repr__(self):
        return '<Module type={} name={}>'.format(
            self.module_type, self.module_name
        )

all_modules = [
    [],
    [
        Module('property.odd'),
        Module('representation.roman_numerals'),
    ],
    [],
]

# Method names for different module types
type_interfaces = {
    'context':          'contextualize',
    'external':         'retrieve',
    'neighbor_search':  ['low_neighbor', 'high_neighbour'],
    'property':         'test',
    'representation':   'convert',
    'sequence_membership': 'is_member',
    'sequence_test':    'get_test_results',
}

def thierry(n, module_selection=MODULES_DEFAULT):
    for mod in all_modules[module_selection]:
        i = importlib.import_module('modules.' + mod.abs_name)
        members = inspect.getmembers(i, inspect.isclass)
        cls = members[0][1]

        print mod,
        print ' -> ',
        method_name = type_interfaces[mod.module_type]
        method = getattr(cls, method_name)
        print method(n)


if __name__ == '__main__':
    thierry(int(sys.argv[1]))
