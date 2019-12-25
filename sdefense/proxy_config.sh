#! /bin/bash

read -p 'Enter proxy ip: ' server
read -p 'Enter proxy port: ' port
echo "
Acquire::http::Proxy http://$server:$port;
" > /etc/apt/apt.conf.d/10proxy
echo ':SUCCESS: Proxy set!'
