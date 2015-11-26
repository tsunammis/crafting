"""
High quality resources
    - https://github.com/vinta/awesome-python


PEP 8 is the de-facto code style guide for Python.
pip install pep8

$ pep8 optparse.py
optparse.py:69:11: E401 multiple imports on one line
optparse.py:77:1: E302 expected 2 blank lines, found 1
optparse.py:88:5: E301 expected 1 blank line, found 0
optparse.py:222:34: W602 deprecated form of raising exception
optparse.py:347:31: E211 whitespace before '('

The program autopep8 can be used to automatically reformat code in the PEP 8 style.
$ pip install autopep8
Use it to format a file in-place with:
$ autopep8 --in-place optparse.py


With pyvenv
    pyvenv myenv
    source myenv/bin/activate
    python

With virtualenv & virtualenvwrapper
http://www.marinamele.com/2014/07/install-python3-on-mac-os-x-and-use-virtualenv-and-virtualenvwrapper.html
    mkvirtualenv --python=/usr/local/bin/python3 myenv
    deactivate
    workon myenv

Magic Methods (source: http://www.rafekettler.com/magicmethods.html)

    Comparison magic methods
        Python has a whole slew of magic methods designed to implement intuitive
        comparisons between objects using operators, not awkward method calls.
        They also provide a way to override the default Python behavior for
        comparisons of objects (by reference). Here's the list of those methods
        and what they do:

    __cmp__(self, other)
        __cmp__ is the most basic of the comparison magic methods. It actually
        implements behavior for all of the comparison operators (<, ==, !=, etc.),
        but it might not do it the way you want (for example, if whether one
        instance was equal to another were determined by one criterion and and
        whether an instance is greater than another were determined by something
        else). __cmp__ should return a negative integer if self < other, zero if
        self == other, and positive if self > other. It's usually best to define
        each comparison you need rather than define them all at once, but __cmp__
        can be a good way to save repetition and improve clarity when you need all
        comparisons implemented with similar criteria.
    __eq__(self, other)
        Defines behavior for the equality operator, ==.
    __ne__(self, other)
        Defines behavior for the inequality operator, !=.
    __lt__(self, other)
        Defines behavior for the less-than operator, <.
    __gt__(self, other)
        Defines behavior for the greater-than operator, >.
    __le__(self, other)
        Defines behavior for the less-than-or-equal-to operator, <=.
    __ge__(self, other)
        Defines behavior for the greater-than-or-equal-to operator, >=.

    Numeric magic methods
        Just like you can create ways for instances of your class to be compared
        with comparison operators, you can define behavior for numeric operators.
        Buckle your seat belts, folks, there's a lot of these. For organization's
        sake, I've split the numeric magic methods into 5 categories: unary
        operators, normal arithmetic operators, reflected arithmetic operators
        (more on this later), augmented assignment, and type conversions.

    Unary operators and functions
        Unary operators and functions only have one operand, e.g. negation, absolute value, etc.

    __pos__(self)
        Implements behavior for unary positive (e.g. +some_object)
    __neg__(self)
        Implements behavior for negation (e.g. -some_object)
    __abs__(self)
        Implements behavior for the built in abs() function.
    __invert__(self)
        Implements behavior for inversion using the ~ operator. For an explanation on what this does, see the Wikipedia article on bitwise operations.
    __round__(self, n)
        Implements behavior for the built in round() function. n is the number of decimal places to round to.
    __floor__(self)
        Implements behavior for math.floor(), i.e., rounding down to the nearest integer.
    __ceil__(self)
        Implements behavior for math.ceil(), i.e., rounding up to the nearest integer.
    __trunc__(self)
        Implements behavior for math.trunc(), i.e., truncating to an integral.

    Normal arithmetic operators
        Now, we cover the typical binary operators (and a function or two):
        +, -, * and the like.
        These are, for the most part, pretty self-explanatory.

    __add__(self, other)
        Implements addition.
    __sub__(self, other)
        Implements subtraction.
    __mul__(self, other)
        Implements multiplication.
    __floordiv__(self, other)
        Implements integer division using the // operator.
    __div__(self, other)
        Implements division using the / operator.
    __truediv__(self, other)
        Implements true division. Note that this only works when from __future__ import division is in effect.
    __mod__(self, other)
        Implements modulo using the % operator.
    __divmod__(self, other)
        Implements behavior for long division using the divmod() built in function.
    __pow__
        Implements behavior for exponents using the ** operator.
    __lshift__(self, other)
        Implements left bitwise shift using the << operator.
    __rshift__(self, other)
        Implements right bitwise shift using the >> operator.
    __and__(self, other)
        Implements bitwise and using the & operator.
    __or__(self, other)
        Implements bitwise or using the | operator.
    __xor__(self, other)
        Implements bitwise xor using the ^ operator.


    Augmented assignment
        Python also has a wide variety of magic methods to allow custom behavior
        to be defined for augmented assignment. You're probably already familiar
        with augmented assignment, it combines "normal" operators with assignment.
        If you still don't know what I'm talking about, here's an example:

        x = 5
        x += 1 # in other words x = x + 1
        Each of these methods should return the value that the variable on the
        left hand side should be assigned to (for instance, for a += b,
        __iadd__ might return a + b, which would be assigned to a).
        Here's the list:

    __iadd__(self, other)
        Implements addition with assignment.
    __isub__(self, other)
        Implements subtraction with assignment.
    __imul__(self, other)
        Implements multiplication with assignment.
    __ifloordiv__(self, other)
        Implements integer division with assignment using the //= operator.
    __idiv__(self, other)
        Implements division with assignment using the /= operator.
    __itruediv__(self, other)
        Implements true division with assignment. Note that this only works
        when from __future__ import division is in effect.
    __imod__(self, other)
        Implements modulo with assignment using the %= operator.
    __ipow__
        Implements behavior for exponents with assignment using the **= operator.
    __ilshift__(self, other)
        Implements left bitwise shift with assignment using the <<= operator.
    __irshift__(self, other)
        Implements right bitwise shift with assignment using the >>= operator.
    __iand__(self, other)
        Implements bitwise and with assignment using the &= operator.
    __ior__(self, other)
        Implements bitwise or with assignment using the |= operator.
    __ixor__(self, other)
        Implements bitwise xor with assignment using the ^= operator.

    Type conversion magic methods
        Python also has an array of magic methods designed to implement behavior
        for built in type conversion functions like float(). Here they are:

    __int__(self)
        Implements type conversion to int.
    __long__(self)
        Implements type conversion to long.
    __float__(self)
        Implements type conversion to float.
    __complex__(self)
        Implements type conversion to complex.
    __oct__(self)
        Implements type conversion to octal.
    __hex__(self)
        Implements type conversion to hexadecimal.
    __index__(self)
        Implements type conversion to an int when the object is used in a slice
        expression. If you define a custom numeric type that might be used in
        slicing, you should define __index__.
    __trunc__(self)
        Called when math.trunc(self) is called. __trunc__ should return the
        value of `self truncated to an integral type (usually a long).
    __coerce__(self, other)
        Method to implement mixed mode arithmetic. __coerce__ should return
        None if type conversion is impossible. Otherwise, it should return a
        pair (2-tuple) of self and other, manipulated to have the same type.

    Representing your Classes
        It's often useful to have a string representation of a class. In Python,
        there's a few methods that you can implement in your class definition
        to customize how built in functions that return representations of your
        class behave.

    __str__(self)
        Defines behavior for when str() is called on an instance of your class.
    __repr__(self)
        Defines behavior for when repr() is called on an instance of your class.
        The major difference between str() and repr() is intended audience.
        repr() is intended to produce output that is mostly machine-readable
        (in many cases, it could be valid Python code even), whereas str() is
        intended to be human-readable.
    __unicode__(self)
        Defines behavior for when unicode() is called on an instance of your class.
        unicode() is like str(), but it returns a unicode string. Be wary: if
        a client calls str() on an instance of your class and you've only
        defined __unicode__(), it won't work. You should always try to define
        __str__() as well in case someone doesn't have the luxury of using unicode.
    __format__(self, formatstr)
        Defines behavior for when an instance of your class is used in new-style
        string formatting. For instance, "Hello, {0:abc}!".format(a) would lead
        to the call a.__format__("abc"). This can be useful for defining your
        own numerical or string types that you might like to give special
        formatting options.
    __hash__(self)
        Defines behavior for when hash() is called on an instance of your class.
        It has to return an integer, and its result is used for quick key
        comparison in dictionaries. Note that this usually entails implementing
        __eq__ as well. Live by the following rule: a == b implies
        hash(a) == hash(b).
    __nonzero__(self)
        Defines behavior for when bool() is called on an instance of your class.
        Should return True or False, depending on whether you would want to
        consider the instance to be True or False.
    __dir__(self)
        Defines behavior for when dir() is called on an instance of your class.
        This method should return a list of attributes for the user. Typically,
        implementing __dir__ is unnecessary, but it can be vitally important
        for interactive use of your classes if you redefine __getattr__ or
        __getattribute__ (which you will see in the next section) or are otherwise
        dynamically generating attributes.
    __sizeof__(self)
        Defines behavior for when sys.getsizeof() is called on an instance of
        your class. This should return the size of your object, in bytes. This
        is generally more useful for Python classes implemented in C extensions,
        but it helps to be aware of it.
"""
