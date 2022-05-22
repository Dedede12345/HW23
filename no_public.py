class MetaNoPublicAttrs(type):

    def __new__(cls, name, parents, attrs):

        nopublic_attrs = {}

        for name, val in attrs.items():
                if not name.startswith("_"):
                    pass
                else:
                    nopublic_attrs[name] = val

        return super(MetaNoPublicAttrs, cls).__new__(cls, name, parents, nopublic_attrs)


class NoPublic(metaclass=MetaNoPublicAttrs):
    _val = "GDe"
    val = "GDe"


instance = NoPublic()

print(hasattr(instance, "_val"))
print(hasattr(instance, "val"))