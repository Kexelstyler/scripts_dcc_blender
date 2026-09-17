import bpy

print("hello world")

class TestPanel(bpy.types.Panel):
    bl_idname = "TEST_PANEL"
    bl_label = "Test Panel"