from model.input_data import *
import time


def test_incorrect_setup_mms_login(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MMS>,objid<" + objId + ">,parent_id<" + slave + ">,smtp_password<P0stgres>,smtp_login<qu@tes.tiss@gm.ail..com>").encode("utf-8"))
    time.sleep(1)
    fix.send_event(message=("CORE||GET_CONFIG|objtype<MMS>,objid<" + objId + ">,receiver_id<1>").encode("utf-8"))
    time.sleep(2)
    fix.search_in_callback(par="smtp_login")
    assert fix.p == "qu@tes.tiss@gm.ail..com"


def test_setup_mail_message_incorrect_cc(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<@#$%^&*(gfsdg)>,to<>,body<Something in body>,from<qutestiss@gmail.com>,subject<TEST MESSAGE>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(1)
    fix.search_in_callback(par="action")
    assert fix.p == "SEND_ERROR"


def test_setup_mail_message_incorrect_from(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<>,to<>,body<Something in body>,from<@#$%^&*(gfsdg)>,subject<TEST MESSAGE>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(1)
    fix.search_in_callback(par="action")
    assert fix.p == "SEND_ERROR"


def test_message_empty_address_and_copy(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<>,to<>,body<Something in body>,from<qutestiss@gmail.com>,subject<MessageEmptyAddressAndCopy").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(1)
    fix.search_in_callback(par="action")
    assert fix.p == "SEND_ERROR"


def test_message_empty_address_and_one_copy(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<qutestiss@gmail.com>,to<>,body<Something in body>,from<qutestiss@gmail.com>,subject<MessageEmptyAddressAndOneCopy>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(1)
    fix.search_in_callback(par="action")
    assert fix.p == "SEND_ERROR"


def test_setup_mail_message_incorrect_to(fix):
    time.sleep(2)
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<>,to<@#$%^&*(gfsdg)>,body<Something in body>,from<qutestiss@gmail.com>,subject<TEST MESSAGE>").encode("utf-8"))
    fix.send_react("MAIL_MESSAGE|999|SEND".encode("utf-8"))
    time.sleep(3)
    fix.search_in_callback(par="action")
    assert fix.p == "SEND_ERROR"
