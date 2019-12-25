#require 'rubygems'
require 'cgi'
require File.dirname(__FILE__) + '/../../../json/json.rb'
require 'net/http'

module Shodan
  
  # The WebAPI class interfaces with the shodanhq.com/api
  # It currently supports 2 methods:
  # 1. search (query)
  # 2. host (ip)
  #
  # Author:: achillean (mailto:jmath at surtri.com)
  #
  # :title:Shodan::WebAPI
  class WebAPI
    attr_accessor :api_key
    attr_accessor :base_url
    attr_accessor :exploitdb
    
    def initialize(api_key)
      @api_key = api_key
      @base_url = "http://www.shodanhq.com/api/"
      @exploitdb = ExploitDB.new(self)
    end
    
    # Internal method that sends out the HTTP request.
    # Expects a webservice function (ex. 'search') name and a hash of arguments.
    def request(func, args)
      # Convert the argument hash into a string
      args_string = args.map{|k, v| "#{CGI.escape(k.to_s)}=#{CGI.escape(v)}"}.join("&")
        
      # Craft the final request URL
      url = "#{@base_url}#{func}?key=#{@api_key}&#{args_string}"
      
      # Send the request
      response = Net::HTTP.get_response(URI.parse(url))
      
      # Convert the JSON data into a native Ruby hash
      data = JSON.parse(response.body)
      
      # Raise an error if something went wrong
      if data.has_key? 'error'
        raise data['error']
      end
      
      return data
    end
    
    # Get all available information on an IP.
    #
    # Arguments:
    # ip  - host IP (string)
    #
    # Returns a hash containing the host information
    def host(ip)
      return request('host', {:ip => ip})
    end
    
    # Perform a search on Shodan.
    #
    # Arguments:
    # query - search query; same format as the website (string)
    #
    # Returns a hash containing the search results
    def search(query)
      return request('search', {:q => query})
    end
  end
  
  # The ExploitDB class depends shouldn't be used independently,
  # as it depends on the WebAPI class.
  #
  # Author:: achillean (mailto:jmath at surtri.com)
  #
  # :title:Shodan::ExploitDB
  class ExploitDB
    attr_accessor :api
    
    def initialize(api)
      @api = api
    end
    
    # Download the exploit code from the ExploitDB archive.
    # 
    # Arguments:
    # id    -- ID of the ExploitDB entry
    # 
    # Returns:
    # A hash with the following fields:
    # filename        -- Name of the file
    # content-type    -- Mimetype
    # data            -- Contents of the file
    def download(id)
      return @api.request('exploitdb/download', {:id => "#{id}"})
    end
    
    # Search the ExploitDB archive.
    #    
    # Arguments:
    # query     -- Search terms
    #
    # Optional arguments:
    # author    -- Name of the exploit submitter
    # platform  -- Target platform (e.g. windows, linux, hardware etc.)
    # port      -- Service port number
    # type      -- Any, dos, local, papers, remote, shellcode and webapps
    #
    # Returns:
    # A dictionary with 2 main items: matches (list) and total (int).
    # Each item in 'matches' is a dictionary with the following elements:
    #
    # id
    # author
    # date
    # description
    # platform
    # port
    # type
    def search(query, params={})
      params[:q] = query
      return @api.request('exploitdb/search', params)
    end
    
  end
  
end
