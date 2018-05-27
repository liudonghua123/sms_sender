# coding=utf-8
import configparser
import pandas as pd
from sms_sender import init_sms_sender, send_sms
import uuid

def initializeConfigs(configPath):
    """
    读取配置文件，返回一个dict的配置项
    """
    # 设置配置文件解析器
    config = configparser.ConfigParser()
    config.read(configPath, encoding="utf-8-sig")
    # 读取配置项
    ACCESS_KEY_ID = config['aliyun_sms']['ACCESS_KEY_ID']
    ACCESS_KEY_SECRET = config['aliyun_sms']['ACCESS_KEY_SECRET']
    SIGN_NAME = config['sms']['SIGN_NAME']
    TEMPLATE_CODE = config['sms']['TEMPLATE_CODE']
    EXCEL_PATH = config['sms']['EXCEL_PATH']
    return {'ACCESS_KEY_ID': ACCESS_KEY_ID, 'ACCESS_KEY_SECRET': ACCESS_KEY_SECRET,
            'SIGN_NAME': SIGN_NAME, 'TEMPLATE_CODE': TEMPLATE_CODE, 'EXCEL_PATH': EXCEL_PATH
            }


def parseExcel(excel_path):
    """
    解析Excel文件，读取第一列的手机号码
    """
    excelData = pd.read_excel(excel_path)
    return excelData


if __name__ == "__main__":
    configs = initializeConfigs('config.ini')
    excelData = parseExcel(configs['EXCEL_PATH'])
    phoneList = excelData['phone']
    init_sms_sender(configs['ACCESS_KEY_ID'], configs['ACCESS_KEY_SECRET'])
    for phoneNum in phoneList:
        __business_id = uuid.uuid1()
        params = "{\"mtname\":\"姜美纹绣\",\"submittime\":\"2018-05-26 00:25\"}"
        print("sending sms to {phoneNum}".format(phoneNum=phoneNum))
        result = send_sms(__business_id, phoneNum, configs['SIGN_NAME'], configs['TEMPLATE_CODE'], params)
        print("send result of {phoneNum} is {result}".format(phoneNum=phoneNum, result=result))
