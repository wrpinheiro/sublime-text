import sublime, sublime_plugin
from os import environ

def plugin_loaded():
  home = environ["HOME"]

  environ["PATH"] = "%s/local/bin:./node_modules/.bin:./bin:%s/local/ruby/gems/bin:%s/local/node/npm/bin:%s/local/ruby/current/bin:%s/.bash/bin:%s/.zsh/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin" % (home, home, home, home, home, home)
  environ["GEM_HOME"] = "%s/local/ruby/gems" % (home)
  environ["GEM_PATH"] = environ["GEM_HOME"]

  print ("PATH=%s" % environ["PATH"])
  print ("GEM_HOME=%s" % environ["GEM_HOME"])
  print ("GEM_PATH=%s" % environ["GEM_PATH"])
