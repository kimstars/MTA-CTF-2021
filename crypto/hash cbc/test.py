from os import urandom
import hashlib
import string

class HashCBC:

    def __init__(self):
        self.key = str(urandom(16))
    def make_iv(self, iv, key):
        iv = hashlib.md5((iv + key).encode()).hexdigest()
        new_iv = 0
        for i in range(0, len(iv), 2):
            new_iv += int(iv[i:i+2], 16)
        return str(new_iv)

    def encrypt1(self, m):
        c = hashlib.md5(("2296" + m).encode()).hexdigest()
        return c
    def encrypt2(self, m):
        c = hashlib.md5(("2090" + m).encode()).hexdigest()
        return c
enc = HashCBC()

cipher = ['5fff5a11d3ed1acb0c34a7007b3f3de5', '133daec3294b0e4a2aaf5ccfa374f44e', '0379852a3ae7c1b1a22704ae0f614144', '5e315d0e2aaf4142a26cff928eee2215', 'bceceee2446416f962ce5b159d02b7a3', 'cac9c4b4f4d40e31d19ac235b50af3e0', '798c3a7103a879f7d659f6c6effac180', '62a9d2901041f3dce717edfdf51becf3', 'f4f7e3d9b725c14cad73b20a1d8cce26', '6189ad857261967553d4a295e5c10f4c', '0143af12f26686865b730221b977a70b', 'aedbd4d0b6767e1cc3a848a696bb6912', 'b8e2f65ebf6d13c80d133b1342696f51', '9ae32e24ccba2eab019450c7897dcc0a', 'b28401a822c54786d52fce34b412e071', '9c4bead0e5d9e97435458a9a2141f3b6', 'b7802150816b6a4ac94ff2ef2dfb81ad', 'ea0ed237d29c01e6398d56e324e7d993', 'f4f7e3d9b725c14cad73b20a1d8cce26', 'ea0ed237d29c01e6398d56e324e7d993', 'faebfe7ca1cd2a99e76d987311ef1de1', 'd4aebb5db70ef374e9bbf984b99a01db', '3b893d0bdee6c5a631dc68b698100410', '9ae32e24ccba2eab019450c7897dcc0a', 'ebbfdf852d4becc529375fa87783fe8d', '9c4bead0e5d9e97435458a9a2141f3b6', '2cea4769497b4eeb0200f7a4e1dca424', '9b3463366857067ed6a55a68d11781b2', 'd7b8cb6279511f54c26d98b8467d94fa', 'cac9c4b4f4d40e31d19ac235b50af3e0', '4acfc9989c972e201be248fccd295de4', '481fde2e0fd6da6630140504a9424ef4', '37cf67e2134db29695707ba7688e09ad', '6189ad857261967553d4a295e5c10f4c', '01808c27c783da5e2ae029078666c7d7', 'b7d22a77eba105deb41a339c81ae3980']
flag  = ""
for c in cipher:
    for s in string.printable:
        en = enc.encrypt1(s)
        en1 = enc.encrypt2(s)
        if(en == c or en1 == c):
            flag += s
            break
        
            
            
print(flag)
