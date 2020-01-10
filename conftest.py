from fixture.load_dll import DllHelper
from model.input_data import *
import pytest
import time




@pytest.fixture
def fix(request):
    fixture = DllHelper()
    # функция disconnect передается в качестве параметра
    request.addfinalizer(fixture.disconnect)
    return fixture

@pytest.fixture(scope="session", autouse=True)
def fix2(request):
    fix = DllHelper()
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<MMS>,objid<" + objId + ">,parent_id<" + slave + ">,name<MMS>,smtp<smtp.gmail.com>,port<465>,protocol<SSL/TLS>,use_secure_connection<1>,smtp_auth<1>").encode("utf-8"))
    time.sleep(1)
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<MAIL_MESSAGE>,objid<" + objId + ">,parent_id<" + objId + ">,name<Test_Message>").encode("utf-8"))
    time.sleep(2)
    print('\nSome recource')
    def fin():
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<MMS>,objid<"+objId+">").encode("utf-8"))
        print('\nSome resource fin')
        # fix.disconnect()
    request.addfinalizer(fin)
    return request

'''
проверка создания объектов, на всякий случай
def test_check_MMS(fix):
    #fix.send_event(message=("CORE||GET_CONFIG|objtype<MAIL_MESSAGE>,receiver_id<1>").encode("utf-8"))
    fix.send_event(message=("CORE||GET_STATE|objtype<MMS>,objid<" + objId + ">,receiver_id<1>").encode("utf-8"))
    time.sleep(1)
    fix.search_in_callback(par="cmdstatus")
    assert fix.p == "Success"


def test_check_mail_message(fix):
    fix.send_event(message=("CORE||GET_STATE|objtype<MAIL_MESSAGE>,objid<" + objId + ">,receiver_id<1>").encode("utf-8"))
    time.sleep(1)
    # print(fix.list)
    fix.search_in_callback(par="cmdstatus")
    assert fix.p == "Success"
'''