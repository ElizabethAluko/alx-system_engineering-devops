# Configuration to enable holberton user to login and open files.

# Create the "holberton" user
user { 'holberton':
  ensure     => present,
  managehome => true,
}

# Grant necessary permissions
group { 'www-data':
  ensure => present,
}

user { 'holberton':
  groups => ['www-data'],
}

# Adjust file permissions
file { '/etc/nginx':
  ensure => directory,
  owner  => 'holberton',
  group  => 'holberton',
  mode   => '0755',
  recurse => true,
}

# Restart Nginx
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => File['/etc/nginx'],
}
