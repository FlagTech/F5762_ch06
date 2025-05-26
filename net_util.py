from urllib.parse import urlparse
import ipaddress
import socket

def get_domain_name(url):
    netloc = urlparse(url).netloc
    domain = netloc.split(':')[0]  # 去除端口號
    return domain

def is_private_ip(ip):
    try:
        return ipaddress.ip_address(ip).is_private
    except ValueError:
        return False  # 不是合法IP
    
def is_ip(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False
    
def domain_points_to_private_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return is_private_ip(ip)
    except Exception:
        return False  # 無法解析的網域名稱
    
def is_private_url(url):
    address = get_domain_name(url)
    if is_ip(address):
        return is_private_ip(address)
    return domain_points_to_private_ip(address)

if __name__ == "__main__":
    # 測試函式
    url = input("請輸入網址：").strip()
    print(get_domain_name(url))
    print(is_private_url(url))
