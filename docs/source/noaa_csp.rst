.. role:: red-text

########################################
Configuring NOAA Cloud Service Providers
########################################

The NOAA Cloud Service Providers (CSP) support the forecast-only,
coupled, and gefs
configurations for the global workflow. Once a suitable CSP instance
and cluster is defined/created, the global workflow may be executed as
on the other platforms discussed in the previous sections. In order
successfully execute the global-workflow, a suitable CSP cluster must
be created. Currently the global-workflow supports the following
instance and storage types as a function of CSP and forecast
resolution.

.. list-table::
   :widths: auto
   :header-rows: 1
   :align: center

   * - **Cloud Service Provider**
     - **Global Workflow Resolution**
     - **Global Workflow Application**
     - **Instance Type**
     - **Partition**
     - **File System**
   * - Amazon Web Services Parallel Works
     - C48, C96, C192, C384
     - ``ATM``, ``GEFS``
     - ``c5.18xlarge (72 vCPUs, 144 GB Memory, amd64)``
     - ``compute``
     - ``/lustre``, ``/bucket``
   * - Azure Parallel Works
     - C48, C96, C192, C384
     - ``ATM``, ``GEFS``
     - ``Standard_F48s_v2 (48 vCPUs, 96 GB Memory, amd64)``
     - ``compute``
     - ``/lustre``, ``/bucket``
   * - GCP Parallel Works
     - C48, C96, C192, C384
     - ``ATM``, ``GEFS``
     - ``c3d-standard-60-lssd (60 vCPUs, 240 GB Memory, amd64)``
     - ``compute``
     - ``/lustre``, ``/bucket``

Instructions regarding configuring the respective CSP instance and
cluster follows.

*********************
Login to the NOAA CSP
*********************

Log in to the `NOAA CSP <http://noaa.parallel.works/login>`_ and into
the resources configuration. The user should arrive at the following
screen. Click the "blue" box pointed by the red arrow to login.

.. image:: _static/noaacsp_login_1.png

Fill the ``Username / Email`` box with your own usernam or NOAA-email.
Note that the ``Username or email`` query is case-sensitive.
And then the respective RSA token key using the same application used
for the other RDHPCS machines (i.e., Hera, Jet, etc.,).

.. image:: _static/noaacsp_login_2.png

*******************************
Configure the NOAA CSP Instance
*******************************

Once logged into the NOAA CSP, navigate to the :red-text:`Marketplace` section
at the left panel as pointed by the red arrow, and click.
Scrow down to selecet "AWS EPIC Wei CentOS" as in red-circle.
Note, current global-workflow still using CentOS built spack-stack.
It will be updated to Rocky 8 soon.

.. image:: _static/noaacsp_instance_1.png
   
Next, click "Forklatest" as shown in the red-circle.

.. image:: _static/noaacsp_instance_2.png
   
A unique name (box pointer by the red-arrow) for the instance.
Best practices suggest one that is clear, concise, and relevant to the application.
Click :red-text:`Fork` (in the red-circle) to fork an instance.

.. image:: _static/noaacsp_instance_3.png

Now, an instance is forked, and it is time to configure the cluster.

1. Select a "Recource Account", usually it is: NOAA AWS Commercial Vault.
2. Select a "Group". Which will be something like: ca-epic, ca-sfs-emc, etc.
3. Copy and paste you Public key (.ssh/id_rsa.pub, .ssh/id_dsa.pu from your laptop).
4. Modify "User Bootstrap". If you are not use "ca-epic" group, please UNCOMMENT line 2.
6. Keep "health Check" as it is.

Click "Save Changes" at top-right as shown in read circle.

.. image:: _static/noaacsp_instance_4.png

The NOAA ParallelWorks currently provides 3 CSPs:
**AWS** (Amazon Web Services), **Azure** (Microsoft Azure),
and **GCP** (Google Cloud Platform).
Existing clusters may also be modified.
Better practice is to fork from Marketplace with something similar to your requests.

******************************
Add CSP Lustre Filesystem
******************************

To run global-workflow on CSPs, we need to attached lustre filesystem as run directory.
Figure, we need to add/define our lustre filesystem, to do so,
navigate to the middle of noaa.parallel.works web-site left panel and select "Lutre" 
as pointed by red-arrow, and then click "AddStorage" at top-right as in the red-circle.

.. image:: _static/noaacsp_lustre_1.png

Select `FSx` for AWS FSx lustre filesystem as in red-circle.
Define the lustre with:

1. Clear and meaningfull `Resource name` as shown in red-arrow 1
2. Short sentice for `Decription` as shown in red-arrow 2
3. Choose **linux** for `Tag` as shown in red-arrow 3

Click "Add Storage" as in red-box at top-right corner.
This will create a "lustre" filesystem template.

.. image:: _static/noaacsp_luster_2.png
	   
After create the template, we need to fill information for this lustre filesystem.
To do so go to noaa.parallel.works web-site, click "Lustre" at left-panel as
indicated by red-arrow 1. Then select the filesystem as define above by `Resource name`
as shown in red-box. Here user can delete this resource if not needed by
click the trash-can as pointed by red-arrow 2.

.. image:: _static/noaacsp_luster_3.png

By click the filesystme in the red-box of the above image,
users led to the lustre definition page.

1. Choose a size in the `Storage Capacity(GB)` box as pointed by red-arrow 1.
   There is a minium of 1200 by AWS. For C48 ATM/GEFS case this will be enough.
   For SFS-C96 case, or C768 ATM/S2S case it should probably increase to 12000.
2. For `File System Deployment`, choose "SCRATCH_2" for now as by red-arrow 2.
   Do not use SCRATCH_1, as it is used for test by PW.
3. Choose **NONE** for `File System Compression` as pointed by red-arrow 3.
   Only choose LZ4 if you understand what it means.
4. Leave "S2 Import Path" and "S3 Export Path" black for now.
5. Click **Save Changes** in red-circle to save the definition/(changes made).

.. image:: _static/noaacsp_luster_4.png

For the storage do be allocated for the global-workflow application it
is suggested that the ``Mount Point`` be ``/lustre``. Once the storage
has been configured, click the ``+ Add Attached Storage`` button in
the upper-right corner. This is illustrated in the following image.

.. image:: _static/noaacsp_luster_5.png

******************************
Attach CSP Lustre Filesystem
******************************

Now we need to attach the defined filesystem to our cluster.
Go back to our noaa.parallel.works web-site, and click `Cluster`
as shown in figuer below, then select the cluster "AWS EPIC Wei CentOS example"
(it should be your own cluster) cluster as show in red-box.
Note, one can remoce/delete this cluster if no longer needed by
click the trash-can shown in the red-circle at right.

.. image:: _static/noaacsp_filesystem_1.png

**************************
Using the NOAA CSP Cluster
**************************

To activate the cluster, click the button circled in
:red-text:red. The cluster status is denoted by the color-coded button
on the right. The amount of time required to start the cluster is
variable and not immediate and may take several minutes for the
cluster to become.

.. image:: _static/noaacsp_using_1.png

For instances where a NOAA CSP cluster does not initialize, useful
output can be found beneath the ``Logs`` section beneath the
``Provision`` tab as illustrated below. Once again, when opening
issues related to the NOAA CSP cluster initialization please include
this information.

.. image:: _static/noaacsp_using_2.png

***************************
Running the Global Workflow
***************************

The global-workflow configuration currently requires that all initial
conditions, observations, and fixed-files, are staged in the
appropriate paths prior to running the global-workflow. As suggested
above, it is strongly recommended the the user configure their
respective experiments to use the ``/lustre`` file system for the
``EXPDIR`` and ``ROTDIR`` contents. The ``/contrib`` file system is
suitable for compiling and linking the workflow components required of
the global-workflow.

The software stack supporting the ``develop`` branch of the
global-workflow is provided for the user and is located beneath
``/contrib/emc_static/spack-stack``. The modules required for the
global-workflow execution may be loaded as follows.

.. code-block:: bash

   user@host:$ module unuse /opt/cray/craype/default/modulefiles
   user@host:$ module unuse /opt/cray/modulefiles
   user@host:$ module use /contrib/emc_static/spack-stack/miniconda/modulefiles/miniconda
   user@host:$ module load py39_4.12.0
   user@host:$ module load rocoto/1.3.3

The execution of the global-workflow should now follow the same steps
as those for the RDHPCS on-premise hosts.


