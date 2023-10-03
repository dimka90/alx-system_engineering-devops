#!/usr/bin/env ruby

arg=ARGV[0]

scanner=arg.scan(/hbtn|htn/)

if scanner.any?
    puts scanner
end
