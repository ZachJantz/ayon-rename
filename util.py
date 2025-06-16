import maya.cmds as cmds
from collections import defaultdict




def is_group(node):
    """
    Returns True if a node is a group node
    """
    if not cmds.listRelatives(node, shapes=1):
        return True
    else:
        return False


def ayon_validate_grps():

    # Check that all groups end in '_GRP'
    scene_grps = [node for node in cmds.ls(tr=1) if is_group(node)]
    invalid_grps  = []
    for grp in scene_grps:
        if grp.endswith("_GRP") is False:
            invalid_grps.append(grp)

    return invalid_grps


def ayon_validate_geo():

    # Check that all geo end with '_GEO'
    ignore = ['front','side','persp','top']
    scene_geo = [node for node in cmds.ls(tr=1) if is_group(node) is False and node not in ignore]
    invalid_geo  = []
    for geo in scene_geo:
        if geo.endswith("_GEO") is False:
            invalid_geo.append(geo)

    return invalid_geo


def ayon_validate_shaders():
    
    # Check that all shader nodes end with either '_SH', '_SG', or '_DSP'
    ignore = ['lambert1','particleCloud1', 'standardSurface1']
    scene_shaders = [mat for mat in cmds.ls(mat=1) if mat not in ignore]
    invalid_shaders = []
    for shader in scene_shaders:
        if shader.endswith(("_SH","_SG","_DSP")) is False:
            invalid_shaders.append(shader)
    
    return invalid_shaders


def detect_duplicates():
    """
    Detects duplicate naming in the scene file that might be go unnoticed in different heirarchies
    """
    all_names = []
    all_names.append(cmds.ls(tr=1))
    all_names = sum(all_names, [])
    count_map = defaultdict(list)
    for name in all_names:
        short_name = name.split('|')[-1]
        count_map[short_name].append(name)

    return {name: paths for name,paths in count_map.items()  if len(paths) >1}