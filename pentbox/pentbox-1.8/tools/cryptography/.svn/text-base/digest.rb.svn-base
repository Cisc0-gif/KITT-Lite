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
class Digest_pb
def initialize()

# Multi Hash Digest (MD5, SHA1, SHA256, SHA384, SHA512, RIPEMD-160).
#

require "digest/md5"
require "digest/sha1"
require "digest/sha2"
require "digest/rmd160"

puts ""
title "// Multi-Digest (MD5, SHA1, SHA256, SHA384, SHA512, RIPEMD-160) //"
puts ""
puts " Insert string to digest."
puts ""
print "   -> "
word = gets_pb.chomp

puts ""
puts "MD5 = " + Digest::MD5.hexdigest(word)
puts ""
puts "SHA1 = " + Digest::SHA1.hexdigest(word)
puts ""
puts "SHA2 (256) = " + Digest::SHA256.hexdigest(word)
puts ""
puts "SHA2 (384) = " + Digest::SHA384.hexdigest(word)
puts ""
puts "SHA2 (512) = " + Digest::SHA512.hexdigest(word)
puts ""
puts "RIPEMD-160 = " + Digest::RMD160.hexdigest(word)
puts ""

end
end
end
