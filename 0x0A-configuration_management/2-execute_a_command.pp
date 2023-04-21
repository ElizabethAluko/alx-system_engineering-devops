# Puppet that kil a proceds name killmenow
exec { 'killmenow':
  path    =>  ['/usr/bin'],
  command => 'pkill -f killmenow'
}
