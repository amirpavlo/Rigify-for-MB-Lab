import bpy

def get_user_preferences(context=None):
    """Multi version compatibility for getting addon keys"""
    if not context:
        context = bpy.context
    prefs = None
    if hasattr(context, "user_preferences"):
        prefs = context.user_preferences
    elif hasattr(context, "preferences"):
        prefs = context.preferences
    if prefs:
        return prefs
    else:
        raise Exception("Could not fetch user preferences")

class RIGIFYFORMBLAB_OT_enable_rigify(bpy.types.Operator):
    bl_idname = "object.rigifyformblab_enable_rigify"
    bl_label = "Enable Rigify add-on"
    bl_description = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        prefs = get_user_preferences(bpy.context)
        prefs.addon_enable(module="rigify")
        return {'FINISHED'}


class RIGIFYFORMBLAB_PT_panel(bpy.types.Panel):
    bl_idname = "RIGIFYFORMBLAB_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS' if bpy.app.version < (2, 80) else 'UI'
    bl_label = "Rigify for MB-Lab"
    # bl_context = "objectmode"
    bl_category = "Rigify for MB-Lab"

    def draw(self, context):

        # legacy_mode = False
        # addons = bpy.context.preferences.addons
        # if "legacy_mode" in addons['rigify'].preferences:
        #     legacy_mode = True if addons['rigify'].preferences['legacy_mode'] == 1 else False

        col = self.layout.column()

        prefs = get_user_preferences(bpy.context)
        if not "rigify" in prefs.addons.keys():
            col.operator('object.rigifyformblab_enable_rigify')
        else:
            col.operator('object.rigifyformblab_addrig')
            col.operator('object.rigifyformblab_generaterig')

            col.label(text="Rename Vertex Groups:")
            col.operator('object.rigifyformblab_rename_vertex_groups')
            col.operator('object.rigifyformblab_unrename_vertex_groups')

            # if legacy_mode:
            #     col.label(text="Manual Weight Paint:", icon='ERROR')
