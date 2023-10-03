#!/usr/bin/env ruby

arg=ARGV[0]

scanner=arg.scan(/^h[\w]n$/)
if scanner.any?
    puts scanner
end
