require "byebug"

class ReverseShuffleMerge

  def initialize
    @reversed_count = {}
    @shuffled_count = {}
    @total_count = {}

    @reversed_word = ""
    @shuffled_word = ""
  end

  def find input
    @first_letter = input.chars.first.ord

    input.chars.each do |w|
      @total_count[w.ord] = 0 unless @total_count[w.ord]
      @total_count[w.ord] += 1
    end

    @total_count.each do |k,v|
      @first_letter = k if k < @first_letter

      @reversed_count[k] = v/2
      @shuffled_count[k] = v/2
    end

    input.reverse.chars.each do |w|
      if belongs_to_reversed?(w)
        @reversed_word = @reversed_word + w
        @reversed_count[w.ord] -= 1
      else
        @shuffled_count[w.ord] -= 1
      end

    end

    return @reversed_word
  end

  private
  def belongs_to_reversed? w
    return false if @reversed_count[w.ord] == 0
    return true if @shuffled_count[w.ord] == 0

    idx = @first_letter
    sum = 0

    while(idx < w.ord) do
      sum += @reversed_count[idx] if @reversed_count.key?(idx)
      idx += 1
    end

    return sum == 0
  end
end

input = $stdin.readlines.join
puts ReverseShuffleMerge.new.find(input)
