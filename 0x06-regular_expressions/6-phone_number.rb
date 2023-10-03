#!/usr/bin/env ruby

arg=ARGV[0]

scanner=arg.scan(/\d{10}+$/)

if scanner.any?
    puts scanner
end
