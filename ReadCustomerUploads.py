__author__ = 'ykogan'

import csv


#table fields w/o temp_vector preceded by upload_date
UPLOAD_ID           = 0
VC_ENTITY_ID        = 2
UPTIME              = 3

MODEL_NAME = 12


def read_entities(column_num):
    # temp_vector fields
    CUSTOMER_ID = 2
    UPLOAD_DATE = 3

    virtual_machines = dict()
    titles = []

    file = open("/Users/ykogan/Desktop/encFolders/combined/itfm_host_details.csv")
    for line in file:
        tuple = line.split(sep=",")
        id_col = tuple[UPLOAD_ID].split(sep="_")
        if (len(id_col) > 3): # this is not the header row
            tuple[0] = id_col[UPLOAD_DATE] # replace the first temp_vector field with upload date
            customer_id = id_col[CUSTOMER_ID]
            tuple[1] = customer_id
            entity_id = tuple[VC_ENTITY_ID]
            vc_id = tuple[VC_ENTITY_ID]

            vm_id = customer_id + "_" + vc_id + '_' + entity_id
            if ((vm_id in virtual_machines)):
                 if (id_col[UPLOAD_DATE] < virtual_machines[vm_id][0]):
                        continue
            virtual_machines[vm_id] = tuple
        else:
            titles = tuple
    file.close()

    result = []

    for vm_id in virtual_machines:
        result = result + [virtual_machines[vm_id][column_num]]

    return result


def read_server_models():
    return read_entities(MODEL_NAME)
