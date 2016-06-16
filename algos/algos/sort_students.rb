class SortStudents do
  def solution(a)
    @start = 0
    @end = 0
    @changes = 0

    # I've changed the merge part of merge sort algorithm to get the rearragements
    mergesort(a)

    return 0 if @changes == 0
    return (@end - @start) + 1
  end

  def mergesort(a)
    return a if a.size <= 1

    middle = a.size / 2
    left  = mergesort(a[0, middle])
    right = mergesort(a[middle, a.size - middle])

    merge(left, right)
  end

  def merge(left, right)
    sorted = []

    i = 0
    j = 0
    k = 0

    while(i < left.size || j < right.size) do
      if i < left.size && j < right.size

        if left[i] <= right[j]
          sorted[k] = left[i]
          i += 1
          k += 1
        else
          sorted[k] = right[j]
          j += 1
          k += 1
          @start = k if k < @start
          @end = k + 1 if k + 1 > @end
          @changes += 1
        end
      else
        if i < left.size
          sorted[k] = left[i]
          k += 1
          i += 1
        else
          sorted[k] = left[j]
          k += 1
          j += 1
        end
      end
    end

    sorted
  end

end
