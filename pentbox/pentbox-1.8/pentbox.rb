#!/usr/bin/env ruby

=begin

    Copyright (C) 2012, 2013, 2014

    Minzsec
    www.facebook.com/rootnameshadow

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

###########################
##  BASIC CONFIGURATION  ##
###########################

# PenTBox can save a log tracking the results given by the modules.
# Format: [1970-01-01 00:00:00 - Module name - Username] Data
#
# THIS DOESN'T WORK BY THE MOMENT. TODO
#
# Default -> false
$pb_log_enabled = false
$pb_log_file = File.dirname(__FILE__) + "/other/log/pentbox_log_" + ENV['USER'] + ".log"

# $protected_mode variable defines if protected mode is activated or not.
#
# Protected mode protects you against "script kiddies" and "lammers". They
# can't run dangerous modules without root privileges.
#
# Recommended for public computers!!
#
# Default -> true
$protected_mode = true

# $text_color variable.
# When true, titles and warnings will be colorful,
# else it will be with default colors.
#
# Default -> true
$text_color = true

###########################

##### Loading time
dir = File.dirname(__FILE__)
require dir + "/lib/pb_proced_lib.rb" # Common procedures and functions.

version = "1.8"
Signal.trap("INT") do
	puts ""
	puts "[*] EXITING ..."
	puts ""
	pb_write_log("exiting", "Core")
	exit
end
#####

pb_write_log("pentbox loaded", "Core")

srand(Time.now.to_i)
banner = rand(4)

puts ""
title " PenTBox #{version} "

# Thanks to Cowsay for the ASCII Art ;-)
case banner
	when 0
		puts "                                     .::!!!!!!!:. "
		puts "  .!!!!!:.                        .:!!!!!!!!!!!! "
		puts "  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$ "
		puts "      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P "
		puts "      $$$$$##WX!:      .<!!!!UW$$$$   $$$$$$$$# "
		puts "      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$* "    
		puts "      ^$$$B  $$$$      $$$$$$$$$$$$   d$$R* "
		puts "        **$bd$$$$      '*$$$$$$$$$$$o+#  "
		puts "             ****          ******* "          
	when 1
		puts "         __"
		puts "        U00U|.'@@@@@@`."
		puts "        |__|(@@@@@@@@@@)"
		puts "             (@@@@@@@@)"
		puts "             `YY~~~~YY'"
		puts "              ||    ||"
	when 2
		puts "             .__."
		puts "             (oo)____"
		puts "             (__)    )--*"
		puts "                ||--|| "
	when 3
		# This banner is thanks to figlet.
		puts "    ____          _____ ____"
		puts "   |  _ \\ ___ _ _|_   _| __ )  _____  __"
		puts "   | |_) / _ \\ '_ \\| | |  _ \\ / _ \\ \\/ /"
		puts "   |  __/  __/ | | | | | |_) | (_) >  <"
		puts "   |_|   \\___|_| |_|_| |____/ \\___/_/\\_\\"
end

sleep(0.25)
option1 = ""

while option1 != "5"
	module_exec = true
	puts ""
	puts "--------- Menu" + " "*10 + "ruby#{RUBY_VERSION} @ #{RUBY_PLATFORM}"
	puts ""
	puts "1- Cryptography tools"
	puts ""
	puts "2- Network tools"
	puts ""
	puts "3- Web"
        puts ""
        puts "4- Ip grabber"
        puts ""
        puts "5- Geolocation ip"
        puts ""
        puts "6- Mass attack"
	puts ""
	puts "7- License and contact"
	puts ""
	puts "8- Exit"
	puts ""
	print "   -> "
	option1 = gets_pb.chomp
	puts ""

	case option1
		when "1"
			puts "1- Base64 Encoder & Decoder"
			puts "2- Multi-Digest (MD5, SHA1, SHA256, SHA384, SHA512, RIPEMD-160)"
			puts "3- Hash Password Cracker (MD5, SHA1, SHA256, SHA384, SHA512, RIPEMD-160)"
			puts "4- Secure Password Generator"
			puts ""
			puts "0- Back"
			puts ""
			print "   -> "
			option2 = gets_pb.chomp
			case option2
				when "0"
					module_exec = false
				when "1"
					require "#{dir}/tools/cryptography/base64.rb"
					Cryptogr_pb::Base64_pb.new()
				when "2"
					require "#{dir}/tools/cryptography/digest.rb"
					Cryptogr_pb::Digest_pb.new()
				when "3"
					require "#{dir}/tools/cryptography/hash_cracker.rb"
					Cryptogr_pb::Hash_cracker_pb.new()
				when "4"
					require "#{dir}/tools/cryptography/sec_password.rb"
					Cryptogr_pb::Sec_password_pb.new()
				else
					module_exec = false
					puts ""
					puts "Invalid option."
					puts ""
			end
		when "2"
			puts "1- Net DoS Tester"
			puts "2- TCP port scanner"
			puts "3- Honeypot"
			puts "4- Fuzzer"
			puts "5- DNS and host gathering"
			puts "6- MAC address geolocation (samy.pl)"
			puts ""
			puts "0- Back"
			puts ""
			print "   -> "
			option2 = gets_pb.chomp
			case option2
				when "0"
					module_exec = false
				when "1"
					if haspermission() == true
						require "#{dir}/tools/network/net_dos.rb"
						Network_pb::Net_dos_pb.new()
					else
						module_exec = false
						puts ""
						puts "Sorry, you haven't permissions to run this module (root?)."
						puts ""
					end
				when "2"
					require "#{dir}/tools/network/port_scanner.rb"
					Network_pb::Port_scanner_pb.new()
				when "3"
					require "#{dir}/tools/network/honeypot.rb"
					Network_pb::Honeypot_pb.new()
				when "4"
					require "#{dir}/tools/network/fuzzer.rb"
					Network_pb::Fuzzer_pb.new()
				when "5"
					require "#{dir}/tools/network/dns_search.rb"
					Network_pb::DNS_search_pb.new()
				when "6"
					require "#{dir}/tools/network/samy_mac_loc.rb"
					Network_pb::Samy_mac_loc_pb.new()
				else
					module_exec = false
					puts ""
					puts "Invalid option."
					puts ""
			end
		when "3"
			puts "1- HTTP directory bruteforce"
			puts "2- HTTP common files bruteforce"
			puts ""
			puts "0- Back"
			puts ""
			print "   -> "
			option2 = gets_pb.chomp
			case option2
				when "0"
					module_exec = false
				when "1"
					require "#{dir}/tools/web/http_brute_dir.rb"
					Web_pb::HTTP_brute_dir_pb.new()
				when "2"
					require "#{dir}/tools/web/http_brute_files.rb"
					Web_pb::HTTP_brute_files_pb.new()
				else
					module_exec = false
					puts ""
					puts "Invalid option."
					puts ""
			end
		when "4"
module_exec = false
puts "
    X------------------------------------X
    | Copyright (C) 2012, 2013, 2014     |
    |                                    |
    |   Minzsec                          |
    |   www.facebook.com/rootnameshadow  |
    X------------------------------------X

    PenTBox is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PenTBox is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with PenTBox. Or you need some confuguration If not, see <http://www.gnu.org/licenses/>.

"
		when "5"
			module_exec = false
			Process.kill("SIGINT", Process.pid()) # Just exit.
		else
			module_exec = false
			puts ""
			puts "Invalid option."
			puts ""
	end
	if module_exec == true
		puts ""
		puts "[*] Module execution finished."
		puts ""
	end
end

