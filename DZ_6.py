
# 1 in homework
class IpProcessing:
    def __init__(self, ips):
        self.ips = ips

    def get_ips_reverse(self):
        reversed_ips = []
        for i in self.ips:
            j = i.split('.')
            r = j[::-1]
            ip = r[0] + '.' + r[1] + '.' + r[2] + '.' + r[3]
            reversed_ips.append(ip)
        return reversed_ips

    def get_ips_without_first_octet(self):
        ips_missed_octet = []
        for i in self.ips:
            j = i.split('.')
            r = j[1:]
            ip = r[0] + '.' + r[1] + '.' + r[2]
            ips_missed_octet.append(ip)
        return ips_missed_octet

    def get_last_octet(self):
        last_octet = []
        for i in self.ips:
            j = i.split('.')
            r = j[-1]
            last_octet.append(r)
        return last_octet


ip_addresses = ["10.11.12.13", "10.11.12.14", "10.11.12.15"]
ip_processing = IpProcessing(ip_addresses)
print('original ip addresses: ', ip_addresses)
print('reversed ip addresses are:', ip_processing.get_ips_reverse())
print('ip addresses with missed first octet:', ip_processing.get_ips_without_first_octet())
print('only last octet of ip addresses:', ip_processing.get_last_octet())


#2 in home work

class FilesProcessing:
    def __init__(self, file_path):
        self.file_path = file_path


    def write(self, d):
        with open(self.file_path, 'w') as f:
            f.write(d)

    def read(self):
        with open(self.file_path, 'r') as f:
            print(f.read())

    def delete(self):
        with open(self.file_path, 'w') as f:
            f.truncate(0)



files_processing = FilesProcessing('new.txt')
files_processing.write(d="New data in the file")
files_processing.read()
files_processing.delete()



