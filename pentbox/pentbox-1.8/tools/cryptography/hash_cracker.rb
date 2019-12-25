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
class Hash_cracker_pb
def initialize()

# Hash Password Cracker (MD5, SHA1, SHA256, SHA384, SHA512, RIPEMD-160).
#

require "digest/md5"
require "digest/sha1"
require "digest/sha2"
require "digest/rmd160"

puts ""
title "// Hash Password Cracker (MD5, SHA1, SHA256, SHA384, SHA512, RIPEMD-160) //"
puts ""
puts " Insert hash to crack."
puts ""
print "   -> "
hash = gets_pb.chomp.downcase
puts ""
puts " Select type of hash that you inserted."
puts ""
puts "1 - MD5"
puts "2 - SHA1"
puts "3 - SHA256"
puts "4 - SHA384"
puts "5 - SHA512"
puts "6 - RIPEMD-160"
puts ""
print "  -> "
type = gets_pb.chomp
puts ""
puts " Select method to crack."
puts ""
puts "1 - Numbers bruteforce"
puts "2 - Dictionary attack"
puts "3 - Dictionary-bruteforce hybrid attack [exhaustive]"
puts ""
print "  -> "
how = gets_pb.chomp
if how == "2" || how == "3"
	puts ""
	puts " Insert dictionary file to use."
	puts ""
	puts "Default: */pentbox/other/pentbox-wlist.txt"
	puts ""
	print "  -> "
	dicf = gets_pb.chomp.gsub("\"", "").gsub("'", "")
	if dicf == ""
		dicf = "#{File.dirname(__FILE__)}/../../other/pentbox-wlist.txt"
	end
	begin
		$dict = File.open(dicf, "r")
	rescue
		puts ""
		puts "Error opening dictionary #{dicf}"
		puts ""
		exit
	end
end

puts ""

def cracknum(algorit, hash)
	puts "[*] Working"
	$cracked = false
	Thread.new do # One thread to compare possibilities.
		$num = 0
		while hash != algorit.hexdigest($num.to_s)
			$num += 1
		end
		$cracked = true
	end
	while $cracked == false # And the principal thread to show the status.
		STDOUT.flush
		print "\r[*] Trying #{$num.to_s}"
		sleep(0.1)
	end
	puts ""
	puts ""
	puts "[*] Cracked password -> #{$num.to_s}"
	puts ""
end

def crackdic(algorit, hash)
	puts "[*] Working"
	$cracked = "?"
	thread = Thread.new do # One thread to read the dictionary and compare possibilities.
		while $word = $dict.gets
			begin
				if hash == algorit.hexdigest($word.chomp)
					$cracked = "y"
					thread.kill
				end
			rescue
			end
		end
		$cracked = "n"
	end
	while $cracked == "?" # And the principal thread to show the status.
		STDOUT.flush
		begin
			print "\r[*] Trying #{$word.chomp}" + " "*15
		rescue
		end
		sleep(0.1)
	end
	puts ""
	if $cracked == "y"
		puts ""
		puts "[*] Cracked password -> #{$word}"
		puts ""
	else
		puts ""
		puts "[*] Dictionary finished, password not found."
		puts ""
	end
end

def crackdichyb(algorit, hash)
	puts "[*] Working"
	$cracked = "?"
	$thread = Thread.new do # One thread to read the dictionary, modify words and compare possibilities.
		while $word = $dict.gets
			begin
				$wordcomp = $word.chomp
			rescue
			end
			Thread.new do # New thread to improve performance in this comparisons.
				if hash == algorit.hexdigest($wordcomp)
					$password = $wordcomp
					$cracked = "y"
					$thread.kill
				end
			end
			if hash == algorit.hexdigest($wordcomp.upcase)
				$password = $wordcomp.upcase
				$cracked = "y"
				$thread.kill
			end
			if hash == algorit.hexdigest($wordcomp.downcase)
				$password = $wordcomp.downcase
				$cracked = "y"
				$thread.kill
			end
			brutecont_t = 0
			Thread.new do # New thread to improve performance in this comparisons.
				100.times do
					begin
						if hash == algorit.hexdigest("#{$word.chomp}#{brutecont_t.to_s}")
							$password = "#{$word.chomp}#{brutecont_t.to_s}"
							$cracked = "y"
							$thread.kill
						end
					rescue
					end
					brutecont_t += 1
				end
			end
			brutecont = 0
			100.times do
				if hash == algorit.hexdigest("#{$wordcomp}#{brutecont.to_s}".upcase)
					$password = "#{$wordcomp}#{brutecont.to_s}".upcase
					$cracked = "y"
					$thread.kill
				end
				brutecont += 1
			end
			brutecont = 0
			100.times do
				if hash == algorit.hexdigest("#{$wordcomp}#{brutecont.to_s}".downcase)
					$password = "#{$wordcomp}#{brutecont.to_s}".downcase
					$cracked = "y"
					$thread.kill
				end
				brutecont += 1
			end
		end
		$cracked = "n"
	end
	while $cracked == "?" # And the principal thread to show the status.
		STDOUT.flush
		print "\r[*] Trying #{$wordcomp}" + " "*15
		sleep(0.1)
	end
	puts ""
	if $cracked == "y"
		puts ""
		puts "[*] Cracked password -> #{$password}"
		puts ""
	else
		puts ""
		puts "[*] Dictionary finished, password not found."
		puts ""
	end
end

case type
	when "1"
		case how
			when "1"
				cracknum(Digest::MD5, hash)
			when "2"
				crackdic(Digest::MD5, hash)
			when "3"
				crackdichyb(Digest::MD5, hash)
			else
				puts ""
				puts "Invalid method to crack."
				puts ""
			end
	when "2"
		case how
			when "1"
				cracknum(Digest::SHA1, hash)
			when "2"
				crackdic(Digest::SHA1, hash)
			when "3"
				crackdichyb(Digest::SHA1, hash)
			else
				puts ""
				puts "Invalid method to crack."
				puts ""
			end
	when "3"
		case how
			when "1"
				cracknum(Digest::SHA256, hash)
			when "2"
				crackdic(Digest::SHA256, hash)
			when "3"
				crackdichyb(Digest::SHA256, hash)
			else
				puts ""
				puts "Invalid method to crack."
				puts ""
			end
	when "4"
		case how
			when "1"
				cracknum(Digest::SHA384, hash)
			when "2"
				crackdic(Digest::SHA384, hash)
			when "3"
				crackdichyb(Digest::SHA384, hash)
			else
				puts ""
				puts "Invalid method to crack."
				puts ""
			end
	when "5"
		case how
			when "1"
				cracknum(Digest::SHA512, hash)
			when "2"
				crackdic(Digest::SHA512, hash)
			when "3"
				crackdichyb(Digest::SHA512, hash)
			else
				puts ""
				puts "Invalid method to crack."
				puts ""
			end
	when "6"
		case how
			when "1"
				cracknum(Digest::RMD160, hash)
			when "2"
				crackdic(Digest::RMD160, hash)
			when "3"
				crackdichyb(Digest::RMD160, hash)
			else
				puts ""
				puts "Invalid method to crack."
				puts ""
			end
	else
		puts ""
		puts "Invalid hash type."
		puts ""

end

end
end
end
