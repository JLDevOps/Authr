# Authr

A visualization tool that can extract information from authentication logs (auth.logs), reverse-search the data, and visualize the origination of the authentication attempts. 

The following information are extracted from the logs:
1. IP Address
2. Port Number
3. Username
4. Authentication Message

Once the information is extracted, each IP from the authentication attempt is checked with Shodan to get it's location data.  An HTML page is created with a map and pins (associated to each IP).

Here is a sample of the data on a heat map: 
***
![Heat Map](https://raw.githubusercontent.com/JLDevOps/Authr/master/Documentation/Images/heatmap-authr.png)

Here is a sample of the data on a heat map: 
***
![Heat Map](https://raw.githubusercontent.com/JLDevOps/Authr/master/Documentation/Images/marker-map.png)

** This tool scrapes authentication logs found via Linux servers (i.e. Ubuntu, Debian, etc.).  This may also be able to work with servers that are using fail2ban.

## Available Functions
The following functionality are currently available from Authr:
1. Create a CSV from authentication logs
2. Create an html heat map from the authentication logs 
3. Create an html scatter map from the authentication log data
4. Create an html map with markers from the authentication log data
5. Create an html map with a ploygon plot (connecting lines to each point) from the authentication log data

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.  You will be able to scrape your own authentication logs

### Prerequisites

#### Shodan

This tool heavily relies on [Shodan](https://shodan.io/) (search engine for Internet-connected devices) to find the location of an IP address.

Go [here](https://account.shodan.io/login) to sign up for an account and get an developer API key.

### Installations

The following steps go through installing Python dependencies and setting up the environment for the tool.

1. Install the Python modules for this tool
    ```
    $ cd Authr
    $ pip install -r requirements.txt
    ```
2. (Optionally) Install VirtualEnv to setup a separate Python environment for the project.
    ```
    $ pip install virtualenv
    $ virtualenv venv
    $ source venv/Scripts/activate
    ```

### Usage

#### Sample Code - Heat Map & CSV
Below is a code sample on how to generate a heat map and csv from your authentication log:

1. Place the following in a python file
    ```bash
        import authr, argparse, os
         
        def main():
            parser = argparse.ArgumentParser(description='Scrape Auth Logs and Inserted into the DB')
            parser.add_argument('-a', '--auth', help='Auth Log', required=True)
            parser.add_argument('-k', '--key', help='Shodan Key', required=True)
    
            args = vars(parser.parse_args())
            log_file_path = args['auth']
            shodan_api_key = args['key']
            
            full_path = os.path.dirname(os.path.abspath(__file__))
            full_log_file_path = full_path + log_file_path
            authr.set_shodan_api_environment(shodan_api_key)
            
            marker_list = authr(full_log_file_path).parse_auth_log(full_log_file_path)
            authr.create_authr_map_with_heatmap_plots(marker_list, "example_map.html")
            authr.create_authr_csv(marker_list, "example-csv.csv")
        
        if __name__ == "__main__":``
           main()
    ```
2. Run the following command
    ```bash
    $ python test.py -a {__path_to_authentication_log_file__} -k {__Shodan_API_Key__}
    ```
#### Using Authr via Terminal/Command Line
You can also run the authr.py file by itself, and provide arguments to what functionality you would like to use.

```bash
    $ python authr.py -a {__path_to_authentication_log_file__} -k {___Shodan_API_Key__}
```

Command Line / Terminal Arguments:
1. -a (Authentication File)
2. -k (Shodan API Key)
3. -f (Filename of your output file (also provide path))
4. -hm (Generate a heat map)
5. -c (Generate a csv)
6. -s (Generate a scatter plot map)
7. -p (Generate a polygon plot map)
8. -m (Generate a marker plot map)

Sample command to generate a heat map: 
```
    $ python authr.py -a \\example-logs\\auth-01-14-2018.log -k {___Shodan_API_Key__} -f example-map.html -hm
```

## Built With

* Python 3.6
* [Shodan](https://shodan.io/) - Search engine API for Internet-connected devices.
* [GMPLOT](https://github.com/vgm64/gmplot) - Used to generate maps with pins for the location of authentications.

## Background Information

This tool was created out of my interest regarding the amount of SSH authentication attempts made on one of my personal Linux servers.
  I was curious at where the attempts were coming from, and decided to scrape and reverse search the IP addresses from the auth logs.
This became more of a research project to figure out where and how attackers found my personal server.

## Authors

* **Jimmy Le** - [Jldevops](https://github.com/jldevops)


## License

Licensed under the [MIT License](LICENSE)
