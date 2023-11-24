# 2-execute_a_command.pp

exec { 'killmenow':
  command     => '/usr/bin/pkill -f killmenow',
  path        => '/usr/bin',
  refreshonly => true,
}

# Ensure the command is only triggered when necessary
file { '/path/to/your/killmenow':
  notify => Exec['killmenow'],
}
