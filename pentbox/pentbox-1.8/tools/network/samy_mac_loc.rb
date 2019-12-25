=begin

    Copyright (C) 2011

    Alberto Ortega Llamas
    alberto.kun666[at]gmail[dot]com

    PenTBox (Penetration Testing Box)

    This file is part of PenTBox.

    PenTBox is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PenTBox is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with PenTBox.  If not, see <http://www.gnu.org/licenses/>.

=end

module Network_pb
class Samy_mac_loc_pb
def initialize()

# MAC address geolocation (samy.pl)
#

require "net/http"
require "uri"

url_sam1 = "http://samy.pl/mapxss/?mac="
# url_sam2 = "http://samy.pl/androidmap/index.php?mac=MAC_ADDR&commit=Probe"

puts ""
title "// MAC address geolocation (samy.pl) //"
puts ""
puts " Insert MAC address."
puts ""
puts " Example: be:be:be:be:be:be"
puts ""
print "   -> "
mac = gets_pb.chomp.gsub(":", "-")

begin
	url = URI.parse(url_sam1 + mac)
	http = Net::HTTP.new(url.host, url.port)
	resp = http.get(url.to_s)
	if resp.code == "200"
		data = resp.body.split("<div id=addy>")[1].split("</div>")[0].gsub("<br>", "\n") # Parsing body.
		puts data
	else
		puts ""
		puts " Error connecting to Samy's host."
		puts ""
	end
rescue
	puts ""
	puts " Error connecting to Samy's host."
	puts ""
end

end
end
end

