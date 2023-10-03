#!/usr/bin/env ruby

arg=ARGV[0]

scanner=arg.scan(/hb(?!o)\w+/)
if scanner.any?
    puts scanner
end
