TODO: make some real examples so people know wtf is going on


#c = Provisor("the_provisor_ldap_password")
#print c.whoami()
#print c.list_users()
#print c.list_groups()
#print c.user_exists("deleriux")
#print c.user_exists("nothing")
#print c.next_uid()
#c.add_group("somegroup", c.next_gid())
#c.del_group("somegroup")
#print c.is_group_member("sudo", "deleriux")
#print c.is_group_member("sudo", "bobby")
#print c.list_group_members("sudo")
#c.add_group_member("sudo", "deleriux")
#c.add_group_member("sudo", "jimmeh")
#c.add_group_member("sudo", "lrvick")
#c.del_group_member("sudo", "jimmeh")
#c.add_user("deleriux2", "abc123", password="someuserpassword")
#c.del_user("deleriux2")
#c.modify_user("deleriux", pubkey="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC2d7b7gu6v86gGp4zYzPX+ZhCbrPuFqSzRNXqWH+YZ9BOwlg5z1Dh61hSxqL/FhIsg3Y8w3Wc5/wUlBevW2hFmea2T4CkDetYAZuKHM2rUdCn7GufdSDPzhCkDPFPtILPp1wa18SC4DHGeFcPl3J8k/BDQOiIxnaY4e1mVk/2dHxUjTmXKMby6IfhsdCgSK5Vub+m/P1EKYT8pL2OeA1byzb0xKtLu7ALKTlnmgzEjo2bi5h4Pfreuu+0sQxlb9l65CH+oF4PHZKG13a8OVuz6nudMXBuNrqdLWAJgbvQ7QeZ0clcSsZEV7I8IYFKvhg+V/BihxCSnSaDYlYOWx0nHqrG2z7ERGnXRu1h11+TlmrtA3U0ws1XPCzO6F6Y0orEOzijW1lTQSBv3ec9T3YbK58zCYn9eDMHyAqXhpVx6nZkM01+f93UYBO5QwzMmIoX5KSt1ZfEDvpFjrZE7d3EZu+f4U/ETAN58NPvubL7Zqqsxn+5P11+opQDa7CnVH7bRs04MkIYjO7ofYMKDBx7VGmGjh0/3WNUBfNXahKIS+vq6yUYzZ/eJg7ONvG+4Q6exg6NFxV1GO9DB+RDp1aJcaMhaQ8z6oMhHixX2LMlbrRSWs8EypG+jgcfIZxImp8ODVC9D4t2Ec3AI10STaU9qNKnxQShtie108w+jD0J0Sw== matthew@home.localdomain")
#del(c)
