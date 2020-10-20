import bpy
import json


class GlobalDataHandler:

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
        else:
            jsonData.update({data_key,data_val})
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


    @staticmethod
    def save_data(context,newData):
        bpy.context.scene.ASSETCREATOR_GLOBALS = json.dumps(newData)