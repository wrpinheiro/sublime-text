import os

os.environ["PATH"] = "/Users/fnando/local/bin:/Users/fnando/local/ruby/gems/bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
os.environ["GEM_HOME"] = "/Users/fnando/local/ruby/gems"
os.environ["GEM_PATH"] = "/Users/fnando/local/ruby/gems"
print ("PATH=%s" % os.environ["PATH"])
print ("GEM_HOME=%s" % os.environ["GEM_HOME"])
print ("GEM_PATH=%s" % os.environ["GEM_PATH"])
