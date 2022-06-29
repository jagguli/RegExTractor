"""
RegExTractor
------------

Python regex generator.

Takes 2 or more strings (or even a single one) and generates a RegEx that
matches similar strings.
The generated RegEx always matches the original strings, but it also
generalizes, usually matching more.

"""

from regextractor.subseq_tree import gen_tree, tree_to_regex, tree_to_HTML


def extract(strs):
    """(The main function)
    Takes a list of strings and generates a RegEx that matches similar strings.
    """
    tree = gen_tree(strs)
    import pprint

    pp = pprint.PrettyPrinter()
    pp.pprint(tree)
    return tree_to_regex(tree)


def extract_HTML(strs):
    tree = gen_tree(strs)
    return tree_to_HTML(tree)
