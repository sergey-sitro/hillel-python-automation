class Example:
    attr = "class attr example"

    def __new__(cls):
        print("new")
        return super(Example, cls).__new__(cls)

    def __init__(
            self,
            obj_attr="obj attr example",
            obj_property="obj property example",
            obj_property_2="obj property example 2",
            *args, **kwargs
        ):
        print("init")
        self.obj_attr = obj_attr
        self.obj_property = obj_property
        self.obj_property_2 = obj_property_2
        self._protected_attr = "protected attr example"
        self.__private_attr = "private attr example"
        return super(Example, self).__init__(*args, **kwargs)

    def __str__(self):
        print("str")
        return super(Example, self).__str__()

    def __repr__(self):
        print("repr")
        return super(Example, self).__repr__()

    def __call__(self, *args, **kwargs):
        print("call")
        return super(Example, self).__call__(*args, **kwargs)

    def method_example(self, *args, **kwargs):
        print("method example")
        return args, kwargs

    @staticmethod
    def static_method_example(*args, **kwargs):
        print("static method example")
        return args, kwargs

    @classmethod
    def class_method_example(cls, *args, **kwargs):
        print("class method example")
        return cls.attr

    @property
    def obj_property(self):
        print("property getter")
        return self.__obj_property

    @obj_property.setter
    def obj_property(self, obj_property):
        print("property setter")
        self.__obj_property = obj_property

    @obj_property.deleter 
    def obj_property(self):
        print("property deleter")
        del self.__obj_property

    def obj_property_2_getter(self):
        print("property_2 getter")
        return self.__obj_property_2

    def obj_property_2_setter(self, obj_property_2):
        print("property_2 setter")
        self.__obj_property_2 = obj_property_2

    def obj_property_2_deleter(self):
        print("property_2 deleter")
        del self.__obj_property_2

    obj_property_2 = property(
        obj_property_2_getter,
        obj_property_2_setter,
        obj_property_2_deleter
    )
