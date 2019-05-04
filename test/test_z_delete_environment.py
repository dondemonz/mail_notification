from model.input_data import *


def test_delete_environment(fix):
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<MMS>,objid<"+objId+">").encode("utf-8"))