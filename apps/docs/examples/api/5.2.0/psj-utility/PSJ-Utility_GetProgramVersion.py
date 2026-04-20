# Title:   JPT.GetProgramVersion()
# Desc:    Get all the version information of the current Jupiter application
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetProgramVersion
# ---
# Get the version information of the current Jupiter
version = JPT.GetProgramVersion()  # [hl]
print(f"Jupiter {version.major}.{version.minor}.{version.sub}")
print(f"Revision {version.build}")
