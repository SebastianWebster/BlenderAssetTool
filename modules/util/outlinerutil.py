import bpy

class OutlinerUtil:

    @staticmethod
    def createchildCol(parentName,childName):
        bpy.ops.collection.create(name = childName)
        bpy.data.collections[parentName].children.link(bpy.data.collections[childName])

    @staticmethod
    #Expecting str and list(str) for *children
    def create_collection_to_parent(parent_id,*children):
        for child in children:
            if isinstance(child, str):
                OutlinerUtil.createchildCol(parent_id,child)
            else:
                for setChild in child:
                    OutlinerUtil.createchildCol(parent_id,setChild)
    
    