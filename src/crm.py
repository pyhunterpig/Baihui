#! /usr/bin/env python
#coding=utf-8
"""
    Baihui CRM API 
    inspiration from https://github.com/miohtama/mfabrik.zoho
"""

__author__ = "pyhunterpig <hunterpig@gmail.com>"
__license__ = "MIT"


try:
    from xml import etree
    from xml.etree.ElementTree import Element, tostring, fromstring, SubElement
except ImportError:
    try:
        from lxml import etree
        from lxml.etree import Element, tostring, fromstring, SubElement
    except ImportError:
        raise RuntimeError("XML library not available:  no etree, no lxml")
   
from functools import partial, update_wrapper
from core import Connection, BaihuiException, decode_json

_VALID_MODULES = ('Users',
                  'Attachments',
                  'Leads',
                  'Accounts',
                  'Contacts',
                  'Potentials',
                  'Campaigns',
                  'Cases',
                  'Solutions',
                  'Products',
                  'PurchaseOrders',
                  'Quotes',
                  'SalesOrders',
                  'Invoices',
                  'Vendors',
                  'Tasks',
                  'Events',
                  'Notes'
                 )

def getModuleMethods():
    """ Methods of Modules  """
    ModuleMethods = {}
    for module in _VALID_MODULES:
        if module == 'Users':
            ModuleMethods[module] = ['getUsers']
        elif module == 'Attachments':
            ModuleMethods[module] = ['downloadFile', 'deleteFile']
        else:
            ModuleMethods[module] = [
                                    'getMyRecords',
                                    'getRecords',
                                    'getRecordById',
                                    'getCVRecords',
                                    'insertRecords',
                                    'updateRecords',
                                    'getSearchRecords',
                                    'getSearchRecordsByPDC',
                                    'deleteRecords',
                                    'getRelatedRecords',
                                    'getFields',
                                    'updateRelatedRecords',
                                    'uploadFile',
                                    'downloadFile',
                                    'deleteFile'
                                    ]
            if module == 'Leads':
                ModuleMethods[module].append('convertLead')
            if module in ['Leads', 'Contacts']:
                ModuleMethods[module] +=['uploadPhoto','downloadPhoto',
                                             'deletePhoto']
    return ModuleMethods
    
    
class APIs(object):
    """Baihui CRM APIs mapped to Python 
       http://statement.wiki.baihui.com/api/API%E6%96%B9%E6%B3%95.html
       方法名称	      目的
       getMyRecords	获取API请求中指定的身份验证令牌的所有者的数据
       getRecords	获取API请求中指定的所有用户的数据
       getRecordById	通过记录ID获取个别记录
       getCVRecords	获取百会CRM的自定义视图数据
       insertRecords	将记录插入到所需的百会CRM模块
       updateRecords	更新或修改百会CRM的记录
       getSearchRecords	通过对选定列的表达式搜索记录
       getSearchRecordsByPDC	根据预先定义的列搜索值
       deleteRecords	删除所选的记录
       convertLead	将线索转换为商机、客户和联系人
       getRelatedRecords	获得主模块的相关记录
       getFields	获取模块中可用字段的详细信息
       updateRelatedRecords	更新与另一条记录相关的记录
       getUsers	获取机构用户列表
       uploadFile	添加附件到记录
       downloadFile	下载记录附件
       deleteFile	删除记录附件
       uploadPhoto	       添加照片到某个联系人或线索
       downloadPhoto       下载某个联系人或线索的照片
       deletePhoto	       删除某个联系人或线索的照片
       
    """

    def __init__(self, Conn, Module):
        self.conn = Conn
        self.module = Module
        self.ModuleMethods = getModuleMethods()
        
    def _method_func(self, methodname, **kwds):
        params = {"format":"xml"}
        params.update(kwds.copy())
        url = "https://crm.baihui.com/crm/private/%s/%s/%s" %(params["format"],
                                                    self.module, methodname)
        return self.conn.do_call(url, params)
    
    def __getattr__(self, methodname):
        if methodname not in self.ModuleMethods[self.module]:
            return AttributeError
        # dispatch our function
        func = partial(self._method_func, methodname)
        # update our partial with self.shift_date attributes
        update_wrapper(func, self._method_func)
        return func
        
        
class CRM(Connection):
    """ CRM specific Baihui APIs mapped to Python """
    
    """ Define the standard parameter for the XML data """
    parameter_xml = 'xmlData'
    
    scope = 'crmapi'
    
    def __getattr__(self, name):
        """
        Implement __getattr__ to call `shift_date` function when function
        called does not exist
        """
        if name not in _VALID_MODULES:
            return AttributeError
        
        return APIs(self, name)
    

    def get_service_name(self):
        """ Called by base class """
        return "ZohoCRM"
    
        
        