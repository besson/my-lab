require_relative "../algos/password"

describe Password do

  it "test_case_0" do
    input = "a0Ba"
    output = 2
    expect(subject.solution(input)).to eq(output)
  end

  it "test_case_1" do
    input = "a0"
    output = -1
    expect(subject.solution(input)).to eq(output)
  end

  it "test_case_2" do
    input = "0"
    output = -1
    expect(subject.solution(input)).to eq(output)
  end

  it "test_case_3" do
    input = "B"
    output = -1
    expect(subject.solution(input)).to eq(output)
  end

  it "test_case_4" do
    input = "aaaaabbb0Baaa0CaaBaaaaB0"
    output = 9
    expect(subject.solution(input)).to eq(output)
  end

  it "test_case_5" do
    input = "aaaaabbb0Baaa0CaaBaaaaB"
    output = 9
    expect(subject.solution(input)).to eq(output)
  end

  it "test_case_6" do
    input = "aaaaabbb0aaa0aaaaaa"
    output = -1
    expect(subject.solution(input)).to eq(output)
  end

  it "test_case_7" do
    input = "1"
    output = -1
    expect(subject.solution(input)).to eq(output)
  end
end


