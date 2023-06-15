# reconfigure nginx to handle more traffic

exec { 'reconfg-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

#restart nginx to apply the changes
exec { 'nginx restart',
  command => 'nginx restart',
  path    => '/etc/init.d/"
}
