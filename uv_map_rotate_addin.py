import bpy
class ShaderNodeuv_map_rotate(bpy.types.NodeCustomGroup):
    bl_name='ShaderNodeuv_map_rotate'
    bl_label='uv_map_rotate'
    bl_icon='NONE'

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs['Vector'].default_value=[0,0,0]
        self.inputs['HAS_Vector'].default_value=0
        self.inputs['HAS_Vector'].hide=True
        self.inputs['brick_width'].default_value=1
        self.inputs['brick_height'].default_value=1
        self.inputs['Angle'].default_value=0
        self.inputs['Clamp'].default_value=0

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
        self.addNode('ShaderNodeValue', { 'name':'Node3' ,'outputs[0].default_value':2  })
        self.addNode('ShaderNodeValue', { 'name':'Node6' ,'outputs[0].default_value':3.1415927  })
        self.addNode('ShaderNodeValue', { 'name':'Node7' ,'outputs[0].default_value':180  })
        self.addNode('ShaderNodeValue', { 'name':'Node8' ,'outputs[0].default_value':0  })
        self.addNode('ShaderNodeValue', { 'name':'Node10' ,'outputs[0].default_value':0  })
        self.addNode('ShaderNodeMath', { 'name':'Node12' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node13' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node14' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node15' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node16' ,'operation':'SINE' })
        self.addNode('ShaderNodeMath', { 'name':'Node17' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node18' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node19' ,'operation':'COSINE' })
        self.addNode('ShaderNodeSeparateXYZ', { 'name':'Node20'  })
        self.addNode('ShaderNodeMath', { 'name':'Node21' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeSeparateXYZ', { 'name':'Node22'  })
        self.addNode('ShaderNodeMath', { 'name':'Node23' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node24' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node25' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node26' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node27' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node28' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node29' ,'operation':'ADD' })
        self.addNode('ShaderNodeMath', { 'name':'Node30' ,'operation':'ADD' })
        self.addNode('ShaderNodeMath', { 'name':'Node31' ,'operation':'ADD' })
        self.addNode('ShaderNodeMath', { 'name':'Node32' ,'operation':'GREATER_THAN' })
        self.addNode('ShaderNodeMath', { 'name':'Node33' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node34' ,'operation':'MINIMUM' })
        self.addNode('ShaderNodeMath', { 'name':'Node35' ,'operation':'MAXIMUM' })
        self.addNode('ShaderNodeMath', { 'name':'Node36' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node37' ,'operation':'MINIMUM' })
        self.addNode('ShaderNodeMath', { 'name':'Node38' ,'operation':'MAXIMUM' })
        self.addNode('ShaderNodeCombineXYZ', { 'name':'Node39'  })
        self.addNode('ShaderNodeCombineXYZ', { 'name':'Node40'  })
        self.addNode('ShaderNodeMixRGB', { 'name':'Node41'  })
        #Sockets
        self.addSocket(False, 'NodeSocketVector', 'Vector')
        self.addSocket(False, 'NodeSocketFloatFactor', 'HAS_Vector')
        self.addSocket(False, 'NodeSocketFloat', 'brick_width')
        self.addSocket(False, 'NodeSocketFloat', 'brick_height')
        self.addSocket(False, 'NodeSocketFloat', 'Angle')
        self.addSocket(False, 'NodeSocketFloat', 'Clamp')
        self.addSocket(True, 'NodeSocketVector', 'RotatedVector')
        #Links
        self.innerLink('nodes["GroupInput"].outputs[1]', 'nodes["Node1"].inputs[0]')
        self.innerLink('nodes["Node0"].outputs[3]', 'nodes["Node1"].inputs[1]')
        self.innerLink('nodes["GroupInput"].outputs[0]', 'nodes["Node1"].inputs[2]')
        self.innerLink('nodes["GroupInput"].outputs[2]', 'nodes["Node12"].inputs[0]')
        self.innerLink('nodes["Node3"].outputs[0]', 'nodes["Node12"].inputs[1]')
        self.innerLink('nodes["GroupInput"].outputs[3]', 'nodes["Node13"].inputs[0]')
        self.innerLink('nodes["Node3"].outputs[0]', 'nodes["Node13"].inputs[1]')
        self.innerLink('nodes["Node6"].outputs[0]', 'nodes["Node14"].inputs[0]')
        self.innerLink('nodes["Node7"].outputs[0]', 'nodes["Node14"].inputs[1]')
        self.innerLink('nodes["GroupInput"].outputs[4]', 'nodes["Node15"].inputs[0]')
        self.innerLink('nodes["Node14"].outputs[0]', 'nodes["Node15"].inputs[1]')
        self.innerLink('nodes["Node15"].outputs[0]', 'nodes["Node16"].inputs[0]')
        self.innerLink('nodes["Node6"].outputs[0]', 'nodes["Node17"].inputs[0]')
        self.innerLink('nodes["Node7"].outputs[0]', 'nodes["Node17"].inputs[1]')
        self.innerLink('nodes["GroupInput"].outputs[4]', 'nodes["Node18"].inputs[0]')
        self.innerLink('nodes["Node17"].outputs[0]', 'nodes["Node18"].inputs[1]')
        self.innerLink('nodes["Node18"].outputs[0]', 'nodes["Node19"].inputs[0]')
        self.innerLink('nodes["Node1"].outputs[0]', 'nodes["Node20"].inputs[0]')
        self.innerLink('nodes["Node20"].outputs[0]', 'nodes["Node21"].inputs[0]')
        self.innerLink('nodes["Node12"].outputs[0]', 'nodes["Node21"].inputs[1]')
        self.innerLink('nodes["Node1"].outputs[0]', 'nodes["Node22"].inputs[0]')
        self.innerLink('nodes["Node22"].outputs[1]', 'nodes["Node23"].inputs[0]')
        self.innerLink('nodes["Node13"].outputs[0]', 'nodes["Node23"].inputs[1]')
        self.innerLink('nodes["Node21"].outputs[0]', 'nodes["Node24"].inputs[0]')
        self.innerLink('nodes["Node19"].outputs[0]', 'nodes["Node24"].inputs[1]')
        self.innerLink('nodes["Node23"].outputs[0]', 'nodes["Node25"].inputs[0]')
        self.innerLink('nodes["Node16"].outputs[0]', 'nodes["Node25"].inputs[1]')
        self.innerLink('nodes["Node24"].outputs[0]', 'nodes["Node26"].inputs[0]')
        self.innerLink('nodes["Node25"].outputs[0]', 'nodes["Node26"].inputs[1]')
        self.innerLink('nodes["Node21"].outputs[0]', 'nodes["Node27"].inputs[0]')
        self.innerLink('nodes["Node16"].outputs[0]', 'nodes["Node27"].inputs[1]')
        self.innerLink('nodes["Node23"].outputs[0]', 'nodes["Node28"].inputs[0]')
        self.innerLink('nodes["Node19"].outputs[0]', 'nodes["Node28"].inputs[1]')
        self.innerLink('nodes["Node27"].outputs[0]', 'nodes["Node29"].inputs[0]')
        self.innerLink('nodes["Node28"].outputs[0]', 'nodes["Node29"].inputs[1]')
        self.innerLink('nodes["Node26"].outputs[0]', 'nodes["Node30"].inputs[0]')
        self.innerLink('nodes["Node12"].outputs[0]', 'nodes["Node30"].inputs[1]')
        self.innerLink('nodes["Node29"].outputs[0]', 'nodes["Node31"].inputs[0]')
        self.innerLink('nodes["Node13"].outputs[0]', 'nodes["Node31"].inputs[1]')
        self.innerLink('nodes["GroupInput"].outputs[5]', 'nodes["Node32"].inputs[0]')
        self.innerLink('nodes["Node8"].outputs[0]', 'nodes["Node32"].inputs[1]')
        self.innerLink('nodes["Node12"].outputs[0]', 'nodes["Node33"].inputs[0]')
        self.innerLink('nodes["Node3"].outputs[0]', 'nodes["Node33"].inputs[1]')
        self.innerLink('nodes["Node30"].outputs[0]', 'nodes["Node34"].inputs[0]')
        self.innerLink('nodes["Node33"].outputs[0]', 'nodes["Node34"].inputs[1]')
        self.innerLink('nodes["Node34"].outputs[0]', 'nodes["Node35"].inputs[0]')
        self.innerLink('nodes["Node10"].outputs[0]', 'nodes["Node35"].inputs[1]')
        self.innerLink('nodes["Node13"].outputs[0]', 'nodes["Node36"].inputs[0]')
        self.innerLink('nodes["Node3"].outputs[0]', 'nodes["Node36"].inputs[1]')
        self.innerLink('nodes["Node31"].outputs[0]', 'nodes["Node37"].inputs[0]')
        self.innerLink('nodes["Node36"].outputs[0]', 'nodes["Node37"].inputs[1]')
        self.innerLink('nodes["Node37"].outputs[0]', 'nodes["Node38"].inputs[0]')
        self.innerLink('nodes["Node10"].outputs[0]', 'nodes["Node38"].inputs[1]')
        self.innerLink('nodes["Node35"].outputs[0]', 'nodes["Node39"].inputs[0]')
        self.innerLink('nodes["Node38"].outputs[0]', 'nodes["Node39"].inputs[1]')
        self.innerLink('nodes["Node10"].outputs[0]', 'nodes["Node39"].inputs[2]')
        self.innerLink('nodes["Node30"].outputs[0]', 'nodes["Node40"].inputs[0]')
        self.innerLink('nodes["Node31"].outputs[0]', 'nodes["Node40"].inputs[1]')
        self.innerLink('nodes["Node10"].outputs[0]', 'nodes["Node40"].inputs[2]')
        self.innerLink('nodes["Node32"].outputs[0]', 'nodes["Node41"].inputs[0]')
        self.innerLink('nodes["Node40"].outputs[0]', 'nodes["Node41"].inputs[1]')
        self.innerLink('nodes["Node39"].outputs[0]', 'nodes["Node41"].inputs[2]')
        self.innerLink('nodes["Node41"].outputs[0]', 'nodes["GroupOutput"].inputs[0]')
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
 
 
 
