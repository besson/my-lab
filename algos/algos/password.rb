require "byebug"

class Password
  def solution(s)
    longest_seq = -1

    s.chars.each_with_index do |c, idx|
      if !(c =~ /[0-9]/)
        temp_seq = 0
        has_uppercase = false
        j = idx;

        while(!(s[j] =~ /[0-9]/) && j > 0) do
          temp_seq += 1
          has_uppercase = true if s[j] =~ /[A-Z]/
          j -= 1
        end

        if has_uppercase && temp_seq > longest_seq
          longest_seq = temp_seq
        end

      end
    end


    longest_seq
  end
end
