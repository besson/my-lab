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
    @small_letter = input.chars.first.ord
    @big_letter = input.chars.last.ord

    input.chars.each do |w|
      @total_count[w.ord] = 0 unless @total_count[w.ord]
      @total_count[w.ord] += 1
    end

    @total_count.each do |k,v|
      @small_letter = k if k < @small_letter
      @big_letter = k if k > @big_letter

      @reversed_count[k] = v/2
      @shuffled_count[k] = v/2
    end

    i = input.size - 1
    while (i >= 0) do

      if input[i].ord == @small_letter

        if @reversed_count[input[i].ord] > 0
          @reversed_count[input[i].ord] -= 1; @reversed_word << input[i]
          last_index = i
        else
          @shuffled_count[input[i].ord] -= 1
        end

        set_smallest_word
      else
        if @shuffled_count[input[i].ord] > 0
          @shuffled_count[input[i].ord] -= 1
        else
          j = i
          smaller = input[i].ord
          small_index = i

          while (j < last_index)
            if input[j].ord <= smaller && @reversed_count[input[j].ord] > 0
              smaller = input[j].ord
              small_index = j
            end
            j += 1
          end

          k = i + 1
          while (k <= small_index)
            @shuffled_count[input[k].ord] += 1
            k += 1
          end

          last_index = small_index
          @reversed_count[smaller] -= 1; @reversed_word << input[small_index]
          i = small_index
        end
      end

      i -= 1
    end

    return @reversed_word
  end

  def set_smallest_word
    return if @reversed_count[@small_letter] > 0

    j = @small_letter + 1
    while (j <= @big_letter)
      if @reversed_count.key?(j) && @reversed_count[j] > 0
        @small_letter = j
        break
      end

      j += 1
    end
  end
end

input = $stdin.readlines.join
puts ReverseShuffleMerge.new.find(input)

