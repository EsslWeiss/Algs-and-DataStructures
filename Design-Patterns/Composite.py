import ipdb
from AbstractComposite import Component


class Package(Component):
    """
        Package class contains complex components that
        can be nested components.
    """
    def __init__(self, id, *args):
        self.id = id
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

    def remove_by_id(self, id):
        """
            remove component from the Package by id
        """
        for comp in self.childs:
            if comp.id == id:
                self.childs.remove(comp)

            if comp.is_composite():
                self.__class__.remove_by_id(comp, id)
    
    def remove_by(self, field, value):
        """
            remove component from the Package by parametrize field
        """
        for comp in self.childs:
            if str(field) in comp.__dict__ and \
                    getattr(comp, str(field)) == value:
                self.childs.remove(comp)
                return

            if comp.is_composite():
                self.__class__.remove_by(comp, field, value)

    def operation(self):
        return [comp.operation() for comp in self.child]
    
    def get_by_id(self, id):
        """
            Get component in package by id
        """
        component = None
        for comp in self.childs:
            if comp.id == id:
                return comp

            if comp.is_composite():
                component = self.__class__.get_by_id(comp, id)
                if component:
                    break

        return component
    
    def get_by(self, field, value):
        component = None
        for comp in self.childs:
            if str(field) in comp.__dict__ \
                    and getattr(comp, str(field)) == value:
                return comp

            if comp.is_composite():
                component = self.__class__.get_by(comp, field, value)
                if component:
                    break

        return component

    def products_repr(self):
        """
            Pack representation
        """
        prod_repr = []
        for comp in self.childs:
            if comp.is_composite():
                prod_repr += self.__class__.products_repr(comp)
            else:
                prod_repr.append({
                    "id": comp.id,
                    "parent_id": comp.parent.id,
                    "title": comp.title,
                    "price": comp.price,
                    "country": comp.title,
                    "ordered": comp.ordered
                })

        return prod_repr    
 
    def __repr__(self):
        return "<slf.id=%s, slf.parent_id=%s, slf.childs=%s, " \
                "slf.package_price=%s>" % (
                self.id,
                self.parent.id,
                True if len(self.childs) > 0 else False,
                self.package_price
            )

class Product(Component):
    """
        Product class represent final object of the structure.
        Product cannot have nested components.
    """
    def __init__(self, id, title, country, price):
        self.id = id
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
        return "<slf.id=%s, slf.parent_id=%s, " \
            "slf.title=%s, slf.price=%s, " \
            "slf.country=%s>, slf.ordered=%s" % (
                self.id,
                self.parent.id,
                self.title,
                self.price,
                self.country,
                self.ordered
            )


def configurate_composite():
    main_pack = Package(id=100)
    sub_pack_1 = Package(id=20)
    sub_pack_3 = Package(id=10)

    prod1 = Product(
            id=1, 
            title="MacBook 2016", 
            country="Bangladesh", 
            price=1200.10)
    prod2 = Product(
            id=2, 
            title="Iphone S6", 
            country="China", 
            price=2000)
    prod3 = Product(
            id=3, 
            title="Sumsung Note 10", 
            country="Japan", 
            price=1200)
    prod4 = Product(
            id=4, 
            title="Xiaomi R9", 
            country="China", 
            price=999)
    
    sub_pack_2 = Package(56, prod1, prod2)
    sub_pack_1.add_many(prod3, prod4)
    sub_pack_3.add(sub_pack_2).add(sub_pack_1)

    main_pack.add(sub_pack_3)
    main_pack.calc_package_price()
    return main_pack


if __name__ == "__main__":
    package = configurate_composite()

    print(package.package_price, "\n")
    print(package.products_repr(), "\n")
    
    local_package = package.get_by_id(56)
    package.remove_by_id(local_package.id)

    print(package.products_repr(), "\n")
    
    product = package.get_by(field="country", value="China")
    print(product, "\n")

