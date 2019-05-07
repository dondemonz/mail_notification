from model.input_data import *
import time
from parse import search


def test_incorrect_setup_mms_login(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MMS>,objid<" + objId + ">,parent_id<" + slave + ">,smtp_password<P0stgres>,smtp_login<qu@tes.tiss@gm.ail..com>").encode("utf-8"))
    time.sleep(1)
    fix.send_event(message=("CORE||GET_CONFIG|objtype<MMS>,objid<" + objId + ">,receiver_id<1>").encode("utf-8"))
    time.sleep(2)
    # print(fix.list)
    for param in fix.list:
        if search('smtp_login<{}>', param) != None:
            assert search('smtp_login<{}>', param).fixed[0] == "qu@tes.tiss@gm.ail..com"


def test_setup_mail_message_incorrect_cc(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<@#$%^&*(gfsdg)>,to<>,body<Something in body>,from<qutestiss@gmail.com>,subject<TEST MESSAGE>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(1)
    n = fix.cb1.decode("utf-8")
    param = search('action<{}>', n)
    # выборка нужного элемента
    param = param.fixed[0]
    assert param == "SEND_ERROR"



def test_setup_mail_message_incorrect_from(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<>,to<>,body<Something in body>,from<@#$%^&*(gfsdg)>,subject<TEST MESSAGE>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(1)
    n = fix.cb1.decode("utf-8")
    param = search('action<{}>', n)
    # выборка нужного элемента
    param = param.fixed[0]
    assert param == "SEND_ERROR"



def test_message_empty_address_and_copy(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<>,to<>,body<Something in body>,from<qutestiss@gmail.com>,subject<MessageEmptyAddressAndCopy").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(1)
    n = fix.cb1.decode("utf-8")
    param = search('action<{}>', n)
    # выборка нужного элемента
    param = param.fixed[0]
    assert param == "SEND_ERROR"


def test_message_empty_address_and_one_copy(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<qutestiss@gmail.com>,to<>,body<Something in body>,from<qutestiss@gmail.com>,subject<MessageEmptyAddressAndOneCopy>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(1)
    n = fix.cb1.decode("utf-8")
    param = search('action<{}>', n)
    # выборка нужного элемента
    param = param.fixed[0]
    assert param == "SEND_ERROR"
def test_setup_mail_message_incorrect_to(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<>,to<@#$%^&*(gfsdg)>,body<Something in body>,from<qutestiss@gmail.com>,subject<TEST MESSAGE>").encode("utf-8"))
    fix.send_react("MAIL_MESSAGE|999|SEND".encode("utf-8"))
    time.sleep(2)
    n = fix.cb1.decode("utf-8")
    time.sleep(1)
    param = search('action<{}>', n)
    # выборка нужного элемента
    param = param.fixed[0]
    assert param == "SEND_ERROR"