import bpy
import json


class GlobalDataHandler:

    @staticmethod
    def typeid_to_globalmapping(type_id):
        global_list_id = {"COLLECTION":"PROJECT_COLLECTIONS","OBJECT":"PROJECT_OBJECTS","MATERIAL":"PROJECT_MATERIALS"}
        return global_list_id[type_id]

    @staticmethod
    def globalmapping_to_typeid(globalmapping):
        global_list_id = {"PROJECT_COLLECTIONS":"COLLECTION","PROJECT_OBJECTS":"OBJECT","PROJECT_MATERIALS":"MATERIAL"}
        return global_list_id[globalmapping]

    @staticmethod
    #Open data if not exist instantiate
    def open_data(context):
        print(json.loads(bpy.context.scene.ASSETCREATOR_GLOBALS))
        return json.loads(bpy.context.scene.ASSETCREATOR_GLOBALS)

    @staticmethod
    #Used for adding new dataentries
    def append_data(context,data_key,data_val):
        jsonData = GlobalDataHandler.open_data(context)
        if data_key in jsonData:
            print("DataKey of : " + data_key + " Already exists in data use UPDATE instead")
            GlobalDataHandler.update_data(context,data_key,data_val)
        else:
            jsonData.update({data_key:data_val})
            GlobalDataHandler.save_data(context,jsonData)

    @staticmethod
    #Used for updating existing data entries
    def update_data(context,data_key,data_val):
        jsonData = GlobalDataHandler.open_data(context)
        if data_key in jsonData:
            jsonData[data_key] = data_val
            GlobalDataHandler.save_data(context,jsonData)
        else:
            print("DataKey of : " + data_key + " does not exist in data use APPEND instead")
            GlobalDataHandler.append_data(context,data_key,data_val)

    @staticmethod
    def add_to_global_list(context,list_id,elements):
        object_list = GlobalDataHandler.open_data(context)[list_id]
        for e in elements:
            object_list.append(e)
        GlobalDataHandler.update_data(context,list_id,object_list)

    @staticmethod
    def get_global_list_count(context,list_id):
        return len(GlobalDataHandler.open_data(context)[list_id])

    @staticmethod
    #Increments a global data of a numerical Type
    def quick_inc(context,data_id):
        val = GlobalDataHandler.open_data(context)[data_id]
        val+=1
        GlobalDataHandler.update_data(context,data_id,val)

    @staticmethod
    def save_data(context,newData):
        bpy.context.scene.ASSETCREATOR_GLOBALS = json.dumps(newData)