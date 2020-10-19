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


from .modules.test_op import test_ot_op,Test_twoOperator

from .modules.test_panel import MainPanel

from .modules.heirarchy_mgmt import UI_Heirarchy_MGMT_Popup

#Collate all here
classes = (test_ot_op,Test_twoOperator,MainPanel,UI_Heirarchy_MGMT_Popup)


#Register with factory might need to change if adding keybindings ectect
register,unregister = bpy.utils.register_classes_factory(classes)



