import bpy
import sys
import os

# Ordner, in dem main.py liegt, ermitteln und zu sys.path hinzufügen (ermöglicht import von eigenen modulen)
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.append(script_dir)

import test

class placeholder(bpy.types.Panel):
    bl_idname = "placeholder"
    bl_label = "placeholder"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PIDGEPIPE"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text=test.placeholder_text)

classes = (
    placeholder,
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

if __name__ == "__main__":
    register()