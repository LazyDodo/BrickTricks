import bpy
class ShaderNodebrick_rounded_corner(bpy.types.ShaderNodeCustomGroup):
    bl_name='ShaderNodebrick_rounded_corner'
    bl_label='brick_rounded_corner'
    bl_icon='NONE'

    def init(self, context):
        self.getNodetree(self.name + '_node_tree')
        self.inputs['Vector'].default_value=[0,0,0]
        self.inputs['HAS_Vector'].default_value=0
        self.inputs['HAS_Vector'].hide=True
        self.inputs['brick_width'].default_value=1
        self.inputs['brick_height'].default_value=1
        self.inputs['border'].default_value=0.0099999998
        self.inputs['feather'].default_value=0.1
        self.inputs['cornerRadius'].default_value=0.050000001

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
        self.addNode('ShaderNodeValue', { 'name':'Node4' ,'outputs[0].default_value':0  })
        self.addNode('ShaderNodeValue', { 'name':'Node6' ,'outputs[0].default_value':9.9999997e-06  })
        self.addNode('ShaderNodeValue', { 'name':'Node7' ,'outputs[0].default_value':2  })
        self.addNode('ShaderNodeValue', { 'name':'Node8' ,'outputs[0].default_value':0  })
        self.addNode('ShaderNodeSeparateXYZ', { 'name':'Node9'  })
        self.addNode('ShaderNodeMath', { 'name':'Node10' ,'operation':'MODULO' })
        self.addNode('ShaderNodeMath', { 'name':'Node11' ,'inputs[1].default_value':0.5 ,'operation':'ABSOLUTE' })
        self.addNode('ShaderNodeSeparateXYZ', { 'name':'Node12'  })
        self.addNode('ShaderNodeMath', { 'name':'Node13' ,'operation':'MODULO' })
        self.addNode('ShaderNodeMath', { 'name':'Node14' ,'inputs[1].default_value':0.5 ,'operation':'ABSOLUTE' })
        self.addNode('ShaderNodeMath', { 'name':'Node15' ,'operation':'MAXIMUM' })
        self.addNode('ShaderNodeMath', { 'name':'Node16' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node17' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node18' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node19' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node20' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node21' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node22' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node23' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node24' ,'inputs[1].default_value':0.5 ,'operation':'ABSOLUTE' })
        self.addNode('ShaderNodeMath', { 'name':'Node25' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node26' ,'operation':'MAXIMUM' })
        self.addNode('ShaderNodeMath', { 'name':'Node27' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node28' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node29' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node30' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node31' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node32' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node33' ,'operation':'DIVIDE' })
        self.addNode('ShaderNodeMath', { 'name':'Node34' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node35' ,'inputs[1].default_value':0.5 ,'operation':'ABSOLUTE' })
        self.addNode('ShaderNodeMath', { 'name':'Node36' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node37' ,'operation':'MAXIMUM' })
        self.addNode('ShaderNodeMath', { 'name':'Node38' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node39' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node40' ,'operation':'ADD' })
        self.addNode('ShaderNodeMath', { 'name':'Node41' ,'inputs[1].default_value':0.5 ,'operation':'POWER' })
        self.addNode('ShaderNodeMath', { 'name':'Node42' ,'inputs[1].default_value':-1 ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node43' ,'operation':'ADD' })
        self.addNode('ShaderNodeMath', { 'name':'Node44' ,'operation':'GREATER_THAN' })
        self.addNode('ShaderNodeMath', { 'name':'Node45' ,'operation':'MULTIPLY' })
        self.addNode('ShaderNodeMath', { 'name':'Node46' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node47' ,'operation':'SUBTRACT' })
        self.addNode('ShaderNodeMath', { 'name':'Node48' ,'operation':'DIVIDE','use_clamp':1  })
        #Sockets
        self.addSocket(False, 'NodeSocketVector', 'Vector')
        self.addSocket(False, 'NodeSocketFloat', 'HAS_Vector')
        self.addSocket(False, 'NodeSocketFloat', 'brick_width')
        self.addSocket(False, 'NodeSocketFloat', 'brick_height')
        self.addSocket(False, 'NodeSocketFloat', 'border')
        self.addSocket(False, 'NodeSocketFloat', 'feather')
        self.addSocket(False, 'NodeSocketFloat', 'cornerRadius')
        self.addSocket(True, 'NodeSocketFloat', 'Height')
        self.addSocket(True, 'NodeSocketFloat', 'Mask')
        #Links
        self.innerLink('nodes["GroupInput"].outputs[1]', 'nodes["Node1"].inputs[0]')
        self.innerLink('nodes["Node0"].outputs[3]', 'nodes["Node1"].inputs[1]')
        self.innerLink('nodes["GroupInput"].outputs[0]', 'nodes["Node1"].inputs[2]')
        self.innerLink('nodes["Node1"].outputs[0]', 'nodes["Node9"].inputs[0]')
        self.innerLink('nodes["Node9"].outputs[0]', 'nodes["Node10"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[2]', 'nodes["Node10"].inputs[1]')
        self.innerLink('nodes["Node10"].outputs[0]', 'nodes["Node11"].inputs[0]')
        self.innerLink('nodes["Node1"].outputs[0]', 'nodes["Node12"].inputs[0]')
        self.innerLink('nodes["Node12"].outputs[1]', 'nodes["Node13"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[3]', 'nodes["Node13"].inputs[1]')
        self.innerLink('nodes["Node13"].outputs[0]', 'nodes["Node14"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[6]', 'nodes["Node15"].inputs[0]')
        self.innerLink('nodes["Node6"].outputs[0]', 'nodes["Node15"].inputs[1]')
        self.innerLink('nodes["GroupInput"].outputs[2]', 'nodes["Node16"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[4]', 'nodes["Node16"].inputs[1]')
        self.innerLink('nodes["Node16"].outputs[0]', 'nodes["Node17"].inputs[0]')
        self.innerLink('nodes["Node7"].outputs[0]', 'nodes["Node17"].inputs[1]')
        self.innerLink('nodes["Node15"].outputs[0]', 'nodes["Node18"].inputs[0]')
        self.innerLink('nodes["Node7"].outputs[0]', 'nodes["Node18"].inputs[1]')
        self.innerLink('nodes["Node16"].outputs[0]', 'nodes["Node19"].inputs[0]')
        self.innerLink('nodes["Node18"].outputs[0]', 'nodes["Node19"].inputs[1]')
        self.innerLink('nodes["Node19"].outputs[0]', 'nodes["Node20"].inputs[0]')
        self.innerLink('nodes["Node7"].outputs[0]', 'nodes["Node20"].inputs[1]')
        self.innerLink('nodes["Node11"].outputs[0]', 'nodes["Node21"].inputs[0]')
        self.innerLink('nodes["Node17"].outputs[0]', 'nodes["Node21"].inputs[1]')
        self.innerLink('nodes["GroupInput"].outputs[4]', 'nodes["Node22"].inputs[0]')
        self.innerLink('nodes["Node7"].outputs[0]', 'nodes["Node22"].inputs[1]')
        self.innerLink('nodes["Node21"].outputs[0]', 'nodes["Node23"].inputs[0]')
        self.innerLink('nodes["Node22"].outputs[0]', 'nodes["Node23"].inputs[1]')
        self.innerLink('nodes["Node23"].outputs[0]', 'nodes["Node24"].inputs[0]')
        self.innerLink('nodes["Node24"].outputs[0]', 'nodes["Node25"].inputs[0]')
        self.innerLink('nodes["Node20"].outputs[0]', 'nodes["Node25"].inputs[1]')
        self.innerLink('nodes["Node25"].outputs[0]', 'nodes["Node26"].inputs[0]')
        self.innerLink('nodes["Node8"].outputs[0]', 'nodes["Node26"].inputs[1]')
        self.innerLink('nodes["GroupInput"].outputs[3]', 'nodes["Node27"].inputs[0]')
        self.innerLink('nodes["GroupInput"].outputs[4]', 'nodes["Node27"].inputs[1]')
        self.innerLink('nodes["Node27"].outputs[0]', 'nodes["Node28"].inputs[0]')
        self.innerLink('nodes["Node7"].outputs[0]', 'nodes["Node28"].inputs[1]')
        self.innerLink('nodes["Node15"].outputs[0]', 'nodes["Node29"].inputs[0]')
        self.innerLink('nodes["Node7"].outputs[0]', 'nodes["Node29"].inputs[1]')
        self.innerLink('nodes["Node27"].outputs[0]', 'nodes["Node30"].inputs[0]')
        self.innerLink('nodes["Node29"].outputs[0]', 'nodes["Node30"].inputs[1]')
        self.innerLink('nodes["Node30"].outputs[0]', 'nodes["Node31"].inputs[0]')
        self.innerLink('nodes["Node7"].outputs[0]', 'nodes["Node31"].inputs[1]')
        self.innerLink('nodes["Node14"].outputs[0]', 'nodes["Node32"].inputs[0]')
        self.innerLink('nodes["Node28"].outputs[0]', 'nodes["Node32"].inputs[1]')
        self.innerLink('nodes["GroupInput"].outputs[4]', 'nodes["Node33"].inputs[0]')
        self.innerLink('nodes["Node7"].outputs[0]', 'nodes["Node33"].inputs[1]')
        self.innerLink('nodes["Node32"].outputs[0]', 'nodes["Node34"].inputs[0]')
        self.innerLink('nodes["Node33"].outputs[0]', 'nodes["Node34"].inputs[1]')
        self.innerLink('nodes["Node34"].outputs[0]', 'nodes["Node35"].inputs[0]')
        self.innerLink('nodes["Node35"].outputs[0]', 'nodes["Node36"].inputs[0]')
        self.innerLink('nodes["Node31"].outputs[0]', 'nodes["Node36"].inputs[1]')
        self.innerLink('nodes["Node36"].outputs[0]', 'nodes["Node37"].inputs[0]')
        self.innerLink('nodes["Node8"].outputs[0]', 'nodes["Node37"].inputs[1]')
        self.innerLink('nodes["Node26"].outputs[0]', 'nodes["Node38"].inputs[0]')
        self.innerLink('nodes["Node26"].outputs[0]', 'nodes["Node38"].inputs[1]')
        self.innerLink('nodes["Node37"].outputs[0]', 'nodes["Node39"].inputs[0]')
        self.innerLink('nodes["Node37"].outputs[0]', 'nodes["Node39"].inputs[1]')
        self.innerLink('nodes["Node38"].outputs[0]', 'nodes["Node40"].inputs[0]')
        self.innerLink('nodes["Node39"].outputs[0]', 'nodes["Node40"].inputs[1]')
        self.innerLink('nodes["Node40"].outputs[0]', 'nodes["Node41"].inputs[0]')
        self.innerLink('nodes["Node41"].outputs[0]', 'nodes["Node42"].inputs[0]')
        self.innerLink('nodes["Node42"].outputs[0]', 'nodes["Node43"].inputs[0]')
        self.innerLink('nodes["Node15"].outputs[0]', 'nodes["Node43"].inputs[1]')
        self.innerLink('nodes["Node43"].outputs[0]', 'nodes["Node44"].inputs[0]')
        self.innerLink('nodes["Node4"].outputs[0]', 'nodes["Node44"].inputs[1]')
        self.innerLink('nodes["GroupInput"].outputs[5]', 'nodes["Node45"].inputs[0]')
        self.innerLink('nodes["Node15"].outputs[0]', 'nodes["Node45"].inputs[1]')
        self.innerLink('nodes["Node43"].outputs[0]', 'nodes["Node46"].inputs[0]')
        self.innerLink('nodes["Node8"].outputs[0]', 'nodes["Node46"].inputs[1]')
        self.innerLink('nodes["Node45"].outputs[0]', 'nodes["Node47"].inputs[0]')
        self.innerLink('nodes["Node8"].outputs[0]', 'nodes["Node47"].inputs[1]')
        self.innerLink('nodes["Node46"].outputs[0]', 'nodes["Node48"].inputs[0]')
        self.innerLink('nodes["Node47"].outputs[0]', 'nodes["Node48"].inputs[1]')
        self.innerLink('nodes["Node48"].outputs[0]', 'nodes["GroupOutput"].inputs[0]')
        self.innerLink('nodes["Node44"].outputs[0]', 'nodes["GroupOutput"].inputs[1]')
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
 
 
 
