from gmplot import gmplot


def create_gmap(latitude, longitude, zoom=5):
    if latitude or longitude is None:
        return gmplot.GoogleMapPlotter(37.771269, -122.511015, zoom)
    else:
        return gmplot.GoogleMapPlotter(latitude, longitude, zoom)


def add_map_marker_list(gmap, latitude_list, longitude_list):
    # Uses list composed of latitude and longitude to create markers from for plotting.
    for lat, long in zip(latitude_list, longitude_list):
        if lat is None:
            continue
        elif long is None:
            continue
        else:
            gmap.marker(lat, long, 'cornflowerblue')
            # print(lat, long)
    return gmap


def add_map_scatter_plots(gmap, latitude_list, longitude_list, plot_hex_color=None):
    # Uses list to create scatter plots on gmap
    if plot_hex_color is None:
        gmap.scatter(latitude_list, longitude_list, '#3B0B39', size=40, marker=False)
    else:
        gmap.scatter(latitude_list, longitude_list, plot_hex_color, size=40, marker=False)

    return gmap


def add_map_polygon_plots(gmap, latitude_list, longitude_list, plot_color=None):
    # Uses list to create polygon plots on gmap
    if plot_color is None:
        gmap.plot(latitude_list, longitude_list, 'cornflowerblue', edge_width=1)
    else:
        gmap.plot(latitude_list, longitude_list, plot_color, edge_width=1)
    return gmap


def add_map_heatmap_plots(gmap, latitude_list, longitude_list):
    gmap.heatmap(latitude_list, longitude_list)
    return gmap


def create_html_map(gmap, filename):
    gmap.draw(filename)

# def main():
#     Sample code to generate an html map with a marker
#     latitude_list = [37.766956, 51.766956, 65.23445]
#     longitude_list = [-122.438481, -102.438481, 100.766956]
#     gmap = create_gmap(37.766956, -122.438481)
#     gmap = add_map_marker(gmap, latitude_list, longitude_list)
#     create_html_map(gmap, 'auth-01-14-2018.log')
#
#
# if __name__ == "__main__":
#     main()
