# Embedded file name:
# /Users/versonator/Hudson/live/Projects/AppLive/Resources/MIDI Remote
# Scripts/LPD8/__init__.py

import Live
import _Framework.Capabilities as caps
from _Generic.GenericScript import GenericScript
from twisterhk import config


def create_instance(c_instance):
    """ The generic script can be customised by using parameters (see config.py). """
    return GenericScript(
        c_instance,
        Live.MidiMap.MapMode.absolute,
        Live.MidiMap.MapMode.absolute,
        config.DEVICE_CONTROLS,
        config.TRANSPORT_CONTROLS,
        config.VOLUME_CONTROLS,
        config.TRACKARM_CONTROLS,
        config.BANK_CONTROLS,
        config.CONTROLLER_DESCRIPTION,
    )


def get_capabilities():
    return {
        caps.CONTROLLER_ID_KEY: caps.controller_id(
            vendor_id=2536,
            product_ids=[117],
            model_name='LPD8'),
        caps.PORTS_KEY: [
            caps.inport(props=[
                caps.NOTES_CC,
                caps.REMOTE,
                caps.SCRIPT,
            ]),
            caps.outport(props=[caps.SCRIPT]),
        ],
    }
