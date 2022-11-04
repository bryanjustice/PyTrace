from math import radians, degrees, cos, sin, asin
import numpy as np

def refractedAngle(n1: float, n2: float, incident: float) -> float:
    """
    Calculate the refracted angle of a plane wave impinging upon a
    planar interface from an origination medium of index n1 into a
    medium of index n2 at some angle of incidence in degrees.
    Returns angle in degrees.
    """
    # convert input angle from degrees to radians
    incident_rad = math.degrees(incident)

    # calculate angle of refraction in radians
    refracted_rad = math.asin((n1/n2)*math.sin(incident_rad))

    # convert output back to degrees before returning
    refracted = math.radians(refracted_rad)

    return refracted
