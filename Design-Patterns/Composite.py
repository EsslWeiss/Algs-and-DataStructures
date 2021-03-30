import ipdb
from AbstractComposite import Component


class Package(Component):
    """
        Package class contains complex components that
        can be nested components.
    """
    def __init__(self, *args):
        self._parent = None
        self.childs = []
        for comp in args:
            comp.parent = self
            self.childs.append(comp)
        
        self.package_price = 0

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, comp):
        self._parent = comp

    def calc_package_price(self, comp_childs=None):
        """
            Calculate products price in Package object
            comp_childs - list of the Package/Product components
        """
        if not comp_childs:
            comp_childs = self.childs

        for comp in comp_childs:
            if comp.is_composite():
                self.calc_package_price(comp_childs=comp.childs)
            else:
                if comp.ordered is False:
                    self.package_price += comp.price
                    comp.ordered = True 
            
    def is_composite(self):
        return True

    def add(self, comp):
        """
            Add component to the Package object
        """
        self.childs.append(comp)
        comp.parent = self
        return self

    def add_many(self, *args):
        """
            Add many components to the Package object
        """
        for comp in args:
            comp.parent = self
            self.childs.append(comp)

    def remove(self, comp):
        """
            remove component from the Package object
        """
        try:
            self.childs.remove(comp)
        except ValueError:
            raise ValueErorr("%s not %s value" % (
                    self.__class__,
                    comp
                ))
        else:
            comp.parent = None
        return True       

    def operation(self):
        return [comp.operation() for comp in self.child]
    
    def pack_repr(self):
        """
            Pack representation
        """
        pack_repr = []
        for comp in self.childs:
            if comp.is_composite():
                pack_repr += self.__class__.pack_repr(comp)
            else:
                pack_repr.append({
                    "parent": comp.parent,
                    "title": comp.title,
                    "price": comp.price,
                    "country": comp.title,
                    "ordered": comp.ordered
                })

        return pack_repr    
    
    def __repr__(self):
        return "<slf.parent=%s, slf.childs=%s, " \
                "slf.package_price=%s>" % (
                self.parent,
                True if len(self.childs) > 0 else False,
                self.package_price
            )

class Product(Component):
    """
        Product class represent final object of the structure.
        Product cannot have nested components.
    """
    def __init__(self, title, country, price):
        self._parent = None
        self.title = title
        self.country = country
        self.price = price
        self.ordered = False
 
    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, comp):
        self._parent = comp

    def operation(self):
        return "$%s %s" % (
                self.price, 
                self.country
            )

    def __repr__(self):
        return "<slf.parent=%s, slf.title=%s, " \
            "slf.price=%s, slf.country=%s>, " \
            "slf.ordered=%s" % (
                self.parent,
                self.title,
                self.price,
                self.country,
                self.ordered
            )


if __name__ == "__main__":
    prod1 = Product(title="MacBook 2016", country="Bangladesh", price=1200.10)
    prod2 = Product(title="Iphone S6", country="China", price=2000.80)
    prod3 = Product(title="Sumsung Note 10", country="Japan", price=1200.99)
    prod4 = Product(title="Xiaomi R9", country="China", price=999.10)

    main_pack = Package()
    sub_pack_a = Package()
    sub_pack1 = Package(prod1, prod3)
    sub_pack2 = Package(prod2, prod4)
    sub_pack_a.add(sub_pack2)

    main_pack.add_many(sub_pack1, sub_pack2)
    
    main_pack.calc_package_price()

    print(main_pack.package_price, "\n")
    print(main_pack.pack_repr())

