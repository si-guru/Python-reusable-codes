###########################################################################################################
<#
Purpose: This powershell script will download a Service Now attachment.
Author : AVM Automation
Version: V1
Input  : Url, UserID, Password, Proxy, incident, filePath
Output : Downloads a ServiceNow attachment.
#>
###########################################################################################################

param(
[parameter(Mandatory=$true)]
[string]$Url,
[parameter(Mandatory=$true)]
[string]$UserID,
[parameter(Mandatory=$true)]
[string]$Password,
[parameter(Mandatory=$true)]
[string]$Proxy,
[parameter(Mandatory=$true)]
[string]$incident,
[parameter(Mandatory=$true)]
[string]$filePath
)
try
{
    # Test filePath
    if(!(Test-Path $filePath))
    {
    throw "Path not found - "+$filePath
    }

    # Build auth header
    $base64AuthInfo = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(("{0}:{1}" -f $UserID, $password)))

    # Set proper headers
    $headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
    $headers.Add('Authorization',('Basic {0}' -f $base64AuthInfo))
    $headers.Add('Accept','application/json')
    $headers.Add('Content-Type','application/xml')

    $method="get"

    # Retrieve incident sys_id
    $incident_url=$Url+"/api/now/table/incident?number="+$incident
    $response = Invoke-RestMethod -Headers $headers -Method $method -Uri $incident_url -Proxy $Proxy -ProxyUseDefaultCredentials
    $sys_id=$response.result.sys_id

    # Retrieve attachment download link
    $download_url=$Url+"/api/now/attachment?table_sys_id="+$sys_id
    $response = Invoke-RestMethod -Headers $headers -Method $method -Uri $download_url -Proxy $Proxy -ProxyUseDefaultCredentials
    if($response.result.Count -le 0)
    {
        $output = "No attachments found for incident - "+$incident
    }
    else
    {
        $download_link = $response.result.download_link
        $fileName=$response.result.file_name

        $downloadPath=Join-Path -Path $filePath -ChildPath $fileName

        # Download the attachment file
        $securePassword = ConvertTo-SecureString $password -AsPlainText -Force
        $cred = New-Object System.Management.Automation.PSCredential ($UserID, $securePassword)  
        $webclientObj = New-Object System.Net.WebClient
        $webclientObj.Credentials=$cred
        $webclientObj.DownloadFile($download_link, $downloadPath)
        $output = "Download file path - "+$downloadPath
    }
    $scriptName = $MyInvocation.MyCommand.Name
    $currentDate= get-date
    $logFilePath= $PSScriptRoot+'\ServiceNow_Log.txt'
    $ErrorMessage =$scriptName + ' | ' + $currentDate + ' | ' + $output  | Add-Content $logFilePath 
    $output   
}
catch
{
    #To get script file name to append in log file
    $scriptName = $MyInvocation.MyCommand.Name
    $currentDate= get-date
    $logFilePath= $PSScriptRoot+'\ServiceNow_Log.txt'
    $ErrorMessage =$scriptName + ' | ' + $currentDate + ' | ' + $_.Exception.Message  | Add-Content $logFilePath
}