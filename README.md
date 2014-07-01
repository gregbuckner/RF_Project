RF_Project
==========

Robot Framework Project Creation

When working with Robot Framework some people like to create their projects using Robot Integrated Development Environment (RIDE) https://code.google.com/p/robotframework-ride/

I like to create my projects in a text editor by creating all the files I need to work with. create_rf_proj automatically creates a Robot Framework project for you and create the necessary files from the command line.

Ex; $> python create_rf_proj.py my_test_proj

The above command will create a directory named My_test_proj and populate it with the following templated files:
__init__.txt  my_test_proj_resources.txt   my_test_proj_variables.py   my_test_proj_library.py


The file templates will have the style below:
'########################################################################### 
'#                                                                         # 
'#                                                                         #  
'# This is the resources file for the My_test_proj Robot Framework project # 
'#                                                                         # 
'#                                                                         # 
'###########################################################################
