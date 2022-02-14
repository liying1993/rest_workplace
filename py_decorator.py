rpc_info = {}
def xmlrpc(in_=(), out=(type(None),)):
    def _xmlrpc(function):
        # 注册签名
        func_name = function.__name__
        rpc_info[func_name] = (in_, out)
        def _check_types(elements, types):
            """用来检查类型的子函数"""
            if len(elements) != len(types):
                raise TypeError('argument count is wrong')
            typed = enumerate(zip(elements, types))
            for index, couple in typed:
                arg, of_the_right_type = couple
                if isinstance(arg, of_the_right_type):
                    continue
                raise TypeError()