#! /usr/bin/env python3
import os
import time

def wait():
  wait = input('PRESS ENTER TO CONTINUE')

print('[*]Starting Library Installation...')
time.sleep(2)
print('[*]Configuring Apt Installation Sources...')

sources = """\
deb http://http.kali.org/kali kali-rolling main non-free contrib
deb-src http://http.kali.org/kali kali-rolling main non-free contrib
"""
with open('/etc/apt/sources.list', 'w+') as f: #config sources list for full package installation
  f.write(sources)
f.close()

print('[*]Sources Configured!')
time.sleep(2)
print('[*]Updating and Upgrading Packages...')
os.system('sudo apt-get update && sudo apt-get upgrade')
print('[*]Installing Linux Packages...')
os.system('sudo apt-get install figlet metasploit-framework hydra burpsuite tor nmap cryptcat netcat unicornsca php maltegoce recon-ng cewl crunch redis tshark tcpdump irssi telnet ftp git apache2 ssh weevely strace gdb radare2 arp-scan dirbuster wfuzz ncrack medusa xxd coreutils exiftool masscan dirb steghide proxychains p7zip macchanger hddtemp lm-sensors postgresql sqlmap logrotate kali-linux-full btscanner bluez bluelog redfang bluesnarfer spooftooph ettercap-graphical ettercap-text-only build-essential ntfs-3g cifs.utils mount dsniffer reaver aircrack-ng libcurl4-openssl-dev libpcap0.8-dev zlib1g zlib1g-dev libssl-dev john snort fierce openvas nikto wpscan mawk curl dhcpd isc-dhcp-server hostapd lighttpd mdk3 php-cgi pyrit unzip xterm openssl rfkill strings ufw clamav clamav-daemon kismet -y')
os.system('sudo ufw enable')
os.system('sudo gem install zsteg')
os.system('sudo apt-get install fail2ban')
print('[*]Starting postgresql service...')
os.system('sudo service postgresql start')
print('[*]Initiating YAML database for metasploit-framework...')
os.system('sudo msfdb init')
print('[*]Installing python2 and 3 libraries...')
os.system('sudo pip install -U -I pyusb')
os.system('sudo pip install -U platformio')
os.system('sudo pip install -r requirements2.txt')
os.system('sudo pip3 install -r requirements3.txt')
print('[*]Installing hg libs...')
os.chdir('hg')
os.system('sudo git clone https://github.com/NullArray/AutoSploit')
os.chdir('AutoSploit')
os.system('sudo chmod +x install.sh')
os.system('sudo ./install.sh')
os.chdir('..')
os.system('sudo git clone https://github.com/dreadlocked/Drupalgeddon2')
os.chdir('..')
print('[*]Installing and Initializing mousejack...')
os.system('sudo git clone https://github.com/BastilleResearch/mousejack.git')
os.chdir('mousejack')
os.system('sudo git submodule init')
os.system('sudo git submoudle update')
os.chdir('..')
os.system('sudo git clone https://github.com/insecurityofthings/jackit.git')
os.chdir('jackit')
os.system('sudo pip install -r requirements.txt')
os.system('sudo pip install -e .')
os.chdir('..')
print('[*]Installing WiFi-Pumpkin...')
os.system('sudo git clone https://github.com/P0cL4bs/WiFi-Pumpkin')
os.chdir("WiFi-Pumpkin")
os.system('sudo ./installer.sh --install')
os.system('sudo pip install --upgrade pyasn1-modules')
os.chdir('..')
print('[*]Installing w3af...')
os.system('sudo git clone https://github.com/andresriancho/w3af.git')
os.chdir('w3af')
os.system('python w3af_console')
os.system('bash /tmp/w3af_dependency_install.sh')
os.chdir('..')
print('[*]Installing gitGraber...')
os.system('sudo git clone https://github.com/hisxo/gitGraber')
os.chdir('gitGraber')
os.system('sudo pip3 install -r requirements.txt')
os.chdir('..')
print('[*]Installing SocialBox...')
os.system('sudo git clone https://github.com/TunisianEagles/SocialBox.git')
os.chdir('SocialBox')
os.system("sudo chmod 777 *")
os.system('sudo ./install-sb.sh')
os.chdir('..')
print('[*]Installing TIDOS-Framework...')
os.system("sudo git clone https://github.com/0xInfection/TIDoS-Framework")
os.chdir("TIDoS-Framework")
os.system("sudo chmod 777 install")
os.system('sudo ./install')
os.chdir("..")
print('[*]Installing Katana...')
os.system('sudo git clone https://github.com/adnane-X-tebbaa/Katana')
os.chdir('Katana')
os.system('sudo pip3 -r requirements.txt')
os.chdir('..')
print('[*]Installing gitHound...')
os.system('sudo wget https://github.com/tillson/git-hound/releases/download/v1.1/git-hound_1.1_Linux_x86_64.tar.gz')
os.system('sudo mkdir git-hound')
os.system('sudo mv git-hound_1.1_Linux_x86_64.tar.gz git-hound')
os.chdir('git-hound')
os.system('sudo gunzip git-hound_1.1_Linux_x86_64.tar.gz')
os.system('sudo tar xvf git-hound_1.1_Linux_x86_64.tar')
os.system('sudo rm git-hound_1.1_Linux_x86_64.tar')
os.system('sudo echo "github_username: username" > config.yml')
os.system('sudo echo "github_password: password" >> config.yml')
print('[*]Input your GitHub Username and Password to config.yml file...')
wait()
os.chir('..')
print('[*]Installing GitRob...')
os.system('sudo wget https://github.com/michenriksen/gitrob/releases/download/v2.0.0-beta/gitrob_linux_amd64_2.0.0-beta.zip')
os.system('sudo mdkdir gitrob')
os.system('sudo mv gitrob_linux_amd64_2.0.0-beta.zip')
os.chdir('gitrob')
os.system('sudo unzip gitrob_linux_amd64_2.0.0-beta.zip')
os.system('sudo rm gitrob_linux_amd64_2.0.0-beta.zip')
print('[*]Input your GitHub API Token using: export GITROB_ACCESS_TOKEN="deadbeefdeadbeefdeadbeefdeadbeef" >> ~/.bashrc')
wait()
os.chdir('..')
print('[*]Installing Python3.7 libs for Chromepass...')
os.chdir('escalate/chromepass')
os.system('sudo pip3 install -r requirements.txt')
os.chdir('../..')
print("[*]Installing PTF...")
os.system("sudo git clone https://github.com/trustedsec/ptf/")
print("[*]Installing domained...")
os.system("sudo git clone https://github.com/TypeError/domained")
os.chdir("domained")
os.system("sudo pip3 install -r ./ext/requirements.txt")
os.system("sudo python3 domained.py --install")
os.chdir("..")
print('[*]Installing Seeker...')
os.system('git clone https://github.com/thewhiteh4t/seeker.git')
os.chdir('seeker')
os.system('sudo chmod 777 install.sh')
os.system('sudo ./install.sh')
os.system('sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip')
os.system('sudo unzip ngrok-stable-linux-amd64.zip')
os.system('sudo rm ngrok-stable-linux-amd64.zip')
os.chdir('..')
print('[*]Installing Pwnstar...')
os.system('sudo git clone https://github.com/SilverFoxx/PwnSTAR.git')
os.chdir('PwnSTAR')
os.system('sudo chmod 777 installer.sh')
os.system('sudo ./installer.sh')
os.chdir('..')
print('[*]Installing hate_crack...')
os.system('sudo git clone https://github.com/trustedsec/hate_crack.git')
os.chdir('hate_crack')
os.system('sudo python hate_crack.py')
print('[!]config.json file generated! User configuration needed in /opt/KITT-Lite/hate_crack/config.json...')
wait()
os.chdir('..')
print("[*]Installing Wotop...")
os.system("sudo git clone https://github.com/nishitm/wotop")
os.chdir('wotop')
os.system('sudo make')
os.chdir('..')
print("[*]Installing Torghost..."_
os.system("sudo git clone https://github.com/SusmithKrishnan/torghost")
os.chdir('torghost')
os.system('sudo chmod 777 install.sh')
os.system('sudo ./install.sh')
os.chdir('..')
print("[*]Installing Vulnx...")
os.system('sudo git clone https://github.com/anouarbensaad/vulnx.git')
os.chdir('vulnx')
os.system('sudo chmod 777 install.sh')
os.system('sudo ./install.sh')
os.chdir('..')
print("[*]Installing Brutedum...")
os.system("sudo git clone https://github.com/GitHackTools/BruteDum")
print("[*]Installing Tool-X...")
os.system("sudo git clone https://github.com/Rajkumrdusad/Tool-X.git")
os.chdir('Tool-X')
os.system('sudo chmod 777 install.aex')
os.system('sudo ./install.aex')
os.chdir('..')
print('[*]Writing fail2ban configurations w/ bantime 5ms, findtime 5ms, and maxretry 3...')
fail2ban = """\
# WARNING: heavily refactored in 0.9.0 release.  Please review and
#          customize settings for your setup.
#
# Changes:  in most of the cases you should not modify this
#           file, but provide customizations in jail.local file,
#           or separate .conf files under jail.d/ directory, e.g.:
#
# HOW TO ACTIVATE JAILS:
#
# YOU SHOULD NOT MODIFY THIS FILE.
#
# It will probably be overwritten or improved in a distribution update.
#
# Provide customizations in a jail.local file or a jail.d/customisation.local.
# For example to change the default bantime for all jails and to enable the
# ssh-iptables jail the following (uncommented) would appear in the .local file.
# See man 5 jail.conf for details.
#
# [DEFAULT]
# bantime = 1h
#
# [sshd]
# enabled = true
#
# See jail.conf(5) man page for more information



# Comments: use '#' for comment lines and ';' (following a space) for inline comments


[INCLUDES]

#before = paths-distro.conf
before = paths-debian.conf

# The DEFAULT allows a global definition of the options. They can be overridden
# in each jail afterwards.

[DEFAULT]

#
# MISCELLANEOUS OPTIONS
#

# "ignorself" specifies whether the local resp. own IP addresses should be ignored
# (default is true). Fail2ban will not ban a host which matches such addresses.
#ignorself = true

# "ignoreip" can be a list of IP addresses, CIDR masks or DNS hosts. Fail2ban
# will not ban a host which matches an address in this list. Several addresses
# can be defined using space (and/or comma) separator.
#ignoreip = 127.0.0.1/8 ::1

# External command that will take an tagged arguments to ignore, e.g. <ip>,
# and return true if the IP is to be ignored. False otherwise.
#
# ignorecommand = /path/to/command <ip>
ignorecommand =

ignoreip = 127.0.0.1, 0.0.0.0

# "bantime" is the number of seconds that a host is banned.
bantime  = 5m

# A host is banned if it has generated "maxretry" during the last "findtime"
# seconds.
findtime  = 5m

# "maxretry" is the number of failures before a host get banned.
maxretry = 3

# "backend" specifies the backend used to get files modification.
# Available options are "pyinotify", "gamin", "polling", "systemd" and "auto".
# This option can be overridden in each jail as well.
#
# pyinotify: requires pyinotify (a file alteration monitor) to be installed.
#              If pyinotify is not installed, Fail2ban will use auto.
# gamin:     requires Gamin (a file alteration monitor) to be installed.
#              If Gamin is not installed, Fail2ban will use auto.
# polling:   uses a polling algorithm which does not require external libraries.
# systemd:   uses systemd python library to access the systemd journal.
#              Specifying "logpath" is not valid for this backend.
#              See "journalmatch" in the jails associated filter config
# auto:      will try to use the following backends, in order:
#              pyinotify, gamin, polling.
#
# Note: if systemd backend is chosen as the default but you enable a jail
#       for which logs are present only in its own log files, specify some other
#       backend for that jail (e.g. polling) and provide empty value for
#       journalmatch. See https://github.com/fail2ban/fail2ban/issues/959#issuecomment-74901200
backend = auto

# "usedns" specifies if jails should trust hostnames in logs,
#   warn when DNS lookups are performed, or ignore all hostnames in logs
#
# yes:   if a hostname is encountered, a DNS lookup will be performed.
# warn:  if a hostname is encountered, a DNS lookup will be performed,
#        but it will be logged as a warning.
# no:    if a hostname is encountered, will not be used for banning,
#        but it will be logged as info.
# raw:   use raw value (no hostname), allow use it for no-host filters/actions (example user)
usedns = warn

# "logencoding" specifies the encoding of the log files handled by the jail
#   This is used to decode the lines from the log file.
#   Typical examples:  "ascii", "utf-8"
#
#   auto:   will use the system locale setting
logencoding = auto

# "enabled" enables the jails.
#  By default all jails are disabled, and it should stay this way.
#  Enable only relevant to your setup jails in your .local or jail.d/*.conf
#
# true:  jail will be enabled and log files will get monitored for changes
# false: jail is not enabled
enabled = false


# "mode" defines the mode of the filter (see corresponding filter implementation for more info).
mode = normal

# "filter" defines the filter to use by the jail.
#  By default jails have names matching their filter name
#
filter = %(__name__)s[mode=%(mode)s]


#
# ACTIONS
#

# Some options used for actions

# Destination email address used solely for the interpolations in
# jail.{conf,local,d/*} configuration files.
destemail = root@localhost

# Sender email address used solely for some actions
sender = root@<fq-hostname>

# E-mail action. Since 0.8.1 Fail2Ban uses sendmail MTA for the
# mailing. Change mta configuration parameter to mail if you want to
# revert to conventional 'mail'.
mta = sendmail

# Default protocol
protocol = tcp

# Specify chain where jumps would need to be added in ban-actions expecting parameter chain
chain = <known/chain>

# Ports to be banned
# Usually should be overridden in a particular jail
port = 0:65535

# Format of user-agent https://tools.ietf.org/html/rfc7231#section-5.5.3
fail2ban_agent = Fail2Ban/%(fail2ban_version)s

#
# Action shortcuts. To be used to define action parameter

# Default banning action (e.g. iptables, iptables-new,
# iptables-multiport, shorewall, etc) It is used to define
# action_* variables. Can be overridden globally or per
# section within jail.local file
banaction = iptables-multiport
banaction_allports = iptables-allports

# The simplest action to take: ban only
action_ = %(banaction)s[name=%(__name__)s, bantime="%(bantime)s", port="%(port)s", protocol="%(protocol)s", chain="%(chain)s"]

# ban & send an e-mail with whois report to the destemail.
action_mw = %(banaction)s[name=%(__name__)s, bantime="%(bantime)s", port="%(port)s", protocol="%(protocol)s", chain="%(chain)s"]
            %(mta)s-whois[name=%(__name__)s, sender="%(sender)s", dest="%(destemail)s", protocol="%(protocol)s", chain="%(chain)s"]

# ban & send an e-mail with whois report and relevant log lines
# to the destemail.
action_mwl = %(banaction)s[name=%(__name__)s, bantime="%(bantime)s", port="%(port)s", protocol="%(protocol)s", chain="%(chain)s"]
             %(mta)s-whois-lines[name=%(__name__)s, sender="%(sender)s", dest="%(destemail)s", logpath=%(logpath)s, chain="%(chain)s"]

# See the IMPORTANT note in action.d/xarf-login-attack for when to use this action
#
# ban & send a xarf e-mail to abuse contact of IP address and include relevant log lines
# to the destemail.
action_xarf = %(banaction)s[name=%(__name__)s, bantime="%(bantime)s", port="%(port)s", protocol="%(protocol)s", chain="%(chain)s"]
             xarf-login-attack[service=%(__name__)s, sender="%(sender)s", logpath=%(logpath)s, port="%(port)s"]

# ban IP on CloudFlare & send an e-mail with whois report and relevant log lines
# to the destemail.
action_cf_mwl = cloudflare[cfuser="%(cfemail)s", cftoken="%(cfapikey)s"]
                %(mta)s-whois-lines[name=%(__name__)s, sender="%(sender)s", dest="%(destemail)s", logpath=%(logpath)s, chain="%(chain)s"]

# Report block via blocklist.de fail2ban reporting service API
#
# See the IMPORTANT note in action.d/blocklist_de.conf for when to use this action.
# Specify expected parameters in file action.d/blocklist_de.local or if the interpolation
# `action_blocklist_de` used for the action, set value of `blocklist_de_apikey`
# in your `jail.local` globally (section [DEFAULT]) or per specific jail section (resp. in
# corresponding jail.d/my-jail.local file).
#
action_blocklist_de  = blocklist_de[email="%(sender)s", service=%(filter)s, apikey="%(blocklist_de_apikey)s", agent="%(fail2ban_agent)s"]

# Report ban via badips.com, and use as blacklist
#
# See BadIPsAction docstring in config/action.d/badips.py for
# documentation for this action.
#
# NOTE: This action relies on banaction being present on start and therefore
# should be last action defined for a jail.
#
action_badips = badips.py[category="%(__name__)s", banaction="%(banaction)s", agent="%(fail2ban_agent)s"]
#
# Report ban via badips.com (uses action.d/badips.conf for reporting only)
#
action_badips_report = badips[category="%(__name__)s", agent="%(fail2ban_agent)s"]

# Report ban via abuseipdb.com.
#
# See action.d/abuseipdb.conf for usage example and details.
#
action_abuseipdb = abuseipdb

# Choose default action.  To change, just override value of 'action' with the
# interpolation to the chosen action shortcut (e.g.  action_mw, action_mwl, etc) in jail.local
# globally (section [DEFAULT]) or per specific section
action = %(action_)s


#
# JAILS
#

#
# SSH servers
#

[sshd]

enabled = true
# To use more aggressive sshd modes set filter parameter "mode" in jail.local:
# normal (default), ddos, extra or aggressive (combines all).
# See "tests/files/logs/sshd" or "filter.d/sshd.conf" for usage example and details.
#mode   = normal
port    = ssh
logpath = %(sshd_log)s
backend = %(sshd_backend)s


[dropbear]

port     = ssh
logpath  = %(dropbear_log)s
backend  = %(dropbear_backend)s


[selinux-ssh]

port     = ssh
logpath  = %(auditd_log)s


#
# HTTP servers
#

[apache-auth]

port     = http,https
logpath  = %(apache_error_log)s


[apache-badbots]
# Ban hosts which agent identifies spammer robots crawling the web
# for email addresses. The mail outputs are buffered.
port     = http,https
logpath  = %(apache_access_log)s
bantime  = 48h
maxretry = 1


[apache-noscript]

port     = http,https
logpath  = %(apache_error_log)s


[apache-overflows]

port     = http,https
logpath  = %(apache_error_log)s
maxretry = 2


[apache-nohome]

port     = http,https
logpath  = %(apache_error_log)s
maxretry = 2


[apache-botsearch]

port     = http,https
logpath  = %(apache_error_log)s
maxretry = 2


[apache-fakegooglebot]

port     = http,https
logpath  = %(apache_access_log)s
maxretry = 1
ignorecommand = %(ignorecommands_dir)s/apache-fakegooglebot <ip>


[apache-modsecurity]

port     = http,https
logpath  = %(apache_error_log)s
maxretry = 2


[apache-shellshock]

port    = http,https
logpath = %(apache_error_log)s
maxretry = 1


[openhab-auth]

filter = openhab
action = iptables-allports[name=NoAuthFailures]
logpath = /opt/openhab/logs/request.log


[nginx-http-auth]

port    = http,https
logpath = %(nginx_error_log)s

# To use 'nginx-limit-req' jail you should have `ngx_http_limit_req_module`
# and define `limit_req` and `limit_req_zone` as described in nginx documentation
# http://nginx.org/en/docs/http/ngx_http_limit_req_module.html
# or for example see in 'config/filter.d/nginx-limit-req.conf'
[nginx-limit-req]
port    = http,https
logpath = %(nginx_error_log)s

[nginx-botsearch]

port     = http,https
logpath  = %(nginx_error_log)s
maxretry = 2


# Ban attackers that try to use PHP's URL-fopen() functionality
# through GET/POST variables. - Experimental, with more than a year
# of usage in production environments.

[php-url-fopen]

port    = http,https
logpath = %(nginx_access_log)s
          %(apache_access_log)s


[suhosin]

port    = http,https
logpath = %(suhosin_log)s


[lighttpd-auth]
# Same as above for Apache's mod_auth
# It catches wrong authentifications
port    = http,https
logpath = %(lighttpd_error_log)s


#
# Webmail and groupware servers
#

[roundcube-auth]

port     = http,https
logpath  = %(roundcube_errors_log)s
# Use following line in your jail.local if roundcube logs to journal.
#backend = %(syslog_backend)s


[openwebmail]

port     = http,https
logpath  = /var/log/openwebmail.log


[horde]

port     = http,https
logpath  = /var/log/horde/horde.log


[groupoffice]

port     = http,https
logpath  = /home/groupoffice/log/info.log


[sogo-auth]
# Monitor SOGo groupware server
# without proxy this would be:
# port    = 20000
port     = http,https
logpath  = /var/log/sogo/sogo.log


[tine20]

logpath  = /var/log/tine20/tine20.log
port     = http,https


#
# Web Applications
#
#

[drupal-auth]

port     = http,https
logpath  = %(syslog_daemon)s
backend  = %(syslog_backend)s

[guacamole]

port     = http,https
logpath  = /var/log/tomcat*/catalina.out

[monit]
#Ban clients brute-forcing the monit gui login
port = 2812
logpath  = /var/log/monit


[webmin-auth]

port    = 10000
logpath = %(syslog_authpriv)s
backend = %(syslog_backend)s


[froxlor-auth]

port    = http,https
logpath  = %(syslog_authpriv)s
backend  = %(syslog_backend)s


#
# HTTP Proxy servers
#
#

[squid]

port     =  80,443,3128,8080
logpath = /var/log/squid/access.log


[3proxy]

port    = 3128
logpath = /var/log/3proxy.log


#
# FTP servers
#


[proftpd]

port     = ftp,ftp-data,ftps,ftps-data
logpath  = %(proftpd_log)s
backend  = %(proftpd_backend)s


[pure-ftpd]

port     = ftp,ftp-data,ftps,ftps-data
logpath  = %(pureftpd_log)s
backend  = %(pureftpd_backend)s


[gssftpd]

port     = ftp,ftp-data,ftps,ftps-data
logpath  = %(syslog_daemon)s
backend  = %(syslog_backend)s


[wuftpd]

port     = ftp,ftp-data,ftps,ftps-data
logpath  = %(wuftpd_log)s
backend  = %(wuftpd_backend)s


[vsftpd]
# or overwrite it in jails.local to be
# logpath = %(syslog_authpriv)s
# if you want to rely on PAM failed login attempts
# vsftpd's failregex should match both of those formats
port     = ftp,ftp-data,ftps,ftps-data
logpath  = %(vsftpd_log)s


#
# Mail servers
#

# ASSP SMTP Proxy Jail
[assp]

port     = smtp,465,submission
logpath  = /root/path/to/assp/logs/maillog.txt


[courier-smtp]

port     = smtp,465,submission
logpath  = %(syslog_mail)s
backend  = %(syslog_backend)s


[postfix]
# To use another modes set filter parameter "mode" in jail.local:
mode    = more
port    = smtp,465,submission
logpath = %(postfix_log)s
backend = %(postfix_backend)s


[postfix-rbl]

filter   = postfix[mode=rbl]
port     = smtp,465,submission
logpath  = %(postfix_log)s
backend  = %(postfix_backend)s
maxretry = 1


[sendmail-auth]

port    = submission,465,smtp
logpath = %(syslog_mail)s
backend = %(syslog_backend)s


[sendmail-reject]
# To use more aggressive modes set filter parameter "mode" in jail.local:
# normal (default), extra or aggressive
# See "tests/files/logs/sendmail-reject" or "filter.d/sendmail-reject.conf" for usage example and details.
#mode    = normal
port     = smtp,465,submission
logpath  = %(syslog_mail)s
backend  = %(syslog_backend)s


[qmail-rbl]

filter  = qmail
port    = smtp,465,submission
logpath = /service/qmail/log/main/current


# dovecot defaults to logging to the mail syslog facility
# but can be set by syslog_facility in the dovecot configuration.
[dovecot]

port    = pop3,pop3s,imap,imaps,submission,465,sieve
logpath = %(dovecot_log)s
backend = %(dovecot_backend)s


[sieve]

port   = smtp,465,submission
logpath = %(dovecot_log)s
backend = %(dovecot_backend)s


[solid-pop3d]

port    = pop3,pop3s
logpath = %(solidpop3d_log)s


[exim]
# see filter.d/exim.conf for further modes supported from filter:
#mode = normal
port   = smtp,465,submission
logpath = %(exim_main_log)s


[exim-spam]

port   = smtp,465,submission
logpath = %(exim_main_log)s


[kerio]

port    = imap,smtp,imaps,465
logpath = /opt/kerio/mailserver/store/logs/security.log


#
# Mail servers authenticators: might be used for smtp,ftp,imap servers, so
# all relevant ports get banned
#

[courier-auth]

port     = smtp,465,submission,imap,imaps,pop3,pop3s
logpath  = %(syslog_mail)s
backend  = %(syslog_backend)s


[postfix-sasl]

filter   = postfix[mode=auth]
port     = smtp,465,submission,imap,imaps,pop3,pop3s
# You might consider monitoring /var/log/mail.warn instead if you are
# running postfix since it would provide the same log lines at the
# "warn" level but overall at the smaller filesize.
logpath  = %(postfix_log)s
backend  = %(postfix_backend)s


[perdition]

port   = imap,imaps,pop3,pop3s
logpath = %(syslog_mail)s
backend = %(syslog_backend)s


[squirrelmail]

port = smtp,465,submission,imap,imap2,imaps,pop3,pop3s,http,https,socks
logpath = /var/lib/squirrelmail/prefs/squirrelmail_access_log


[cyrus-imap]

port   = imap,imaps
logpath = %(syslog_mail)s
backend = %(syslog_backend)s


[uwimap-auth]

port   = imap,imaps
logpath = %(syslog_mail)s
backend = %(syslog_backend)s


#
#
# DNS servers
#


# !!! WARNING !!!
#   Since UDP is connection-less protocol, spoofing of IP and imitation
#   of illegal actions is way too simple.  Thus enabling of this filter
#   might provide an easy way for implementing a DoS against a chosen
#   victim. See
#    http://nion.modprobe.de/blog/archives/690-fail2ban-+-dns-fail.html
#   Please DO NOT USE this jail unless you know what you are doing.
#
# IMPORTANT: see filter.d/named-refused for instructions to enable logging
# This jail blocks UDP traffic for DNS requests.
# [named-refused-udp]
#
# filter   = named-refused
# port     = domain,953
# protocol = udp
# logpath  = /var/log/named/security.log

# IMPORTANT: see filter.d/named-refused for instructions to enable logging
# This jail blocks TCP traffic for DNS requests.

[named-refused]

port     = domain,953
logpath  = /var/log/named/security.log


[nsd]

port     = 53
action   = %(banaction)s[name=%(__name__)s-tcp, port="%(port)s", protocol="tcp", chain="%(chain)s", actname=%(banaction)s-tcp]
           %(banaction)s[name=%(__name__)s-udp, port="%(port)s", protocol="udp", chain="%(chain)s", actname=%(banaction)s-udp]
logpath = /var/log/nsd.log


#
# Miscellaneous
#

[asterisk]

port     = 5060,5061
action   = %(banaction)s[name=%(__name__)s-tcp, port="%(port)s", protocol="tcp", chain="%(chain)s", actname=%(banaction)s-tcp]
           %(banaction)s[name=%(__name__)s-udp, port="%(port)s", protocol="udp", chain="%(chain)s", actname=%(banaction)s-udp]
           %(mta)s-whois[name=%(__name__)s, dest="%(destemail)s"]
logpath  = /var/log/asterisk/messages
maxretry = 10


[freeswitch]

port     = 5060,5061
action   = %(banaction)s[name=%(__name__)s-tcp, port="%(port)s", protocol="tcp", chain="%(chain)s", actname=%(banaction)s-tcp]
           %(banaction)s[name=%(__name__)s-udp, port="%(port)s", protocol="udp", chain="%(chain)s", actname=%(banaction)s-udp]
           %(mta)s-whois[name=%(__name__)s, dest="%(destemail)s"]
logpath  = /var/log/freeswitch.log
maxretry = 10


# To log wrong MySQL access attempts add to /etc/my.cnf in [mysqld] or
# equivalent section:
# log-warning = 2
#
# for syslog (daemon facility)
# [mysqld_safe]
# syslog
#
# for own logfile
# [mysqld]
# log-error=/var/log/mysqld.log
[mysqld-auth]

port     = 3306
logpath  = %(mysql_log)s
backend  = %(mysql_backend)s


# Log wrong MongoDB auth (for details see filter 'filter.d/mongodb-auth.conf')
[mongodb-auth]
# change port when running with "--shardsvr" or "--configsvr" runtime operation
port     = 27017
logpath  = /var/log/mongodb/mongodb.log


# Jail for more extended banning of persistent abusers
# !!! WARNINGS !!!
# 1. Make sure that your loglevel specified in fail2ban.conf/.local
#    is not at DEBUG level -- which might then cause fail2ban to fall into
#    an infinite loop constantly feeding itself with non-informative lines
# 2. Increase dbpurgeage defined in fail2ban.conf to e.g. 648000 (7.5 days)
#    to maintain entries for failed logins for sufficient amount of time
[recidive]

logpath  = /var/log/fail2ban.log
banaction = %(banaction_allports)s
bantime  = 1w
findtime = 1d


# Generic filter for PAM. Has to be used with action which bans all
# ports such as iptables-allports, shorewall

[pam-generic]
# pam-generic filter can be customized to monitor specific subset of 'tty's
banaction = %(banaction_allports)s
logpath  = %(syslog_authpriv)s
backend  = %(syslog_backend)s


[xinetd-fail]

banaction = iptables-multiport-log
logpath   = %(syslog_daemon)s
backend   = %(syslog_backend)s
maxretry  = 2


# stunnel - need to set port for this
[stunnel]

logpath = /var/log/stunnel4/stunnel.log


[ejabberd-auth]

port    = 5222
logpath = /var/log/ejabberd/ejabberd.log


[counter-strike]

logpath = /opt/cstrike/logs/L[0-9]*.log
# Firewall: http://www.cstrike-planet.com/faq/6
tcpport = 27030,27031,27032,27033,27034,27035,27036,27037,27038,27039
udpport = 1200,27000,27001,27002,27003,27004,27005,27006,27007,27008,27009,27010,27011,27012,27013,27014,27015
action  = %(banaction)s[name=%(__name__)s-tcp, port="%(tcpport)s", protocol="tcp", chain="%(chain)s", actname=%(banaction)s-tcp]
           %(banaction)s[name=%(__name__)s-udp, port="%(udpport)s", protocol="udp", chain="%(chain)s", actname=%(banaction)s-udp]

# consider low maxretry and a long bantime
# nobody except your own Nagios server should ever probe nrpe
[nagios]

logpath  = %(syslog_daemon)s     ; nrpe.cfg may define a different log_facility
backend  = %(syslog_backend)s
maxretry = 1


[oracleims]
# see "oracleims" filter file for configuration requirement for Oracle IMS v6 and above
logpath = /opt/sun/comms/messaging64/log/mail.log_current
banaction = %(banaction_allports)s

[directadmin]
logpath = /var/log/directadmin/login.log
port = 2222

[portsentry]
logpath  = /var/lib/portsentry/portsentry.history
maxretry = 1

[pass2allow-ftp]
# this pass2allow example allows FTP traffic after successful HTTP authentication
port         = ftp,ftp-data,ftps,ftps-data
# knocking_url variable must be overridden to some secret value in jail.local
knocking_url = /knocking/
filter       = apache-pass[knocking_url="%(knocking_url)s"]
# access log of the website with HTTP auth
logpath      = %(apache_access_log)s
blocktype    = RETURN
returntype   = DROP
action       = %(action_)s[blocktype=%(blocktype)s, returntype=%(returntype)s]
bantime      = 1h
maxretry     = 1
findtime     = 1


[murmur]
# AKA mumble-server
port     = 64738
action   = %(banaction)s[name=%(__name__)s-tcp, port="%(port)s", protocol=tcp, chain="%(chain)s", actname=%(banaction)s-tcp]
           %(banaction)s[name=%(__name__)s-udp, port="%(port)s", protocol=udp, chain="%(chain)s", actname=%(banaction)s-udp]
logpath  = /var/log/mumble-server/mumble-server.log


[screensharingd]
# For Mac OS Screen Sharing Service (VNC)
logpath  = /var/log/system.log
logencoding = utf-8

[haproxy-http-auth]
# HAProxy by default doesn't log to file you'll need to set it up to forward
# logs to a syslog server which would then write them to disk.
# See "haproxy-http-auth" filter for a brief cautionary note when setting
# maxretry and findtime.
logpath  = /var/log/haproxy.log

[slapd]
port    = ldap,ldaps
logpath = /var/log/slapd.log

[domino-smtp]
port    = smtp,ssmtp
logpath = /home/domino01/data/IBM_TECHNICAL_SUPPORT/console.log

[phpmyadmin-syslog]
port    = http,https
logpath = %(syslog_authpriv)s
backend = %(syslog_backend)s


[zoneminder]
# Zoneminder HTTP/HTTPS web interface auth
# Logs auth failures to apache2 error log
port    = http,https
logpath = %(apache_error_log)s"
"""

with open('/etc/fail2ban/jail.local', 'w+') as f:
  f.write(fail2ban)
f.close()

os.system('sudo service fail2ban restart')
print('[*]Writing dynamic proxychain to proxychain config...')

proxychains = """\
# proxychains.conf  VER 3.1
#
#        HTTP, SOCKS4, SOCKS5 tunneling proxifier with DNS.
#	

# The option below identifies how the ProxyList is treated.
# only one option should be uncommented at time,
# otherwise the last appearing option will be accepted
#
dynamic_chain
#
# Dynamic - Each connection will be done via chained proxies
# all proxies chained in the order as they appear in the list
# at least one proxy must be online to play in chain
# (dead proxies are skipped)
# otherwise EINTR is returned to the app
#
#strict_chain
#
# Strict - Each connection will be done via chained proxies
# all proxies chained in the order as they appear in the list
# all proxies must be online to play in chain
# otherwise EINTR is returned to the app
#
#random_chain
#
# Random - Each connection will be done via random proxy
# (or proxy chain, see  chain_len) from the list.
# this option is good to test your IDS :)

# Make sense only if random_chain
#chain_len = 2

# Quiet mode (no output from library)
#quiet_mode

# Proxy DNS requests - no leak for DNS data
proxy_dns 

# Some timeouts in milliseconds
tcp_read_time_out 15000
tcp_connect_time_out 8000

# ProxyList format
#       type  host  port [user pass]
#       (values separated by 'tab' or 'blank')
#
#
#        Examples:
#
#            	socks5	192.168.67.78	1080	lamer	secret
#		http	192.168.89.3	8080	justu	hidden
#	 	socks4	192.168.1.49	1080
#	        http	192.168.39.93	8080	
#		
#
#       proxy types: http, socks4, socks5
#        ( auth types supported: "basic"-http  "user/pass"-socks )
#
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
#socks4 	127.0.0.1 9050

http 67.205.171.99 8080
socks4 167.114.79.139 32537
socks4 186.211.185.106 49314
socks4 139.159.47.22 39593
socks4 91.217.96.1 56636
socks4 181.143.214.213 3629
socks4 36.37.214.226 37797
http 51.79.65.157 3128
https 125.165.217.95 8080
https 182.144.141.223 53603
https 202.138.248.123 45229
https 109.86.207.1 46878
https 77.232.186.2 8080
https 171.5.102.251 8080
http  54.180.123.253 8080
http 159.65.168.195 80
socks4 198.50.177.44 44699
socks5 159.203.166.41 1080
"""
with open('/etc/proxychains.conf', 'w+') as f:
  f.write(proxychains)
f.close()

print('[*]Setting Up HomePWN...')
os.system('sudo git clone https://github.com/ElevenPaths/HomePWN')
os.chdir('HomePWN')
os.system("sudo ./install.sh")
os.chdir('..')

print("[*]Setting Up Social-Engineer-Toolkit...")
os.chdir('phishing/SET')
os.system('sudo pip3 install -r requirements.txt')
os.sysetm('sudo python3 setup.py')

print('[*]Updating and Upgrading Packages...')
os.system('sudo apt-get update && sudo apt-get upgrade')
os.system('sudo apt autoremove')
print('[+]Library Installation Complete...')
