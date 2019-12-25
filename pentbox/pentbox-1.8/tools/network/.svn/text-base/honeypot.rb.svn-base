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

module Network_pb
class Honeypot_pb
def initialize()

# This is a Honeypot. You can create with this your own Honeypot with your options or autoconfigure one.
#

require "socket"

puts ""
title "// Honeypot //"
puts ""
warning "You must run PenTBox with root privileges.\n"
puts ""
puts " Select option."
puts ""
puts "1- Fast Auto Configuration"
puts "2- Manual Configuration [Advanced Users, more options]"
puts ""
print "   -> "
configuration = gets_pb.chomp

def honeyconfig(port, message, sound, log, logname) # Function to launch the Honeypot.
	begin
		tcpserver = TCPServer.new("", port)
		if tcpserver
			puts ""
			puts "  HONEYPOT ACTIVATED ON PORT #{port} (#{Time.now.to_s})"
			puts ""
			if log == "y" || log == "Y"
				# If log is enabled, writes Honeypot activation time.
				begin
					File.open(logname, "a") do |logf|
						logf.puts "#################### PenTBox Honeypot log"
						logf.puts ""
						logf.puts "  HONEYPOT ACTIVATED ON PORT #{port} (#{Time.now.to_s})"
						logf.puts ""
					end
				rescue Errno::ENOENT
					puts ""
					puts " Saving log error: No such file or directory."
					puts ""
				end
			end
			loop do
				socket = tcpserver.accept
				sleep(1) # It is to solve possible DoS Attacks.
				if socket
					Thread.new do
						remotePort, remoteIp = Socket.unpack_sockaddr_in(socket.getpeername) # Gets the remote port and ip.
						puts ""
						puts "  INTRUSION ATTEMPT DETECTED! from #{remoteIp}:#{remotePort} (#{Time.now.to_s})"
						puts " -----------------------------"
						reciv = socket.recv(1000).to_s
						puts reciv
						if sound == "y" || sound == "Y"
							# If sound is enabled, then beep 3 times.
							puts "\a\a\a"
						end
						if log == "y" || log == "Y"
							# If log is enabled, writes the intrusion.
							begin
								File.open(logname, "a") do |logf|
									logf.puts ""
									logf.puts "  INTRUSION ATTEMPT DETECTED! from #{remoteIp}:#{remotePort} (#{Time.now.to_s})"
									logf.puts " -----------------------------"
									logf.puts reciv
								end
							rescue Errno::ENOENT
								puts ""
								puts " Saving log error: No such file or directory."
								puts ""
							end
						end
						sleep(2) # This is a sticky honeypot.
						socket.write(message)
						socket.close
					end
				end
			end
		end
	rescue Errno::EACCES
		puts ""
		puts " Error: Honeypot requires root privileges."
		puts ""
	rescue Errno::EADDRINUSE
		puts ""
		puts " Error: Port in use."
		puts ""
	rescue
		puts ""
		puts " Unknown error."
		puts ""
	end
end

case configuration
	when "1"
		access = rand(3)
		case access
			when 0
				honeyconfig(80, "<HEAD>\n<TITLE>Access denied</TITLE>\n</HEAD>\n<H2>Access denied</H2>\n" + "<H3>HTTP Referrer login failed</H3>\n" + "<H3>IP Address login failed</H3>\n" + "<P>\n#{Time.now.to_s}\n</P>", "N", "N", "")
			when 1
				honeyconfig(80, "<HEAD>\n<TITLE>Access denied</TITLE>\n</HEAD>\n<H2>Access denied</H2>\n" + "<H3>IP Address login failed</H3>\n" + "<P>\n#{Time.now.to_s}\n</P>", "N", "N", "")
			when 2
				honeyconfig(80, "<HEAD>\n<TITLE>Access denied</TITLE>\n</HEAD>\n<H2>Access denied</H2>\n" + "<P>\n#{Time.now.to_s}\n</P>", "N", "N", "")
		end
	when "2"
		puts ""
		puts " Insert port to Open."
		puts ""
		print "   -> "
		port = gets_pb.chomp
		puts ""
		puts " Insert false message to show."
		puts ""
		print "   -> "
		message = gets_pb.chomp
		puts ""
		puts " Save a log with intrusions?"
		puts ""
		print " (y/n)   -> "
		log = gets_pb.chomp
		if log == "Y" || log == "y"
			puts ""
			puts " Log file name? (incremental)"
			puts ""
			puts "Default: */pentbox/other/log_honeypot.txt"
			puts ""
			print "   -> "
			logname = gets_pb.chomp.gsub("\"", "").gsub("'", "")
			if logname == ""
				logname = "#{File.dirname(__FILE__)}/../../other/log_honeypot.txt"
			end
		end
		puts ""
		puts " Activate beep() sound when intrusion?"
		puts ""
		print " (y/n)   -> "
		sound = gets_pb.chomp
		honeyconfig(port, message, sound, log, logname)
	else
		puts ""
		puts "Invalid option."
		puts ""
end

end
end
end
