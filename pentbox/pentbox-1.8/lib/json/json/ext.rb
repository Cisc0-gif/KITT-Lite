require File.dirname(__FILE__) + '/common.rb'

module JSON
  # This module holds all the modules/classes that implement JSON's
  # functionality as C extensions.
  module Ext
    require File.dirname(__FILE__) + '/ext/parser.rb'
    require File.dirname(__FILE__) + '/ext/generator.rb'
    $DEBUG and warn "Using c extension for JSON."
    JSON.parser = Parser
    JSON.generator = Generator
  end

  JSON_LOADED = true
end
