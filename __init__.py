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
import json

from .modules.test_op import test_ot_op,Test_twoOperator

from .modules.test_panel import MainPanel

from .modules.heirarchy_mgmt import UI_Heirarchy_MGMT_Popup

#Collate all here
classes = (test_ot_op,Test_twoOperator,MainPanel,UI_Heirarchy_MGMT_Popup)

# Used to store info on the .blend file so it can be reference even after saves ectect
GLOBAL_DATA = {"PROJECT_INITILIZED":False,"LOADTEST":'Yo'}
# Create var to hold data as a string
bpy.types.Scene.ASSETCREATOR_GLOBALS = bpy.props.StringProperty()
# Assign the data to the data as a JSON string so it can be recalled with:
# GLOBAL_DATA = json.loads(bpy.types.Scene.ASSETCREATOR_GLOBALS)
bpy.types.Scene.ASSETCREATOR_GLOBALS = json.dumps(GLOBAL_DATA)

#Register with factory might need to change if adding keybindings ectect
register,unregister = bpy.utils.register_classes_factory(classes)



