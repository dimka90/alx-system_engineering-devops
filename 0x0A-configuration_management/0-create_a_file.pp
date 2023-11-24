# created a manifest using a puppet that create a new file with some attributes

node default{

file {'/tmp/school':
mode    => '0744',
owner   =>'www-data',
group   =>'www-data',
content =>'I love Puppet',
}

}
