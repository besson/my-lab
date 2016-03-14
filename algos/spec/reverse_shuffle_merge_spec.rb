require_relative "../algos/reverse_shuffle_merge"

describe ReverseShuffleMerge do

  it "test_case_0" do
    input = "eggegg"
    output = "egg"
    expect(subject.find(input)).to eq(output)
  end

  it "test_case_1" do
    input = "bdabaceadaedaaaeaecdeadababdbeaeeacacaba"
    output = "aaaaaabaaceededecbdb"
    expect(subject.find(input)).to eq(output)
  end

  it "test_case_2" do
    input = "sbcnzxqnrygkocahxjebvueaawwcythjdrhvizqsshgtwdolmillxpshxpxqrywkivceufclhydhshrklkphajbftuapiocjlcthfirhgaohfysqjolssbzhbovdstbyqdpnjbpfmgqrzfctcwcrztvgbegunarvecseoulabaonguckqbtrvuagreyclyjytpvozqdnhldlnsocenuzksawirgsbjobpldjdlrxbricrauuksbmecvvwagnnacaqghmjpzrlsvlpbbcuaddgvlhvuvkxexjcfhxrodmcwlrzyyiksuksshhonahsyzbbprwuitmoyoqurtqsaslevgvpfbzkkhgcnpjdpseuiylluvdetsqssbrxpiclxxvosuqipsqvvwsezhl"
    output = "aaaaaavvcembskuabxddlpbbsgiaskucosdlhndqzovpjlcyerauvrbcugnbluescevrnubgvtzrcwccfzrqgmfpbjnpdqybtsdvobhzsslojqsyfhoghrifhtclcoiputjhpklkrhsdyhlcuevikwyrqxpxhspxllimlowtghssqzivhrjtywweuvejxokgyrnqxzns"
    expect(subject.find(input)).to eq(output)
  end

  it "test_case_3" do
    input = "djjcddjggbiigjhfghehhbgdigjicafgjcehhfgifadihiajgciagicdahcbajjbhifjiaajigdgdfhdiijjgaiejgegbbiigida"
    output = "aaaaabccigicgjihidfiejfijgidgbhhehgfhjgiibggjddjjd"
    expect(subject.find(input)).to eq(output)
  end

end


