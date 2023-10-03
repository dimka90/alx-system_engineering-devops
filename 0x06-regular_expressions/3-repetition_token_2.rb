#!/usr/bin/env ruby

arg=ARGV[0]

scanner=arg.scan(/hbt{1,4}n/)

if scanner.any?
    puts scanner
end
