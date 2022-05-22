# def make_hook(f):
#     """Decorator to turn 'foo' method into '__foo__'"""
#     f.is_hook = 1
#     return f
#
# class MyType(type):
#     def __new__(mcls, name, bases, attrs):
#
#         if name.startswith('None'):
#             return None
#
#         # Go over attributes and see if they should be renamed.
#         newattrs = {}
#         for attrname, attrvalue in attrs.iteritems():
#             if getattr(attrvalue, 'is_hook', 0):
#                 newattrs['__%s__' % attrname] = attrvalue
#             else:
#                 newattrs[attrname] = attrvalue
#
#         return super(MyType, mcls).__new__(mcls, name, bases, newattrs)
#
#     def __init__(self, name, bases, attrs):
#         super(MyType, self).__init__(name, bases, attrs)
#
#         # classregistry.register(self, self.interfaces)
#         print "Would register class %s now." % self
#
#     def __add__(self, other):
#         class AutoClass(self, other):
#             pass
#         return AutoClass
#         # Alternatively, to autogenerate the classname as well as the class:
#         # return type(self.__name__ + other.__name__, (self, other), {})
#
#     def unregister(self):
#         # classregistry.unregister(self)
#         print "Would unregister class %s now." % self
#
# class MyObject:
#     __metaclass__ = MyType
#
#
# class NoneSample(MyObject):
#     pass
#
# # Will print "NoneType None"
# print type(NoneSample), repr(NoneSample)
#
# class Example(MyObject):
#     def __init__(self, value):
#         self.value = value
#     @make_hook
#     def add(self, other):
#         return self.__class__(self.value + other.value)
#
# # Will unregister the class
# Example.unregister()
#
# inst = Example(10)
# # Will fail with an AttributeError
# #inst.unregister()
#
# print inst + inst
# class Sibling(MyObject):
#     pass
#
# ExampleSibling = Example + Sibling
# # ExampleSibling is now a subclass of both Example and Sibling (with no
# # content of its own) although it will believe it's called 'AutoClass'
# print ExampleSibling
# print ExampleSibling.__mro__
"""
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    uppercase_attr = {}
    for name, val in future_class_attr.items():
        if not name.startswith("__"):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val
    return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr

class Foo(metaclass = upper_attr):
    bar = "bip"

print(hasattr(Foo, "bar"))
print(hasattr(Foo, "BAR"))
"""

# class UpperAttrMetaclass(type):
#
#     def __new__(upper_metaclass, future_class_name, future_class_parents, future_class_attr):
#         uppercase_attr = {}
#         for name, val in future_class_attr.items():
#             if not name.startswith("__"):
#                 uppercase_attr[name.upper()] = val
#             else:
#                 uppercase_attr[name] = val
#         return type.__new__(upper_metaclass, future_class_name, future_class_parents, uppercase_attr)


# class UpperAttrMetaclass(type):
#
#     def __new__(cls, name: str, parents: tuple, attrs: dict):
#
#         upper_attrs = {}
#
#         for name, val in attrs.items():
#             if not name.startswith("__"):
#                 upper_attrs[name.upper()] = val
#             else:
#                 upper_attrs[name] = val
#         return super(UpperAttrMetaclass, cls).__new__(name, parents, upper_attrs)

























