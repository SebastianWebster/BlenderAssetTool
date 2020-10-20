import bpy

from ..globaldata_util import GlobalDataHandler


class OutlinerUtil:

    @staticmethod
    # Given a collection name, potential parent and potential children
    def add_collection(collection_name, **options):
        bpy.ops.collection.create(name=collection_name)
        # If there is a parent Assign else assign to scene collection
        if 'parent' in options:
            print("Linking collection " + collection_name +
                  " to parent : " + options['parent'])
            bpy.data.collections[options['parent']].children.link(
                bpy.data.collections[collection_name])
        else:
            bpy.context.scene.collection.children.link(
                bpy.data.collections[collection_name])

    # Adds a new primitive to a defined collection
    def add_new_primitive():
        pass

    @staticmethod
    # Check for Kwarg that defines a primitve to populate the lowPoly and if object has a name
    def add_new_obj(context, project_name, **kwargs):
        # Check if a name was priveded for the object
        project_data = GlobalDataHandler.open_data(context)
        counter = project_data["UNIQUE_OBJ_COUNT"]
        sub_collections = project_data["OBJ_SUB_COLLECTIONS"]

        obj_name = ""
        if "obj_name" in kwargs:
            obj_name = kwargs["obj_name"]
        else:
            objname = "OBJ" + str(counter)

        if "prim_type" in kwargs:
            pass

        counter += 1
        # Link to parentScene
        OutlinerUtil.add_collection(objname, parent=project_name)
        # Add Child Collections
        for definintion in sub_collections:
            OutlinerUtil.add_collection(objname + "_" + definintion, parent=objname)
            #Add objects here if any

        GlobalDataHandler.update_data(context, "UNIQUE_OBJ_COUNT", counter)
