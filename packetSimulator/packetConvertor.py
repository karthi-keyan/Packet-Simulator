protocol = {'udp': 0, 'icmp': 1, 'tcp': 2}
service  = {'time': 0, 'remote_job': 1, 'netbios_dgm': 2, 'eco_i': 3, 'csnet_ns': 4, 'finger': 5, 'nnsp': 6, 'ldap': 7, 'netstat': 8, 'red_i': 9, 'urp_i': 10, 'supdup': 11, 'courier': 12, 'exec': 13, 'discard': 14, 'systat': 15, 'pop_3': 16, 'http': 17, 'name': 18, 'echo': 19, 'netbios_ns': 20, 'ssh': 21, 'efs': 22, 'bgp': 23, 'tim_i': 24, 'X11': 25, 'http_443': 26, 'iso_tsap': 27, 'smtp': 28, 'daytime': 29, 'printer': 30, 'private': 31, 'pm_dump': 32, 'sunrpc': 33, 'login': 34, 'rje': 35, 'telnet': 36, 'domain': 37, 'Z39_50': 38, 'klogin': 39, 'gopher': 40, 'domain_u': 41, 'nntp': 42, 'pop_2': 43, 'other': 44, 'ftp_data': 45, 'ctf': 46, 'mtp': 47, 'auth': 48, 'uucp': 49, 'vmnet': 50, 'IRC': 51, 'hostnames': 52, 'shell': 53, 'netbios_ssn': 54, 'ecr_i': 55, 'sql_net': 56, 'uucp_path': 57, 'ftp': 58, 'urh_i': 59, 'ntp_u': 60, 'kshell': 61, 'link': 62, 'whois': 63, 'imap4': 64, 'http_8001': 65}
flag     = {'REJ': 0, 'RSTR': 1, 'S1': 2, 'S2': 3, 'RSTO': 4, 'S0': 5, 'S3': 6, 'SH': 7, 'SF': 8, 'OTH': 9, 'RSTOS0': 10}

features= ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'class']


def convertPacket(packet):
        convertedPacket=[]
        convertedPacketTemp=[]
        for i,each in enumerate(packet):
                if i==0:
                        convertedPacket.append(eval(each.split('\'')[1]))
                elif i==40:
                        convertedPacket.append(eval(each.split('\'')[0]))
                elif i==1:
                        convertedPacketTemp.append(protocol[each])
                elif i==2:
                        convertedPacketTemp.append(service[each])
                elif i==3:
                        convertedPacketTemp.append(flag[each])
                elif features[i]=="num_outbound_cmds" or features[i]=="is_host_login":
                        pass
                else:
                        convertedPacket.append(eval(each))
        convertedPacket+=convertedPacketTemp
        return convertedPacket


