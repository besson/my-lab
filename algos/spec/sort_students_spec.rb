require_relative "../algos/sort_students"

describe SortStudents do

  it "test_case_0" do
    input = [1,2,6,5,5,8,9]
    output = 3
    expect(subject.solution(input)).to eq(output)
  end

  it "test_case_1" do
    input = [1,2,5,5,6,8,9]
    output = 0
    expect(subject.solution(input)).to eq(output)
  end

  it "test_case_2" do
    input = [9,2,6,5,5,8,1]
    output = 7
    expect(subject.solution(input)).to eq(output)
  end

  it "test_case_3" do
    input = [1,2,5,6,5,8,9]
    output = 2
    expect(subject.solution(input)).to eq(output)
  end

  it "test_case_4" do
    input = [1,2,5,5,9,8,6]
    output = 3
    expect(subject.solution(input)).to eq(output)
  end




end

