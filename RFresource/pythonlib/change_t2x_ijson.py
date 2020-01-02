#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import json


def change_json(input_json_file, key, expected_value, new_json_file):
    # check file exit
    print (os.path.isfile(input_json_file))
    # read json file
    fp1 = open(input_json_file, 'r')
    input_json = json.loads(fp1.read())
    fp1.close()
    # change json
    input_json[key] = expected_value
    # write json file
    fp2 = open(new_json_file, 'w')
    json.dump(input_json, fp2, sort_keys=True, indent=4, separators=(',', ': '))
    fp2.close()


input_json_file = sys.argv[1]
key = sys.argv[2]
expected_value = sys.argv[3]
new_json_file = sys.argv[4]
change_json(input_json_file, key, expected_value, new_json_file)

# cmd = 'sudo ' + exe_file + ' ' + \
#       '--syscfg' + ' ' + variables.SYS_CONFIG + ' ' + \
#       '--modcfg' + ' ' + variables.MOD_CONFIG + ' ' + \
#       '--imucfg' + ' ' + variables.IMU_CONFIG + ' ' + \
#       '--camcfg' + ' ' + camera_config + ' ' + \
#       '--dbtype' + ' ' + db_type + ' ' + \
#       '--database' + ' ' + db_dir + ' ' + \
#       '--filetype' + ' ' + 'rtvgroup' + ' ' + \
#       '--bagrtv' + ' ' + image_path + ' ' + \
#       '--loglevel' + ' ' + variables.LOG_LEVEL + ' ' + \
#       '--ologpath' + ' ' + result_path + '/log.txt' + ' ' + \
#       '--output' + ' ' + result_path + ' ' + \
#       '--testname' + ' ' + os.path.split(image_path)[1] + ' >/dev/null 2>&1'