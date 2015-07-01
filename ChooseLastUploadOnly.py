__author__ = 'ykogan'


import csv


#table fields w/o temp_vector preceded by upload_date
UPLOAD_ID           = 0
VC_ENTITY_ID        = 2
UPTIME              = 3
OS_GENERIC_TYPE     = 4
MEMORY_SIZE_GB      = 6
NUMBER_OF_CORES     = 7
SAN_SIZE_GB         = 8
NAS_SIZE_GB         = 9
NUM_OF_REQUESTS     = 10
NUM_OF_IOPS         = 11
NUMBER_OF_VCPUS     = 12
VC_ID               = 15
RES_CPU_RATE_GHZ    = 19
RES_MEMORY_SIZE_GB  = 20
FAULT_TOLERANT      = 21


def load_data_vector():
    # temp_vector fields
    CUSTOMER_ID = 2
    UPLOAD_DATE = 3

    virtual_machines = dict()
    titles = []

    file = open("/Users/ykogan/Desktop/encFolders/combined/itfm_vm_configuration.csv")
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

    with open('/Users/ykogan/Desktop/encFolders/combined/itfm_vm_configuration_new.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(titles)

        for vm_id in virtual_machines:
            writer.writerow(virtual_machines[vm_id])

    csvfile.close()
    return


Z = load_data_vector()
