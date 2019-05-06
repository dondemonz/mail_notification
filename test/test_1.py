from model.input_data import *
import time

def test_create_mms_and_mail_message(fix):
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<MMS>,objid<" + objId + ">,parent_id<" + slave + ">,name<MMS>,smtp<smtp.gmail.com>,port<465>,protocol<SSL/TLS>,use_secure_connection<1>,smtp_auth<1>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,name<Test_Message>").encode("utf-8"))
    time.sleep(2)
    # реализовать проверку на наличие объектов

def test_1(fix):
    fix.send_event(message=("CORE||GET_CONFIG|objtype<MAIL_MESSAGE>,receiver_id<1>").encode("utf-8"))
    time.sleep(2)
    # q = fix.cb1.decode("utf-8")
    #print("!!!q"+q)
    #print(fix.list)
    #time.sleep(1)
    #q = fix.cb1.decode("utf-8")
    #print(q)
