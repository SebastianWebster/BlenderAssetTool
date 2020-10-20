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

from .modules.globaldata_util import GlobalDataHandler

from .modules.test_panel import MainPanel

from .modules.heirarchy_mgmt import UI_Heirarchy_MGMT_Popup

#Collate all here
classes = (MainPanel,UI_Heirarchy_MGMT_Popup)

def register():
    bpy.utils.register_class(MainPanel)
    bpy.utils.register_class(UI_Heirarchy_MGMT_Popup)
    bpy.types.Scene.ASSETCREATOR_GLOBALS = bpy.props.StringProperty(default=json.dumps({"DATASTRUCT_ID":"ASSETCREATOR_GLOBALS","PROJECT_INIT":False}))


def unregister():
    del bpy.types.Scene.ASSETCREATOR_GLOBALS
    bpy.utils.unregister_class(UI_Heirarchy_MGMT_Popup)
    bpy.utils.unregister_class(MainPanel)


