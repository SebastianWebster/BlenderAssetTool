import bpy
from .util.outlinerutil import OutlinerUtil

class UI_Heirarchy_MGMT_Popup(bpy.types.Operator):
    # Hardcoded configs
    bl_label = "Manage Heirarchy"
    bl_idname = "wm.heirarchy_manager"

    defaultlayout = {
    "high_poly_alias": "_high",
    "low_poly_alias": "_low",
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
        bpy.ops.collection.create(name=self.project_name)
        bpy.context.scene.collection.children.link(bpy.data.collections[self.project_name])
        
        for i in range(self.obj_count):
            childcollname = "object" + str(i+1)
            OutlinerUtil.create_collection_to_parent(self.project_name,childcollname)
            OutlinerUtil.create_collection_to_parent(childcollname,self.get_definitions())
            


    def execute(self, context):
        print("Name:" + self.project_name)

        self.init_heirarchy(context)

        return {"FINISHED"}

    def invoke(self, context, event):
        wm = context.window_manager

        return wm.invoke_props_dialog(self)
