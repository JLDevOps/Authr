import argparse
import os

import shodan

def host_info_search(api, host):
    host = api.host(host)
    return host


def get_shodan_call(ip):
    api = shodan.Shodan(str(os.environ['SHODAN_API_KEY']))
    try:
        host_info = api.host(ip)
        return host_info
    except:
        return None


def get_ip(host_info):
    # print(host_info.get('ip_str', 'n/a'))
    return host_info.get('ip_str', 'n/a')


def get_organization(host_info):
    # print(host_info.get('org','n/a'))
    return host_info.get('org', 'n/a')


def get_latitude(host_info):
    # print(host_info.get('latitude', 'n/a'))
    return host_info.get('latitude', 'n/a')


def get_longitude(host_info):
    # print(host_info.get('longitude', 'n/a'))
    return host_info.get('longitude', 'n/a')


def get_postal_code(host_info):
    # print(host_info.get('postal_code', 'n/a'))
    return host_info.get('postal_code', 'n/a')


def get_country_name(host_info):
    # print(host_info.get('country_name', 'n/a'))
    return host_info.get('country_name', 'n/a')


def get_city(host_info):
    # print(host_info.get('city', 'n/a'))
    return host_info.get('city', 'n/a')


def get_hostnames(host_info):
    # print(host_info.get('hostnames', 'n/a'))
    return host_info.get('hostnames', 'n/a')


def get_port(host_info):
    for item in host_info['data']:
        print("""Port: %s """ % (item['port']))
    return item['port']

#
# def main():
#     """
#     Main function allows for Shodan API testing
#     """
#     parser = argparse.ArgumentParser(description='Searching for Host information')
#     parser.add_argument('-ip', '--host', help="IP Address", required=True)
#     args = vars(parser.parse_args())
#     host = args['host']
#     host_info = get_shodan_call(host)
#     # host_info = host_info_search(api,host)
#
#     get_ip(host_info)
#     get_hostnames(host_info)
#     get_port(host_info)
#     get_organization(host_info)
#     get_latitude(host_info)
#     get_longitude(host_info)
#     get_city(host_info)
#     get_country_name(host_info)
#     get_postal_code(host_info)
#
#
# if __name__ == "__main__":
#     main()
