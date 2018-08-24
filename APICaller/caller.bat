@echo off
rem set value="https://dev22777.service-now.com/api/now/table/incident"
set value="http://ctsc00879343001:28893/sites/SPPOC/_api/lists/GetByTitle('Asset Details')/items?'$select=Title,Id,Asset_x0020_Id"
set user_name="cts\445781"
set password="MyLife@2"
rem set payload="{'number':'INC0011016'}"
rem set payload=""
set proxy_url="http://proxy.cognizant.com:6050;https://proxy.cognizant.com:6050"
set proxy_username="528664"
set proxy_password="LuckyD00d"
python APICaller.py %value% %user_name% %password% %proxy_url% %proxy_username% %proxy_password% %payload%