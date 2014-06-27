# Edx Xblock for Interactive Video Paella Player version 1.0 #
This Xblock allows the use of interactive videos created with Camtasia using Paella Player.
You can easily integrate the XBlock into Edx and start to use the player.

## Installation instructions ##
In order to install the XBlock into your Edx devstack Server you need to.

## Download the XBlock from github. Place the files inside your server.
##.   Install your block::
You must replace `/path/to/your/block` with the path where you have downloaded the xblock

        $ vagrant ssh
        vagrant@precise64:~$ sudo -u edxapp /edx/bin/pip.edxapp install /path/to/your/block

##.  Enable the block

    #.  In ``edx-platform/lms/envs/common.py``, uncomment::

        # from xmodule.x_module import prefer_xmodules
        # XBLOCK_SELECT_FUNCTION = prefer_xmodules

    #.  In ``edx-platform/cms/envs/common.py``, uncomment::

        # from xmodule.x_module import prefer_xmodules
        # XBLOCK_SELECT_FUNCTION = prefer_xmodules

    #.  In ``edx-platform/cms/envs/common.py``, change::

            'ALLOW_ALL_ADVANCED_COMPONENTS': False,

        to::

            'ALLOW_ALL_ADVANCED_COMPONENTS': True,

##.  Add the block to your courses' advanced settings in Studio

    #. Log in to Studio, and open your course
    #. Settings -> Advanced Settings
    #. Change the value for the key ``"advanced_modules"`` to ``paellainteractivevideo``


##.  Add your block into your course

    #. Edit a unit
    #. Advanced -> your-block

##. Deploying your XBlock

To deploy your block to your own hosted version of edx-platform, you need to install it
into the virtualenv that the platform is running out of, and add to the list of ``ADVANCED_COMPONENT_TYPES``
in ``edx-platform/cms/djangoapps/contentstore/views/component.py``.

#. Using the XBlock in the course

.In the Studio go to:

.Add a paellainteractivevideo policy key on the advanced_modules keys

.After that, a new button called Advanced will appear in your unit edit view

.And a new option called Paella Interactive Video player. Wich will add the component with the paella demo video to the course.

.You can change the parameters of the video pressing the edit button.

.Right now you can change the title of the video in the platform and the url witch must link with a paella interactive video (url lo main XML of interactive video).
