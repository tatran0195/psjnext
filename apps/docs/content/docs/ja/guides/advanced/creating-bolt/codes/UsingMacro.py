#*******************************************************************************
# COPYRIGHT NOTES
# ---------------
# This is a part of the PSJ Library
# Copyright (C) 2002-2020 Technostar Ltd.
# All rights reserved.
#
# This source code can be used, distributed or modified
# only under terms and conditions
# of the accompanying license agreement.
#*******************************************************************************
# PSJ GUI EXAMPLES
# ---------------------
# This example demonstrades how to create a simple part with PSJ by using Macro
#*******************************************************************************

import re
import JPT
from os import listdir
from os.path import isfile, join
from pyjdg import *
import random

# Initial parameters
color = random.randint(10000, 60000000)
code_folder = JPT.GetAppPathInfo(0) + r"SampleData\PSJ\PSJ-GUI\CreateBolt"
picture_folder = code_folder + r"\CreatingBolt_Pics"
default_img_file = picture_folder + r"\M3.JPG"
select_option = ["M3",
                 "M4",
                 "M5",
                 "M6",
                 "M8",
                 "M10",
                 "M12",
                 "M14",
                 "M16",
                 "M18",
                 "M20",
                 "M22",
                 "M24",
                 "M27",
                 "M30"]

# Set the size for the bolt
def get_bolt_size(get_param_bolt_type):
    """ Bolt type for standard size"""
    switcher = {
                0: [2e-3, 6.01e-3, 3e-3],
                1: [2.8e-3, 7.66e-3, 4e-3],
                2: [3.5e-3, 8.79e-3, 5e-3],
                3: [4e-3, 11.5e-3, 6e-3],
                4: [5.3e-3, 14.38e-3, 8e-3],
                5: [6.4e-3, 18.9e-3, 10e-3],
                6: [7.5e-3, 21.1e-3, 12e-3],
                7: [8.8e-3, 24.49e-3, 14e-3],
                8: [10-3, 26.75e-3, 16e-3],
                9: [11.5e-3, 30.14e-3, 18e-3],
                10: [12.5e-3, 33.53e-3, 20e-3],
                11: [14e-3, 35.72e-3, 22e-3],
                12: [15e-3, 39.98e-3, 24e-3],
                13: [17e-3, 45.2e-3, 27e-3],
                14: [18.7e-3, 50.85e-3, 30e-3]
                }
    return switcher.get(get_param_bolt_type, "Inputted bolt type has not been supported yet")

# Replace the specified strings with the space character
def replace_str(err: str, instr: str) -> list:
    modstr = instr
    for i in range (len(err)):
        modstr = modstr.replace(str(err[i]), " ")
    modstr = re.sub("\s+", " ", modstr).strip().split(" ")
    return modstr

# Change bolt picture based on the selected bolt type
def change_bolt_pic(dlg):
    """ Change the picture of the select bolt """
    path = picture_folder + "\\"
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for i in onlyfiles:
        filename, file_extension = i.split('.')
        if dlg.get_item_text('bolt_type') == filename:
            fullpath = path + i
            dlg.set_image_file('ImageCtrl', fullpath)

# Execute button event
def on_execute_button_clicked(dlg, part_name, coord_system, bolt_type, bolt_length):
    """Creating a bolt when click on the Apply or OK button

    Input args:
        dlg: Call class dlg for using [dlg.] - API between the GUI Command Build and Python
        part_name (str): Name of the creating part, from the created GUI
        coord_system (int): ID of the coordinate system, from the created GUI
        bolt_type (int): ID of the bolt type, from the created GUI
        bolt_length (float): Length (L) of the creating bolt
    """

    # Preparing parameters for the creation
    [k, e, d] = get_bolt_size(bolt_type) # Get size of the creating bolt based on the selected bolt_type option
    nut_radius = e/2
    thread_radius = d/2
    cylinder_height = k
    cylinder_position = cylinder_height
    get_param_bolt_length = float(bolt_length)*0.001

    # Creating bolt head and bolt body
    JPT.Exec('CreateCylinderFrustum([0, 0, 0], {2}, {2}, {3}, 6, 10, "{0}", {4}, 27:{1})'.
             format(part_name, coord_system, nut_radius, cylinder_height, color))
    JPT.Exec('CreateCylinderFrustum([0, {2}, 0], {3}, {3}, {4}, 36, 10, "{0}", 6409934, 27:{1})'.
             format(part_name, coord_system, cylinder_position, thread_radius, get_param_bolt_length, color))

    # Making assemble faces
    errstr = ", []-\""
    all_part = sorted([a.id for a in JPT.GetAllParts()], reverse = False)
    assemble_faces = JPT.Exec('AssembleFaceMatingStep([], [], [3:{0}, 3:{1}], 0.0003).' \
                              .format(all_part[-2], all_part[-1]))
    JPT.Exec('AssembleFaceEx([{0}, {1}], 0.0003, 0, 0)'\
             .format(replace_str(errstr, assemble_faces)[-2],
                                 replace_str(errstr, assemble_faces)[-1]))

    # Merging 2 created parts into 1 part
    JPT.Exec('MergePart(1e-08, 1, [3:{0}, 3:{1}])'.format(all_part[-2], all_part[-1]))

    # Show the created part only
    JPT.InverseHideBodies(all_part[-2])
    JPT.ViewFitToModel()

    # Change the part_name parameter (On the GUI) automatically
    if str(dlg.get_item_text("part_name")).find("_") != -1:
        if dlg.get_item_text("part_name").split("_")[-1].isdigit() == True:
            new_name = dlg.get_item_text("part_name")[:-(len(dlg.get_item_text("part_name").split("_")[-1]) + 1)] + "_" + str(int(dlg.get_item_text("part_name").split("_")[-1]) + 1)
        else:
            new_name = dlg.get_item_text("part_name") + "_" + str(len([_.id for _ in JPT.GetAllParts()]) + 1)
    else:
        new_name = dlg.get_item_text("part_name") + "_" + str(len([_.id for _ in JPT.GetAllParts()]) + 1)
    dlg.set_item_text("part_name", new_name)

def main():
    """ Create JDB from JDG """
    #
    dlg=JDGCreator(title="Sample 1 - Bolt Creation",resizable=True,validation=True)
    #
    dlg.add_vlayout(name="Layout3",layout="Window")
    #
    dlg.add_label(name="Label1",text="Unit System: mm",layout="Layout3")
    dlg.add_imagectrl(name="ImageCtrl",image_file=default_img_file,layout="Layout3")
    #
    dlg.add_hlayout(name="Layout2",layout="Layout3")
    dlg.add_label(name="Label3",text="Part Name:",width=100,layout="Layout2")
    dlg.add_textbox(name="part_name",text="Bolt_1",layout="Layout2")
    #
    dlg.add_hlayout(name="Layout5",layout="Layout3")
    dlg.add_label(name="Label6",text="Coordinate System:",width=100,layout="Layout5")
    dlg.add_combobox(name="coord_system",options=["Global"],layout="Layout5")
    #
    dlg.add_hlayout(name="Layout8",layout="Layout3")
    dlg.add_label(name="Label9",text="Bolt Type:",width=100,layout="Layout8")
    dlg.add_combobox(name="bolt_type",options=select_option,width=80,layout="Layout8")
    #
    dlg.add_hlayout(name="Layout11",layout="Layout3")
    dlg.add_label(name="Label12",text="Bolt Length:",width=100,layout="Layout11")
    dlg.add_textbox(name="bolt_length",text="20",layout="Layout11")
    #
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonApply",text="Apply",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    #
    dlg.on_command("ButtonApply",on_execute_button_clicked)
    dlg.on_command("ButtonOk",on_execute_button_clicked)
    dlg.on_command("bolt_type", change_bolt_pic)
    #
    dlg.generate_window()

if __name__=='__main__':
    main()
