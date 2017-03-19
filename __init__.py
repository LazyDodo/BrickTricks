bl_info = {
    "name": "BrickTricks",
    "author": (
        "LazyDodo, "
        "Secrop"
     ),
    "version": (0, 0, 1,1),
    "blender": (2, 7, 8),
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

import bpy,nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem
 
class ExtraNodesCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return (context.space_data.tree_type == 'ShaderNodeTree' and
                context.scene.render.use_shading_nodes)
 
node_categories = [
    ExtraNodesCategory("SH_BRICK_TRIKS", "BrickTricks", items=[
        NodeItem("ShaderNodeuv_map_tile_pattern_1"),
        NodeItem("ShaderNodeuv_map_tile_pattern_2"),
        NodeItem("ShaderNodeuv_map_brick_wall"),
        NodeItem("ShaderNodeuv_map_swirl"),
        NodeItem("ShaderNodebrick_rounded_corner"),
        NodeItem("ShaderNodebrick_square_corner"),
        NodeItem("ShaderNodeuv_map_rotate"),
        NodeItem("ShaderNodebonus_hexagon"),
        ]),
    ]
      
def register():
    bpy.utils.register_class(ShaderNodebonus_hexagon)
    bpy.utils.register_class(ShaderNodebrick_rounded_corner)
    bpy.utils.register_class(ShaderNodebrick_square_corner)
    bpy.utils.register_class(ShaderNodeuv_map_brick_wall)
    bpy.utils.register_class(ShaderNodeuv_map_rotate)
    bpy.utils.register_class(ShaderNodeuv_map_swirl)
    bpy.utils.register_class(ShaderNodeuv_map_tile_pattern_1)
    bpy.utils.register_class(ShaderNodeuv_map_tile_pattern_2)
    nodeitems_utils.register_node_categories("BRICK_TRICKS_NODES", node_categories)
 
 
def unregister():
    nodeitems_utils.unregister_node_categories("BRICK_TRICKS_NODES")
    bpy.utils.unregister_class(ShaderNodebonus_hexagon)
    bpy.utils.unregister_class(ShaderNodebrick_rounded_corner)
    bpy.utils.unregister_class(ShaderNodebrick_square_corner)
    bpy.utils.unregister_class(ShaderNodeuv_map_brick_wall)
    bpy.utils.unregister_class(ShaderNodeuv_map_rotate)
    bpy.utils.unregister_class(ShaderNodeuv_map_swirl)
    bpy.utils.unregister_class(ShaderNodeuv_map_tile_pattern_1)
    bpy.utils.unregister_class(ShaderNodeuv_map_tile_pattern_2)
 
if __name__ == "__main__":
    register()
   