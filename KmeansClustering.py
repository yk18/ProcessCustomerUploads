__author__ = 'ykogan'
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

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
RES_CPU_RATE_GHZ    = 19
RES_MEMORY_SIZE_GB  = 20
FAULT_TOLERANT      = 21

column_names = dict()
column_names[UPLOAD_ID] = 'Upload ID'
column_names[VC_ENTITY_ID] = 'VC Entity ID'
column_names[UPTIME] = 'Uptime'
column_names[OS_GENERIC_TYPE] = 'OS Generic Type'
column_names[MEMORY_SIZE_GB] = 'Memory Size (GB)'
column_names[NUMBER_OF_CORES] = 'Number of Cores'
column_names[SAN_SIZE_GB] = 'SAN Size GB'
column_names[NAS_SIZE_GB] = 'NAS Size GB'
column_names[NUM_OF_REQUESTS] = 'Number of Requests'
column_names[NUM_OF_IOPS] = 'Number of IOPS'
column_names[NUMBER_OF_VCPUS] = 'Number of VCPUs'
column_names[RES_CPU_RATE_GHZ] = 'Res CPU Rate (GHZ)'
column_names[RES_MEMORY_SIZE_GB] = 'Res Memory (GB)'
column_names[FAULT_TOLERANT] = 'Fault Tolerant'


def cluster_and_plot(Z, x_axis_title, y_axis_title, is_log):
    n_clusters = 3
    ##############################################################################
    # Compute clustering with Means

    k_means = KMeans(init='k-means++', n_clusters=n_clusters, n_init=10)
    k_means.fit(Z)
    k_means_labels = k_means.labels_
    k_means_cluster_centers = k_means.cluster_centers_
    k_means_labels_unique = np.unique(k_means_labels)


    ##############################################################################
    # Plot result

    fig = plt.figure(figsize=(8, 8))
    plt.clf()

    colors = ['#4EACC5', '#FF9C34', '#4E9A06']
    #colors = ['#000000', '#00FF00', '#0000FF', '#4EACC5', '#FF9C34', '#4E9A06']

    if (is_log):
        plt.yscale('log')
        plt.xscale('log')

    plt.ylabel(y_axis_title)
    plt.xlabel(x_axis_title)
    plt.title(x_axis_title +' vs ' + y_axis_title + ': for %d VMs' % (len(Z)))



    for k, col in zip(range(n_clusters), colors):
        my_members = k_means_labels == k
        cluster_center = k_means_cluster_centers[k]

        plt.plot(Z[my_members, 0], Z[my_members, 1], 'w',
                markerfacecolor=col, marker='.')

        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                markeredgecolor='k', markersize=6)


    plt.show()
    return



def load_data_vector(x_axis_field, y_axis_field):
    # temp_vector fields
    CUSTOMER_ID = 2
    UPLOAD_DATE = 3

    customers = dict()

    file = open("/Users/ykogan/Desktop/encFolders/combined/itfm_vm_configuration.csv")
    for line in file:
        tuple = line.split(sep=",")
        id_col = tuple[UPLOAD_ID].split(sep="_")
        if (len(id_col) > 3): # this is not the header row
            tuple[0] = id_col[UPLOAD_DATE] # replace the first temp_vector field with upload date
            if ((id_col[CUSTOMER_ID] in customers)):
                if (tuple[VC_ENTITY_ID] in customers[id_col[CUSTOMER_ID]]):
                    # if this date is older than existing
                    if (id_col[UPLOAD_DATE] < customers[id_col[CUSTOMER_ID]][tuple[VC_ENTITY_ID]][0]):
                        continue
            else: # add a new customer
                customers[id_col[CUSTOMER_ID]] = dict() # add the vm to the customer array
            customers[id_col[CUSTOMER_ID]][tuple[VC_ENTITY_ID]] = tuple
    file.close()

    X = []
    Y = []
    Z = np.ndarray(shape=(0,2), dtype=float)

    for customer in customers:
        for machine in customers[customer]:
            y_field = customers[customer][machine][y_axis_field]
            x_field = customers[customer][machine][x_axis_field]
            if (float(y_field) > 0 and float(x_field) > 0):
                X = X + [x_field]
                Y = Y + [y_field]
                Z = np.append(Z, [[float(x_field), float(y_field)]])

    Z.shape = (len(Z)/2,2)
    return Z


Y_AXIS_FIELD = MEMORY_SIZE_GB
X_AXIS_FIELD = NUMBER_OF_VCPUS
Y_AXIS_TITLE = column_names[Y_AXIS_FIELD]
X_AXIS_TITLE = column_names[X_AXIS_FIELD]

Z = load_data_vector(X_AXIS_FIELD, Y_AXIS_FIELD)
cluster_and_plot(Z, X_AXIS_TITLE, Y_AXIS_TITLE, is_log=True)