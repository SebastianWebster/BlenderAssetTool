import bpy
import json
from .util.outlinerutil import OutlinerUtil
from .globaldata_util import GlobalDataHandler

class UI_Heirarchy_MGMT_Popup(bpy.types.Operator):
    # Hardcoded configs
    bl_label = "Manage Heirarchy"
    bl_idname = "wm.heirarchy_manager"

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
        data = GlobalDataHandler.open_data(context)
        _instanced = data["PROJECT_INIT"]

        if _instanced == False:
            # Create a new collection with no parents or children
            OutlinerUtil.add_collection(self.project_name)
            # With default of 1 create the framework for 'n' objects
            for i in range(self.obj_count):
                OutlinerUtil.add_new_obj(context,self.project_name)

            # Assign to the scene data so there can be no error of attempting to instance the project twice
            GlobalDataHandler.update_data(context,"PROJECT_INIT",True)
            GlobalDataHandler.append_data(context,"PROJECT_NAME",self.project_name)

        else:
            print("Already Instanced skipping")

    def execute(self, context):
        self.init_heirarchy(context)
        return {"FINISHED"}

    def invoke(self, context, event):
        wm = context.window_manager

        return wm.invoke_props_dialog(self)


class UI_AddNew_Quick_Object_Popup(bpy.types.Operator):
    bl_label = "Quick Add New Object"
    bl_idname = "wm.quick_add_obj"

    def execute(self, context):
        proj_name = GlobalDataHandler.open_data(context)["PROJECT_NAME"]
        OutlinerUtil.add_new_obj(context,proj_name)

        return {"FINISHED"}


class UI_AddNewObject_Popup(bpy.types.Operator):
    bl_label = "Add New Object"
    bl_idname = "wm.add_newobj"

    object_name = bpy.props.StringProperty(name="Project Name:")
    primType = bpy.props.IntProperty(name="Object Count", default=1)

    def execute(self, context):



        return {"FINISHED"}

    def invoke(self, context, event):
        wm = context.window_manager

        return wm.invoke_props_dialog(self)




