#! /usr/bin/env python
#coding=utf-8
"""
    Baihui API core functions.
    inspiration from https://github.com/miohtama/mfabrik.zoho
"""

__author__ = "pyhunterpig <hunterpig@gmail.com>"
__license__ = "MIT"


import requests

import logging

try:
    from xml import etree
    from xml.etree.ElementTree import Element, tostring, fromstring
except ImportError:
     try:
         from lxml import etree
         from lxml.etree import  Element, tostring, fromstring
     except ImportError:
         print "XML library not available:  no etree, no lxml"
         raise


try:
    import json as simplejson
except ImportError:
    try:
        import simplejson
    except ImportError:
        # Python 2.4, no simplejson installed
        raise RuntimeError("You need json or simplejson library with your Python")


logger = logging.getLogger("Baihui API")


class BaihuiException(Exception):
    """ 
    
    """


class Connection(object):
    """ Baihui API connector.

    Absract base class for all different Baihui API connections.
    Subclass this and override necessary methods to support different Baihui API groups.
    """

    def __init__(self, **kwargs):
        """
        @param username: hunterpig@gmail.com

        @param password: xxxxxxx

        @param authtoken: Given by Baihui

        @param extra_auth_params: Dictionary of optional HTTP POST parameters passed to the login call

        @param auth_url: Which URL we get authtoken
        """
        options = {
            'username': None,
            'password': None,
            'authtoken': None,
            'auth_url': "https://i.baihui.com/apiauthtoken/nb/create",
            'scope': None
        }
        options.update(kwargs)
        if options['username'] is not None and options['password'] is not None:
            self.username = options["username"]
            self.password = options["password"]

        if options['authtoken']:
            self.authtoken = options["authtoken"]

        self.auth_url = options['auth_url']

        if options['scope'] is not None:
            self.scope = options["scope"]
        else:
            if not self.scope:
                raise BaihuiException("No Scope")


    def get_service_name(self):
        """ Return API name which we are using. """
        raise NotImplementedError("Subclass must implement")


    def _create_authtoken(self):
        """
        
        @return: authtoken code
        """
        #https://i.baihui.com/apiauthtoken/nb/create?SCOPE=ZohoCRM/crmapi&EMAIL_ID=[Username/EmailID]&PASSWORD=[Password]
        params = {
            'SCOPE': "/".join([self.get_service_name(), self.scope]),
            'EMAIL_ID': self.username,
            'PASSWORD': self.password
        }

        r = requests.get(self.auth_url, params=params)
        
        body = r.text

        data = self._parse_authtoken_response(body)

        if data["WARNING"] != "null":
            # Baihui has set an error field
            raise BaihuiException("Could not auth:" + data["WARNING"])

        if data["CAUSE"] != "null":
            # Baihui has set an error field
            raise BaihuiException("Could not auth:" + data["CAUSE"])
        
        if data["RESULT"] != "TRUE":
            raise BaihuiException("Ticket result was not valid")

        return data["AUTHTOKEN"]

    def _parse_authtoken_response(self, data):
        """ http://statement.wiki.baihui.com/crm/authtoken-introduced.html

        Example response::

            #
            #Wed Jan 22 11:31:26 CST 2014
            CAUSE=ACCOUNT_REGISTRATION_NOT_CONFIRMED
            RESULT=FALSE
            
        """

        output = {}

        lines = data.split("\n")
        for line in lines:

            if line.startswith("#"):
                # Comment
                continue

            if line.strip() == "":
                # Empty line
                continue

            if not "=" in line:
                raise BaihuiException("Bad authtoken data:" + data)

            key, value = line.split("=")
            output[key] = value

        return output

    def create_authtoken(self):
        """ create the Baihui API authtoken """
        if hasattr(self, 'username') and hasattr(self, 'password') and not hasattr(self, 'authtoken'):
            self.authtoken = self._create_authtoken()
        else:
            return

    def do_xml_call(self, url, parameters, root):
        """  Do Baihui API call with outgoing XML payload.

        Authtoken parameters will be added automatically.

        @param url: URL to be called

        @param parameters: Optional POST parameters.

        @param root: ElementTree DOM root node to be serialized.
        """

        parameters = parameters.copy()
        parameters[self.parameter_xml] = tostring(root)
        return self.do_call(url, parameters)

    def do_call(self, url, parameters):
        """ Do Baihui API call.

        @param url: URL to be called

        @param parameters: Optional POST parameters.
        """
        # Do not mutate orginal dict
        parameters = parameters.copy()
        parameters["authtoken"] = self.authtoken
        parameters["scope"] = self.scope

        

        if logger.getEffectiveLevel() == logging.DEBUG:
            # Output Baihui API call payload
            logger.debug("Doing Baihui API call:" + url)
            for key, value in parameters.items():
                logger.debug(key + ": " + value)
        self.parameters = parameters
        
        r = requests.post(url, params=parameters)
        response = r.text

        if logger.getEffectiveLevel() == logging.DEBUG:
            # Output Baihui API call payload
            logger.debug("Baihui API response:" + url)
            logger.debug(str(r.headers))
            logger.debug(response)

        return response

    def check_successful_xml(self, response):
        """ Make sure that we get "succefully" response.
        
        Throw exception of the response looks like something not liked.
        
        @raise: BaihuiException if any error
        
        @return: Always True
        """

        # Example response
        # <response uri="/crm/private/xml/Leads/insertRecords"><result><message>Record(s) added successfully</message><recorddetail><FL val="Id">177376000000142007</FL><FL val="Created Time">2010-06-27 21:37:20</FL><FL val="Modified Time">2010-06-27 21:37:20</FL><FL val="Created By">Ohtamaa</FL><FL val="Modified By">Ohtamaa</FL></recorddetail></result></response>

        root = fromstring(response)
            
        # Check error response
        # <response uri="/crm/private/xml/Leads/insertRecords"><error><code>4401</code><message>Unable to populate data, please check if mandatory value is entered correctly.</message></error></response>
        for error in root.findall("error"):
            parameters = self.parameters
            parameters_encoded = self.parameters_encoded
            print "Got error"
            for message in error.findall("message"):
                raise BaihuiException(message.text)
        
        return True

    def get_inserted_records(self, response):
        """
        @return: List of record ids which were created by insert recoreds
        """
        root = fromstring(response)
        
        records = []
        for result in root.findall("result"):
            for record in result.findall("recorddetail"):
                record_detail = {}
                for fl in record.findall("FL"):
                    record_detail[fl.get("val")] = fl.text
                records.append(record_detail)
        return records



def decode_json(json_data):
    """ Helper function to handle Baihui specific JSON decode.

    @return: Python dictionary/list of incoming JSON data

    @raise: BaihuiException if JSON'ified error message is given by Baihui
    """

    # {"response": {"uri":"/crm/private/json/Leads/getRecords","error": {"code":4500,"message":"Problem occured while processing the request"}}}
    data = simplejson.loads(json_data)

    response = data.get("response", None)
    if response:
        error = response.get("error", None)
        if error:
            raise BaihuiException("Error while calling JSON Baihui api:" + str(error))

    return data
