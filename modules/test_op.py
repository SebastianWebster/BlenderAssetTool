import bpy

class test_ot_op(bpy.types.Operator):
    bl_idname = "view3d.cursor_center"
    bl_label = "Simple Op"
    bl_description = "Centre"

    def execute(self,context):
        bpy.ops.view3d.snap_cursor_to_center()
        return {'FINISHED'}


class Test_twoOperator(bpy.types.Operator):
    bl_idname = "object.test_two"
    bl_label = "test_two"

    def execute(self, context):
        print("Zaeet")
        return {'FINISHED'}
