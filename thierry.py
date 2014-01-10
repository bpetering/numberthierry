# encoding: utf-8

import sys
import importlib

import modules.representation


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
    [Module('representation.roman_numerals')],
    []
]

def thierry(n, module_selection=MODULES_DEFAULT):
    for mod in all_modules[module_selection]:
        i = importlib.import_module('modules.' + mod.abs_name)
        if mod.module_type == 'representation':
            # TODO do all repr at once, etc
            print mod.module_name,
            print ' -> ',
            print i.RomanNumerals.convert(n)


if __name__ == '__main__':
    thierry(int(sys.argv[1]))
