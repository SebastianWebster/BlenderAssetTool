import bpy
from .util.outlinerutil import OutlinerUtil

class UI_Heirarchy_MGMT_Popup(bpy.types.Operator):
    # Hardcoded configs
    bl_label = "Manage Heirarchy"
    bl_idname = "wm.heirarchy_manager"

    instantiated = False

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
        if self.instantiated == False:
            #create a new collection with no parents or children
            OutlinerUtil.add_collection(self.project_name)
            
            for i in range(self.obj_count):
                objname = "OBJ" + str(i)
                OutlinerUtil.add_collection(objname,parent = self.project_name)
                for definintion in self.get_definitions():
                    OutlinerUtil.add_collection(objname + "_" + definintion,parent = objname)

        else:
            print("Already Instanced skipping")


    def execute(self, context):
        print("Name:" + self.project_name)

        self.init_heirarchy(context)

        return {"FINISHED"}

    def invoke(self, context, event):
        wm = context.window_manager

        return wm.invoke_props_dialog(self)
