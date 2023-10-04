#!/usr/bin/env ruby

arg=ARGV[0]

#scanner=arg.scan(/hb(?!o)\w+/)
scanner=arg.scan(/htb*n/).join
if scanner.any?
    puts scanner
end
