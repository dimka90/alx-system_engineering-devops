#!/usr/bin/env ruby

arg=ARGV[0]

scanner=arg.scan(/hbt{2,5}n/)

if scanner.any?
    puts scanner
end
