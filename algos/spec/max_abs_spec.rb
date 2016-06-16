require_relative "../algos/max_abs"

describe MaxAbs do

  it "test_case_0" do
    input = [4, 6, 2, 2, 6, 6, 1]
    output = 4
    expect(subject.solution(input)).to eq(output)
  end

  it "test_case_1" do
    input = [4]
    output = 0
    expect(subject.solution(input)).to eq(output)
  end

  it "test_case_2" do
    input = [4, 6, 2, 2, 6, 6, 1, 4]
    output = 7
    expect(subject.solution(input)).to eq(output)
  end

  it "test_case_3" do
    input = [2, 2, 2, 2]
    output = 3
    expect(subject.solution(input)).to eq(output)
  end

  it "test_case_4" do
    input = [23577, 48241, 82322, 80060, 17504, 81836, 17072, 17267, 67264, 59267, 21839, 94486, 47319, 57232, 3287, 19361, 22446, 87175, 77986, 99804, 97970, 29303, 56972, 89249, 29807, 25446, 17802, 26541, 76345, 24964, 50588, 61682, 64060, 33273, 90011, 32739, 63146, 89544, 93065, 76052, 81144, 9579, 98698, 99116, 16275, 78757, 18746, 99919, 4603, 24819, 60552, 58533, 53124, 7496, 71101, 78492, 83585, 76482, 39507, 61951, 56737, 61786, 27185, 88489, 49365, 22695, 98672, 63440, 16574, 45163, 13566, 99887, 43588, 76216, 60237, 61201, 74950, 18508, 82269, 4583, 65946, 85314, 60429, 34324, 90150, 90045, 93113, 83159, 17062, 73884, 61119, 83845, 75347, 26781, 13370, 71138, 89362, 15036, 64693, 23577]

    output = 99
    expect(subject.solution(input)).to eq(output)
  end





end


