from model.input_data import *
import time
from parse import search


def test_incorrect_setup_mms_login(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MMS>,objid<" + objId + ">,parent_id<" + slave + ">,smtp_password<P0stgres>,smtp_login<qu@tes.tiss@gm.ail..com>").encode("utf-8"))
    # проверка установленных параметров

def test_correct_setup_mms(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MMS>,objid<" + objId + ">,parent_id<" + slave + ">,smtp_password<P0stgres>,smtp_login<qutestiss@gmail.com>").encode("utf-8"))
    # проверка установленных параметров

def test_setup_mail_message_incorrect_to(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<>,to<@#$%^&*(gfsdg)>,body<Something in body>,from<qutestiss@gmail.com>,subject<TEST MESSAGE>").encode("utf-8"))
    fix.send_react("MAIL_MESSAGE|999|SEND".encode("utf-8"))
    time.sleep(1)
    n = fix.cb1.decode("utf-8")
    # print(n)
    time.sleep(1)
    param = search('action<{}>', n)
    # выборка нужного элемента
    param = param.fixed[0]
    assert param == "SEND_ERROR"


def test_setup_mail_message_incorrect_cc(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<@#$%^&*(gfsdg)>,to<>,body<Something in body>,from<qutestiss@gmail.com>,subject<TEST MESSAGE>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(1)
    n = fix.cb1.decode("utf-8")
    #print(n)
    param = search('action<{}>', n)
    # выборка нужного элемента
    param = param.fixed[0]
    assert param == "SEND_ERROR"
    # проверка Core.RegisterEventHandler("MAIL_MESSAGE","999","*",check);
    # e.action == "SEND_ERROR","Failed sent CC");



def test_setup_mail_message_incorrect_from(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<>,to<>,body<Something in body>,from<@#$%^&*(gfsdg)>,subject<TEST MESSAGE>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(1)
    n = fix.cb1.decode("utf-8")
    print(n)
    param = search('action<{}>', n)
    # выборка нужного элемента
    param = param.fixed[0]
    assert param == "SEND_ERROR"
    # проверка Core.RegisterEventHandler("MAIL_MESSAGE","999","*",check);
    # Unit.Ok(e.action == "SEND_ERROR","Failed sent FROM");


def test_message_empty_address_and_copy(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<>,to<>,body<Something in body>,from<qutestiss@gmail.com>,subject<MessageEmptyAddressAndCopy").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(1)
    n = fix.cb1.decode("utf-8")
    print(n)
    param = search('action<{}>', n)
    # выборка нужного элемента
    param = param.fixed[0]
    assert param == "SEND_ERROR"
    # проверка Core.RegisterEventHandler("MAIL_MESSAGE","999","*",check);
    #	Unit.Ok(e.action == "SEND_ERROR","Failed sent with empty address");


def test_message_empty_address_and_one_copy(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<qutestiss@gmail.com>,to<>,body<Something in body>,from<qutestiss@gmail.com>,subject<MessageEmptyAddressAndOneCopy>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(1)
    n = fix.cb1.decode("utf-8")
    print(n)
    param = search('action<{}>', n)
    # выборка нужного элемента
    param = param.fixed[0]
    assert param == "SEND_ERROR"
    # проверка Core.RegisterEventHandler("MAIL_MESSAGE","999","*",check);
    # e.action == "SEND_ERROR","Failed sent with one copy");


def test_message_one_adress_and_copy(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<qutestiss@gmail.com>,to<qatest@iss.ru>,body<Something in body>,from<qutestiss@gmail.com>,subject<MessageOneAdressAndCopy>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(2)
    n = fix.cb1.decode("utf-8")
    print(n)
    param = search('action<{}>', n)
    time.sleep(1)
    # выборка нужного элемента
    param = param.fixed[0]
    assert param == "SENT"
    # проверка Core.RegisterEventHandler("MAIL_MESSAGE","999","*",check);
    # e.action == "SENT","Message sent with one copy");


def test_message_two_adress_and_copy(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<vtestp986@gmail.com;qatest@iss.ru>,to<qatestiss@yandex.ru;qutestiss@gmail.com>,body<Something in body>,from<qutestiss@gmail.com>,subject<MessageTwoAdressAndCopy>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(2)
    n = fix.cb1.decode("utf-8")
    print(n)
    param = search('action<{}>', n)
    time.sleep(1)
    # выборка нужного элемента
    param = param.fixed[0]
    assert param == "SENT"
    # проверка Core.RegisterEventHandler("MAIL_MESSAGE","999","*",check);
    # e.action == "SENT","Message sent with two copy");


def test_message_one_address_and_copy_with_trash(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<qutestiss@gmail.com;asd!@#^$^fdg@.dsrgfdfusg#@sd..sdfa342*()_+_>,to<qatest@iss.ru;xcvb(&@#$*@#(DSUGFH@(HF(@Fsdgkdfg/.(())'h,\,]54-=+_+}381-)>,body<Something in body>,from<qutestiss@gmail.com>,subject<MessageOneAdressAndCopyWithTrash>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(2)
    n = fix.cb1.decode("utf-8")
    print(n)
    param = search('action<{}>', n)
    time.sleep(1)
    # выборка нужного элемента
    param = param.fixed[0]
    assert param == "SENT"
    # проверка Core.RegisterEventHandler("MAIL_MESSAGE","999","*",check);
    # e.action == "SENT","Message sent with two copy");


def test_another_message_one_address_and_copy_with_trash(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<qutestiss@gmail.com;asd2>,to<qatest@iss.ru;xcvb123asd>,body<Something in body>,from<qutestiss@gmail.com>,subject<AnotherMessageOneAdressAndCopyWithTrash>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND").encode("utf-8"))
    time.sleep(2)
    n = fix.cb1.decode("utf-8")
    print(n)
    param = search('action<{}>', n)
    time.sleep(1)
    # выборка нужного элемента
    param = param.fixed[0]
    assert param == "SENT"
    # проверка Core.RegisterEventHandler("MAIL_MESSAGE","999","*",check);
    # e.action == "SENT","Message sent with two copy");


def test_params_in_message(fix):
    fix.send_event(message=("CORE||UPDATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,cc<>,to<qatest@iss.ru>,body<#body#>,from<qutestiss@gmail.com>,subject<#subject#>,attachments<>").encode("utf-8"))
    fix.send_react(("MAIL_MESSAGE|" + objId + "|SEND|body<Test message with params and attachment>,subject<Message with params>,attachments<C:\\test.jpg>").encode("utf-8"))
    time.sleep(1)
    n = fix.cb1.decode("utf-8")
    print(n)
    param = search('action<{}>', n)
    time.sleep(2)
    # выборка нужного элемента
    param = param.fixed[0]
    assert param == "SENT"
    # проверка Core.RegisterEventHandler("MAIL_MESSAGE","999","*",check);
    #e.action == "SENT","Message sent with two copy");


