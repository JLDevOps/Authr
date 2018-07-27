import argparse
import csv
import os

import auth_scrape_functions as asf
import map_functions as mf
import shodan_functions as sf

shodan_ip_info = {}


class authr():
    def __init__(self, log_file):
        self.auth_row_list = []
        self.log_file = log_file

    @staticmethod
    def set_shodan_api_environment(shodan_api_key):
        os.environ['SHODAN_API_KEY'] = str(shodan_api_key)

    def parse_auth_log(self, log_file):
        with open(log_file, encoding='utf-8') as file:
            for line in file:
                try:
                    self.auth_row_list.append(auth_marker(line))
                    print(auth_marker(line))
                except(Exception):
                    continue
        return self.auth_row_list

    @staticmethod
    def create_authr_map_with_markers(marker_list, output_filename):
        """Use file path + file name to create a google map html page with markers"""
        latitude = []
        longitude = []

        auth_marker_row = marker_list[0]
        gmap = mf.create_gmap(auth_marker_row.latitude, auth_marker_row.longitude)

        for index, auth_row in enumerate(marker_list):
            latitude.append(auth_row.latitude)
            longitude.append(auth_row.longitude)

        for index, auth_row in enumerate(marker_list):
            marked_map = mf.add_map_marker_list(gmap, latitude, longitude)

        if output_filename is None:
            mf.create_html_map(marked_map, "example-map.html")
        else:
            mf.create_html_map(marked_map, output_filename)

    @staticmethod
    def create_authr_map_with_scatter_plots(marker_list, output_filename, plot_hex_color=None):
        """Use file path + file name to create a google map html page with markers"""
        latitude = []
        longitude = []

        auth_marker_row = marker_list[0]
        gmap = mf.create_gmap(auth_marker_row.latitude, auth_marker_row.longitude)

        for index, auth_row in enumerate(marker_list):
            if (auth_row.latitude is None) or (auth_row.longitude is None):
                continue
            else:
                latitude.append(auth_row.latitude)
                longitude.append(auth_row.longitude)

        marked_map = mf.add_map_scatter_plots(gmap, latitude, longitude, plot_hex_color)

        if output_filename is None:
            mf.create_html_map(marked_map, "example-map.html")
        else:
            mf.create_html_map(marked_map, output_filename)

    @staticmethod
    def create_authr_map_with_polygon_plots(marker_list, output_filename, plot_color=None):
        """Use file path + file name to create a google map html page with polygon plot"""
        latitude = []
        longitude = []

        auth_marker_row = marker_list[0]
        gmap = mf.create_gmap(auth_marker_row.latitude, auth_marker_row.longitude)

        for index, auth_row in enumerate(marker_list):
            if (auth_row.latitude is None) or (auth_row.longitude is None):
                continue
            else:
                latitude.append(auth_row.latitude)
                longitude.append(auth_row.longitude)

        marked_map = mf.add_map_polygon_plots(gmap, latitude, longitude, plot_color)

        if output_filename is None:
            mf.create_html_map(marked_map, "example-map.html")
        else:
            mf.create_html_map(marked_map, output_filename)

    @staticmethod
    def create_authr_map_with_heatmap_plots(marker_list, output_filename):
        """Use file path + file name to create a google map html page with heatmap"""
        latitude = []
        longitude = []

        auth_marker_row = marker_list[0]
        gmap = mf.create_gmap(auth_marker_row.latitude, auth_marker_row.longitude)

        for index, auth_row in enumerate(marker_list):
            if (auth_row.latitude is None) or (auth_row.longitude is None):
                continue
            else:
                latitude.append(auth_row.latitude)
                longitude.append(auth_row.longitude)

        marked_map = mf.add_map_heatmap_plots(gmap, latitude, longitude)

        if output_filename is None:
            mf.create_html_map(marked_map, "example-map.html")
        else:
            mf.create_html_map(marked_map, output_filename)

    @staticmethod
    def create_authr_csv(marker_list, output_filename):
        """Create csv file with the authr information per row from log file"""
        header = ['IP', 'Authentication_Message', 'User', 'Port', 'Latitude', 'Longitude', 'City', 'Country',
                  'Postal_Code']
        with open(output_filename, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)
        csv_file.close()

        with open(output_filename, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for index, auth_row in enumerate(marker_list):
                try:
                    csv_writer.writerow(
                        [auth_row.ip, auth_row.authentication_message, auth_row.user, auth_row.port, auth_row.latitude,
                         auth_row.longitude, auth_row.city, auth_row.country, auth_row.postal_code])
                except(Exception):
                    pass
        csv_file.close()


class auth_marker():
    def __init__(self, auth_log_row):
        self.ip = asf.Parse_IP(str(auth_log_row))
        self.authentication_message = str(auth_log_row)
        self.user = asf.Parse_Usr(str(auth_log_row))
        self.port = asf.Parse_Port(str(auth_log_row))

        if str(self.ip) in shodan_ip_info:
            self.latitude = (shodan_ip_info[str(self.ip)]).latitude
            self.longitude = (shodan_ip_info[str(self.ip)]).longitude
            self.city = (shodan_ip_info[str(self.ip)]).city
            self.country = (shodan_ip_info[str(self.ip)]).country
            self.postal_code = (shodan_ip_info[str(self.ip)]).postal_code
        else:
            host_info = sf.get_shodan_call(self.ip)
            if host_info is not None:
                self.latitude = sf.get_latitude(host_info)
                self.longitude = sf.get_longitude(host_info)
                self.city = sf.get_city(host_info)
                self.country = sf.get_country_name(host_info)
                self.postal_code = sf.get_postal_code(host_info)
                shodan_ip_info[str(self.ip)] = auth_marker
            else:
                self.latitude = None
                self.longitude = None
                self.city = None
                self.country = None
                self.postal_code = None
                shodan_ip_info[str(self.ip)] = auth_marker

    def __repr__(self):
        print("latitude: ", str(self.latitude))
        print("longitude: ", str(self.longitude))
        print("city: ", str(self.city))
        print("country: ", str(self.country))
        print("postal code: ", str(self.postal_code))
        print("IP: ", str(self.ip))
        print("authentication message: ", str(self.authentication_message))
        print("user: ", str(self.user))
        print("port: ", str(self.port))


def main():
    parser = argparse.ArgumentParser(description='Scrape Auth Logs and Inserted into the DB')
    parser.add_argument('-a', '--auth', help='Auth Log', required=True)
    parser.add_argument('-k', '--key', help='Shodan Key', required=True)
    parser.add_argument('-f', '--filename', help='Filename and Path', required=False)
    parser.add_argument('-hm', '--heatmap', help='Heat Map', required=False, action='store_true')
    parser.add_argument('-c', '--csv', help='CSV', required=False)
    parser.add_argument('-s', '--scatter', help='Scatter Plot', required=False, action='store_true')
    parser.add_argument('-p', '--polygon', help='Polygon Plot', required=False, action='store_true')
    parser.add_argument('-m', '--marker', help='Marker Plot', required=False, action='store_true')

    args = vars(parser.parse_args())
    log_file_path = args['auth']
    shodan_api_key = args['key']
    filename = args['filename']
    csv_filename = args['csv']

    if filename is None:
        filename = 'example_map.html'


    authr.set_shodan_api_environment(shodan_api_key)
    marker_list = authr(log_file_path).parse_auth_log(log_file_path)

    if csv_filename:
        print("Csv created")
        authr.create_authr_csv(marker_list, csv_filename)

    if args['heatmap'] is True:
        authr.create_authr_map_with_heatmap_plots(marker_list, filename)

    if args['marker'] is True:
        authr.create_authr_map_with_markers(marker_list, filename)

    if args['polygon'] is True:
        authr.create_authr_map_with_polygon_plots(marker_list, filename)

    if args['scatter'] is True:
        authr.create_authr_map_with_scatter_plots(marker_list, filename)


if __name__ == "__main__":
    main()
