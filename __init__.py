bl_info = {
    "name": "BrickTricks",
    "author": (
        "LazyDodo, "
        "Secrop"
     ),
    "version": (0, 0, 1,5),
    "blender": (2, 80, 0),
    "location": "Nodes > Add nodes",
    "description": "Brick Tricks Cycles Nodes",
    "warning": "",
    "wiki_url": "",
    "category": "Node"} 

from .bonus_hexagon_addin import ShaderNodebonus_hexagon
from .brick_rounded_corner_addin import ShaderNodebrick_rounded_corner
from .brick_square_corner_addin import ShaderNodebrick_square_corner
from .uv_map_brick_wall_addin import ShaderNodeuv_map_brick_wall
from .uv_map_rotate_addin import ShaderNodeuv_map_rotate
from .uv_map_swirl_addin import ShaderNodeuv_map_swirl
from .uv_map_tile_pattern_1_addin import ShaderNodeuv_map_tile_pattern_1
from .uv_map_tile_pattern_2_addin import ShaderNodeuv_map_tile_pattern_2
from .uv_map_diamond_addin import ShaderNodeuv_map_diamond

import bpy,nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem
from bpy.types import Menu
from bl_ui import node_add_menu

class ExtraNodesCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return (context.space_data.tree_type == 'ShaderNodeTree' and
                context.scene.render.engine in ['BLENDER_EEVEE', 'CYCLES'])

node_categories = [
    ExtraNodesCategory("SH_BRICK_TRIKS", "BrickTricks", items=[
        NodeItem("ShaderNodeuv_map_tile_pattern_1"),
        NodeItem("ShaderNodeuv_map_tile_pattern_2"),
        NodeItem("ShaderNodeuv_map_diamond"),
        NodeItem("ShaderNodeuv_map_brick_wall"),
        NodeItem("ShaderNodeuv_map_swirl"),
        NodeItem("ShaderNodebrick_rounded_corner"),
        NodeItem("ShaderNodebrick_square_corner"),
        NodeItem("ShaderNodeuv_map_rotate"),
        NodeItem("ShaderNodebonus_hexagon"),
        ]),
    ]

class NODE_MT_category_shader_bricktricks(Menu):
    bl_idname = "NODE_MT_category_shader_bricktricks"
    bl_label = "Brick Tricks"

    def draw(self, context):
        layout = self.layout

        node_add_menu.add_node_type(layout, "ShaderNodeuv_map_tile_pattern_1")
        node_add_menu.add_node_type(layout, "ShaderNodeuv_map_tile_pattern_2")
        node_add_menu.add_node_type(layout, "ShaderNodeuv_map_diamond")
        node_add_menu.add_node_type(layout, "ShaderNodeuv_map_brick_wall")
        node_add_menu.add_node_type(layout, "ShaderNodeuv_map_swirl")
        node_add_menu.add_node_type(layout, "ShaderNodebrick_rounded_corner")
        node_add_menu.add_node_type(layout, "ShaderNodebrick_square_corner")
        node_add_menu.add_node_type(layout, "ShaderNodeuv_map_rotate")
        node_add_menu.add_node_type(layout, "ShaderNodebonus_hexagon")
        node_add_menu.draw_assets_for_catalog(layout, self.bl_label)

def bricktricks_draw(self, context):
    layout = self.layout
    layout.menu("NODE_MT_category_shader_bricktricks")

def register():
    if bpy.app.version >= (4, 0, 0):
        bpy.utils.register_class(NODE_MT_category_shader_bricktricks)
        bpy.types.NODE_MT_shader_node_add_all.append(bricktricks_draw)
    else:
        nodeitems_utils.register_node_categories("BRICK_TRICKS_NODES", node_categories)
    bpy.utils.register_class(ShaderNodebonus_hexagon)
    bpy.utils.register_class(ShaderNodebrick_rounded_corner)
    bpy.utils.register_class(ShaderNodebrick_square_corner)
    bpy.utils.register_class(ShaderNodeuv_map_brick_wall)
    bpy.utils.register_class(ShaderNodeuv_map_rotate)
    bpy.utils.register_class(ShaderNodeuv_map_swirl)
    bpy.utils.register_class(ShaderNodeuv_map_tile_pattern_1)
    bpy.utils.register_class(ShaderNodeuv_map_tile_pattern_2)
    bpy.utils.register_class(ShaderNodeuv_map_diamond)
 
 
def unregister():
    bpy.utils.unregister_class(ShaderNodebonus_hexagon)
    bpy.utils.unregister_class(ShaderNodebrick_rounded_corner)
    bpy.utils.unregister_class(ShaderNodebrick_square_corner)
    bpy.utils.unregister_class(ShaderNodeuv_map_brick_wall)
    bpy.utils.unregister_class(ShaderNodeuv_map_rotate)
    bpy.utils.unregister_class(ShaderNodeuv_map_swirl)
    bpy.utils.unregister_class(ShaderNodeuv_map_tile_pattern_1)
    bpy.utils.unregister_class(ShaderNodeuv_map_tile_pattern_2)
    bpy.utils.unregister_class(ShaderNodeuv_map_diamond)
    if bpy.app.version >= (4, 0, 0):
        bpy.types.NODE_MT_shader_node_add_all.remove(bricktricks_draw)
        bpy.utils.unregister_class(NODE_MT_category_shader_bricktricks)
    else:
        nodeitems_utils.unregister_node_categories("BRICK_TRICKS_NODES")
    
if __name__ == "__main__":
    register()
   
