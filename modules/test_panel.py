import bpy


class MainPanel(bpy.types.Panel):
    bl_idname = "main_PT_panel"
    bl_label = "AssetCreator"
    bl_category = "AssetCreator"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    #Defines if a project has been started, stops user from running startnewproject twice and deleting everything
    projectinit = False

    def draw (self,context):
        layout = self.layout
        row = layout.row()
        row.operator('wm.heirarchy_manager',text = "Start New Project")
        row = layout.row()
        row.operator('wm.quick_add_new_mat',text = "Quick Material")
        row.operator('wm.add_newmat',text = "Add Material")
        row = layout.row()
        row.operator('wm.quick_add_obj',text = "Quick Object")
        row.operator('wm.add_newobj',text = "Add Object")


        row = layout.row()

    