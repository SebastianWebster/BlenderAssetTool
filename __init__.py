bl_info = {
    "name" : "AssetCreator3",
    "author" : "Sebastian Webster",
    "description" : "Please",
    "blender" : (2, 83, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy

import sys
import os


from .modules.test_op import test_ot_op
from .modules.test_op import Test_twoOperator
from .modules.test_panel import test_pt_panel

classes = (test_ot_op,test_pt_panel,Test_twoOperator)

register,unregister = bpy.utils.register_classes_factory(classes)



