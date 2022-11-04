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


def phase_velocity():
    """
    Calculate the phase velocity given a medium of 
    some refractive index n
    """
    return ph_velocity

def wavelength(n: float, f: float):
    """
    Calculate the periodic wavelength of a plane wave in a medium
    of given index and at a specfic frequency
    f in Hz
    returns wavelength in nm
    """
    # convert wavelength to nm

    return waveLength

def brewster_angle(n1: float, n2: float) -> float:
    """
    Calculate the Brewster's angle, which is the angle of incidence
    at which light is perfectly transmitted through a delectric interface
    between two mediums of indexes n1 and n2.
    """
    return angle

def depth_of_field():
    """
    """
    return depth

def focal_length(diop: float) -> float:
    """
    """
    return flength


