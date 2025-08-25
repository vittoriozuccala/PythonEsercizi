# Video SharePoint List: https://www.youtube.com/watch?v=Qf1Qemn2O64
# Sharepoint SCB: https://santandernet.sharepoint.com/sites/DWHItaly/
# Lista Elenco Server: https://santandernet.sharepoint.com/sites/DWHItaly/Lists/listaElencoServer/AllItems.aspx

# import shareplum as sp  # https://pypi.org/project/SharePlum/ (Site, Office365)
# import shareplum.site as ss  # https://pypi.org/project/SharePlum/  (Version)
# import openpyxl as ox   # https://pypi.org/project/openpyxl/
# import json

config = {
    "user": "n219547@eu.santanderconsumer.com",
    "password": "Sella2025!",
    "url": "https://santandernet.sharepoint.com",
    "site": "https://santandernet.sharepoint.com/sites/DWHItaly"
}

USERNAME = config['user']
PASSWORD = config['password']
SHAREPOINT_URL = config['url']
SHAREPOINT_SITE = config['site']

# class SharePoint:
#     def auth(self):
#         self.authcookie = sp.Office365(SHAREPOINT_URL, username=USERNAME, password=PASSWORD)
#         self.site = sp.Site(SHAREPOINT_SITE, version=ss.Version.v365, authcookie=self.authcookie)
        
#         return self.site
    
#     def connect_to_list(self, ls_name):
#         self.auth_site = self.auth()
#         list_data = self.auth_site.List(list_name=ls_name).GetListItems()
#         return list_data
    
# splist = SharePoint().connect_to_list('listaElencoServer')


from shareplum import Site, Office365
from shareplum.site import Version
from requests_ntlm import HttpNtlmAuth

cred = HttpNtlmAuth(USERNAME, PASSWORD)
site = Site(SHAREPOINT_SITE, ssl_version=False, version=Version.v365, auth=cred)
# sp_list = site.List('listaElencoServer')
# list_data = sp_list.GetListItems()
