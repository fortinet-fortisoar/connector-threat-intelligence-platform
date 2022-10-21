""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

import requests
from connectors.core.connector import get_logger, ConnectorError
logger = get_logger('threat-intelligence-platform')


class ThreatIntelligencePlatform(object):

    def __init__(self, config):
        self.server_url = config.get('server').strip()
        self.api_key = config.get('api_key')
        self.headers = {'accept': 'application/json', 'Authorization': self.api_key}
        if not self.server_url.startswith('https://'):
            self.server_url = 'https://{0}/'.format(self.server_url)

    def make_api_call(self, endpoint=None, method='GET', headers=None, health_check=False):
        url = self.server_url + endpoint
        logger.debug('Final url to make rest call is: {0}'.format(url))
        if headers:
            self.headers.update(headers)
        try:
            logger.debug('Making a request with {0} method and {1} headers.'.format(method, self.headers))
            response = requests.request(method, url, headers=self.headers)
            if response.status_code in [200]:
                if health_check:
                    return response
                try:
                    logger.debug(
                        'Converting the response into JSON format after returning with status code: {0}'.format(
                            response.status_code))
                    response_data = response.json()
                    return {'status': response_data['status'] if 'status' in response_data else 'Success', 'data': response_data}
                except Exception as e:
                    response_data = response.content
                    logger.error('Failed with an error: {0}. The response details are: {1}'.format(e, response_data))
                    return {'status': 'Failure', 'data': response_data}
            else:
                logger.error('Failed with response {0}'.format(response))
                raise ConnectorError(
                    {'status': 'Failure', 'status_code': str(response.status_code), 'response': response})
        except Exception as e:
            logger.exception(str(e))
            raise ConnectorError(str(e))

    def get_domain_infrastructure_analysis_details(self, params):
        endpoint = '/v1/infrastructureAnalysis?domainName={0}'.format(params.get('domain_name'))
        return self.make_api_call(endpoint=endpoint)

    def get_ssl_certificate_chain_details(self, params):
        endpoint = '/v1/sslCertificatesChain?domainName={0}'.format(params.get('domain_name'))
        return self.make_api_call(endpoint=endpoint)

    def get_ssl_configuration_analysis_details(self, params):
        endpoint = '/v1/sslConfiguration?domainName={0}'.format(params.get('domain_name'))
        return self.make_api_call(endpoint=endpoint)

    def get_domain_malware_check_details(self, params):
        endpoint = '/v1/malwareCheck?domainName={0}'.format(params.get('domain_name'))
        return self.make_api_call(endpoint=endpoint)

    def get_connected_domains_details(self, params):
        endpoint = '/v1/connectedDomains?domainName={0}'.format(params.get('domain_name'))
        return self.make_api_call(endpoint=endpoint)

    def get_domain_reputation_details(self, params):
        q_type = params.get('query_type')
        if q_type == 'V1':
            endpoint = '/v1/reputation?domainName={0}&mode={1}'.format(params.get('domain_name'), params.get('mode'))
        else:
            endpoint = '/v2/reputation?domainName={0}&mode={1}'.format(params.get('domain_name'), params.get('mode'))
        return self.make_api_call(endpoint=endpoint)


def _run_operation(config, params):
    tip_obj = ThreatIntelligencePlatform(config)
    command = getattr(ThreatIntelligencePlatform, params['operation'])
    response = command(tip_obj, params)
    return response


def _check_health(config):
    try:
        tip_obj = ThreatIntelligencePlatform(config)
        tip_obj.make_api_call(endpoint='/v1/infrastructureAnalysis?domainName=threatintelligenceplatform.com', health_check=True)
        return True
    except Exception as err:
        logger.exception('Health check failed with: {0}'.format(err))
        raise ConnectorError('Health check failed with: {0}'.format(err))
