import bpy

from ..globaldata_util import GlobalDataHandler


class OutlinerUtil:

    @staticmethod
    # Returns an alias for an object type, will probably make this user defined
    def get_type_alias(item_type):
        item_alias_defs = {"COLLECTION":"","OBJECT":"_OBJ","MATERIAL":"_MAT"}
        return item_alias_defs[item_type]

    @staticmethod
    def link_collection_parent(child_id,**options):
        if 'parent' in options:
            print("Linking collection " + child_id +
                  " to parent : " + options['parent'])
            bpy.data.collections[options['parent']].children.link(
                bpy.data.collections[child_id])
        else:
            bpy.context.scene.collection.children.link(
                bpy.data.collections[child_id])


    @staticmethod
    #Kwargs for <str>name,<str>parentid,<str>type,<itr>Children
    def add_new_collection(context,type_id,**kwargs):
        #Ensures there are no selected objects, which would cook up the system
        bpy.ops.object.select_all(action='DESELECT')
        
        project_data = GlobalDataHandler.open_data(context)
        collection_name = "new_collection"
        postfix = OutlinerUtil.get_type_alias(type_id)
        global_listmapping = GlobalDataHandler.typeid_to_globalmapping(type_id)
        if "name" in kwargs:
            collection_name = kwargs["name"]
        # If no unique ID specified generate one via checking the global lists of materials,collections and objects
        else:
            collection_name = type_id + "_" +str(len(project_data[global_listmapping]))

        # Create the Collection and assign parent if there is one
        bpy.ops.collection.create(name=collection_name)
        if "parent" in kwargs:
            OutlinerUtil.link_collection_parent(collection_name,parent = kwargs["parent"])
        else:
            OutlinerUtil.link_collection_parent(collection_name)

        #Iterate over children and assign this collection as parent
        if "children" in kwargs:
            for child in kwargs["children"]:
                OutlinerUtil.add_new_collection(collection_name + "_" + project_data["OBJ_SUB_COLLECTIONS"], parent=collection_name)
        
        #UpdateLists and actives here
        GlobalDataHandler.add_to_global_list(context,global_listmapping,[collection_name])