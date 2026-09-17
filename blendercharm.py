import bpy

print("hello world")

class SuzannePanel(bpy.types.Panel):
    bl_idname = "SUZANNE"
    bl_label = "Suzanne"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "KeysShelf"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Suzanne!", icon="MESH_MONKEY")
        row = layout.row()
        suzanne = row.operator("mesh.primitive_monkey_add", text="Suzanne!")
        suzanne.location = (3,3,3)

classes = (
    SuzannePanel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

try:
    unregister()
except Exception:
    pass

# __name__ beinhaltet den namen der python-datei, währen __main__ die der ausführenden python-anwendung ist (in dem Fall Blender)
# In unserem Fall ist diese konkrete Datei der zu ausführende code (register, unregister...) also __main__
# Wird diese Datei durch einen anderen Code in der selben Anwendung aufgerufen/importiert so ist __name__ =/= __main__ sonder der, der Python Datei
if __name__ == "__main__": # ab hier werden die funktionen aufgerufen, wenn dies die auszuführende Datei ist
    register()