require File.dirname(__FILE__) + '/json/common.rb'
module JSON
  require File.dirname(__FILE__) + '/json/version.rb'

  begin
    require File.dirname(__FILE__) + '/json/ext.rb'
  rescue LoadError
    require File.dirname(__FILE__) + '/json/pure.rb'
  end
end
