import bpy
class ShaderNodeuv_map_tile_pattern_1(bpy.types.ShaderNodeCustomGroup):
    bl_name='ShaderNodeuv_map_tile_pattern_1'
    bl_label='uv_map_tile_pattern_1'
    bl_icon='NONE'

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs['Vector'].default_value=[0,0,0]
        self.inputs['HAS_Vector'].default_value=0
        self.inputs['HAS_Vector'].hide=True
        self.inputs['scale'].default_value=1

    def update(self):
        if self.inputs['Vector'].is_linked:
            self.inputs['HAS_Vector'].default_value=1
        else:    
            self.inputs['HAS_Vector'].default_value=0
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
        self.addNode('ShaderNodeValue', { 'name':'Node4' ,'outputs[0].default_value':0.5  })
        self.addNode('ShaderNodeValue', { 'name':'Node5' ,'outputs[0].default_value':0.25  })
        self.addNode('ShaderNodeValue', { 'name':'Node6' ,'outputs[0].default_value':0  })
        self.addNode('ShaderNodeValue', { 'name':'Node9' ,'outputs[0].default_value':1  })
        self.addNode('ShaderNodeValue', { 'name':'Node10' ,'outputs[0].default_value':0.5  })
        self.addNode('ShaderNodeValue', { 'name':'Node11' ,'outputs[0].default_value':0.25  })
        self.addNode('ShaderNodeValue', { 'name':'Node12' ,'outputs[0].default_value':0  })
        self.addNode('ShaderNodeSeparateXYZ', { 'name':'Node13'  })
        self.addNode('ShaderNodeMath', { 'name':'Node14' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node15' ,'inputs[1].default_value':0.5 ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node16' ,'inputs[1].default_value':0.5 ,'operation':'ROUND' })
        self.addNode('ShaderNodeMath', { 'name':'Node17' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeSeparateXYZ', { 'name':'Node18'  })
        self.addNode('ShaderNodeMath', { 'name':'Node19' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node20' ,'inputs[1].default_value':0.5 ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node21' ,'inputs[1].default_value':0.5 ,'operation':'ROUND' })
        self.addNode('ShaderNodeMath', { 'name':'Node22' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node23' ,'operation':'LESS_THAN' })
        self.addNode('ShaderNodeMath', { 'name':'Node24' ,'operation':'LESS_THAN' })
        self.addNode('ShaderNodeMath', { 'name':'Node25' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node26' ,'operation':'ABSOLUTE' })
        self.addNode('ShaderNodeMath', { 'name':'Node27' ,'inputs[1].default_value':0.000001 ,'operation':'LESS_THAN' })
        self.addNode('ShaderNodeMath', { 'name':'Node28' ,'operation':'MODULO' })
        self.addNode('ShaderNodeMath', { 'name':'Node29' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node30' ,'operation':'MODULO' })
        self.addNode('ShaderNodeCombineXYZ', { 'name':'Node31'  })
        self.addNode('ShaderNodeSeparateXYZ', { 'name':'Node32'  })
        self.addNode('ShaderNodeMath', { 'name':'Node33' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node34' ,'inputs[1].default_value':0.5 ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node35' ,'inputs[1].default_value':0.5 ,'operation':'ROUND' })
        self.addNode('ShaderNodeSeparateXYZ', { 'name':'Node36'  })
        self.addNode('ShaderNodeMath', { 'name':'Node37' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node38' ,'inputs[1].default_value':0.5 ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node39' ,'inputs[1].default_value':0.5 ,'operation':'ROUND' })
        self.addNode('ShaderNodeCombineXYZ', { 'name':'Node40'  })
        self.addNode('ShaderNodeMath', { 'name':'Node41' ,'operation':'MODULO' })
        self.addNode('ShaderNodeMath', { 'name':'Node42' ,'operation':'MODULO' })
        self.addNode('ShaderNodeCombineXYZ', { 'name':'Node43'  })
        self.addNode('ShaderNodeSeparateXYZ', { 'name':'Node44'  })
        self.addNode('ShaderNodeMath', { 'name':'Node45' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node46' ,'inputs[1].default_value':0.5 ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node47' ,'inputs[1].default_value':0.5 ,'operation':'ROUND' })
        self.addNode('ShaderNodeSeparateXYZ', { 'name':'Node48'  })
        self.addNode('ShaderNodeMath', { 'name':'Node49' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node50' ,'inputs[1].default_value':0.5 ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node51' ,'inputs[1].default_value':0.5 ,'operation':'ROUND' })
        self.addNode('ShaderNodeCombineXYZ', { 'name':'Node52'  })
        self.addNode('ShaderNodeMixRGB', { 'name':'Node53'  })
        self.addNode('ShaderNodeMixRGB', { 'name':'Node54'  })
        self.addNode('ShaderNodeMixRGB', { 'name':'Node55'  })
        #Sockets
        self.addSocket(False, 'NodeSocketVector', 'Vector')
        self.addSocket(False, 'NodeSocketFloatFactor', 'HAS_Vector')
        self.addSocket(False, 'NodeSocketFloat', 'scale')
        self.addSocket(True, 'NodeSocketVector', 'UV')
        self.addSocket(True, 'NodeSocketVector', 'cellID')
        self.addSocket(True, 'NodeSocketFloat', 'brick_width')
        self.addSocket(True, 'NodeSocketFloat', 'brick_height')
        self.addSocket(True, 'NodeSocketFloat', 'tile_mask')
        #Links
        self.innerLink('nodes["GroupInput"].outputs[1]', 'nodes["Node1"].inputs[0]')
        self.innerLink('nodes["Node0"].outputs[3]', 'nodes["Node1"].inputs[1]')
        self.innerLink('nodes["GroupInput"].outputs[0]', 'nodes["Node1"].inputs[2]')
        self.innerLink('nodes["Node1"].outputs[0]', 'nodes["Node13"].inputs[0]')
        self.innerLink('nodes["Node13"].outputs[0]', 'nodes["Node14"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[2]', 'nodes["Node14"].inputs[1]')
        self.innerLink('nodes["Node14"].outputs[0]', 'nodes["Node15"].inputs[0]')
        self.innerLink('nodes["Node15"].outputs[0]', 'nodes["Node16"].inputs[0]')
        self.innerLink('nodes["Node14"].outputs[0]', 'nodes["Node17"].inputs[0]')
        self.innerLink('nodes["Node16"].outputs[0]', 'nodes["Node17"].inputs[1]')
        self.innerLink('nodes["Node1"].outputs[0]', 'nodes["Node18"].inputs[0]')
        self.innerLink('nodes["Node18"].outputs[1]', 'nodes["Node19"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[2]', 'nodes["Node19"].inputs[1]')
        self.innerLink('nodes["Node19"].outputs[0]', 'nodes["Node20"].inputs[0]')
        self.innerLink('nodes["Node20"].outputs[0]', 'nodes["Node21"].inputs[0]')
        self.innerLink('nodes["Node19"].outputs[0]', 'nodes["Node22"].inputs[0]')
        self.innerLink('nodes["Node21"].outputs[0]', 'nodes["Node22"].inputs[1]')
        self.innerLink('nodes["Node17"].outputs[0]', 'nodes["Node23"].inputs[0]')
        self.innerLink('nodes["Node10"].outputs[0]', 'nodes["Node23"].inputs[1]')
        self.innerLink('nodes["Node22"].outputs[0]', 'nodes["Node24"].inputs[0]')
        self.innerLink('nodes["Node10"].outputs[0]', 'nodes["Node24"].inputs[1]')
        self.innerLink('nodes["Node23"].outputs[0]', 'nodes["Node25"].inputs[0]')
        self.innerLink('nodes["Node24"].outputs[0]', 'nodes["Node25"].inputs[1]')
        self.innerLink('nodes["Node25"].outputs[0]', 'nodes["Node26"].inputs[0]')
        self.innerLink('nodes["Node26"].outputs[0]', 'nodes["Node27"].inputs[0]')
        self.innerLink('nodes["Node22"].outputs[0]', 'nodes["Node28"].inputs[0]')
        self.innerLink('nodes["Node10"].outputs[0]', 'nodes["Node28"].inputs[1]')
        self.innerLink('nodes["Node10"].outputs[0]', 'nodes["Node29"].inputs[0]')
        self.innerLink('nodes["Node28"].outputs[0]', 'nodes["Node29"].inputs[1]')
        self.innerLink('nodes["Node17"].outputs[0]', 'nodes["Node30"].inputs[0]')
        self.innerLink('nodes["Node11"].outputs[0]', 'nodes["Node30"].inputs[1]')
        self.innerLink('nodes["Node29"].outputs[0]', 'nodes["Node31"].inputs[0]')
        self.innerLink('nodes["Node30"].outputs[0]', 'nodes["Node31"].inputs[1]')
        self.innerLink('nodes["Node12"].outputs[0]', 'nodes["Node31"].inputs[2]')
        self.innerLink('nodes["Node1"].outputs[0]', 'nodes["Node32"].inputs[0]')
        self.innerLink('nodes["Node32"].outputs[0]', 'nodes["Node33"].inputs[0]')
        self.innerLink('nodes["Node11"].outputs[0]', 'nodes["Node33"].inputs[1]')
        self.innerLink('nodes["Node33"].outputs[0]', 'nodes["Node34"].inputs[0]')
        self.innerLink('nodes["Node34"].outputs[0]', 'nodes["Node35"].inputs[0]')
        self.innerLink('nodes["Node1"].outputs[0]', 'nodes["Node36"].inputs[0]')
        self.innerLink('nodes["Node36"].outputs[1]', 'nodes["Node37"].inputs[0]')
        self.innerLink('nodes["Node10"].outputs[0]', 'nodes["Node37"].inputs[1]')
        self.innerLink('nodes["Node37"].outputs[0]', 'nodes["Node38"].inputs[0]')
        self.innerLink('nodes["Node38"].outputs[0]', 'nodes["Node39"].inputs[0]')
        self.innerLink('nodes["Node35"].outputs[0]', 'nodes["Node40"].inputs[0]')
        self.innerLink('nodes["Node39"].outputs[0]', 'nodes["Node40"].inputs[1]')
        self.innerLink('nodes["Node12"].outputs[0]', 'nodes["Node40"].inputs[2]')
        self.innerLink('nodes["Node17"].outputs[0]', 'nodes["Node41"].inputs[0]')
        self.innerLink('nodes["Node10"].outputs[0]', 'nodes["Node41"].inputs[1]')
        self.innerLink('nodes["Node22"].outputs[0]', 'nodes["Node42"].inputs[0]')
        self.innerLink('nodes["Node11"].outputs[0]', 'nodes["Node42"].inputs[1]')
        self.innerLink('nodes["Node41"].outputs[0]', 'nodes["Node43"].inputs[0]')
        self.innerLink('nodes["Node42"].outputs[0]', 'nodes["Node43"].inputs[1]')
        self.innerLink('nodes["Node12"].outputs[0]', 'nodes["Node43"].inputs[2]')
        self.innerLink('nodes["Node1"].outputs[0]', 'nodes["Node44"].inputs[0]')
        self.innerLink('nodes["Node44"].outputs[0]', 'nodes["Node45"].inputs[0]')
        self.innerLink('nodes["Node10"].outputs[0]', 'nodes["Node45"].inputs[1]')
        self.innerLink('nodes["Node45"].outputs[0]', 'nodes["Node46"].inputs[0]')
        self.innerLink('nodes["Node46"].outputs[0]', 'nodes["Node47"].inputs[0]')
        self.innerLink('nodes["Node1"].outputs[0]', 'nodes["Node48"].inputs[0]')
        self.innerLink('nodes["Node48"].outputs[1]', 'nodes["Node49"].inputs[0]')
        self.innerLink('nodes["Node11"].outputs[0]', 'nodes["Node49"].inputs[1]')
        self.innerLink('nodes["Node49"].outputs[0]', 'nodes["Node50"].inputs[0]')
        self.innerLink('nodes["Node50"].outputs[0]', 'nodes["Node51"].inputs[0]')
        self.innerLink('nodes["Node47"].outputs[0]', 'nodes["Node52"].inputs[0]')
        self.innerLink('nodes["Node51"].outputs[0]', 'nodes["Node52"].inputs[1]')
        self.innerLink('nodes["Node12"].outputs[0]', 'nodes["Node52"].inputs[2]')
        self.innerLink('nodes["Node27"].outputs[0]', 'nodes["Node53"].inputs[0]')
        self.innerLink('nodes["Node43"].outputs[0]', 'nodes["Node53"].inputs[1]')
        self.innerLink('nodes["Node31"].outputs[0]', 'nodes["Node53"].inputs[2]')
        self.innerLink('nodes["Node27"].outputs[0]', 'nodes["Node54"].inputs[0]')
        self.innerLink('nodes["Node52"].outputs[0]', 'nodes["Node54"].inputs[1]')
        self.innerLink('nodes["Node40"].outputs[0]', 'nodes["Node54"].inputs[2]')
        self.innerLink('nodes["Node27"].outputs[0]', 'nodes["Node55"].inputs[0]')
        self.innerLink('nodes["Node6"].outputs[0]', 'nodes["Node55"].inputs[1]')
        self.innerLink('nodes["Node9"].outputs[0]', 'nodes["Node55"].inputs[2]')
        self.innerLink('nodes["Node53"].outputs[0]', 'nodes["GroupOutput"].inputs[0]')
        self.innerLink('nodes["Node54"].outputs[0]', 'nodes["GroupOutput"].inputs[1]')
        self.innerLink('nodes["Node4"].outputs[0]', 'nodes["GroupOutput"].inputs[2]')
        self.innerLink('nodes["Node5"].outputs[0]', 'nodes["GroupOutput"].inputs[3]')
        self.innerLink('nodes["Node55"].outputs[0]', 'nodes["GroupOutput"].inputs[4]')
    def getNodetree(self, name):
        if bpy.data.node_groups.find(name)==-1:
            self.createNodetree(name)
        else:
            self.node_tree=bpy.data.node_groups[name]
                   
    def addSocket(self, is_output, sockettype, name):
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
 
 
 
