import sys
import os
import string

def create_rf_proj():
  working_directory = os.popen('pwd').readline()
  make_proj_dir = 'mkdir ' + sys.argv[1].capitalize()  
  if os.path.isdir(sys.argv[1].capitalize()):
    print 'Project %s already exists. \nExiting...' % sys.argv[1].capitalize() 
    sys.exit()
  else:
    os.system(make_proj_dir)
  resource_file = sys.argv[1] + '/'+ sys.argv[1] + '_resources.txt'
  variable_file = sys.argv[1] + '/'+ sys.argv[1] + '_variables.py'
  library_file =  sys.argv[1] + '/'+ sys.argv[1] + '_library.py'
  init_file = sys.argv[1] + '/' + '__init__.txt'
  make_files = "touch" + " " +  resource_file + " " + variable_file + " " + library_file + " " + init_file
  os.system(make_files) 
  annotate_resource_file = open(resource_file, 'w')
  annotate_resource_file.write(resource_file_template())
  annotate_resource_file.close()
  annotate_variablefile = open(variable_file, 'w')
  annotate_variablefile.write(variable_file_template())
  annotate_variablefile.close()
  annotate_libraryfile = open(library_file, 'w')
  annotate_libraryfile.write(library_file_template())
  annotate_libraryfile.close()
  annotate_initfile = open(init_file, 'w')
  annotate_initfile.write(init_file_template())
  annotate_initfile.close()
  print '\033[32mProject %s created in directory %s \033[0m' % (sys.argv[1].capitalize(), working_directory) 
  os.system('ls ' + sys.argv[1].capitalize()) 
  print '\n'
 	
def resource_file_template():
    resources_statement = 'This is the resources file for the %s Robot Framework project'  % sys.argv[1].capitalize()
    resource_file_template = '#' * 140 + '\n' + '#' + '{:>139}'.format('#') + '\n' + '#' + '{:>139}'.format('#') + \
    '\n' + '#' + '{:^138}'.format(resources_statement) + '{:<}'.format('#') + \
    '\n' + '#' + '{:>139}'.format('#') + '\n' + '#' + '{:>139}'.format('#') + '\n' + '#' * 140 + '\n\n' \
    '*** Settings ***' + '\n\n' '*** Keywords ***' 
    return resource_file_template

def variable_file_template():
    variable_statement1 = "This is the variable file for the %s Robot Framework project, put page locators in this section"  % sys.argv[1].capitalize()
    variable_statement2 = "This is the variable file for the %s Robot Framework project, put input variables in this section"  % sys.argv[1].capitalize()
    variable_statement3 = "This is the variable file for the %s Robot Framework project, put expected(matching) variables in this section"  % sys.argv[1].capitalize()
    variable_file_template = "#" * 140 + "\n" + "#" + '{:>139}'.format('#') + "\n" + "#" + '{:>139}'.format('#') + \
   	"\n" + "#" + '{:^138}'.format(variable_statement1) + '{:<}'.format('#') + \
   	"\n" + "#" + '{:>139}'.format('#') + "\n" + "#" + '{:>139}'.format('#') + "\n" + "#" * 140 + "\n\n\n\n" + \
    "#" * 140 + "\n" + "#" + '{:>139}'.format('#') + "\n" + "#" + '{:>139}'.format('#') + \
   	"\n" + "#" + '{:^138}'.format(variable_statement2) + '{:<}'.format('#') + \
   	"\n" + "#" + '{:>139}'.format('#') + "\n" + "#" + '{:>139}'.format('#') + "\n" + "#" * 140 + "\n\n\n\n" + \
   	"#" * 140 + "\n" + "#" + '{:>139}'.format('#') + "\n" + "#" + '{:>139}'.format('#') + \
   	"\n" + "#" + '{:^138}'.format(variable_statement3) + '{:<}'.format('#') + \
   	"\n" + "#" + '{:>139}'.format('#') + "\n" + "#" + '{:>139}'.format('#') + "\n" + "#" * 140
    return variable_file_template

def library_file_template():
    library_statement = "This is the library file for the %s Robot Framework project, put your custom functions in here"  % sys.argv[1].capitalize()
    library_file_template = "#" * 140 + "\n" + "#" + '{:>139}'.format('#') + "\n" + "#" + '{:>139}'.format('#') + \
   	"\n" + "#" + '{:^138}'.format(library_statement) + '{:<}'.format('#') + \
   	"\n" + "#" + '{:>139}'.format('#') + "\n" + "#" + '{:>139}'.format('#') + "\n" + "#" * 140 
    return library_file_template

def init_file_template():
    init_statement = "This is the initialization file for the %s Robot Framework project, put initialization information here"  % sys.argv[1].capitalize()
    init_file_template = "#" * 140 + "\n" + "#" + '{:>139}'.format('#') + "\n" + "#" + '{:>139}'.format('#') + \
    "\n" + "#" + '{:^138}'.format(init_statement) + '{:<}'.format('#') + \
    "\n" + "#" + '{:>139}'.format('#') + "\n" + "#" + '{:>139}'.format('#') + "\n" + "#" * 140 
    return init_file_template

create_rf_proj()        
