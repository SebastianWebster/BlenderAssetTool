from .modules.globaldata_util import GlobalDataHandler
from .auto_loader import AutoLoader  
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


def register():
    AutoLoader.AutoRegister()
    bpy.types.Scene.ASSETCREATOR_GLOBALS = bpy.props.StringProperty(default=json.dumps({"DATASTRUCT_ID": "ASSETCREATOR_GLOBALS", "PROJECT_INIT": False, "UNIQUE_OBJ_COUNT": 0,"PROJECT_COLLECTIONS" : [],"PROJECT_OBJECTS" : [],"PROJECT_MATERIALS" : [],"ACTIVE_MATERIAL_GROUP":"","ACTIVE_OBJECT":"","OBJ_SUB_COLLECTIONS":["high","low","EXTRAS","LODS"]}))


def unregister():
    del bpy.types.Scene.ASSETCREATOR_GLOBALS
    AutoLoader.UnRegister()
