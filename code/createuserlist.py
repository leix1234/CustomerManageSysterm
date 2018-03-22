import sys
import cPickle as p
import os

userlistfile = './config/userlist.dat'

userlist = {
    'admin':'admin',
    'xiaolei':'hhuc20072210',
    'sunjingru':'850620'
}

if True == os.path.isfile(userlistfile):
    print 'file is exist'
else:
    f = file(userlistfile,'w')
    p.dump(userlist,f)
    f.close()
    print 'create user list success'
    f2 = file(userlistfile)
    storeduserlist = p.load(f2)
    f2.close()
    print 'storeduserlist:', storeduserlist


