=begin

    Copyright (C) 2009, 2010

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

module Cryptogr_pb
class Base64_pb
def initialize()

# Base64 encoder/decoder.
#

require "base64"

puts ""
title "// Base64 Encoder & Decoder //"
puts ""
puts " Insert string to encode or decode."
puts ""
print "   -> "
word = gets_pb.chomp

puts ""
puts "Encoded -> " + Base64.encode64(word)
puts ""
puts "Decoded -> " + Base64.decode64(word)
puts ""

end
end
end
