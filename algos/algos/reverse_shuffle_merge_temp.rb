reversed_count = {}
shuffled_count = {}
total_count = {}

first_letter = input.chars.first

reversed_word = ""
shuffled_word = ""

input.chars.each do |w|
  total_count[w] = 0 unless total_count[w]
  total_count[w] += 1
end

total_count.each do |k,v|
  first_letter = k if k.ord < first_letter.sum

  reversed_count[k] = v/2
  shuffled_count[k] = v/2
end

input.chars.each do |w|
  if w == first_letter && shuffled_count[w] > 0
    shuffled_word = shuffled_word + w
    shuffled_count[w] -= 1

  elsif reversed_count[w] > 0
    reversed_word = w + reversed_word
    reversed_count[w] -= 1

  else
    shuffled_word = shuffled_word + w
    shuffled_count[w] -= 1
  end
end

puts reversed_word
    end
end