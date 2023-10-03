#!/usr/bin/env ruby

text=ARGV[0]
match_t=text.scan(/School/)
if match_t.any?
    puts "#{match_t.join('')}"
end
