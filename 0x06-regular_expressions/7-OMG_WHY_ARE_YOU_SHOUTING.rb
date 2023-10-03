#!/usr/bin/env ruby

arg=ARGV[0]

scanner=arg.scan(/[A-Z]/)

if scanner.any?
    puts "#{scanner.join('')}"
end 
