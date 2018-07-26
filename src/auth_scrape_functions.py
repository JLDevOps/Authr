import re

def Parse_Usr(line):
    usr = None
    try:
        if "Accepted password" in line or "Accepted publickey for" in line:
            usr = re.search(r'(\bfor\s)(\w+)', line)
            return usr.group(1)
        elif "sudo:" in line:
            usr = re.search(r'(sudo:\s+)(\w+)', line)
            return usr.group(1)
        # elif "authentication failure" in line:
        #     usr = re.search(r'USER=\w+', line)
        #     return usr.group(1)
        elif "for invalid user" in line:
            usr = re.search(r'(\buser\s)(\w+)', line)
            return usr.group(2)
        elif "Invalid user " in line:
            usr = re.search(r'(\buser\s)(\w+)', line)
            return usr.group(2)
        elif "Failed password for" in line:
            usr = re.search(r'\w+\s*for (.+)\s* from', line)
            return usr.group(1)
        elif "user=" in line:
            usr = re.search(r'(\buser=)(\w+)', line)
            return usr.group(2)
    except(Exception):
        return None

def Parse_IP(line):
    ip = None
    if "from " in line:
        ip = re.search(
            r'(\bfrom\s)(\b((\s*((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\s*)|(\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*)\b))',
            line)
        return ip.group(5)
    if "rhost=" in line:
        ip = re.search(
            r'(\b((\s*((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\s*)|(\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*)\b))',
            line)
        return ip.group(4)

    if ip is not None:
        return ip.group(5)


# parse a date from the line
def Parse_Date(line):
    date = re.search(r'^[A-Za-z]{3}\s*[0-9]{1,2}\s[0-9]{1,2}:[0-9]{2}:[0-9]{2}', line)
    if date is not None:
        return date.group(0)


# parse a command from a line
def Parse_Cmd(line):
    # parse command to end of line
    cmd = re.search(r'(\bCOMMAND=)(.+?$)', line)
    if cmd is not None:
        return cmd.group(2)

def Parse_Port(line):
    port = re.search(r'(port (.+) )', line)

    if port is not None:
        return re.sub(r',', "", str(port.group(2)))


def Parse_Current_Server(line):
    current_server = re.search(r'\s[0-9]{1,2}:[0-9]{2}:[0-9]{2} (.+)\s* sshd', line)
    if current_server is not None:
        return current_server.group(1)

def month_letter_to_num(abbr):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_num = months.index(abbr) + 1
    if 1 <= month_num <= 9:
        return ("0" + str(month_num))
    else:
        return str(month_num)

def Parse_Month(date):
    month = re.search(r'(\w((?:[a-z]+)))', date)
    return month.group(1)

def Parse_Day(date):
    day = re.search(r'\w+[a-z]\s*(\d+)', date)
    day_num = int(day.group(1))
    if 1 <= day_num <= 9:
        return ("0" + str(day_num))
    else:
        return str(day.group(1))

def Parse_Time(date):
    time = re.search(r'((\d+)[-:\/](\d+)[-:\/](\d+))',date)
    return time.group(1)

def Create_Datetime(line, year):
    date = Parse_Date(line)
    month = Parse_Month(date)
    month_num = month_letter_to_num(month)
    day = Parse_Day(date)
    time = Parse_Time(date)
    datetime = str(year) + "-" +str(month_num) + "-" +  str(day) + " " + str(time)
    return datetime


#For testing purposes:
def main():
    #log_string = "Jan  8 08:15:57 Jekyll-JLDevops sshd[2641]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser=daatat rhost=76.14.198.204"
    log_string = "authentication message:  Jan 10 22:08:00 Jekyll-JLDevops sshd[11814]: Invalid user admin from 120.7.187.105"
    print(Parse_IP(log_string))
    print(Parse_Usr(log_string))


if __name__ == "__main__":
    main()






