import bpy
import json
from .util.outlinerutil import OutlinerUtil

class UI_Heirarchy_MGMT_Popup(bpy.types.Operator):
    # Hardcoded configs
    bl_label = "Manage Heirarchy"
    bl_idname = "wm.heirarchy_manager"

    #Temp Method for storing configs, probably will make this into a JSON file/parser later
    defaultlayout = {
    "high_poly_alias": "high",
    "low_poly_alias": "low",
    "extra_objects": "EXTRAS",
    "lods_alias": "LODS"
    }

    # USER USER DEFINED INPUTS
    project_name = bpy.props.StringProperty(name="Project Name:")
    obj_count = bpy.props.IntProperty(name="Object Count", default=1)

    # METHODS
    def get_definitions(self):
        return (self.defaultlayout["high_poly_alias"],
        self.defaultlayout["low_poly_alias"],
        self.defaultlayout["extra_objects"],
        self.defaultlayout["lods_alias"])

    def init_heirarchy(self, context):
        _GLOBAL_DATA = json.loads(bpy.types.Scene.ASSETCREATOR_GLOBALS)
        print(_GLOBAL_DATA['LOADTEST'])
        _instanced = _GLOBAL_DATA['PROJECT_INITILIZED']

        if _instanced == False:
            # Create a new collection with no parents or children
            OutlinerUtil.add_collection(self.project_name)
            # With default of 1 create the framework for 'n' objects
            for i in range(self.obj_count):
                objname = "OBJ" + str(i)
                OutlinerUtil.add_collection(objname,parent = self.project_name)
                for definintion in self.get_definitions():
                    OutlinerUtil.add_collection(objname + "_" + definintion,parent = objname)

            # Assign to the scene data so there can be no error of attempting to instance the project twice
            _GLOBAL_DATA['PROJECT_INITILIZED'] = True
            _GLOBAL_DATA['LOADTEST'] = 'ProjectInitB4'
            bpy.types.Scene.ASSETCREATOR_GLOBALS = json.dumps(_GLOBAL_DATA)

        else:
            print("Already Instanced skipping")



    def execute(self, context):
        self.init_heirarchy(context)
        return {"FINISHED"}


    def invoke(self, context, event):
        wm = context.window_manager

        return wm.invoke_props_dialog(self)
