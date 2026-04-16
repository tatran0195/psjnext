# Title:   JPT.DisableMessageBox()
# Desc:    Disable and set default value of the pop-up message box on screen
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_DisableMessageBox
# ---
# Disable pop-up message and set the default value of message box to be YES
JPT.DisableMessageBox(JPT.MsgBoxOptionType.MB_OPTION_YES)  # [hl]
returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB_INFORMATION_YESNO)
print(returnValue) # Return a string object with value = YES

# Disable pop-up message and set the default value of message box to be NO
JPT.DisableMessageBox(JPT.MsgBoxOptionType.MB_OPTION_NO)  # [hl]
returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB_INFORMATION_YESNO)
print(returnValue) # Return a string object with value = NO

# Disable pop-up message and set the default value of message box to be CANCEL
JPT.DisableMessageBox(JPT.MsgBoxOptionType.MB_OPTION_CANCEL)  # [hl]
returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB_INFORMATION_YESNOCANCEL)
print(returnValue) # Return a string object with value = CANCEL

# Disable pop-up message and set the default value of message box to be OK
JPT.DisableMessageBox(JPT.MsgBoxOptionType.MB_OPTION_OK)  # [hl]
returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB_INFORMATION_OKCANCEL)
print(returnValue) # Return a string object with value = OK
