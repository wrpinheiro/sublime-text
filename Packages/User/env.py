import os

home = os.environ["HOME"]

os.environ["PATH"] = "%s/local/bin:%s/local/ruby/gems/2.1/bin:%s/local/node/npm/bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin" % (home, home, home)
os.environ["GEM_HOME"] = "%s/local/ruby/gems/2.1" % (home)
os.environ["GEM_PATH"] = os.environ["GEM_HOME"]

print ("PATH=%s" % os.environ["PATH"])
print ("GEM_HOME=%s" % os.environ["GEM_HOME"])
print ("GEM_PATH=%s" % os.environ["GEM_PATH"])
