# A Convenience to load all field classes and yaml handling.

if "a"[0].kind_of? Fixnum
  unless Fixnum.methods.include? :ord
    class Fixnum
      def ord; self; end
    end
  end
end

require File.dirname(__FILE__) + '/bit-struct/bit-struct.rb'
require File.dirname(__FILE__) + '/bit-struct/fields.rb'
require File.dirname(__FILE__) + '/bit-struct/yaml.rb'

