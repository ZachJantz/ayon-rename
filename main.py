# Launch script for the rename tool
# zachjantz 06-16-2025

import rename_tool, alert_footer, util, dup_resolver
#required for testing in maya
# reload(rename_tool)
# reload(dup_resolver)
# reload(util)
# reload(alert_footer)



if __name__ == '__main__':
    rename_tool.main()