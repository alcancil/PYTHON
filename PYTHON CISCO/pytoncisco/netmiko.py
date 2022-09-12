from netmiko import ConnectHandler
net_connect = ConnectHandler(
    device_type="cisco_xe",
    host="cisco5.domain.com",
    username="admin",
    password="password",
)