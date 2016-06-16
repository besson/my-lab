class MaxAbs 
  def solution(a)
    n = a.length
    result = 0
    first_idx = {}

    for i in 0 .. (n - 1)
      if !first_idx[a[i]]
        first_idx[a[i]] = i
      end
    end

    for i in 0 .. (n - 1)
      if (i - first_idx[a[i]]).abs > result
        result = (i - first_idx[a[i]]).abs
      end
    end

    return result
  end
end
