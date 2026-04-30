class BaseDataClass:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # 遍历子类的注解以获取字段
        for field_name in cls.__annotations__:
            # 创建 getter 方法
            def get_method(self, field=field_name):
                return getattr(self, field)
            # 创建 setter 方法
            def set_method(self, value, field=field_name):
                setattr(self, field, value)
            # 将方法设置到子类
            setattr(cls, f'get_{field_name}', get_method)
            setattr(cls, f'set_{field_name}', set_method)