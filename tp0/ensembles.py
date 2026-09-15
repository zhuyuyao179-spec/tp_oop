"""Coordination d'une flotte de robots avec des ensembles."""


def robots_double_mission(robots_exploration, robots_transport):
    """
    Retourne les robots affectés aux deux missions.
    """
    return robots_exploration & robots_transport


def robots_toutes_missions(robots_exploration, robots_transport):
    """
    Retourne tous les robots impliqués dans au moins une mission.
    """
    return robots_exploration | robots_transport


def robots_exploration_seulement(robots_exploration, robots_transport):
    """
    les robots d'exploration non affectés au transport.
    """
    return robots_exploration - robots_transport


def ajouter_robot_mission(robots_mission, robot):
    """
    Ajoute un robot à une mission 

    """
    return robots_mission | {robot}


def retirer_robot_mission(robots_mission, robot):
    """
    Retire un robot d'une mission 
    """
    return robots_mission - {robot}
