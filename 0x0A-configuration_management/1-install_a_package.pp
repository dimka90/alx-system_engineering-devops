# creating resource that installed flask package

exec { 'flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
}
