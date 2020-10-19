import bpy
class OutlinerUtil:

    @staticmethod
    # Given a collection name, potential parent and potential children
    def add_collection(collection_name,**options):
        bpy.ops.collection.create(name=collection_name)
        #If there is a parent Assign else assign to scene collection
        if 'parent' in options:
            print("Linking collection " + collection_name + " to parent : " + options['parent'])
            bpy.data.collections[options['parent']].children.link(bpy.data.collections[collection_name])
        else:
            bpy.context.scene.collection.children.link(bpy.data.collections[collection_name])