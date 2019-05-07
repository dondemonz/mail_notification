from model.input_data import *
import time


def test_1_correct_setup_mms(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MMS>,objid<" + objId + ">,parent_id<" + slave + ">,smtp_password<P0stgres>,smtp_login<qutestiss@gmail.com>").encode("utf-8"))
    time.sleep(1)
    fix.send_event(message=("CORE||GET_CONFIG|objtype<MMS>,objid<" + objId + ">,receiver_id<1>").encode("utf-8"))
    time.sleep(2)
    fix.search_in_callback(par="smtp_login")
    assert fix.p == "qutestiss@gmail.com"


def test_message_one_adress_and_copy(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<qutestiss@gmail.com>,to<qatest@iss.ru>,body<Something in body>,from<qutestiss@gmail.com>,subject<MessageOneAdressAndCopy>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(2)
    fix.search_in_callback(par="action")
    assert fix.p == "SENT"


def test_message_two_adress_and_copy(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<vtestp986@gmail.com;qatest@iss.ru>,to<qatestiss@yandex.ru;qutestiss@gmail.com>,body<Something in body>,from<qutestiss@gmail.com>,subject<MessageTwoAdressAndCopy>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(3)
    fix.search_in_callback(par="action")
    assert fix.p == "SENT"


def test_message_one_address_and_copy_with_trash(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<qutestiss@gmail.com;asd!@#^$^fdg@.dsrgfdfusg#@sd..sdfa342*()_+_>,to<qatest@iss.ru;xcvb(&@#$*@#(DSUGFH@(HF(@Fsdgkdfg/.(())'h,\,]54-=+_+}381-)>,body<Something in body>,from<qutestiss@gmail.com>,subject<MessageOneAdressAndCopyWithTrash>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(3)
    fix.search_in_callback(par="action")
    assert fix.p == "SENT"


def test_another_message_one_address_and_copy_with_trash(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<qutestiss@gmail.com;asd2>,to<qatest@iss.ru;xcvb123asd>,body<Something in body>,from<qutestiss@gmail.com>,subject<AnotherMessageOneAdressAndCopyWithTrash>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(2)
    fix.search_in_callback(par="action")
    assert fix.p == "SENT"


def test_params_in_message(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<>,to<qatest@iss.ru>,body<#body#>,from<qutestiss@gmail.com>,subject<#subject#>,attachments<>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND|body<Test message with params and attachment>,subject<Message with params>,attachments<C:\\test.jpg>").encode("utf-8"))
    time.sleep(2)
    fix.search_in_callback(par="action")
    assert fix.p == "SENT"
