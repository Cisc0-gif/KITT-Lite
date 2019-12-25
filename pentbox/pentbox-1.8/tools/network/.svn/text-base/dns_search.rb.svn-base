=begin

    Copyright (C) 2010

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
class DNS_search_pb
def initialize()

# DNS and host gathering. NS, MX, SHODAN, bruteforce and PTR IP range.
#

require File.dirname(__FILE__) + "/../../lib/net/dns/resolver.rb"
require File.dirname(__FILE__) + "/../../lib/net/shodan/shodan.rb"
require "timeout"

wordlist = File.dirname(__FILE__) + "/../../other/hosts.txt"
shodan_api_key = "1V95wJZnxcdos0mxObLqEjuReAVw1Zh7" # PenTBox SHODAN Developer API Key.
dns_server = "8.8.8.8" # Google DNS server by default.
max_threads = 15 # Maximum number of simultaneous threads.
puts ""
title "// DNS and host gathering //"
puts ""
puts " Insert domain to scan."
puts ""
print "   -> "
domain = gets_pb.chomp.gsub("www.", "")

def brutepetition(line, domain, resolv)
	Thread.new do
		continue = false
		while continue == false # This improves the performance, restart idle threads after 3 seconds.
			begin
				Timeout::timeout(3) do
					puts resolv.query("#{line}.#{domain}", Net::DNS::A).answer
					continue = true
				end
			rescue Timeout::Error
			end
		end
	end
end

def ptrpetition(ip, resolv, forshodan = false)
	if forshodan == false
		Thread.new do
			continue = false
			while continue == false
				begin
					Timeout::timeout(3) do
						puts resolv.query(ip, Net::DNS::PTR).answer
						continue = true
					end
				rescue Timeout::Error
				end
			end
		end
	else
		continue = false
		while continue == false
			begin
				Timeout::timeout(2) do
					return resolv.query(ip, Net::DNS::PTR).answer
					continue = true
				end
			rescue Timeout::Error
			end
		end
	end
end

begin
	resolv = Net::DNS::Resolver.new(:nameservers => dns_server)
	resolv.udp_timeout = 0
	resolv.retry_number = 5
	resolv.retry_interval = 1
	puts "\nUsing DNS Server -> " + dns_server
	puts "\n[*] Searching DNS NS ..."
	puts resolv.query(domain, Net::DNS::NS).answer
	puts "\n[*] Searching DNS MX ..."
	puts resolv.query(domain, Net::DNS::MX).answer
	puts "\n[*] Searching with SHODAN"
	begin
		api = Shodan::WebAPI.new(shodan_api_key)
		query = domain
		result = api.search(query)
		result['matches'].each do |host|
			print "IP #{host['ip']} #{host['country_name']} #{host['os']} => "
			result = ptrpetition(host['ip'], resolv, true)
			if result.size == 0
				puts "DNS not found"
			else
				puts result
			end
		end
	rescue
		puts "    Error searching with SHODAN"
	end

	puts "\n[*] Searching DNS by bruteforcing ..."
	puts "Threads -> " + max_threads.to_s
	puts "Wordlist -> " + wordlist
	puts "----"
	begin
		list = File.open(wordlist, "r")
	rescue
		puts "\nError opening #{wordlist}"
		puts ""
		exit
	end
	while line = list.gets
		line = line.chomp
		newthreads = false
		while newthreads == false
			if Thread.list.length < max_threads + 1 # The "+1" is the main thread.
				brutepetition(line, domain, resolv)
				newthreads = true
			else
				newthreads = false
				sleep(0.2)
			end
		end
	end
	list.close
	while Thread.list.length != 1
		puts "[*] Waiting for #{(Thread.list.length - 1).to_s} threads to finish ..."
		sleep(5)
	end

	puts "\nNext step is reverse DNS [PTR] to all /24 IP range of main domain."
	print "Press enter to continue ... "
	warning "This can cause a lot of false positives."
	gets_pb
	begin
		main_ip = resolv.query(domain, Net::DNS::A).answer[0].to_s.split(" ")[4].split(".") # Array with IP octets.
	rescue
		begin
			main_ip = resolv.query("www.#{domain}", Net::DNS::A).answer[0].to_s.split(" ")[4].split(".")
		rescue
			puts "Error resolving IP for #{domain}"
			exit
		end
	end
	loop do
		puts "[*] Reversing DNS [PTR] range #{main_ip[0]}.#{main_ip[1]}.#{main_ip[2]}.0-255"
		for i in 0..255 do
			ip = "#{main_ip[0]}.#{main_ip[1]}.#{main_ip[2]}.#{i.to_s}"
			newthreads = false
			while newthreads == false
				if Thread.list.length < max_threads + 1 # The "+1" is the main thread.
					ptrpetition(ip, resolv)
					newthreads = true
				else
					newthreads = false
					sleep(0.2)
				end
			end
		end
		while Thread.list.length != 1
			sleep(5)
			puts "[*] Waiting for #{(Thread.list.length - 1).to_s} threads to finish ..."
		end
		print "\nContinue? Press enter to continue ... "
		goback = gets_pb.chomp
		if goback != "back" # You can increase or decrease the range.
			if main_ip[2] == "255"
				main_ip[2] = "0"
				if main_ip[1] == "255"
					main_ip[1] = "0"
					if main_ip[0] == "255"
						puts "\nError: It was the last one IP in the world."
						puts ""
						exit
					else
						main_ip[0] = "#{main_ip[0].to_i + 1}"
					end
				else
					main_ip[1] = "#{main_ip[1].to_i + 1}"
				end
			else
				main_ip[2] = "#{main_ip[2].to_i + 1}"
			end
		else
			if main_ip[2] == "0"
				main_ip[2] = "255"
				if main_ip[1] == "0"
					main_ip[1] = "255"
					if main_ip[0] == "0"
						puts "\nError: It was the first one IP in the world."
						puts ""
						exit
					else
						main_ip[0] = "#{main_ip[0].to_i - 1}"
					end
				else
					main_ip[1] = "#{main_ip[1].to_i - 1}"
				end
			else
				main_ip[2] = "#{main_ip[2].to_i - 1}"
			end
		end
	end
end

end
end
end
