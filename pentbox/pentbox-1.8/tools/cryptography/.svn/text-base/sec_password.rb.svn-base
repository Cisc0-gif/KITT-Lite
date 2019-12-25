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
class Sec_password_pb
def initialize()

# This program generates secure passwords against bruteforce or diccionary attacks.
#

puts ""
title "// Secure Password Generator //"
puts ""
puts " Insert one word familiar to you, or a short phrase (name, country ...)."
puts "           For example, a name -> madrid"
puts "                   Or a phrase -> hello world"
puts ""
print "   -> "
$familiar = gets_pb.chomp

def sub(original, subs)
	$familiar = $familiar.gsub(original, subs)
end

sub(" ", "_")
puts ""
puts ""
puts "Low security -> " + $familiar + rand(100).to_s
puts ""

$familiar = $familiar.capitalize
puts "Medium security -> " + rand(500).to_s + "_" + $familiar + "_" + rand(500).to_s
puts ""

sub("a", "@")
puts "High security -> " + "." + rand(1000).to_s + "._" + $familiar + "_." + rand(1000).to_s + "."
puts ""

sub("e", "3")
sub("t", "7")
sub("o", "0")
randomlet = rand(5)
case randomlet
	when 0
		randomlet = "!"
	when 1
		randomlet = "="
	when 2
		randomlet = "*"
	when 3
		randomlet = "#"
	when 4
		randomlet = "$"
end
puts "Ultra High security -> " + randomlet + "~" + rand(5000).to_s + "._." + $familiar + "._." + rand(5000).to_s + "~" + randomlet
puts ""

# Erase variables from memory.
$familiar = "1" * $familiar.length
randomlet = "1"
$familiar = "0" * $familiar.length
randomlet = "0"
$familiar = "\xFF" * $familiar.length
randomlet = "\xFF"
$familiar = "\x00" * $familiar.length
randomlet = "\x00"

end
end
end
