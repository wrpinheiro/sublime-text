import os

home = os.environ["HOME"]

os.environ["PATH"] = "%s/local/bin:%s/local/ruby/gems/bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin" % (home, home)
os.environ["GEM_HOME"] = "%s/local/ruby/gems" % (home)
os.environ["GEM_PATH"] = "%s/local/ruby/gems" % (home)

print ("PATH=%s" % os.environ["PATH"])
print ("GEM_HOME=%s" % os.environ["GEM_HOME"])
print ("GEM_PATH=%s" % os.environ["GEM_PATH"])
