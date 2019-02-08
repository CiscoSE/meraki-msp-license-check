# meraki-msp-license-check

## Description
This sample code can be used in a MSP enviroment to validate the license expiration date for different Meraki organizations.

## Prerequisites
Enable API access and obtain an API key to allow access to the organizations. For more information you can reference https://documentation.meraki.com/zGeneral_Administration/Other_Topics/The_Cisco_Meraki_Dashboard_API 

Example:

	Enter your Dashboard API key: <API_KEY>
  	[{'id': 533665, 'name': 'Scott'}, {'id': 653307, 'name': 'Home'}]
  	1: 533665: Scott
  	2: 653307: Home
  	Select an org: 1
  	You are good until  : Apr 2, 2021 UTC
