#!/usr/bin/env ruby

arg=ARGV[0]

scanner=arg.scan(/^\d{1,10}$/)

if scanner.any?
    puts scanner
end
