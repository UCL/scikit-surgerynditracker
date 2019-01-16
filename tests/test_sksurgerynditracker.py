# coding=utf-8

"""scikit-surgerynditracker tests"""

import pytest
from sksurgerynditracker.nditracker import NDITracker

#configuration.
SETTINGS_VEGA = {
        "tracker type": "vega",
        "ip address" : "192.168.2.17",
        "port" : 8765,
        "romfiles" : [
            "../data/8700339_smallblue-150130.rom",
            "../data/8700339.rom"]
        }

SETTINGS_POLARIS = {
        "tracker type": "polaris",
        "romfiles" : [
            "../data/8700339_smallblue-150130.rom",
            "../data/8700339.rom"]
        }

SETTINGS_AURORA = {
        "tracker type": "aurora",
        }

SETTINGS_DUMMY = {
        "tracker type": "dummy",
        }

def test_connect():
    #what testing can we do with out being attached to a tracker?
    #What testing can we do when we are attached to a tracker?
    #We could build a fake ndi tracker, that listens on a port
    #and responds appropriately.
    tracker = NDITracker()
    tracker.connect(SETTINGS_DUMMY)
    tracker.close()

def test_connect_network():
    tracker = NDITracker()
    with pytest.raises(IOError):
        tracker.connect(SETTINGS_VEGA)
    with pytest.raises(ValueError):
        tracker.close()

def test_connect_serial():
    tracker = NDITracker()
    with pytest.raises(IOError):
        tracker.connect(SETTINGS_POLARIS)
    with pytest.raises(ValueError):
        tracker.close()

def test_configure():
    tracker = NDITracker()
    no_rom = {
        "tracker type": "polaris",
        }
    with pytest.raises(KeyError):
        tracker._configure(no_rom)
    #here we can pass a variety of configuration dictionaries and check that
    #performance is as expected.
    assert True

def test_config_vega():
    #here we can pass a variety of configuration dictionaries and check that
    #performance is as expected.
    assert True

def test_config_aurora():
    #here we can pass a variety of configuration dictionaries and check that
    #performance is as expected.
    assert True

def test_config_polaris():
    #here we can pass a variety of configuration dictionaries and check that
    #performance is as expected.
    assert True

def test_close():

    with pytest.raises(ValueError):
        tracker = NDITracker()
        tracker.close()

def test_read_sroms_from_file():
    assert True

def test_initialise_ports():
    assert True

def test_enable_tools():
    assert True

def test_get_frame():
    assert True

def test_get_tool_descriptions():
    assert True

def test_start_tracking():
    assert True

def test_stop_tracking():
    assert True

def test_check_for_errors():
    assert True

