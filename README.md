# Hornet Maya Rename
## Features
### Options
Options controls how renaming occurs.
- Padding controls the amount of number padding that occurs in any automated naming. It allows 2-8 spaces worth of padding.
- The start number controls the what value automated naming begins at.
- There are four options for the context over Appending and Search and Replace can execute over.
### Batch Rename
Batch renaming based on user defined naming structures.
- Batch rename works by creating a naming template, name_someinfo_#_GEO, where automated numbering occurs at # placement.
- Note: Batch rename only works over selected nodes to ensure structure compliance.
### Append
Appending context allows for the fast adding of prefixes or suffixes over a series of nodes.
- Enter a custom string and it will add it either as a prefix or suffix to nodes based on the context set in options.
- There are multiple preset suffixes for common artist needs that will be added automatically.
### Search and Replace
Allows the user to find specific strings in node names and replace them.
- Search will just select the nodes in the given context that contain the input string.
- Replace will replace the search string with a string for nodes in the enabled context.
- To search the entire outliner, make sure the option is set to all.
### Propogate Group Name
Added this because if you have a big model where you are working with a bunch of groups it makes it easier to just name a group and press the button.
- Takes the name of a group and names the geo inside based off the group name, i.e., parts_GRP -> parts_01_GEO.
### Duplicate Check
Check for duplicate names in different heirarchies.
- Launches a dialog that displays conflicting names and the paths to those names.
- Select the paths and enter a new compliant name.
## Dev




