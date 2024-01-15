import bpy
class ShaderNodeuv_map_swirl(bpy.types.ShaderNodeCustomGroup):
    bl_name='ShaderNodeuv_map_swirl'
    bl_label='uv_map_swirl'
    bl_icon='NONE'

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs['Point'].default_value=[0,0,0]
        self.inputs['HAS_Point'].default_value=0
        self.inputs['HAS_Point'].hide=True
        self.inputs['Scale'].default_value=5
        self.inputs['Center'].default_value=[0.5,0.5,0]
        self.inputs['brickwidth'].default_value=1
        self.inputs['brickheight'].default_value=1

    def update(self):
        if self.inputs['Point'].is_linked:
            self.inputs['HAS_Point'].default_value=1
        else:    
            self.inputs['HAS_Point'].default_value=0
            pass

    def value_set(self, obj, path, value):
        if '.' in path:
            path_prop, path_attr = path.rsplit('.', 1)
            prop = obj.path_resolve(path_prop)
        else:
            prop = obj
            path_attr = path
        setattr(prop, path_attr, value)

    def createNodetree(self, name) :
        self.node_tree = bpy.data.node_groups.new(name, 'ShaderNodeTree')
        #Nodes
        self.addNode('NodeGroupInput', { 'name':'GroupInput'  })
        self.addNode('NodeGroupOutput', { 'name':'GroupOutput'  })
        self.addNode('ShaderNodeTexCoord', { 'name':'Node0'  })
        self.addNode('ShaderNodeMixRGB', { 'name':'Node1'  })
        self.addNode('ShaderNodeValue', { 'name':'Node10' ,'outputs[0].default_value':3.1415927  })
        self.addNode('ShaderNodeValue', { 'name':'Node11' ,'outputs[0].default_value':4  })
        self.addNode('ShaderNodeValue', { 'name':'Node12' ,'outputs[0].default_value':3  })
        self.addNode('ShaderNodeValue', { 'name':'Node13' ,'outputs[0].default_value':1e-06  })
        self.addNode('ShaderNodeValue', { 'name':'Node14' ,'outputs[0].default_value':0  })
        self.addNode('ShaderNodeValue', { 'name':'Node15' ,'outputs[0].default_value':0.1963  })
        self.addNode('ShaderNodeValue', { 'name':'Node16' ,'outputs[0].default_value':0.9817  })
        self.addNode('ShaderNodeValue', { 'name':'Node17' ,'outputs[0].default_value':6.283  })
        self.addNode('ShaderNodeValue', { 'name':'Node18' ,'outputs[0].default_value':3.1415925  })
        self.addNode('ShaderNodeValue', { 'name':'Node19' ,'outputs[0].default_value':5  })
        self.addNode('ShaderNodeSeparateXYZ', { 'name':'Node21'  })
        self.addNode('ShaderNodeSeparateXYZ', { 'name':'Node22'  })
        self.addNode('ShaderNodeMath', { 'name':'Node23' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeSeparateXYZ', { 'name':'Node24'  })
        self.addNode('ShaderNodeSeparateXYZ', { 'name':'Node25'  })
        self.addNode('ShaderNodeMath', { 'name':'Node26' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node27' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node28' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node29' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node30' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node31' ,'operation':'ADD' })
        self.addNode('ShaderNodeMath', { 'name':'Node32' ,'inputs[1].default_value':0.5 ,'operation':'POWER' })
        self.addNode('ShaderNodeMath', { 'name':'Node33' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node34' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node35' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node36' ,'inputs[1].default_value':0.5 ,'operation':'ABSOLUTE' })
        self.addNode('ShaderNodeMath', { 'name':'Node37' ,'operation':'ADD' })
        self.addNode('ShaderNodeMath', { 'name':'Node38' ,'operation':'LESS_THAN' })
        self.addNode('ShaderNodeMath', { 'name':'Node39' ,'operation':'ADD' })
        self.addNode('ShaderNodeMath', { 'name':'Node40' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node41' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node42' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node43' ,'operation':'ADD' })
        self.addNode('ShaderNodeMath', { 'name':'Node44' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMixRGB', { 'name':'Node45'  })
        self.addNode('ShaderNodeMixRGB', { 'name':'Node46'  })
        self.addNode('ShaderNodeMath', { 'name':'Node47' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node48' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node49' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node50' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node51' ,'operation':'ADD' })
        self.addNode('ShaderNodeMath', { 'name':'Node52' ,'operation':'LESS_THAN' })
        self.addNode('ShaderNodeMath', { 'name':'Node53' ,'inputs[1].default_value':-1 ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMixRGB', { 'name':'Node54'  })
        self.addNode('ShaderNodeMath', { 'name':'Node55' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node56' ,'operation':'ADD' })
        self.addNode('ShaderNodeMath', { 'name':'Node57' ,'inputs[1].default_value':0.5 ,'operation':'ADD' })
        self.addNode('ShaderNodeMath', { 'name':'Node58' ,'inputs[1].default_value':0.5 ,'operation':'ROUND' })
        self.addNode('ShaderNodeMath', { 'name':'Node59' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node60' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node61' ,'inputs[1].default_value':0.5 ,'operation':'POWER' })
        self.addNode('ShaderNodeMath', { 'name':'Node62' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node63' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node64' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node65' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node66' ,'inputs[1].default_value':0.5 ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node67' ,'inputs[1].default_value':0.5 ,'operation':'ROUND' })
        self.addNode('ShaderNodeMath', { 'name':'Node68' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node69' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node70' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node71' ,'inputs[1].default_value':0.5 ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node72' ,'inputs[1].default_value':0.5 ,'operation':'ROUND' })
        self.addNode('ShaderNodeMath', { 'name':'Node73' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node74' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeCombineXYZ', { 'name':'Node75'  })
        self.addNode('ShaderNodeMath', { 'name':'Node76' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node77' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node78' ,'inputs[1].default_value':0.5 ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node79' ,'inputs[1].default_value':0.5 ,'operation':'ROUND' })
        self.addNode('ShaderNodeMath', { 'name':'Node80' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node81' ,'inputs[1].default_value':0.5 ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node82' ,'inputs[1].default_value':0.5 ,'operation':'ROUND' })
        self.addNode('ShaderNodeCombineXYZ', { 'name':'Node83'  })
        self.addNode('ShaderNodeCombineXYZ', { 'name':'Node84'  })
        #Sockets
        self.addSocket(False, 'NodeSocketVector', 'Point')
        self.addSocket(False, 'NodeSocketFloat', 'HAS_Point')
        self.addSocket(False, 'NodeSocketFloat', 'Scale')
        self.addSocket(False, 'NodeSocketVector', 'Center')
        self.addSocket(False, 'NodeSocketFloat', 'brickwidth')
        self.addSocket(False, 'NodeSocketFloat', 'brickheight')
        self.addSocket(True, 'NodeSocketVector', 'UV')
        self.addSocket(True, 'NodeSocketVector', 'CellID')
        self.addSocket(True, 'NodeSocketVector', 'Position')
        self.addSocket(True, 'NodeSocketFloat', 'brick_width')
        self.addSocket(True, 'NodeSocketFloat', 'brick_height')
        #Links
        self.innerLink('nodes["GroupInput"].outputs[1]', 'nodes["Node1"].inputs[0]')
        self.innerLink('nodes["Node0"].outputs[3]', 'nodes["Node1"].inputs[1]')
        self.innerLink('nodes["GroupInput"].outputs[0]', 'nodes["Node1"].inputs[2]')
        self.innerLink('nodes["Node1"].outputs[0]', 'nodes["Node21"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[3]', 'nodes["Node22"].inputs[0]')
        self.innerLink('nodes["Node21"].outputs[0]', 'nodes["Node23"].inputs[0]')
        self.innerLink('nodes["Node22"].outputs[0]', 'nodes["Node23"].inputs[1]')
        self.innerLink('nodes["Node1"].outputs[0]', 'nodes["Node24"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[3]', 'nodes["Node25"].inputs[0]')
        self.innerLink('nodes["Node24"].outputs[1]', 'nodes["Node26"].inputs[0]')
        self.innerLink('nodes["Node25"].outputs[1]', 'nodes["Node26"].inputs[1]')
        self.innerLink('nodes["Node23"].outputs[0]', 'nodes["Node27"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[2]', 'nodes["Node27"].inputs[1]')
        self.innerLink('nodes["Node26"].outputs[0]', 'nodes["Node28"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[2]', 'nodes["Node28"].inputs[1]')
        self.innerLink('nodes["Node27"].outputs[0]', 'nodes["Node29"].inputs[0]')
        self.innerLink('nodes["Node27"].outputs[0]', 'nodes["Node29"].inputs[1]')
        self.innerLink('nodes["Node28"].outputs[0]', 'nodes["Node30"].inputs[0]')
        self.innerLink('nodes["Node28"].outputs[0]', 'nodes["Node30"].inputs[1]')
        self.innerLink('nodes["Node29"].outputs[0]', 'nodes["Node31"].inputs[0]')
        self.innerLink('nodes["Node30"].outputs[0]', 'nodes["Node31"].inputs[1]')
        self.innerLink('nodes["Node31"].outputs[0]', 'nodes["Node32"].inputs[0]')
        self.innerLink('nodes["Node10"].outputs[0]', 'nodes["Node33"].inputs[0]')
        self.innerLink('nodes["Node11"].outputs[0]', 'nodes["Node33"].inputs[1]')
        self.innerLink('nodes["Node12"].outputs[0]', 'nodes["Node34"].inputs[0]')
        self.innerLink('nodes["Node10"].outputs[0]', 'nodes["Node34"].inputs[1]')
        self.innerLink('nodes["Node34"].outputs[0]', 'nodes["Node35"].inputs[0]')
        self.innerLink('nodes["Node11"].outputs[0]', 'nodes["Node35"].inputs[1]')
        self.innerLink('nodes["Node28"].outputs[0]', 'nodes["Node36"].inputs[0]')
        self.innerLink('nodes["Node36"].outputs[0]', 'nodes["Node37"].inputs[0]')
        self.innerLink('nodes["Node13"].outputs[0]', 'nodes["Node37"].inputs[1]')
        self.innerLink('nodes["Node27"].outputs[0]', 'nodes["Node38"].inputs[0]')
        self.innerLink('nodes["Node14"].outputs[0]', 'nodes["Node38"].inputs[1]')
        self.innerLink('nodes["Node27"].outputs[0]', 'nodes["Node39"].inputs[0]')
        self.innerLink('nodes["Node37"].outputs[0]', 'nodes["Node39"].inputs[1]')
        self.innerLink('nodes["Node37"].outputs[0]', 'nodes["Node40"].inputs[0]')
        self.innerLink('nodes["Node27"].outputs[0]', 'nodes["Node40"].inputs[1]')
        self.innerLink('nodes["Node39"].outputs[0]', 'nodes["Node41"].inputs[0]')
        self.innerLink('nodes["Node40"].outputs[0]', 'nodes["Node41"].inputs[1]')
        self.innerLink('nodes["Node27"].outputs[0]', 'nodes["Node42"].inputs[0]')
        self.innerLink('nodes["Node37"].outputs[0]', 'nodes["Node42"].inputs[1]')
        self.innerLink('nodes["Node27"].outputs[0]', 'nodes["Node43"].inputs[0]')
        self.innerLink('nodes["Node37"].outputs[0]', 'nodes["Node43"].inputs[1]')
        self.innerLink('nodes["Node42"].outputs[0]', 'nodes["Node44"].inputs[0]')
        self.innerLink('nodes["Node43"].outputs[0]', 'nodes["Node44"].inputs[1]')
        self.innerLink('nodes["Node38"].outputs[0]', 'nodes["Node45"].inputs[0]')
        self.innerLink('nodes["Node33"].outputs[0]', 'nodes["Node45"].inputs[1]')
        self.innerLink('nodes["Node35"].outputs[0]', 'nodes["Node45"].inputs[2]')
        self.innerLink('nodes["Node38"].outputs[0]', 'nodes["Node46"].inputs[0]')
        self.innerLink('nodes["Node44"].outputs[0]', 'nodes["Node46"].inputs[1]')
        self.innerLink('nodes["Node41"].outputs[0]', 'nodes["Node46"].inputs[2]')
        self.innerLink('nodes["Node15"].outputs[0]', 'nodes["Node47"].inputs[0]')
        self.innerLink('nodes["Node46"].outputs[0]', 'nodes["Node47"].inputs[1]')
        self.innerLink('nodes["Node47"].outputs[0]', 'nodes["Node48"].inputs[0]')
        self.innerLink('nodes["Node46"].outputs[0]', 'nodes["Node48"].inputs[1]')
        self.innerLink('nodes["Node48"].outputs[0]', 'nodes["Node49"].inputs[0]')
        self.innerLink('nodes["Node16"].outputs[0]', 'nodes["Node49"].inputs[1]')
        self.innerLink('nodes["Node49"].outputs[0]', 'nodes["Node50"].inputs[0]')
        self.innerLink('nodes["Node46"].outputs[0]', 'nodes["Node50"].inputs[1]')
        self.innerLink('nodes["Node45"].outputs[0]', 'nodes["Node51"].inputs[0]')
        self.innerLink('nodes["Node50"].outputs[0]', 'nodes["Node51"].inputs[1]')
        self.innerLink('nodes["Node28"].outputs[0]', 'nodes["Node52"].inputs[0]')
        self.innerLink('nodes["Node14"].outputs[0]', 'nodes["Node52"].inputs[1]')
        self.innerLink('nodes["Node51"].outputs[0]', 'nodes["Node53"].inputs[0]')
        self.innerLink('nodes["Node52"].outputs[0]', 'nodes["Node54"].inputs[0]')
        self.innerLink('nodes["Node51"].outputs[0]', 'nodes["Node54"].inputs[1]')
        self.innerLink('nodes["Node53"].outputs[0]', 'nodes["Node54"].inputs[2]')
        self.innerLink('nodes["Node54"].outputs[0]', 'nodes["Node55"].inputs[0]')
        self.innerLink('nodes["Node17"].outputs[0]', 'nodes["Node55"].inputs[1]')
        self.innerLink('nodes["Node32"].outputs[0]', 'nodes["Node56"].inputs[0]')
        self.innerLink('nodes["Node55"].outputs[0]', 'nodes["Node56"].inputs[1]')
        self.innerLink('nodes["Node56"].outputs[0]', 'nodes["Node57"].inputs[0]')
        self.innerLink('nodes["Node57"].outputs[0]', 'nodes["Node58"].inputs[0]')
        self.innerLink('nodes["Node55"].outputs[0]', 'nodes["Node59"].inputs[0]')
        self.innerLink('nodes["Node58"].outputs[0]', 'nodes["Node59"].inputs[1]')
        self.innerLink('nodes["Node59"].outputs[0]', 'nodes["Node60"].inputs[0]')
        self.innerLink('nodes["Node18"].outputs[0]', 'nodes["Node60"].inputs[1]')
        self.innerLink('nodes["Node19"].outputs[0]', 'nodes["Node61"].inputs[0]')
        self.innerLink('nodes["Node12"].outputs[0]', 'nodes["Node62"].inputs[0]')
        self.innerLink('nodes["Node61"].outputs[0]', 'nodes["Node62"].inputs[1]')
        self.innerLink('nodes["Node60"].outputs[0]', 'nodes["Node63"].inputs[0]')
        self.innerLink('nodes["Node62"].outputs[0]', 'nodes["Node63"].inputs[1]')
        self.innerLink('nodes["Node59"].outputs[0]', 'nodes["Node64"].inputs[0]')
        self.innerLink('nodes["Node63"].outputs[0]', 'nodes["Node64"].inputs[1]')
        self.innerLink('nodes["Node64"].outputs[0]', 'nodes["Node65"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[4]', 'nodes["Node65"].inputs[1]')
        self.innerLink('nodes["Node65"].outputs[0]', 'nodes["Node66"].inputs[0]')
        self.innerLink('nodes["Node66"].outputs[0]', 'nodes["Node67"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[4]', 'nodes["Node68"].inputs[0]')
        self.innerLink('nodes["Node67"].outputs[0]', 'nodes["Node68"].inputs[1]')
        self.innerLink('nodes["Node64"].outputs[0]', 'nodes["Node69"].inputs[0]')
        self.innerLink('nodes["Node68"].outputs[0]', 'nodes["Node69"].inputs[1]')
        self.innerLink('nodes["Node56"].outputs[0]', 'nodes["Node70"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[5]', 'nodes["Node70"].inputs[1]')
        self.innerLink('nodes["Node70"].outputs[0]', 'nodes["Node71"].inputs[0]')
        self.innerLink('nodes["Node71"].outputs[0]', 'nodes["Node72"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[5]', 'nodes["Node73"].inputs[0]')
        self.innerLink('nodes["Node72"].outputs[0]', 'nodes["Node73"].inputs[1]')
        self.innerLink('nodes["Node56"].outputs[0]', 'nodes["Node74"].inputs[0]')
        self.innerLink('nodes["Node73"].outputs[0]', 'nodes["Node74"].inputs[1]')
        self.innerLink('nodes["Node69"].outputs[0]', 'nodes["Node75"].inputs[0]')
        self.innerLink('nodes["Node74"].outputs[0]', 'nodes["Node75"].inputs[1]')
        self.innerLink('nodes["Node14"].outputs[0]', 'nodes["Node75"].inputs[2]')
        self.innerLink('nodes["Node56"].outputs[0]', 'nodes["Node76"].inputs[0]')
        self.innerLink('nodes["Node58"].outputs[0]', 'nodes["Node76"].inputs[1]')
        self.innerLink('nodes["Node64"].outputs[0]', 'nodes["Node77"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[4]', 'nodes["Node77"].inputs[1]')
        self.innerLink('nodes["Node77"].outputs[0]', 'nodes["Node78"].inputs[0]')
        self.innerLink('nodes["Node78"].outputs[0]', 'nodes["Node79"].inputs[0]')
        self.innerLink('nodes["Node76"].outputs[0]', 'nodes["Node80"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[5]', 'nodes["Node80"].inputs[1]')
        self.innerLink('nodes["Node80"].outputs[0]', 'nodes["Node81"].inputs[0]')
        self.innerLink('nodes["Node81"].outputs[0]', 'nodes["Node82"].inputs[0]')
        self.innerLink('nodes["Node79"].outputs[0]', 'nodes["Node83"].inputs[0]')
        self.innerLink('nodes["Node82"].outputs[0]', 'nodes["Node83"].inputs[1]')
        self.innerLink('nodes["Node14"].outputs[0]', 'nodes["Node83"].inputs[2]')
        self.innerLink('nodes["Node64"].outputs[0]', 'nodes["Node84"].inputs[0]')
        self.innerLink('nodes["Node76"].outputs[0]', 'nodes["Node84"].inputs[1]')
        self.innerLink('nodes["Node14"].outputs[0]', 'nodes["Node84"].inputs[2]')
        self.innerLink('nodes["Node75"].outputs[0]', 'nodes["GroupOutput"].inputs[0]')
        self.innerLink('nodes["Node83"].outputs[0]', 'nodes["GroupOutput"].inputs[1]')
        self.innerLink('nodes["Node84"].outputs[0]', 'nodes["GroupOutput"].inputs[2]')
        self.innerLink('nodes["GroupInput"].outputs[4]', 'nodes["GroupOutput"].inputs[3]')
        self.innerLink('nodes["GroupInput"].outputs[5]', 'nodes["GroupOutput"].inputs[4]')
    def getNodetree(self, name):
        if bpy.data.node_groups.find(name)==-1:
            self.createNodetree(name)
        else:
            self.node_tree=bpy.data.node_groups[name]
                   
    def addSocket(self, is_output, sockettype, name):
        if bpy.app.version >= (4, 0, 0):
            if is_output==True:
                socket = self.node_tree.interface.new_socket(name, in_out='OUTPUT', socket_type=sockettype)
            else:
                socket = self.node_tree.interface.new_socket(name, in_out='INPUT', socket_type=sockettype)
        else:
            #for now duplicated socket names are not allowed
            if is_output==True:
                if self.node_tree.nodes['GroupOutput'].inputs.find(name)==-1:
                    socket=self.node_tree.outputs.new(sockettype, name)
            elif is_output==False:
                if self.node_tree.nodes['GroupInput'].outputs.find(name)==-1:
                    socket=self.node_tree.inputs.new(sockettype, name)
        return socket
       
    def addNode(self, nodetype, attrs):
        node=self.node_tree.nodes.new(nodetype)
        for attr in attrs:
            self.value_set(node, attr, attrs[attr])
        return node
   
    def getNode(self, nodename):
        if self.node_tree.nodes.find(nodename)>-1:
            return self.node_tree.nodes[nodename]
        return None
   
    def innerLink(self, socketin, socketout):
        SI=self.node_tree.path_resolve(socketin)
        SO=self.node_tree.path_resolve(socketout)
        self.node_tree.links.new(SI, SO)
       
    def free(self):
        if self.node_tree.users==1:
            bpy.data.node_groups.remove(self.node_tree, do_unlink=True)
 
 
 
