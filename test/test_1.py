from model.input_data import *
import time
from parse import search
import re

def test_create_mms_and_mail_message(fix):
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<MMS>,objid<" + objId + ">,parent_id<" + slave + ">,name<MMS>,smtp<smtp.gmail.com>,port<465>,protocol<SSL/TLS>,use_secure_connection<1>,smtp_auth<1>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,name<Test_Message>").encode("utf-8"))
    time.sleep(2)

def test_check_MMS(fix):
    #fix.send_event(message=("CORE||GET_CONFIG|objtype<MAIL_MESSAGE>,receiver_id<1>").encode("utf-8"))
    fix.send_event(message=("CORE||GET_STATE|objtype<MMS>,objid<" + objId + ">,receiver_id<1>").encode("utf-8"))
    time.sleep(1)
    for param in fix.list:
        if search('cmdstatus<{}>', param) != None:
            assert search('cmdstatus<{}>', param).fixed[0] == "Success"


def test_check_mail_message(fix):
    fix.send_event(message=("CORE||GET_STATE|objtype<MAIL_MESSAGE>,objid<" + objId + ">,receiver_id<1>").encode("utf-8"))
    time.sleep(1)
    print(fix.list)
    for param in fix.list:
        if search('cmdstatus<{}>', param) != None:
            assert search('cmdstatus<{}>', param).fixed[0] == "Success"
