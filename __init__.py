from .modules.heirarchy_mgmt import UI_Heirarchy_MGMT_Popup, UI_AddNewObject_Popup,UI_AddNew_Quick_Object_Popup
from .modules.test_panel import MainPanel
from .modules.globaldata_util import GlobalDataHandler
import json
import os
import sys
import bpy

bl_info = {
    "name": "AssetCreator3",
    "author": "Sebastian Webster",
    "description": "Please",
    "blender": (2, 83, 0),
    "version": (0, 0, 1),
    "location": "View3D",
    "warning": "",
    "category": "Generic"
}


# Collate all here
classes = (MainPanel, UI_Heirarchy_MGMT_Popup)


def register():
    bpy.utils.register_class(MainPanel)
    bpy.utils.register_class(UI_Heirarchy_MGMT_Popup)
    bpy.utils.register_class(UI_AddNewObject_Popup)
    bpy.utils.register_class(UI_AddNew_Quick_Object_Popup)
    bpy.types.Scene.ASSETCREATOR_GLOBALS = bpy.props.StringProperty(default=json.dumps({"DATASTRUCT_ID": "ASSETCREATOR_GLOBALS", "PROJECT_INIT": False, "UNIQUE_OBJ_COUNT": 0, "OBJ_SUB_COLLECTIONS": {
                                                                    "high_poly_alias": "high", "low_poly_alias": "low", "extra_objects": "EXTRAS", "lods_alias": "LODS"}}))


def unregister():
    del bpy.types.Scene.ASSETCREATOR_GLOBALS
    bpy.utils.unregister_class(UI_AddNew_Quick_Object_Popup)
    bpy.utils.unregister_class(UI_AddNewObject_Popup)
    bpy.utils.unregister_class(UI_Heirarchy_MGMT_Popup)
    bpy.utils.unregister_class(MainPanel)
