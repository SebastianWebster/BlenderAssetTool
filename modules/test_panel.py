import bpy

class test_pt_panel(bpy.types.Panel):
    bl_idname = "test_pt_panel"
    bl_label = "Test Panel"
    bl_category = "AssetCreator3"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw (self,context):
        layout = self.layout
        row = layout.row()
        row.operator('object.test_two',text = "WORKBRUHa?")
        row.operator('view3d.cursor_center',text = "WORKBRUH?")
    