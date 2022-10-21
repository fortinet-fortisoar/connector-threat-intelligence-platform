## About the connector
Threat Intelligence Platform combines several threat intelligence sources to provide in-depth insights on threat hosts and attack infrastructure.This connector facilitates automated operations to pull off real-time host configuration analysis to come up with actionable threat intelligence that is vital in detection, mitigation, and remediation.
<p>This document provides information about the Threat Intelligence Platform Connector, which facilitates automated interactions, with a Threat Intelligence Platform server using FortiSOAR&trade; playbooks. Add the Threat Intelligence Platform Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Threat Intelligence Platform.</p>

### Version information

Connector Version: 1.0.0


Authored By: spryIQ.co

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-threat-intelligence-platform`

## Prerequisites to configuring the connector
- You must have the URL of Threat Intelligence Platform server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Threat Intelligence Platform server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Threat Intelligence Platform</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>URL of the Threat Intelligence Platform connector to access the connector website.<br>
<tr><td>API key<br></td><td>Provide API token, used for user authentication.<br>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Domain Infrastructure Analysis Details<br></td><td>Retrieved information for a given domain name, get a collection of its web, mail, and name servers as well as its known subdomains. For each infrastructure entry, find out its IP address, geolocation, and subnetwork information.<br></td><td>domain_infrastructure_analysis_details <br/>Investigation<br></td></tr>
<tr><td>Get SSL Certificate Chain Details<br></td><td>Retrieved information for a given domain name, get detailed information about its SSL Certificate and the complete SSL Certificate chain.<br></td><td>ssl_certificate_chain_details <br/>Investigation<br></td></tr>
<tr><td>Get SSL Configuration Analysis Details<br></td><td>Retrieved information for a given domain name, establish and test SSL connection to the host and analyze how it is configured - to detect common configuration issues potentially leading to vulnerabilities.<br></td><td>ssl_configuration_analysis_details <br/>Investigation<br></td></tr>
<tr><td>Get Domain Malware Check Details<br></td><td>Retrieved information for a given domain name,check if it is considered to be dangerous in different security data sources. Dangerous domains could be related to a malware distribution network or host a malicious code.<br></td><td>domain_malware_check_details <br/>Investigation<br></td></tr>
<tr><td>Get Connected Domains Details<br></td><td>Retrieve a list of domain names resolving to a given domain name, including subdomains. Make sure the website does not share the IP address with malicious domains, as that may result in over blocking – a situation when a blocked malicious site also blocks other sites with the same IP. Research the infrastructure of connected domains.<br></td><td>connected_domains_details <br/>Investigation<br></td></tr>
<tr><td>Get Domain Reputation  Details<br></td><td>Evaluate a domain's reputation based on numerous security data sources as well as on an instant host's audit procedure. For a given domain name or IPv4 address, collect and evaluate over 120 parameters and calculate the resulting reputation score.<br></td><td>domain_reputation_details <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Get Domain Infrastructure Analysis Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Domain Name<br></td><td>Required domain name whose geolocation data needs to be retrieved.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "domainName": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "resourceType": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ipv4": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "geolocation": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "subnetwork": {}
</code><code><br>}</code>

### operation: Get SSL Certificate Chain Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Domain Name<br></td><td>Required domain name whose geolocation data needs to be retrieved.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "chainHierarchy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "commonName": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "validFrom": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "validTo": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "serialNumber": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "signatureAlgorithm": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "subject": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "issuer": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "purposes": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "purposesCA": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "publicKey": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "extensions": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "certificatePEM": ""
</code><code><br>}</code>

### operation: Get SSL Configuration Analysis Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Domain Name<br></td><td>Required domain name whose geolocation data needs to be retrieved.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "hasWarnings": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "testResults": {}
</code><code><br>}</code>

### operation: Get Domain Malware Check Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Domain Name<br></td><td>Required domain name whose geolocation data needs to be retrieved.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "safeScore": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "warningDetails": []
</code><code><br>}</code>

### operation: Get Connected Domains Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Domain Name<br></td><td>Required domain name whose geolocation data needs to be retrieved.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "numberOfDomains": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "domains": []
</code><code><br>}</code>

### operation: Get Domain Reputation  Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Domain Name<br></td><td>Required domain name whose geolocation data needs to be retrieved.<br>
</td></tr><tr><td>Mode<br></td><td>Select the type of query that is how you want to perform  'fast' or 'full'. Only select test codes will run—i.e., 62 WHOIS Domain Status, 82 Malware Databases Check, 87 SSL certificate validity, and 93 WHOIS Domain Check—while other tests and data collectors will be disabled and in full mode all tests will be performed, similar to what the TIP GUI displays.<br>
</td></tr><tr><td>Query Type<br></td><td>Select the type of query that is how you want to perform get domain operation the v2 API version differs from the v1 only in the output format.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "mode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "reputationScore": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "testResults": []
</code><code><br>}</code>
## Included playbooks
The `Sample - threat-intelligence-platform - 1.0.0` playbook collection comes bundled with the Threat Intelligence Platform connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Threat Intelligence Platform connector.

- Get Domain Infrastructure Analysis Details
- Get SSL Certificate Chain Details
- Get SSL Configuration Analysis Details
- Get Domain Malware Check Details
- Get Connected Domains Details
- Get Domain Reputation  Details

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
