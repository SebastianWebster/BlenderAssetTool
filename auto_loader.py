import bpy
import inspect

from .modules import test_panel
from .modules import heirarchy_mgmt

class AutoLoader:


    # Note hasattr("bl_idname") filters out any static utility classes from being accidentally registered and trowing errors
    # Since all blender operators require this attribute
    @staticmethod
    def AutoRegister():
        print("Registering classes")
        _modules = [heirarchy_mgmt,test_panel]
        for _mod in _modules:
            for name,obj in inspect.getmembers(_mod):
                if inspect.isclass(obj) and hasattr(obj,"bl_idname"):
                    print("Class :" + name + " ClassType : " + str(type(obj)))
                    bpy.utils.register_class(obj)
    @staticmethod
    def UnRegister():
        print("de-registering classes")
        _modules = [test_panel,heirarchy_mgmt]
        for _mod in _modules:
            for name,obj in reversed(inspect.getmembers(_mod)):
                if inspect.isclass(obj) and hasattr(obj,"bl_idname"):
                    bpy.utils.unregister_class(obj)




