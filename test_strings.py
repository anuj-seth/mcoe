def test_double_quoted_strings_are_strings():
    string = "Hello, world."
    assert(__ == isinstance(string, basestring))

def test_single_quoted_strings_are_also_strings():
    string = 'Goodbye, world.'
    assert(__ == isinstance(string, basestring))

def test_triple_quote_strings_are_also_strings():
    string = """Howdy, world!"""
    assert(__ == isinstance(string, basestring))

def test_triple_single_quotes_work_too():
    string = '''Bonjour tout le monde!'''
    assert(__ == isinstance(string, basestring))

def test_raw_strings_are_also_strings():
    # raw strings treat backslashes as literal characters
    string = r"Konnichi \nwa, world!"
    assert(__ == isinstance(string, basestring))

def test_use_single_quotes_to_create_string_with_double_quotes():
    string = 'He said, "Go Away."'
    assert(__ == string)

def test_use_double_quotes_to_create_strings_with_single_quotes():
    string = "Don't"
    assert(__ == string)

def test_use_backslash_for_escaping_quotes_in_strings():
    a = "He said, \"Don't\""
    b = 'He said, "Don\'t"'
    assert(__ == (a == b))

def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line():
    string = "It was the best of times,\n\
It was the worst of times."
    assert(__ == len(string))
    
def test_triple_quoted_strings_can_span_lines():
    string = """
Howdy,
world!
"""
    assert(__ == len(string))

def test_triple_quoted_strings_need_less_escaping():
    a = "Hello \"world\"."
    b = """Hello "world"."""
    assert(__ == (a == b))
    
def test_escaping_quotes_at_the_end_of_triple_quoted_string():
    string = """Hello "world\""""
    assert(__ == string)

def test_plus_concatenates_strings():
    string = "Hello, " + "world"
    assert(__ == string)

def test_adjacent_strings_are_concatenated_automatically():
    string = "Hello" ", " "world"
    assert(__ == string)

def test_plus_will_not_modify_original_strings():
    hi = "Hello, "
    there = "world"
    string = hi + there
    assert(__ == hi)
    assert(__ == there)

def test_plus_equals_will_append_to_end_of_string():
    hi = "Hello, "
    there = "world"
    hi += there
    assert(__ == hi)

def test_plus_equals_also_leaves_original_string_unmodified():
    original = "Hello, "
    hi = original
    there = "world"
    hi += there
    assert(__ == original)

def test_most_strings_interpret_escape_characters():
    string = "\n"
    assert('\n' == string)
    assert("""\n""" == string)
    assert(__ == len(string))
    assert(__ == len(r"\n"))
