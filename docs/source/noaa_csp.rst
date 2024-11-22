.. role:: red-text

########################################
Configuring NOAA Cloud Service Providers
########################################

The NOAA Cloud Service Providers (CSP) support the forecast-only,
coupled, and GEFS configurations for the global workflow.
Once a suitable CSP instance and cluster is defined/created,
the global-workflow may be executed similarly to the on-prem machines.
Currently the global-workflow supports the following
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
screen as in Figure 1. Click the "blue" box indicated by the red arrow to login.

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_login_1.png
   :name: noaacsp_login_1
   :class: with-border
   :align: center

   Figure 1 NOAA-PARALLElWORKS Home Page

As shown in Figure 2, Fill the ``Username / Email`` box with your username or NOAA email (usually in "FirstName.LastName" format).
Note that the ``Username or email`` query field is case-sensitive.
Then enter the respective ``Pin + RSA`` combination using the same RSA token application used
for access to other RDHPCS machines (e.g., Hera, Gaea).

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_login_2.png
   :name: noaacsp_login_2
   :class: with-border
   :align: center

   Figure 2 NOASS-PARALLELWORKS Login Page

*******************************
Configure the NOAA CSP Instance
*******************************

Once logged into the NOAA CSP, navigate to the ``Marketplace`` section
in the left sidebar as indicated by the red arrow in Figure 3, and click.
Scroll down to selecet "AWS EPIC Wei CentOS" circled in red.
Note that the current global-workflow is still using CentOS built spack-stack,
but it will be updated to Rocky 8 soon.

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_instance_1.png
   :name: noaacsp_instance_1
   :class: with-border
   :align: center

   Figure 3 ParallWork Marketplace

Next, click "Fork latest" as shown in the red-circle in Figure 4.

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_instance_2.png
   :name: noaacsp_instance_2
   :class: with-border
   :align: center

   Figure 4 Fork Instance From Marketplace
   
Please provide a unique name in the "New compute node" field for the instance
(see the box pointer by the red arrow in Figure 5).
Best practices suggest one that is clear, concise, and relevant to the application.
Click ``Fork`` (in the red-circle) to fork an instance.

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_instance_3.png
   :name: noaacsp_instance_3
   :class: with-border
   :align: center

   Figure 5 Create the Fork

Now, an instance is forked, and it is time to configure the cluster. Fellow these steps as shown in Figure 6:

#. Select a "Resource Account"; usually it is *NOAA AWS Commercial Vault*.
#. Select a "Group", which will be something like: ca-epic, ca-sfs-emc, etc.
#. Copy and paste your public key (e.g., *.ssh/id_rsa.pub*, *.ssh/id_dsa.pu* from your laptop).
#. Modify "User Bootstrap". If you are not using the "ca-epic" group, please UNCOMMENT line 2.
#. Keep "Health Check" as it is.

Click "Save Changes" at top-right as shown in red circle.

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_instance_4.png
   :name: noaacsp_instance_4
   :class: with-border
   :align: center

   Figure 6 Save the Instance

The NOAA ParallelWorks (PW) currently provides 3 CSPs:
**AWS** (Amazon Web Services), **Azure** (Microsoft Azure),
and **GCP** (Google Cloud Platform).
Existing clusters may also be modified.
However, it is best practice to fork from Marketplace with something similar to your requests
(rather than modifying an existing cluster).

******************************
Add CSP Lustre Filesystem
******************************

To run global-workflow on CSPs, we need to attach the ``/lustre`` filesystem as run directory.
First, we need to add/define our ``/lustre`` filesystem.
To do so, navigate to the middle of the NOAA PW website left side panel and select "Lustre"
(see the red arrow in Figure 7), and then click "Add Storage"
at the top right as shown in the red-circle.

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_lustre_1.png
   :name: noaacsp_lustre_1
   :class: with-border
   :align: center

   Figure 7 Add Lustre Storage

Select `FSx` for the AWS FSx ``/lustre`` filesystem as shown in the red circle.

Define ``/lustre`` with steps in Figure 8:

#. A clear and meaningful `Resource name` as shown by the first red arrow
#. A short sentence for `Description`, as shown in the second red arrow
#. Choose **linux** for `Tag` as shown by red arrow #3

Click "Add Storage" as in red-box at top-right corner.

This will create a "lustre" filesystem template as in red-squre as in Figure 8.

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_lustre_2.png
   :name: noaacsp_lustre_2
   :class: with-border
   :align: center

   Figure 8 Define Lustre Attributes
	   
After creating the template, we need to fill information for this lustre filesystem.
To do so, go to the NOAA PW website, and click "Lustre" on the left side panel as
indicated by red arrow 1 as in Figure 8. Then select the filesystem defined above by `Resource name`,
as shown in the red box. Here, the user can delete this resource if not needed by
clicking the trash can (indicated by red-arrow 2).

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_lustre_3.png
   :name: noaacsp_lustre_3
   :class: with-border
   :align: center

   Figure 9 Show the Lustre in PW page

By clicking the filesystem in the red box of the image above,
users will be led to the lustre definition page.

Then follow the steps illustrated in Figure 9 as below:

#. Choose a size in the `Storage Capacity(GB)` box as pointed by red-arrow 1.
   There is a minium of 1200 by AWS. For C48 ATM/GEFS case this will be enough.
   For SFS-C96 case, or C768 ATM/S2S case it should probably increase to 12000.
#. For `File System Deployment`, choose "SCRATCH_2" for now as by red-arrow 2.
   Do not use SCRATCH_1, as it is used for test by PW.
#. Choose **NONE** for `File System Compression` as pointed by red-arrow 3.
   Only choose LZ4 if you understand what it means.
#. Leave "S3 Import Path" and "S3 Export Path" black for now.
#. Click **Save Changes** in red-circle to save the definition/(changes made).

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_lustre_4.png
   :name: noaacsp_lustre_4
   :class: with-border
   :align: center

   Figure 10 Defining the Lustre Filesystem Capacity

For the storage to be allocated for the global-workflow application,
it is suggested that the ``Mount Point`` be ``/lustre``. Once the storage
has been configured, following the steps below to attach the Lustre Filesystem.

******************************
Attach CSP Lustre Filesystem
******************************

Now we need to attach the defined filesystem to our cluster.
Go back to the NOAA PW web-site, and click `Cluster`
as shown in Figuer 11 below, then select the cluster "AWS EPIC Wei CentOS example"
(it should be your own cluster) cluster as show in the red-box.
Note, one can remove/delete this cluster if no longer needed by
clicking the trash-can shown in the red-circle at right.

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_filesystem_1.png
   :name: noaacsp_filesystem_1
   :class: with-border
   :align: center

   Figure 11 Add Attached Filesystems

When get into the cluster page we will see things as in Figure 12, click the `Definition` in the top menu as
in the red-box. Then we can attached the defined filesystems.
When finished, remeber to click `Save Changes` to save the changes.

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_filesystem_2.png
   :name: noaacsp_filesystem_2
   :class: with-border
   :align: center

   Figure 12 Add Attached /lustre and/or /bucket Filesystems

Scroll down to the bottom as show in Figure 13, and click `Add Attached Filesystems` as in the red-circle.

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_filesystem_3.png
   :name: noaacsp_filesystem_3
   :class: with-border
   :align: center

   Figure 13 Add Attached /lustre and/or /bucket Filesystems

After clicking `Add Attached Filesystems`, `Attached Filesystems settings`, following steps listed here
which also shown in Figure 14.

#. In the `Storage` box, select the lustre filesystem defined above, as in red-arrow 1.
#. In the `Mount Point` box, name it `/lustre` (the common and default choice) as pointed by red-arrow 2.
   If you choose a different name, make sure to make the Global-Workflow setup step
   use the name chosen here.

If you have a `S3 bucket`, one can attached as:

#. In the `Storage` box, select the bucket you want to use, as in red-arrow 3.
#. In the `Mount Point` box, name it `/bucket` (the common and default choice) as pointed by red-arrow 4.

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_filesystem_4.png
   :name: noaacsp_filesystem_4
   :class: with-border
   :align: center

   Figure 14 Add Attached /lustre and/or /bucket Filesystems

Always remember to click `Save Changes` after making any changes to the cluster.

**************************
Using the NOAA CSP Cluster
**************************

To activate the cluster, click `Clusters` on the left panel of the NOAA PW website shown in Figure 15,
as indicated by the red arrow. Then click the `Sessions` button in the red square, and click the power
button in the red circle. The cluster status is denoted by the color-coded button
on the right: red means stopped; orange  means requested; green means active. The amount of time required to start
the cluster varies and is not immediate; it may take several minutes (often 10-20) for the cluster to become active.

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_using_1.png
   :name: noaacsp_using_1
   :class: with-border
   :align: center

   Figure 15 Activate the Cluster

when the cluster is activate, user will see things numbered in Figure 16 and also listed below:

#. Green dot means the cluster is active, pointed by red-arrow 1.
#. Green dot means the cluster is active, pointed by red-arrow 2.
#. Green button means the cluster is active, pointed by red-arrow 3.
#. Click the blue-square with arrow inside pointed by red-arrow 4 will copy the cluster's IP into clipboard,
   which you can open a laptop xterm/window, and do `ssh username@the-ip-address` in the xterm window will connect you
   to the AWS cluster, and you can do you work there.
#. Which is the `username@the-ip-address`, or your AWS PW cluster. Click it, will have a PW web terminal appear in the
   bottom of the web-site, which you can work on this terminal to use your AWS cluster.

Please note, as soon as the cluster is activated, AWS/PW starts charging you for use the cluster.
As this cluster is exclusive for yourself, AWS keep charging you as long as the cluster is active.
For running global-workflow, one need to keep the cluster active if there is any rocoto jobs running,
as rocoto is using `crontab`, which needs the cluster active all the time, or the crontab job will be terminated.

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_using_2.png
   :name: noaacsp_using_2
   :class: with-border
   :align: center

   Figure 16 Knowing the Cluster

After finishing your work on the AWS cluster, you should terminate/stop the cluster, unless you have reasons to keep it active.
To stop/terminate the cluster, go to the cluster session, and click the `green` power button as show in Figure 17.
A window pop up, and click the red `Turn Off` button to switch off the cluster. 

.. figure:: https://raw.githubusercontent.com/wiki/NOAA-EMC/global-workflow/images/noaacsp_using_3.png
   :name: noaacsp_using_3
   :class: with-border
   :align: center

   Figure 17 Terminating the Cluster

***************************
Running the Global Workflow
***************************

Assume you have a AWS cluster running, after login to the cluster through `ssh` from your laptop terminal,
or access the cluster from your web terminal, one can start clone, compile, and run global-workflow.

#. clone global-workflow(assume you have setup access to githup):

   .. code-block:: console

      cd /contrib/$USER   #you should have a username, and have a directory at /contrib where we save our permanent files.
      git clone --recursive git@github.com:NOAA-EMC/global-workflow.git global-workflow
      #or the develop fork at EPIC:
      git clone --recursive git@github.com:NOAA-EPIC/global-workflow-cloud.git global-workflow-cloud

#. compile global-workflow:

   .. code-block:: console

      cd /contrib/$USER/global-workflow
      cd sorc
      build_all.sh   # or similar command to compile for gefs, or others.
      link_workflow.sh  # after build_all.sh finished successfully

#. As users may define a very small cluster as controller, one may use the script below to compile in compute node.
   Save the this script in a file, say, com.slurm, and submit this job with command "sbatch com.slurm":

   .. code-block:: console

      #!/bin/bash
      #SBATCH --job-name=compile
      #SBATCH --account=$USER
      #SBATCH --qos=batch
      #SBATCH --partition=compute
      #SBATCH -t 01:15:00
      #SBATCH --nodes=1
      #SBATCH -o compile.%J.log
      #SBATCH --exclusive

      gwhome=/contrib/Wei.Huang/src/global-workflow-cloud  # Change this to your own "global-workflow" source dir
      cd ${gwhome}/sorc
      source ${gwhome}/workflow/gw_setup.sh
      #build_all.sh
      build_all.sh -w
      link_workflow.sh

#. run global-workflow C48 ATM test case (assume user has /lustre filesystem attached):

   .. code-block:: console

      cd /contrib/$USER/global-workflow

      HPC_ACCOUNT=${USER} pslot=c48atm RUNTESTS=/lustre/$USER/run \
          ./workflow/create_experiment.py \
          --yaml ci/cases/pr/C48_ATM.yaml

      cd /lustre/$USER/run/EXPDIR/c48atm
      crontab c48atm

EPIC has copied the C48 and C96 ATM, GEFS and some other data to AWS, and the current code has setup to use those data.
If user wants to run own case, user needs to make changes to the IC path and others to make it work.
The execution of the global-workflow should now follow the same steps
as those for the RDHPCS on-premises hosts.
