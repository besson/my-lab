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
    @last_letter = input.chars.last.ord

    byebug
    input.chars.each do |w|
      @total_count[w.ord] = 0 unless @total_count[w.ord]
      @total_count[w.ord] += 1
    end

    @total_count.each do |k,v|
      @first_letter = k if k < @first_letter
      @last_letter = k if k > @last_letter

      @reversed_count[k] = v/2
      @shuffled_count[k] = v/2
    end

    input.chars.each do |w|
      if belongs_to_reversed?(w)
        @reversed_word = w + @reversed_word
        @reversed_count[w.ord] -= 1
      else
        @shuffled_word = @shuffled_word + w
        @shuffled_count[w.ord] -= 1
      end

    end

    return @reversed_word
  end

  private
  def belongs_to_reversed? w
    return false if @reversed_count[w.ord] == 0
    return true if @shuffled_count[w.ord] == 0

    bidx = @first_letter
    aidx = @last_letter
    before_sum = 0
    after_sum = 0

    while(bidx <= w.ord) do
      before_sum += @total_count[bidx] if @total_count.key?(bidx)
      bidx += 1
    end

    while(aidx > w.ord) do
      after_sum += @total_count[aidx] if @total_count.key?(aidx)
      aidx -= 1
    end

    before_sum > after_sum
  end
end
